import os
import traceback
from Themes.dt3 import dt3
import numpy as np
from PyQt5 import uic
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt, QSortFilterProxyModel

from Applications.Views.DayBook.model_day_book import ModelDBK


class DayBookWindow(QMainWindow):
    def __init__(self):
        super(DayBookWindow, self).__init__()

        # Load your UI and set window flags
        loc1 = os.getcwd().split('Application')
        ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'DayBook.ui')
        uic.loadUi(ui_login, self)
        # self.setWindowFlag(Qt.FramelessWindowHint)
        # self.dragging = True
        # self.offset = None
        self.last_serialno = 0
        # self.initUI()
        self.tables_details_DBK()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet(dt3)

    def tables_details_DBK(self):
        try:

            self.heads = ['Date', 'particular', 'Voucher Type']
            self.visibleColumns = len(self.heads)
            self.table = np.zeros((2000, len(self.heads)), dtype=object)
            self.model = ModelDBK(self.table, self.heads)
            self.smodel = QSortFilterProxyModel()
            self.smodel.setSourceModel(self.model)
            self.tableView.setModel(self.smodel)
            self.smodel.setDynamicSortFilter(False)
            self.smodel.setFilterKeyColumn(0)
            self.smodel.setFilterCaseSensitivity(False)
            #############################################
            self.tableView.horizontalHeader().setSectionsMovable(True)
            self.tableView.verticalHeader().setSectionsMovable(True)
            self.tableView.verticalHeader().setFixedWidth(30)
            self.tableView.setContextMenuPolicy(Qt.CustomContextMenu)
            self.tableView.setDragDropMode(self.tableView.InternalMove)
            self.tableView.setDragDropOverwriteMode(False)
        except:
            print(traceback.print_exc())
