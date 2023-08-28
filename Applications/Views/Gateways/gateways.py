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


class GatewaysWindow(QMainWindow):
    def __init__(self):
        super(GatewaysWindow, self).__init__()
        loc1 = os.getcwd().split('Application')
        ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'Gateways.ui')
        uic.loadUi(ui_login, self)

        # self.setAttribute(Qt.WA_TranslucentBackground)

        self.lbTitle = self.findChild(QLabel, 'lbTitle')  # Assuming lbTitle is the object name of your QLabel

    def updateTitleLabel(self, company_name):
        self.lbTitle.setText(f"Welcome to {company_name}")

    # def initveriable(self):
