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
from Themes.dt3 import dt3
# from model import ModelTS

import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget, QWidget, QPushButton
from PyQt5.QtCore import Qt

class DayBookWindow(QMainWindow):
    def __init__(self):
        super(DayBookWindow, self).__init__()

        # Load your UI and set window flags
        loc1 = os.getcwd().split('Application')
        ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'DayBook.ui')
        uic.loadUi(ui_login, self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet(dt3)