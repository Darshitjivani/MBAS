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

class HomeWindow(QMainWindow):
    def __init__(self):
        super(HomeWindow, self).__init__()
        loc1 = os.getcwd().split('Application')
        ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'HomeWindow.ui')
        uic.loadUi(ui_login, self)

        self.label2 = QLabel("Click me!")
        self.label2.setOpenExternalLinks(True)
        self.label2.linkActivated.connect(self.on_link_activated)

    def on_link_activated(self, link):
        # Implement the action you want to perform when the text is clicked
        print("Text clicked:", link)