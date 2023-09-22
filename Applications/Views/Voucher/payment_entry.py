import os
from PyQt5 import uic
from Themes.dt3 import dt3
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow


class PaymentEntryWindow(QMainWindow):
    def __init__(self, lbDate=None):
        super(PaymentEntryWindow, self).__init__()

        # Load your UI and set window flags
        loc1 = os.getcwd().split('Application')
        ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'PaymentEntry.ui')
        uic.loadUi(ui_login, self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet(dt3)