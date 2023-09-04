import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QAbstractTableModel, QSortFilterProxyModel, QVariant
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


        # Create a layout for widget_2
        # widget_2_layout = QVBoxLayout()
        # self.widget_2.setLayout(widget_2_layout)
        # Create a model for the QTableView


        # Create a QTableView to display company names and dates

        # self.db_handler = DatabaseHandler(os.path.join(loc1[0], 'Database', 'MBAS.db'))


        # self.createObjects()
        initialObjects(self)
        allObjects(self)
        allSlots(self)
        intialSlots(self)


        self.login.show()
        self.hideAllFrames()

    def hideAllFrames(self):
            self.fCreateCompany.hide()

    def showCreateCompany(self):
            self.hideAllFrames()
            self.fCreateCompany.show()

    def showmaximized(self):
        self.showMaximized()  # show the window in full screen
        # self.home.show()
    #     self.login.loginSuccessful.connect(self.showHomeWindow)  # Connect the signal to the slot
    #
    # def showHomeWindow(self, user_id):
    #     home = HomeWindow(user_id)
    #     self.setCentralWidget(home)


                # self.setWindowTitle("MBAS")

        # self.title = tBar('MBAS')
        # self.gotologin1.clicked.connect(self.createObjects)

    # def createslote(self):
    #     self.login = loginFunction()


        # self.gotologin1.clicked.connect(self.LoginPage)

    # def gotologin(self):
    #     login = LoginPage()
    #     self.setCentralWidget(login)






# def main():



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UIMain()
    window.setWindowTitle("MBAS")
    window.setGeometry(100, 100, 800, 600)
    # window.show()
    # window.hide()
    app.exec()
