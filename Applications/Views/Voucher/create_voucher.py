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
from Applications.Utils.support import saveVoucherData
from Applications.Views.Gateways.gateways import GatewaysWindow
import sqlite3

from Applications.Views.Voucher.modelVoucher import ModelVoucher
from Applications.Views.Voucher.table import Terminal



# class ComboBoxDelegate(QItemDelegate):
#     def __init__(self, parent=None):
#         super(ComboBoxDelegate, self).__init__(parent)
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
        # self.lastSerialNo=0
        # self.initUI()
        # self.tables_details_TWM()
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
    #             self.table[self.lastSerialNo] = [v1, v2, v3, v4, self.lastSerialNo]
    #             self.lastSerialNo += 1
    #             self.model.lastSerialNo += 1
    #             self.model.insertRows()
    #             self.model.rowCount()
    #             ind = self.model.index(0, 0)
    #             ind1 = self.model.index(0, 1)
    #             self.model.dataChanged.emit(ind, ind1)
    #             # Check if the sum of "Debit" and "Credit" columns is equal
    #
    #             # debit_sum = np.sum(self.table[:self.lastSerialNo, 3].astype(float))
    #             # print("debit sum:", debit_sum)
    #             # credit_sum = np.sum(self.table[:self.lastSerialNo, 2].astype(float))
    #             # print("credit sum:", credit_sum)
    #             #
    #             # if debit_sum == credit_sum:
    #             #     # Disable further insertion of rows
    #             #     self.pbAdd.setEnabled(False)
    #             #     print("sum of both is same.")
    #
    #             # print(self.table)
    #         print("data table :",self.table)
    #     except:
    #         print(traceback.print_exc())

    # def tables_details_TWM(self):
    #     try:
    #
    #         self.heads = ['UserID', 'perticular', 'Credit', 'Debit', "serialno"]
    #
    #         self.visibleColumns = len(self.heads)
    #         self.table = np.zeros((20000, len(self.heads)), dtype=object)
    #         self.model = ModelVoucher(self.table, self.heads)
    #         self.smodel = QSortFilterProxyModel()
    #         self.smodel.setSourceModel(self.model)
    #         self.tableView.setModel(self.smodel)
    #
    #         # Set the combo box delegate for the desired column (e.g., column 2)
    #         # combo_delegate = ComboBoxDelegate(self)
    #         # self.tableView.setItemDelegateForColumn(1, combo_delegate)
    #
    #         self.smodel.setDynamicSortFilter(False)
    #         self.smodel.setFilterKeyColumn(0)
    #         self.smodel.setFilterCaseSensitivity(False)
    #         #############################################
    #         self.tableView.horizontalHeader().setSectionsMovable(True)
    #         self.tableView.verticalHeader().setSectionsMovable(True)
    #         self.tableView.verticalHeader().setFixedWidth(30)
    #         self.tableView.setContextMenuPolicy(Qt.CustomContextMenu)
    #         self.tableView.setDragDropMode(self.tableView.InternalMove)
    #         self.tableView.setDragDropOverwriteMode(False)
    #
    #         self.tableView.hideColumn(4)
    #         # self.tableView.hideColumn(0)
    #         # for row in range(self.model.rowCount()):
    #         #     combo_box = QComboBox()
    #         #     combo_box.addItems(['cell11', 'cell12', 'cell13', 'cell14', 'cell15'])
    #             # self.tableView.setCellWidget(row, 2, combo_box)  # Set the combo box widget
    #
    #         # self.tableView.clicked.connect(self.cellClicked)
    #
    #     except:
    #         print(traceback.print_exc())

    # def cellClicked(self, index):
    #     row = index.row()
    #     col = index.column()
    #
    #     if col == 3:
    #         # Debit column is clicked, check if the corresponding credit cell is empty
    #         credit_index = self.model.index(row, col + 1)
    #         credit_data = self.model.data(credit_index, Qt.DisplayRole)
    #         if credit_data is None or credit_data == '':
    #             # Add a new row for credit if it's empty
    #             self.model.insertRow(row + 1)
    #
    #     elif col == 4 and row > 0:
    #         # Credit column is clicked, check if the corresponding debit cell is empty
    #         debit_index = self.model.index(row, col - 1)
    #         debit_data = self.model.data(debit_index, Qt.DisplayRole)
    #
    #         if debit_data is None or debit_data == '':
    #             # Add a new row for debit if it's empty
    #             self.model.insertRow(row + 1)
    # def submitClicked(self):
    #     try:
    #         # Call the saveVoucherData function when the "Submit" button is clicked
    #         saveVoucherData(self.table, self)
    #     except:
    #         print(traceback.print_exc())

    #
    # def keyPressEvent(self, event):
    #     try:
    #         print("hello")
    #         if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
    #             print("hello : y")
    #             self.AddRow()
    #             # Calculate the sum of "Debit" and "Credit" columns
    #             debit_sum = np.sum(self.table[:self.lastSerialNo, 3].astype(float))
    #             print("debit sum:", debit_sum)
    #             credit_sum = np.sum(self.table[:self.lastSerialNo, 2].astype(float))
    #             print("credit sum:", credit_sum)
    #
    #             if debit_sum == credit_sum:
    #                 # Disable further insertion of rows
    #                 self.pbAdd.setEnabled(False)
    #                 print("sum of both is same.")
                # debit_sum = np.sum(self.table[:self.lastSerialNo, 3].astype(float))
                # credit_sum = np.sum(self.table[:self.lastSerialNo, 2].astype(float))
                #
                # if debit_sum == credit_sum:
                #     print("Sum of Debit and Credit is equal. Further insertions disabled.")
                # else:
                #     print("Sum of Debit and Credit is not equal. Allowing insertion.")
                #     self.AddRow()  # Add a new row when the Enter key is pressed
                # self.model.insertRows(self.model.rowCount(), 1)
        # except:
        #     print(traceback.print_exc())

    # def initUI(self):
    #     # Create a QStandardItemModel
    #     data = [["" for _ in range(4)] for _ in range(4)]  # Initialize with empty data
    #     heads = ["Column 1", "Column 2", "Column 3", "Column 4"]
    #     model = ModelVoucher(data, heads)
    #     # model = ModelVoucher(4, 4)
    #     # for row in range(4):
    #     #     for column in range(4):
    #     #         item = ModelVoucher("row %d, column %d" % (row, column))
    #     #         model.setItem(row, column, item)
    #
    #     # Create a QTableView and set the model
    #     self.tableView = QTableView()
    #     self.tableView.setModel(model)
    #
    #     # Add a combo box to the third column (column index 2) in each row
    #     for row in range(4):
    #         combo_box = QComboBox()
    #         combo_box.addItems(['cell11', 'cell12', 'cell13', 'cell14', 'cell15'])
    #         index = model.index(row, 2)
    #         self.tableView.setIndexWidget(index, combo_box)
    #
    #     # Create a central widget for the main window
    #     central_widget = QWidget(self)
    #     layout = QVBoxLayout()
    #     layout.addWidget(self.tableView)
    #     central_widget.setLayout(layout)
    #     self.setCentralWidget(central_widget)
    #
    #
