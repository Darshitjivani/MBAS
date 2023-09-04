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
from Applications.Views.CompanyCreate.company_create import CompanyCreateWindow


class HomeWindow(QMainWindow):
    def __init__(self):
        super(HomeWindow, self).__init__()
        loc1 = os.getcwd().split('Application')
        ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'HomeWindow.ui')
        uic.loadUi(ui_login, self)
        # self.setWindowFlag(Qt.FramelessWindowHint)
        # self.fCreateCompany.hide()








        # self.user_id = userid
        # self.create_company.clicked.connect(self.companyCreateFunction)

        #
    # def companyCreateFunction(self):
    #     print("Hello")
    #     try:
    #
    #         company_create = CompanyCreateWindow(userid=1)
    #         print(company_create)
    #     except Exception as e:
    #         print(e)
    #
    #
    #     self.setCentralWidget(company_create)

# if __name__ == '__main__':
#     import sys
#     app = QApplication(sys.argv)
#     window = HomeWindow()
#     window.show()
#
#     # window.show()
#     # window.hide()
#     app.exec()