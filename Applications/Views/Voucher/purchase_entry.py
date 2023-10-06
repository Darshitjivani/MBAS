import os
from PyQt5 import uic
from PyQt5.QtGui import QMouseEvent

from Themes.dt3 import dt3
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication


class PurchaseEntryWindow(QMainWindow):
    def __init__(self, lbDate=None):
        super(PurchaseEntryWindow, self).__init__()

        # Load your UI and set window flags
        loc1 = os.getcwd().split('Application')
        ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'PurchaseEntry.ui')
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
    #     self.dragging = False
    #     self.offset = None
    # def mousePressEvent(self, event):
    #     if event.buttons() == Qt.LeftButton and self.label_3.geometry().contains(event.pos()):
    #         self.dragging = True
    #         self.offset = event.pos()
    #
    # def mouseMoveEvent(self, event):
    #     if self.dragging:
    #         self.move(event.globalPos() - self.offset)
    #
    # def mouseReleaseEvent(self, event):
    #     if event.button() == Qt.LeftButton:
    #         self.dragging = False
    #         self.offset = None