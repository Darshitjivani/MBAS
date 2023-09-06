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
from Applications.Views.Gateways.gateways import GatewaysWindow
import sqlite3

class BranchCreateWindow(QMainWindow):
    def __init__(self):
        super(BranchCreateWindow, self).__init__()
        loc1 = os.getcwd().split('Application')
        ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'Branch.ui')
        uic.loadUi(ui_login, self)