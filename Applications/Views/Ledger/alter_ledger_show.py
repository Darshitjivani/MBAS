import os
from PyQt5 import uic
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from Themes.dt3 import dt3


class AlterLedgerWindow(QMainWindow):
    def __init__(self):
        super(AlterLedgerWindow, self).__init__()

        # Load your UI and set window flags
        loc1 = os.getcwd().split('Application')
        ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'LedgerUpdate.ui')
        uic.loadUi(ui_login, self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet(dt3)
        self.dragging = False
        self.offset = None


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