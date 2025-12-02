import qrcode # type: ignore

def generate_qr(data, filename):
    img = qrcode.make(data)
    img.save(filename)
    print(f"QR Code saved as {filename}")

while True:
    print("\n--- QR Code Generator ---")
    print("1. URL")
    print("2. Text")
    print("3. contact (vCard)")
    print("4. Wi-Fi")
    print("5. Email")
    print("6. Phone")
    print("7. payment QR")
    print("8. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        url = input("Enter URL: ")
        generate_qr(url, "url_qr.png")

    elif choice == "2":
        text = input("Enter text: ")
        generate_qr(text, "text_qr.png")

    elif choice == "3":
        name = input("Full Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
END:VCARD"""
        generate_qr(vcard, "contact_qr.png")

    elif choice == "4":
        ssid = input("WiFi Name: ")
        password = input("Password: ")
        security = input("Security (WPA/WEP/nopass): ")
        wifi = f"WIFI:T:{security};S:{ssid};P:{password};;"
        generate_qr(wifi, "wifi_qr.png")

    elif choice == "5":
        email_addr = input("Email: ")
        subject = input("Subject: ")
        body = input("message: ")
        mailto = f"mailto:{email_addr}?subject={subject}&body={body}"
        generate_qr(mailto, "email_qr.png")

    elif choice == "6":
        phone = input("Phone Number: ")
        tel = f"tel:{phone}"
        generate_qr(tel, "phone_qr.png")
        
    elif choice == "7":
        print("\npayment QR Options:")
        print("1. EasyPaisa payment Link")
        print("2. JazzCash payment Link")
        print("3. Bank Payment Link")
        print("4. Any Other Payment URL")

        pay_choice = input("Choose payment option: ")

        if pay_choice == "1":
            pay_url = input("Enter Your EasyPaisa URL: ")
            generate_qr(pay_url, "easypaisa_qr.png")

        elif pay_choice == "2":
            pay_url = input("Enter Your JazzCash URL: ")
            generate_qr(pay_url, "jazzcash_qr.png")

        elif pay_choice == "3":
            pay_url = input("Enter Your bank payment link: ")
            generate_qr(pay_url, "bank_payment_qr.png")
        elif pay_choice == "4":
            pay_url = input("Enter any payment URL: ")
            generate_qr(pay_url, "payment_qr.png")
        else:
            print("Invalid choice.")

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")