from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QAbstractTableModel, QSortFilterProxyModel
import csv
# from tabletask import Ui_MainWindow
import os
from PyQt5 import uic
from PyQt5 import *
from Themes.dt3 import dt3
import qdarkstyle
import traceback
import numpy as np
# from model import ModelTS
from Applications.Views.Gateways.gateways import GatewaysWindow
import sys
import sqlite3

class CompanyCreateWindow(QMainWindow):
    def __init__(self):
        super(CompanyCreateWindow, self).__init__()
        loc1 = os.getcwd().split('Application')
        ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'CompanyCreate1.ui')
        uic.loadUi(ui_login, self)
        # self.setWindowFlag(Qt.FramelessWindowHint)
        dark = qdarkstyle.load_stylesheet()
        self.setStyleSheet(dt3)


        # dark= qdarkstyle.load_stylesheet()
        # self.setStyleSheet(dt3)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CompanyCreateWindow()
    window.setWindowTitle("MBAS")
    # window.setGeometry(350, 100, 800, 600)
    window.show()
    app.exec()
