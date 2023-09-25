import os
from PyQt5 import uic

from Applications.Views.TrialBalance.modeltrialbal import ModelTB
from Themes.dt3 import dt3
from PyQt5.QtCore import Qt, QSortFilterProxyModel, QDate
from PyQt5.QtWidgets import QMainWindow, QMenu, QFileDialog, QApplication, QTableView


class ContraEnteryWindow(QMainWindow):
    def __init__(self):
        super(ContraEnteryWindow, self).__init__()

        # Load your UI and set window flags
        loc1 = os.getcwd().split('Application')
        ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'ContraEntry.ui')
        uic.loadUi(ui_login, self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet(dt3)
