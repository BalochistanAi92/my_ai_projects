from asyncio import timeouts
import os
import folium
from geopy.distance import geodesic

class CPECNavigator:
    def __init__(self):
        self.cpec_route = {
            'khunjrab pass': (36.8500, 75.4333),
            'Gilgit': (35.9208, 74.3144),
            'Raikot': (35.4913, 74.5914),
            'Thakot': (34.7500, 72.9167),
            'Abbottabad': (34.7500, 72.9167),
            'Haripur': (33.9791, 72.9350),
            'D.I.khan': (31.82, 70.94),
            'Zohb': (31.3497, 69.4665),
            'Qila saifullah': (30.6951, 68.3613),
            'Quetta': (30.1834, 66.9987),
            'Matung': (29.7988, 66.8472),
            'Mogochar': (29.3495, 66.6385),
            'Kalat': (29.0523, 66.5879),
            'Surab': (28.4901, 66.2635),
            'Basima': (27.9094, 65.8739),
            'Punjgur': (26.97061, 64.0887),
            'Hoshab': (26.0155, 63.88187),
            'Gwadar': (25.1264, 62.3225),
        }
        self.vehicle_speeds = {
            'car': 60,
            'truck': 45,
            'bus': 50,
        }
        pass
    def calculate_route_distance(self, start_city, end_city):
        """Calculate distance between two CPEC cities - NOW IMPLEMENTED"""
        if start_city not in self.cpec_route or end_city not in self.cpec_route:
            return "City not found in CPEC route"
        
        start_coords = self.cpec_route[start_city]
        end_coords = self.cpec_route[end_city]

        distance = geodesic(start_coords, end_coords).kilometers
        return round(distance, 2)

    def calculate_travel_time(self, start_city, end_city, vehicle_type='car'):
        """calculate estimated travel time between cities - FIXED!"""
        distance = self.calculate_route_distance(start_city, end_city)

        if isinstance(distance, str):
            return distance 
        avg_speed = self.vehicle_speeds.get(vehicle_type, 60)
        time_hours = distance / avg_speed

        hours = int(time_hours)
        minutes = int((time_hours -hours) *60)

        return hours, minutes 
    def format_time(self, hours, minutes):
        """Format time in a readable way - ADDED THIS METHOD!"""
        if hours == 0:
            return f"{minutes} minutes"
        elif minutes == 0:
            return f"{hours} hours"
        else:
            return f"{hours}h {minutes}m"
        
    def get_detailed_route_info(self, start_city, end_city):
        """Get both distance and time in one function - FIXED!"""
        distance = self.calculate_route_distance(start_city, end_city)
        hours, minutes = self.calculate_travel_time(start_city, end_city, 'car')
        time_str = self.format_time(hours, minutes)

        return {
            'route': f"{start_city}  {end_city}",
            'distance_km': distance,
            'estimated_time': time_str,
            'vehicle_type': {
                'car': self.format_time(*self.calculate_travel_time(start_city, end_city, 'car')),
                'truck':self.format_time(*self.calculate_travel_time(start_city, end_city, 'truck')),
                'bus':self.format_time(*self.calculate_travel_time(start_city, end_city, 'bus')),
            }
        }
    def create_visual_route_map(self, start_city, end_city):
        """Create an interactive map showing the route"""
        try:
            
            m = folium.Map(location=[30.3753, 69.3451], zoom_start=6)
            
            cities_in_order = list(self.cpec_route.keys())

            if start_city not in cities_in_order or end_city not in cities_in_order:
                return None
            
            start_index = cities_in_order.index(start_city)
            end_index = cities_in_order.index(end_city)
            
            if start_index > end_index:
                start_index, end_index = end_index, start_index
            
            route_cities = cities_in_order[start_index:end_index+1]

            for city in route_cities:
                folium.Marker(
                    self.cpec_route[city],
                    popup=city,
                    tooltip=city,
                    icon=folium.Icon(color='green', icon='info-sign')
                ).add_to(m)
            
            route_coords = [self.cpec_route[city] for city in route_cities]
            folium.PolyLine(route_coords, color="black", weight=3, opacity=0.8).add_to(m)

            distance = self.calculate_route_distance(start_city, end_city)
            if isinstance(distance, str):
                return None
            
            hours, minutes = self.calculate_travel_time(start_city, end_city, 'car')
            
            info_text = f"""
            <div style="font-family: Arial; font-size: 14px;">
                <h4>🚗 {start_city} to {end_city}</h4>
                <b>Distance:</b> {distance} km<br>
                <b>Travel Time:</b> {self.format_time(hours, minutes)} by car<br>
                <b>Route:</b> CPEC Highway
            </div>
            """
            
            folium.Marker(
                [28.0, 70.0],  
                popup=folium.Popup(info_text, max_width=300),
                icon=folium.Icon(color='green', icon='flag')
            ).add_to(m)
            
            if not os.path.exists('static/maps'):
                os.makedirs('static/maps')
            
            safe_start = start_city.replace(' ', '_')
            safe_end = end_city.replace(' ', '_')
            map_file = f"static/maps/route_map_{safe_start}_{safe_end}.html"
            m.save(map_file)
            
            return f"/maps/route_map_{safe_start}_{safe_end}.html"
            
        except Exception as e:
            print(f"Map creation error: {e}")
            return None
    
if __name__ == "__main__":
    nav = CPECNavigator()
     
    
    
    print("=== DEBUG: Checking Cities ===")
    print("Cities in dictionary:", list(nav.cpec_route.keys()))
    print("Looking for 'khunjrab pass':", 'khunjrab pass' in nav.cpec_route)
    print("Looking for 'Gwadar':", 'Gwadar' in nav.cpec_route)
    print("==============================\n")
    
    print("CPEC Route Navigator Ready!")

    
    distance = nav.calculate_route_distance('khunjrab pass', 'Gwadar')
    print(f"Distance: {distance}")

    if not isinstance(distance, str):
        hours, minutes = nav.calculate_travel_time('khunjrab pass', 'Gwadar', 'car')
        print(f"Travel time by car: {nav.format_time(hours, minutes)}")

        route_info = nav.get_detailed_route_info('Quetta', 'Gwadar')
        if 'error' not in route_info:
            print(f"\nComplete Route Info:")
            print(f"Route: {route_info['route']}")
            print(f"Distance: {route_info['distance_km']} km")
            print(f"Estimated time: {route_info['estimated_time']}")                  
            print(f"\nAll vehicle times from Quetta to Gwadar:")
            for vehicle, time in route_info['vehicle_type'].items():
                print(f"  {vehicle}: {time}")
        else:
            print(f"Error: {route_info['error']}")
    else:
        print(f"Error: {distance}")