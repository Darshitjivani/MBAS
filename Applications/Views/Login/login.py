from PyQt5 import uic
from qtpy import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent, QKeySequence
from PyQt5.QtWidgets import QMainWindow, QShortcut
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
        self.createShortcuts()
        self.dragging = False
        self.offset = None
        self.click = 0


        #-------------------------------- by default hide password ---------------------------------------#
        self.lePassword.setEchoMode(self.lePassword.Password)
        self.pbhide.clicked.connect(self.hidePass)

    def hidePass(self):
        self.click += 1
        if self.click % 2 == 1:
            self.lePassword.setEchoMode(self.lePassword.Normal)
        else:
            self.lePassword.setEchoMode(self.lePassword.Password)

    def createShortcuts(self):
        self.quitSc = QShortcut(QKeySequence('Esc'), self)
        self.quitSc.activated.connect(self.close)
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



