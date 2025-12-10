from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

class Interface (QMainWindow):
    def __init__(self):
        super(Interface, self).__init__()
        loadUi("interfaceQr.ui", self)
        self.show()