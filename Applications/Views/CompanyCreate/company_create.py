from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QAbstractTableModel, QSortFilterProxyModel, QRegExp
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

import sqlite3

class CompanyCreateWindow(QMainWindow):
    def __init__(self):
        super(CompanyCreateWindow, self).__init__()
        loc1 = os.getcwd().split('Application')
        ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'CompanyCreate.ui')
        uic.loadUi(ui_login, self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet(dt3)

        # Create and set a QRegExpValidator for text fields
        text_pattern = QRegExp("^[A-Za-z]*$")
        text_validator = QRegExpValidator(text_pattern)
        email_pattern = r'^[\w\d\.-]+@[\w\.-]+\.\w+$'
        # Create a QRegExpValidator with the custom pattern
        email_validator = QRegExpValidator(QRegExp(email_pattern))

        # Create and set a QIntValidator for integer fields
        int_validator = QIntValidator()
        website_pattern = QRegExp("^[A-Za-z0-9\s\-\(\)_]+$")
        website_validator = QRegExpValidator(website_pattern)
        self.leComapnyName.setValidator(text_validator)
        self.leMobile.setValidator(int_validator)
        self.leMailingName.setValidator(text_validator)

        self.leState.setValidator(text_validator)
        self.leCountry.setValidator(text_validator)
        self.lePincode.setValidator(int_validator)
        self.leFax.setValidator(int_validator)
        self.leEmail.setValidator(email_validator)
        self.leWebsite.setValidator(website_validator)
        self.leCurrencySymbol.setValidator(text_validator)
        self.leFormalName.setValidator(text_validator)


