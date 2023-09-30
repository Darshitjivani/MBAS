import os
from PyQt5 import uic
from PyQt5.QtGui import QKeySequence

from Themes.dt3 import dt3
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QShortcut


class DateFilterInDayBookWindow(QMainWindow):
    def __init__(self):
        super(DateFilterInDayBookWindow, self).__init__()

        # Load your UI and set window flags
        loc1 = os.getcwd().split('Application')
        ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'DateFilterInDayBook.ui')
        uic.loadUi(ui_login, self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet(dt3)
        self.createShortcuts()


    def createShortcuts(self):
        self.quitSc = QShortcut(QKeySequence('Esc'), self)
        self.quitSc.activated.connect(self.hide)