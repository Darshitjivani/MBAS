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

from Applications.Views.Login.login import LoginWindow
from Applications.Utils.execute_support import *


class UIMain(QMainWindow):
    def __init__(self):
        super(UIMain, self).__init__()
        loc1 = os.getcwd().split('Application')
        ui_main = os.path.join(loc1[0], 'Resources', 'UI', 'Welcom_screen.ui')
        uic.loadUi(ui_main, self)

        # self.createObjects()
        initialObjects(self)
        self.login.show()
        # self.gotologin1.clicked.connect(self.createObjects)

    # def createObjects(self):
    #     self.login=LoginPage()


        # self.gotologin1.clicked.connect(self.LoginPage)

    # def gotologin(self):
    #     login = LoginPage()
    #     self.setCentralWidget(login)






# def main():



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UIMain()
    # window.show()
    app.exec()
