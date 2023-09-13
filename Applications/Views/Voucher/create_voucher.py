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

from Applications.Views.Voucher.modelVoucher import ModelTS
from Applications.Views.Voucher.table import Terminal
# from Applications.Views.Voucher.support import accountNamesReady


# class ComboBoxDelegate(QItemDelegate):
#     def __init__(self, parent=None):
#         super(ComboBoxDelegate, self).__init__(parent)
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
#     def createEditor(self, parent, option, index):
#         combo_box = QComboBox(parent)
#         combo_box.addItems(['cell11', 'cell12', 'cell13', 'cell14', 'cell15'])
#         return combo_box

    # def updateComboBox(self, account_names):
    #     self.comboBox.clear()
    #     self.comboBox.addItems(account_names)

class CreateVoucherWindow(QMainWindow):
    def __init__(self):
        super(CreateVoucherWindow, self).__init__()
        loc1 = os.getcwd().split('Application')
        ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'CreateVoucher.ui')
        uic.loadUi(ui_login, self)
        self.setStyleSheet(dt3)

        # self.tableWidget.setColumnCount(4)  # Assuming you have 4 columns
        # self.tableWidget.setHorizontalHeaderLabels(["Dr/Cr", "Account Name", "Amount", "Currency"])

        # Set the width of each column (adjust these values as needed)
        # self.tableWidget.setColumnWidth(0, 200)  # Column 0 width
        # self.tableWidget.setColumnWidth(1, 190)  # Column 1 width
        # self.tableWidget.setColumnWidth(2, 155)  # Column 2 width
        # self.tableWidget.setColumnWidth(3, 150)  # Column 3 width
        # self.tableshow = Terminal()
        # self.pbAdd.clicked.connect(self.tableshow.show)

        self.last_serialno=0
        # self.initUI()
        self.tables_details_TWM()
        # self.window = Terminal()
        # self.pbAdd.clicked.connect(self.window.show)
        # self.window.adddata.clicked.connect(self.AddRow)

    # def AddRow(self):
    #     try:
    #         self.window.hide()
    #         v1 = self.window.line1.text()
    #         v2 = self.window.line2.text()
    #         v3 = self.window.line3.text()
    #         v4 = self.window.line4.text()
    #         # v5 = self.window.line5.text()
    #
    #         fltr = self.table[(np.where(self.table[:, 0] == v1))]
    #
    #         if fltr.size != 0:
    #             srno = fltr[0][4]
    #
    #             editlist = [1, 2, 3]
    #             self.table[srno, editlist] = [v2, v3, v4]
    #             for j in editlist:
    #                 ind = self.model.index(srno, j)
    #                 self.model.dataChanged.emit(ind, ind)
    #
    #         else:
    #             self.table[self.lastSerialNo] = [v1, v2, v3, v4]
    #             # self.last .lastSerialNo += 1
    #             self.model.insertRows()
    #             self.model.rowCount()
    #             ind = self.model.index(0, 0)
    #             ind1 = self.model.index(0, 1)
    #             self.model.dataChanged.emit(ind, ind1)
                # Check if the sum of "Debit" and "Credit" columns is equal

                # debit_sum = np.sum(self.table[:self.lastSerialNo, 3].astype(float))
                # print("debit sum:", debit_sum)
                # credit_sum = np.sum(self.table[:self.lastSerialNo, 2].astype(float))
                # print("credit sum:", credit_sum)
                #
                # if debit_sum == credit_sum:
                #     # Disable further insertion of rows
                #     self.pbAdd.setEnabled(False)
                #     print("sum of both is same.")

                # print(self.table)
        #     print("data table :",self.table)
        # except:
        #     print(traceback.print_exc())

    def tables_details_TWM(self):
        try:

            self.heads = ['Cr/Dr', 'perticular', 'Credit Amount', 'Debite Amount','Currency']
            self.visibleColumns = len(self.heads)
            self.table = np.zeros((2000, len(self.heads)), dtype=object)
            self.model = ModelTS(self.table, self.heads)
            self.smodel = QSortFilterProxyModel()
            self.smodel.setSourceModel(self.model)
            self.tableView.setModel(self.smodel)

            # Set the combo box delegate for the desired column (e.g., column 2)
            # combo_delegate = ComboBoxDelegate(self)
            # self.tableView.setItemDelegateForColumn(1, combo_delegate)

            self.smodel.setDynamicSortFilter(False)
            # self.smodel.setFilterKeyColumn(0)
            self.smodel.setFilterCaseSensitivity(False)
            #############################################
            self.tableView.horizontalHeader().setSectionsMovable(True)
            self.tableView.verticalHeader().setSectionsMovable(True)
            self.tableView.verticalHeader().setFixedWidth(30)
            self.tableView.setContextMenuPolicy(Qt.CustomContextMenu)
            self.tableView.setDragDropMode(self.tableView.InternalMove)
            self.tableView.setDragDropOverwriteMode(False)




    # #
    # #         self.tableView.hideColumn(4)
    # #         # self.tableView.hideColumn(0)
    # #         # for row in range(self.model.rowCount()):
    # #         #     combo_box = QComboBox()
    # #         #     combo_box.addItems(['cell11', 'cell12', 'cell13', 'cell14', 'cell15'])
    # #             # self.tableView.setCellWidget(row, 2, combo_box)  # Set the combo box widget
    # #
    # #         # self.tableView.clicked.connect(self.cellClicked)
        #
        except:
            print(traceback.print_exc())

