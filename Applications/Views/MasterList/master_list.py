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

class MasterListWindow(QMainWindow):
    def __init__(self):
        super(MasterListWindow, self).__init__()

        # Load your UI and set window flags
        loc1 = os.getcwd().split('Application')
        ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'CreateMasterList.ui')
        uic.loadUi(ui_login, self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet(dt3)
        self.hideAllFrames()

    def hideAllFrames(self):
        self.fLedger.hide()
        self.fGroup.hide()
        self.fBranch.hide()

    def showCreateGroup(self):
        self.hideAllFrames()
        self.fGroup.show()


    def showCreateLadger(self):
        self.hideAllFrames()
        self.fLedger.show()

    def showCreateBranch(self):
        self.hideAllFrames()
        self.fBranch.show()
