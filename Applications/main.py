import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QAbstractTableModel, QSortFilterProxyModel, QVariant, pyqtSignal
import csv
# from tabletask import Ui_MainWindow
import os
from PyQt5 import uic
from PyQt5 import *
import qdarkstyle
import traceback
import numpy as np
# from model import ModelTS
import sqlite3
from Resources.icons import icons_rc
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent, QKeySequence
from Themes.dt3 import dt3
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

from Applications.Views.Login.login import LoginWindow
from Applications.Utils.execute_support import *



class UIMain(QMainWindow):
    def __init__(self):
        super(UIMain, self).__init__()
        loc1 = os.getcwd().split('Application')
        ui_main = os.path.join(loc1[0], 'Resources', 'UI', 'HomeWindow.ui')
        uic.loadUi(ui_main, self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.pbMaximized.clicked.connect(self.showmaximized)
        self.dragging = False
        self.offset = None
        # self.createShortcuts()


        # self.createObjects()
        initialObjects(self)
        # allObjects(self)
        # allSlots(self)
        intialSlots(self)


        self.login.show()
        self.hideAllFrames()
        # self.lbLanding.show()

        self.maxwin = True

        self.pbMaximized.clicked.connect(self.showmaxORnormal)
        self.pbMinimized.clicked.connect(self.showminimized)

        self.setStyleSheet(dt3)

    #
    def showminimized(self):
        self.showMinimized()  # show the window in minimized screen


    def showmaxORnormal(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()


    def hideAllFrames(self):
        self.fCreateCompany.hide()

    def showCreateCompany(self):
        self.hideAllFrames()
        self.fCreateCompany.show()
        # self.flogo.hide()
        # self.lbLanding.hide()




    def showmaximized(self):
        self.showMaximized()  # show the window in full screen

    #----------------------------------- Show List Of Company --------------------------------#
    def showEvent(self, event):
        super().showEvent(event)
        listOfCompany(self)


    #---------------------------------- Movement of window ----------------------------------#

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

    #----------------------------- Shortcut For Close ------------------------------------#

    # def createShortcuts(self):
    #     self.quitSc = QShortcut(QKeySequence('Esc'), self)
    #     self.quitSc.activated.connect(self.close)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UIMain()
    window.setWindowTitle("MBAS")
    window.setGeometry(350, 100, 800, 600)
    # window.show()
    # window.hide()
    app.exec()
