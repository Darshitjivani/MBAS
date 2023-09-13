import sys
import traceback
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtWidgets import QTableView
import time

from PyQt5 import QtGui
from PyQt5.QtGui import QBrush


import logging

import numpy as np
import sys
import traceback
from PyQt5 import QtCore
from PyQt5.QtCore import Qt,QModelIndex
from PyQt5.QtWidgets import QMessageBox




class ModelTS(QtCore.QAbstractTableModel):

    def __init__(self, data,heads,isReset=False):
        super(ModelTS, self).__init__()
        self._data = data
        # self._data1 = data
        self.heads=heads
        self.updated_row={}
        if(isReset):
            self.last_serialno = data.shape[0]
        else:
            self.last_serialno = 0


    def data(self, index, role):
        '''
         This function defines a method called data within a class.
          It is responsible for providing data and roles for items in a Qt model-view framework.
         Depending on the role, it returns either the data value,
          text representation, or alignment for a specific cell at the given index.
         :param index:
         :param role:
         :return:
                             '''
        try:

            value = self._data[index.row(), index.column()]
            if role == Qt.DisplayRole:

                if isinstance(value, int):
                    value = int(value)
                    return value
                elif isinstance(value, float):
                    if(value > 1000000):
                        value = int(value)
                    return value
                else:
                    return str(value)

            if role == Qt.TextAlignmentRole:
                value = self._data[index.row(), index.column()]

                if isinstance(value, int) or isinstance(value, float):
                    # Align right, vertical middle.
                    return Qt.AlignVCenter + Qt.AlignRight

            if role == Qt.EditRole:
                value = self._data[index.row(), index.column()]
                return str(value)




        except Exception as e:

            print(traceback.print_exc())



    def setData(self, index, value, role=None):
        '''
            setData method for a Qt model, which is triggered when data is edited.
            It checks if the edited value is different from the original and updates a dictionary called updated_row
            with the changes if the column index is 0, 1 corresponding to
            specific keys in the dictionary for a given 'Did'.


           :param index:
           :param value:
           :param role:
           :return:
                       '''
        try:

            if role == Qt.EditRole:

                if value == '':
                    return False
                    # return False
                else:
                    if value == '':
                        return False
                    else:
                        Tid = self._data[index.row()][0]
                        Uid = self._data[index.row()][1]
                        if Tid != '':
                            if Tid not in self.updated_row:
                                self.updated_row[Tid] = {}
                                self.updated_row[Tid]['1'] = Uid
                                self.updated_row[Tid]['1'] = str(value)
                            else:
                                self.updated_row[Tid]['1'] = str(value)

                    self._data[index.row()][index.column()] = str(value)
                    print("data table:",self._data)

                    return True
        except Exception as e:
            print(traceback.print_exc())
            # Client_logger.error(f"{e}", exc_info=True)


    def flags(self, index):
        '''
         The flags function  in this code defines the item flags for an item at a given index in a Qt model,
         allowing it to be selectable, enabled, and editable, all specified using bitwise OR operations on Qt flags.
         :param index:
         :return :
                             '''
        try:

            return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable
        except Exception as e:
            print(traceback.print_exc())
            # Client_logger.error(f"{e}", exc_info=True)

    def rowCount(self, index=''):
        '''
          The rowCount method returns the value of self.last_serialno, which presumably
          represents the number of rows in a data structure or container, and it accepts an optional index parameter,
          :param index:
          :return:
                              '''
        try:

            return self.last_serialno
        except Exception as e:
            print(traceback.print_exc())
            # Client_logger.error(f"{e}", exc_info=True)


    def columnCount(self, index):
        '''
            The columnCount method returns the value of self.heads, which presumably
           represents the number of rows in a data structure or container, and it accepts an optional index paramete
           :param index:
           :return:
                               '''
        try:

            return len(self.heads)
        except Exception as e:
            print(traceback.print_exc())
            # Client_logger.error(f"{e}", exc_info=True)

    def headerData(self, section, orientation, role):
        '''
          returns the header data for a specific section (column or row) based on the provided section,
          orientation, and role parameters. If the role is Qt.DisplayRole and the orientation is horizontal,
           it returns the header label as a string from the self.heads list based on the given section inde
          :param section:
          :param orientation:
          :param role:
          :return:
                              '''
        try:

            if role == Qt.DisplayRole:
                if orientation == Qt.Horizontal:
                    return str(self.heads[section])
        except Exception as e:
            print(traceback.print_exc())
            # Client_logger.error(f"{e}", exc_info=True)
    def insertRows(self, position=0, rows=1, index=QModelIndex()):
        '''
            this function  insert one row at a specified position in a Qt model view. It signals the beginning
              and end of the insertion operation using beginInsertRows and endInsertRows, respectively,
             while catching and printing any exceptions that occur during the process.
             :param position:
             :param rows:
             :param index:
             :return True:
                             '''
        try:
            # self.beginInsertRows(QModelIndex(), position, position + rows - 1)
            # self.beginInsertRows(QModelIndex(), position, position + rows - 1)
            self.beginInsertRows(QModelIndex(), self.last_serialno - 1, self.last_serialno - 1)
            self.endInsertRows()
            return True
        except Exception as e:
            print(traceback.print_exc())
            # Client_logger.error(f"{e}", exc_info=True)
    def DelRows(self, position=0, rows=0, index=QModelIndex()):
        '''
           this function  delete one row at a specified position in a Qt model view. It signals the beginning
            and end of the insertion operation using beginRemoveRows and endRemoveRows, respectively,
           while catching and printing any exceptions that occur during the process.

           :param position:
           :param rows:
           :param index:
           :return:
                               '''
        try:



            self.beginRemoveRows(QModelIndex(),position,position+rows)
            self.endRemoveRows()


            return  True
        except Exception as e:
            print(traceback.print_exc())
            # Client_logger.error(f"{e}", exc_info=True)
    #
    # def DelRows(self, position=0, rows=1, index=QModelIndex()):
    #     self.beginRemoveRows(QModelIndex(), 0, 0)
    #     self.endRemoveRows()
    #     return  True
    #

    def DelAllRows(self, position=0, rows=1, index=QModelIndex()):
        '''
            function DelAllRows attempts to remove all rows in a Qt model.
             However, it lacks the necessary logic to adjust the
            range of rows to be removed based on the provided arguments,
            :param position:
            :param rows:
            :param index:
            :return:
                                '''
        try:


            rrr = self.rowCount()
            self.beginRemoveRows(QModelIndex(),0,rrr-1)


            self.endRemoveRows()
            return  True
        except Exception as e:
            print(traceback.print_exc())
            # Client_logger.error(f"{e}", exc_info=True)

