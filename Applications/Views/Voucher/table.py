import platform
from PyQt5 import uic
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtWidgets import *
import qdarkstyle
import os
from Themes.dt3 import dt3
import numpy as np
from PyQt5.QtGui import QIcon, QKeySequence, QMouseEvent


class Terminal(QMainWindow):
    def __init__(self):

        super(Terminal, self).__init__()
        self.osType = platform.system()
        loc1 = os.getcwd().split('Application')
        ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'table.ui')
        uic.loadUi(ui_login, self)
        dark = qdarkstyle.load_stylesheet_pyqt5()
        self.setStyleSheet(dt3)
        self.lastSerialNo = 0
        self.dragging = False
        self.offset = None

        osType = platform.system()
        if (osType == 'Darwin'):
            flags = Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        else:
            flags = Qt.WindowFlags(Qt.SubWindow | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)

        self.pbcancel.clicked.connect(self.hide)
        self.createShortcuts()

    def movWin(self, x, y):
        self.move(self.pos().x() + x, self.pos().y() + y)


    def createShortcuts(self):
        self.quitSc = QShortcut(QKeySequence('Esc'), self)
        self.quitSc.activated.connect(self.hide)

    def my_function(self):
        print("Button clicked and function called!")

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            # Calculate the offset between the mouse click and the window position
            self.offset = event.globalPos() - self.pos()
            self.dragging = True


    def mouseMoveEvent(self, event: QMouseEvent):
        if self.dragging:
            # Move the window with the mouse while dragging
            self.move(event.globalPos() - self.offset)


    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            # Stop dragging when the left mouse button is released
            self.dragging = False
            self.offset = None