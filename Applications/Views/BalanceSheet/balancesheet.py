import os
from PyQt5 import uic
from PyQt5.QtGui import QKeySequence

from Themes.dt3 import dt3
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QShortcut


class BalanceSheetWindow(QMainWindow):
    def __init__(self):
        super(BalanceSheetWindow, self).__init__()

        # Load your UI and set window flags
        loc1 = os.getcwd().split('Application')
        ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'BalanceSheet.ui')
        uic.loadUi(ui_login, self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet(dt3)