# class ModelVoucher(QtCore.QAbstractTableModel):
#     def __init__(self, data, heads, isReset=False):
#         super(ModelVoucher, self).__init__()
#         self._data = data
#         self.heads = heads
#
#     def data(self, index, role=Qt.DisplayRole | Qt.EditRole):
#         try:
#             value = self._data[index.row()][index.column()]
#             if role == Qt.DisplayRole:
#                 return value
#
#             if role == Qt.DisplayRole:
#                 value = self._data[index.row()][index.column()]
#
#                 if index.column() in [1, 2, 3, 4]:
#                     # Align right, vertical middle
#                     return Qt.AlignVCenter + Qt.AlignRight
#
#         except:
#             print(traceback.print_exc())
#
#     def setData(self, index, value, role=Qt.EditRole):
#         if role in (Qt.DisplayRole, Qt.EditRole):
#             if not value:
#                 return False
#             self._data[index.row()][index.column()] = value
#             self.dataChanged.emit(index, index)
#         return True
#
#     def rowCount(self, index=''):
#         return len(self._data)
#
#     def columnCount(self, index):
#         return len(self.heads)
#
#     def headerData(self, section, orientation, role):
#         if role == Qt.DisplayRole:
#             if orientation == Qt.Horizontal:
#                 return str(self.heads[section])
#
#     def insertRows(self, position=0, rows=1, index=QModelIndex()):
#         try:
#             self.beginInsertRows(QModelIndex(), position, position + rows - 1)
#             self.endInsertRows()
#             return True
#         except:
#             print(sys.exc_info())
#
#     def insertMultiRows(self, position=0, rows=1, index=QModelIndex()):
#         try:
#             self.beginInsertRows(QModelIndex(), position, position + rows - 1)
#             self.endInsertRows()
#             return True
#         except:
#             print(sys.exc_info())
#
#     def flags(self, index):
#         return Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable
#
#     def DelRows(self, position=0, rows=1, index=QModelIndex()):
#         try:
#             self.beginRemoveRows(QModelIndex(), position, position + rows - 1)
#             self.endRemoveRows()
#             return True
#         except:
#             print(sys.exc_info())
#
#     def DelAllRows(self, position=0, rows=1, index=QModelIndex()):
#         try:
#             self.beginRemoveRows(QModelIndex(), 0, len(self._data) - 1)
#             self.endRemoveRows()
#             return True
#         except:
#             print(sys.exc_info())


