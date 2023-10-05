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
from Themes.dt3 import dt3

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget, QWidget, QPushButton
from PyQt5.QtCore import Qt

class AlterMasterListWindow(QMainWindow):
    def __init__(self):
        super(AlterMasterListWindow, self).__init__()

        # Load your UI and set window flags
        loc1 = os.getcwd().split('Application')
        ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'AlterMasterList.ui')
        uic.loadUi(ui_login, self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet(dt3)
        self.hideAllFrames()

    def hideAllFrames(self):
        self.fAlterGroup.hide()
        self.fAlterLedger.hide()
        self.fAlterBranch.hide()

    def showAlterGroup(self):
        self.hideAllFrames()
        self.fAlterGroup.show()


    def showAlterLedger(self):
        self.hideAllFrames()
        self.fAlterLedger.show()

    def showAlterBranch(self):
        self.hideAllFrames()
        self.fAlterBranch.show()