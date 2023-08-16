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
# from model import ModelTS
from Applications.Views.Home.home import HomeWindow

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        loc1 = os.getcwd().split('Application')
        ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'Login.ui')
        uic.loadUi(ui_login, self)

        # self.passwordfield.setEachoMode(QtWidgets.QLineEdit.Password)
        self.gotologin.clicked.connect(self.loginfunction)
    #
    def loginfunction(self):

        home = HomeWindow()
        self.setCentralWidget(home)
        # self.gotologin.clicked.connect(self.loginfunction)
        # user = self.emailfield.text()
        # password = self.passwordfield.text()
        #
        # if len(user) == 0 and len(password)==0:
        #     self.error.setText("Please input all feild.")