# class ModelVoucher(QtCore.QAbstractTableModel):
#
#     def __init__(self, data, heads, isReset=False):
#         super(ModelVoucher, self).__init__()
#         self._data = data
#         # self._data1 = data
#         self.heads = heads
#         if (isReset):
#             self.lastSerialNo = data.shape[0]
#         else:
#             self.lastSerialNo = 0
#
#
#
#     def data(self, index, role=Qt.DisplayRole | Qt.EditRole):
#         try:
#             value = self._data[index.row(), index.column()]
#             if role == Qt.DisplayRole:
#                 # if index.column() in [1, 2, 3]:
#                 #     value = float(value)
#                 #     return value
#                 return value
#
#             if role == Qt.DisplayRole:
#                 value = self._data[index.row(), index.column()]
#
#                 if index.column() in [1, 2, 3, 4]:
#                     # Align right, vertical middle
#                     return Qt.AlignVCenter + Qt.AlignRight
#
#         except:
#             print(traceback.print_exc())
#
#     def setData(self, index, value, role=Qt.EditRole):
#         if role in (Qt.DisplayRole, Qt.EditRole):
#             # print('Edit role:', index.row(), index.column())
#             # if value is blank
#             if not value:
#                 return False
#             self._data[index.row()][index.column()] = value
#             self.dataChanged.emit(index, index)
#         return True
#
#     def rowCount(self, index=''):
#         return self.lastSerialNo
#
#     def columnCount(self, index):
#         return len(self.heads)
#
#     def headerData(self, section, orientation, role):
#         if role == Qt.DisplayRole:
#             if orientation == Qt.Horizontal:
#                 return str(self.heads[section])
#
#     def insertRows(self, position=0, rows=1, index=QModelIndex()):
#         try:
#             self.beginInsertRows(QModelIndex(), position, position + rows - 1)
#             # self.beginInsertRows(QModelIndex(), self.lastSerialNo - 1, self.lastSerialNo - 1)
#             self.endInsertRows()
#             return True
#         except:
#             print(sys.exc_info())
#
#     # def insertRows(self, position=0, rows=1, index=QModelIndex()):
#     #     try:
#     #         # self.beginInsertRows(QModelIndex(), position, position + rows - 1)
#     #         self.beginInsertRows(QModelIndex(), self.lastSerialNo - 1, self.lastSerialNo - 1)
#     #         self.endInsertRows()
#     #         return True
#     #     except:
#     #         print(sys.exc_info())
#
#     def insertMultiRows(self, position=0, rows=1, index=QModelIndex()):
#         try:
#             self.beginInsertRows(QModelIndex(), position, position + rows - 1)
#             # self.beginInsertRows(QModelIndex(), self.lastSerialNo - 1, self.lastSerialNo - 1)
#             self.endInsertRows()
#             return True
#         except:
#             print(sys.exc_info())
#
#     def flags(self, index):
#         return Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable
#
#     def DelRows(self, position=0, rows=1, index=QModelIndex()):
#         self.beginRemoveRows(QModelIndex(), 0, 0)
#         self.endRemoveRows()
#         return True
#
#     def DelAllRows(self, position=0, rows=1, index=QModelIndex()):
#
#         rrr = self.rowCount()
#         self.beginRemoveRows(QModelIndex(), 0, rrr - 1)
#
#         self.endRemoveRows()
#         return True
