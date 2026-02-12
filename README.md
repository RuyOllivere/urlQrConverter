# urlQrConverter  

Convert any URL into a QR Code in seconds.  
Built with Qt Designer, qrcode, and notifypy.

<p align="center">
  <img src="assets/demo.gif" alt="App Demo Animation" width="600"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue.svg"/>
  <img src="https://img.shields.io/badge/Qt-QtDesigner-green.svg"/>
  <img src="https://img.shields.io/badge/License-MIT-orange.svg"/>
  <img src="https://img.shields.io/badge/Status-Active-success.svg"/>
</p>

---

## Features

- Convert any URL into a QR Code instantly  
- Modern UI built with Qt Designer  
- Desktop notifications using notifypy  
- Save QR codes as image files  
- Fast and lightweight  

---

## Built With

- PyQt5 / Qt Designer  
- qrcode  
- notifypy  

---

# Installation Guide

## 1. Clone the Repository

```bash
git clone https://github.com/rubim666/urlQrConverter.git
cd urlQrConverter
```

---

## 2. Create Virtual Environment (Recommended)

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

If you have `requirements.txt`:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install PyQt5 qrcode[pil] notifypy
```

---

## 4. Run the Application

```bash
python main.py
```

---

# Notifications

The application uses notifypy to send desktop notifications when:

- A QR code is successfully generated  
- A QR code is saved  

---

# Requirements

- Python 3.9+
- pip
- Windows / macOS / Linux

---

# Future Improvements

- Dark mode toggle  
- Custom QR colors  
- Copy QR to clipboard  
- URL validation  

---

# License

MIT License

---

# Author

Developed by @rubim666  

If you find this project useful, consider giving it a star on GitHub.
