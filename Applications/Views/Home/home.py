import platform
import traceback

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QAbstractTableModel, QSortFilterProxyModel
import csv
# from tabletask import Ui_MainWindow
import os
from PyQt5 import uic
from Themes.dt3 import dt3



class HomeWindow(QMainWindow):
    def __init__(self, ):
        super(HomeWindow, self).__init__()
        loc1 = os.getcwd().split('Application')
        ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'HomeWindow.ui')
        uic.loadUi(ui_login, self)
        self.setStyleSheet(dt3)

        # self.maxwin = True
    #     self.pbMaximized.clicked.connect(self.showmaxORnormal)
    # def showmaxORnormal(self):
    #     if self.isMaximized():
    #         self.showNormal()
    #     else:
    #         self.showMaximized()



