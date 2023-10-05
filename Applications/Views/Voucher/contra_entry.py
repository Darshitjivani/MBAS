import os
from PyQt5 import uic
from PyQt5.QtGui import QMouseEvent

from Applications.Views.TrialBalance.modeltrialbal import ModelTB
from Themes.dt3 import dt3
from PyQt5.QtCore import Qt, QSortFilterProxyModel, QDate
from PyQt5.QtWidgets import QMainWindow, QMenu, QFileDialog, QApplication, QTableView


class ContraEnteryWindow(QMainWindow):
    def __init__(self):
        super(ContraEnteryWindow, self).__init__()

        # Load your UI and set window flags
        loc1 = os.getcwd().split('Application')
        ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'ContraEntry.ui')
        uic.loadUi(ui_login, self)
        self.setStyleSheet(dt3)
        self.setWindowFlags(Qt.FramelessWindowHint| Qt.Popup)

        desktop = QApplication.primaryScreen()
        screen_geometry = desktop.geometry()
        window_geometry = self.geometry()
        x = (screen_geometry.width() - window_geometry.width()) // 2
        y = (screen_geometry.height() - window_geometry.height()) // 2
        self.move(x, y)

        # ----------------------------------- For Window Movement ----------------------------------$
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
