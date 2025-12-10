from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from pyshorteners import Shortener

from PyQt5.QtGui import QIcon, QPixmap

import qrcode

from notifypy import Notify
# python -m pip install -r requirements.txt

def CREATE_SHORT_URL(url):
    link = Shortener()

    return link.tinyurl.short(url)

# GENERATE QR CODE
def run_example(url, *args, **kwargs):
    """
    Build an example QR Code and display it.

    There's an even easier way than the code here though: just use the ``make``
    shortcut.
    """
    qr = qrcode.QRCode(*args, **kwargs)
    qr.add_data(url)

    im = qr.make_image()
    im.show()
# -------------------------

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("interfaceQr.ui", self)
        self.show()


        self.text_url = ''
        self.text_short = ''

        self.generateQr.clicked.connect(self.setText)

    def getURL(self):
        return self.textUrl.text()
    
    def setURLshort(self):
        self.textShort.setText(self.text_url)

    
    def setText(self):

        if not self.getURL():
            notify = Notify()
            notify.title = "Error"
            notify.message = "Please enter a valid URL"
            notify.send()
            return

        else:
            self.text_url = CREATE_SHORT_URL(self.getURL())
            print(self.text_url)

            run_example(self.text_url)

            self.setURLshort()

    def setQrcode(self):
        pixmap = QPixmap('qrcode.png')
        self.img.setPixmap(pixmap)



if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    app.exec_()
    
