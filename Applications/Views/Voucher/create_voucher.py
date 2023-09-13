from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QAbstractTableModel, QSortFilterProxyModel
import csv
# from tabletask import Ui_MainWindow
import os
from PyQt5 import uic
from Themes.dt3 import dt3
# from PyQt5 import *
# import qdarkstyle
# import traceback
# import numpy as np
# # from model import ModelTS
# from Applications.Utils.support import saveVoucherData
# from Applications.Views.Gateways.gateways import GatewaysWindow
# import sqlite3
#
# from Applications.Views.Voucher.modelVoucher import ModelVoucher
# from Applications.Views.Voucher.table import Terminal


class CreateVoucherWindow(QMainWindow):
    def __init__(self):
        super(CreateVoucherWindow, self).__init__()
        loc1 = os.getcwd().split('Application')
        ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'CreateVoucher.ui')
        uic.loadUi(ui_login, self)
        self.setStyleSheet(dt3)
