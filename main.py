from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFileDialog
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
from pyshorteners import Shortener1
import pyshorteners.tinyurl
from iptracker import IPTracker
import sys
from flask import Flask
from os import path

from PyQt5.QtGui import QIcon, QPixmap

import qrcode

from notifypy import Notify
# python -m pip install -r requirements.txt

def CREATE_SHORT_URL(url):
    link = Shortener1()

    return link.tinyurl.short(url)

# GENERATE QR CODE
def run_example(url, *args, **kwargs):
    """
    Build an example QR Code and display it.

    There's an even easier way than the code here though: just use the ``make``
    shortcut.
    """
    qr = qrcode.QRCode(*args, **kwargs, box_size=8)
    qr.add_data(url)

    im = qr.make_image()
    im.save("qrcode.png")
# -------------------------

# IPGRABBER
# def ipGrabber(url):
#     username = 'henriq'
#     password = '123456'
#     redirectUrl = url
#     tracker = IPTracker(username, password, redirectUrl)
#     print(tracker.create_account())
#     print(tracker.login())
#     tracking_link = tracker.generate_link()
#     print("Tracking Link:", tracking_link)

def loadFile(file):
    base_path = getattr(sys, "_MEIPASS", path.dirname(path.abspath(__file__)))
    return path.join(base_path, file)

def getPath(localPath):
    return f"{'a'}"


app = Flask(__name__)

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi(loadFile("./interfaceQr.ui"), self)
        self.show()

        self.text_url = ''
        self.text_short = ''

        self.generateQr.clicked.connect(self.setText)
        self.generateQr.clicked.connect(self.setQrcode)
        self.saveQr.clicked.connect(self.saveQrCode)

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

            # ipGrabber(self.text_url)

            self.setURLshort()

            self.saveQr.setEnabled(True)

    def setQrcode(self):
        pixmap = QPixmap('qrcode.png')
        self.img.setPixmap(pixmap)

    # @pyqtSlot()
    # def on_saveQr_clicked(self):
    #     self.saveQr()

    def saveQrCode(self):
        archieve, _ = QFileDialog.getSaveFileName(self, "Save image")
        if archieve:
            pathway = path.dirname(archieve)

            name = archieve.removeprefix(pathway)

            with open('qrcode.png', 'rb') as photo:
                data = photo.read()

            # saving file located by user
            with open(pathway +f'{name}.png', 'wb') as op:
                op.write(data)
    # def saveQrcode(self):


if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    app.exec_()
    
