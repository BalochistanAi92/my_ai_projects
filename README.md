## Projects

### 1. Text Analyzer
- Basic text analysis and word counting

### 2. Advanced Text Analyzer  
- Enhanced analysis with first/last word detection
### 3. 🌐 URL QR Code Generator

A fast and lightweight Python tool to generate QR codes for URLs. Perfect for quickly sharing links in a physical format.

## ✨ Features
*   **Instant Generation**: Convert any URL to a QR code in seconds.
*   **Simple CLI/GUI**: Use via command line or a clean graphical interface.
*   ---

### 4.: All Kind QR Codes Generator**
This is for your advanced, multi-format project. Save it as **`README.md`** in its project folder.

```markdown
# 🎨 All Kind QR Codes Generator

An advanced, feature-rich application to generate QR codes for various data types: contact details (vCard), WiFi credentials, plain text, emails, and more.
## 📱 Supported QR Code Types
| Type | Format | Description |
| :--- | :--- | :--- |
| **WiFi Network** | `WIFI:S:SSID;T:WPA;P:Pass;;` | Share your WiFi access securely. |
| **Contact (vCard)** | `VCARD` data | Create scannable digital business cards. |
| **Email** | `mailto:` | Pre-fill recipient, subject, and body. |
| **Plain Text** | Raw text | Encode any textual information. |

## 🧩 Modules & Architecture
This project demonstrates **modular software design**:
*   `generator/core.py` – Base QR generation logic.
*   `generator/formats/` – Specialized modules (wifi.py, vcard.py, etc.).
*   `ui/app.py` – Unified graphical interface (Flask/Tkinter)


