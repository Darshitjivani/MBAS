import sys
import traceback
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtWidgets import QTableView
import time

from PyQt5 import QtGui
from PyQt5.QtGui import QBrush


class ModelVoucher(QtCore.QAbstractTableModel):

    def __init__(self, data, heads, isReset=False):
        super(ModelVoucher, self).__init__()
        self._data = data
        # self._data1 = data
        self.heads = heads
        if (isReset):
            self.lastSerialNo = data.shape[0]
        else:
            self.lastSerialNo = 0



    def data(self, index, role=Qt.DisplayRole | Qt.EditRole):
        try:
            value = self._data[index.row(), index.column()]
            if role == Qt.DisplayRole:
                # if index.column() in [1, 2, 3]:
                #     value = float(value)
                #     return value
                return value

            if role == Qt.DisplayRole:
                value = self._data[index.row(), index.column()]

                if index.column() in [1, 2, 3, 4]:
                    # Align right, vertical middle
                    return Qt.AlignVCenter + Qt.AlignRight

        except:
            print(traceback.print_exc())

    def setData(self, index, value, role=Qt.EditRole):
        if role in (Qt.DisplayRole, Qt.EditRole):
            # print('Edit role:', index.row(), index.column())
            # if value is blank
            if not value:
                return False
            self._data[index.row()][index.column()] = value
            self.dataChanged.emit(index, index)
        return True

    def rowCount(self, index=''):
        return self.lastSerialNo

    def columnCount(self, index):
        return len(self.heads)

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self.heads[section])

    def insertRows(self, position=0, rows=1, index=QModelIndex()):
        try:
            self.beginInsertRows(QModelIndex(), position, position + rows - 1)
            # self.beginInsertRows(QModelIndex(), self.lastSerialNo - 1, self.lastSerialNo - 1)
            self.endInsertRows()
            return True
        except:
            print(sys.exc_info())

    # def insertRows(self, position=0, rows=1, index=QModelIndex()):
    #     try:
    #         # self.beginInsertRows(QModelIndex(), position, position + rows - 1)
    #         self.beginInsertRows(QModelIndex(), self.lastSerialNo - 1, self.lastSerialNo - 1)
    #         self.endInsertRows()
    #         return True
    #     except:
    #         print(sys.exc_info())

    def insertMultiRows(self, position=0, rows=1, index=QModelIndex()):
        try:
            self.beginInsertRows(QModelIndex(), position, position + rows - 1)
            # self.beginInsertRows(QModelIndex(), self.lastSerialNo - 1, self.lastSerialNo - 1)
            self.endInsertRows()
            return True
        except:
            print(sys.exc_info())

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable

    def DelRows(self, position=0, rows=1, index=QModelIndex()):
        self.beginRemoveRows(QModelIndex(), 0, 0)
        self.endRemoveRows()
        return True

    def DelAllRows(self, position=0, rows=1, index=QModelIndex()):

        rrr = self.rowCount()
        self.beginRemoveRows(QModelIndex(), 0, rrr - 1)

        self.endRemoveRows()
        return True
