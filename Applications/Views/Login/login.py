from PyQt5 import uic
from qtpy import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QMainWindow
from Applications.Utils.config_reader import *



class LoginWindow(QMainWindow):

    def __init__(self):
        super(LoginWindow, self).__init__()
        loc1 = os.getcwd().split('Application')
        ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'Login.ui')
        uic.loadUi(ui_login, self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setGeometry(350, 100, 800, 600)
        self.initVaribles()

        self.dragging = False
        self.offset = None
    def initVaribles(self):
        userId,password=readConfig()

        self.leUserName.setText(userId)
        self.lePassword.setText(password)

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



