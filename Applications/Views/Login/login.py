import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QAbstractTableModel, QSortFilterProxyModel
import csv
# from tabletask import Ui_MainWindow
import os
from PyQt5 import uic
from PyQt5 import *
import qdarkstyle
import traceback
import numpy as np
from qtpy import QtCore

# from model import ModelTS
from Applications.Views.Home.home import HomeWindow
import sqlite3

from Applications.Utils.config_reader import *



class LoginWindow(QMainWindow):

    def __init__(self):
        super(LoginWindow, self).__init__()
        loc1 = os.getcwd().split('Application')
        ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'Login.ui')
        uic.loadUi(ui_login, self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # self.setAttribute(Qt.WA_TranslucentBackground)

        self.setGeometry(100, 100, 800, 600)


        self.initVaribles()

        # self.db_handler = db_handler


        # self.passwordfield.setEachoMode(QtWidgets.QLineEdit.Password)
        # self.loginfunction()
        # self.show()
        # allSlots(self)
        # self.gotologin.clicked.connect(self.loginFunction)

    def initVaribles(self):
        userId,password=readConfig()

        self.leUserName.setText(userId)
        self.lePassword.setText(password)

    #     self.ckSavedata.stateChanged.connect(self.updateConfig)
    #
    # def updateConfig(self, state):
    #     if state == Qt.Checked:
    #         print("hello")
    #         userId = self.leUserName.text()
    #         print(userId)
    #         password = self.lePassword.text()
    #         print(password)
    #         self.updateConfig(userId, password)



