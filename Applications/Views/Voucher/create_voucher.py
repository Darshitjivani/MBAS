import json

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSortFilterProxyModel
import os
from PyQt5 import uic
import traceback
import numpy as np
from Applications.Views.Voucher.modelVoucher import ModelTS
from Themes.dt3 import dt3


class CreateVoucherWindow(QMainWindow):
    def __init__(self):
        super(CreateVoucherWindow, self).__init__()
        loc1 = os.getcwd().split('Application')
        ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'CreateVoucher.ui')
        uic.loadUi(ui_login, self)
        self.setStyleSheet(dt3)


        self.last_serialno=0
        self.dr_last_serialno = 0
        self.cr_last_serialno = 0
        # self.initUI()
        self.tables_details_TWM()
        # self.window = Terminal()
        # self.pbAdd.clicked.connect(self.window.show)
        # self.window.adddata.clicked.connect(self.AddRow)



    def tables_details_TWM(self):
        try:


            self.heads = ['Cr/Dr', 'perticular', 'Debite Amount','Credit Amount','Currency']
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
        #
        except:
            print(traceback.print_exc())

    def saveAsDefaultColumnProfile(self):
        try:
            loc1 = os.getcwd().split('Application')
            defaultDir = os.path.join(loc1[0], 'Resources', 'ColumnProfile')

            binData = self.tableView.horizontalHeader().saveState()
            save = QFileDialog.getSaveFileName(self, 'Save file', defaultDir)[0]
            print('save TrialBal save column profile', save)

            with open(save, 'wb') as f:
                f.write(binData)
            f.close()

            loc = os.getcwd().split('Application')[0]
            settingsFilePath = os.path.join(loc1[0], 'Resources', 'Settings.json')

            f1 = open(settingsFilePath)
            pathDetails = json.load(f1)
            f1.close()
            a = pathDetails['TrialBal']['defaultColumnProfile']
            save = "Resources" + str(a.split('Resources')[1])
            print('save TrialBal save column profile', save)

            pathDetails_new = json.dumps(pathDetails, indent=4)

            f2 = open(settingsFilePath, 'w+')
            f2.write(pathDetails_new)
            pathDetails= json.load(f1)
            f2.close()

        except:
            print(traceback.print_exc())

    def defaultColumnProfile(self):
        loc = os.getcwd().split('Application')
        settingsFilePath = os.path.join(loc[0], 'Resources', 'Settings.json')
        f1 = open(settingsFilePath)
        pathDetails = json.load(f1)
        f1.close()
        lastCPFilePath = pathDetails['TrialBal']['defaultColumnProfile']
        lastCPFilePath = os.path.join(loc[0], lastCPFilePath)

        with open(lastCPFilePath, 'rb') as f:
            binData = f.read()
        f.close()
        self.tableView.horizontalHeader().restoreState(binData)

    def ResetDefaultColumnProfile(self):
        loc = os.getcwd().split('Application')
        settingsFilePath = os.path.join(loc[0], 'Resources', 'Settings.json')
        f1 = open(settingsFilePath)
        pathDetails = json.load(f1)
        f1.close()
        lastCPFilePath = pathDetails['TrialBal']['defaultColumnProfile']
        with open(lastCPFilePath, 'rb') as f:
            binData = f.read()
        f.close()
        self.tableView.horizontalHeader().restoreState(binData)

    def saveColumnProfile(self):
        try:
            loc = os.getcwd().split('Application')
            defaultDir = os.path.join(loc[0], 'Resources', 'ColumnProfile')
            # defaultDir = r'../Resources/POTW_ColPro/ColumnProfile'

            binData = self.tableView.horizontalHeader().saveState()
            save = QFileDialog.getSaveFileName(self, 'Save file', defaultDir)[0]


            with open(save, 'wb') as f:
                f.write(binData)
            f.close()

            loc = os.getcwd().split('Application')
            settingsFilePath = os.path.join(loc[0], 'Resources', 'Settings.json')

            f1 = open(settingsFilePath)
            pathDetails = json.load(f1)
            f1.close()
            a = pathDetails['TrialBal']['lastSavedColumnProfile']
            save = "Resources" + str(a.split('Resources')[1])
            print('save TrialBal save column profile', save)

            pathDetails_new = json.dumps(pathDetails, indent=4)

            f2 = open(settingsFilePath, 'w+')
            f2.write(pathDetails_new)
            # pathDetails= json.load(f1)
            f2.close()

        except:
            print(traceback.print_exc())

    def openColumnProfile(self):
        loc = os.getcwd().split('Application')
        defaultDir = os.path.join(loc[0], 'Resources','ColumnProfile')

        openF = QFileDialog.getOpenFileName(self, 'Open file', defaultDir)[0]

        with open(openF, 'rb') as f:
            binData = f.read()
        f.close()

        self.tableView.horizontalHeader().restoreState(binData)

    def headerRightClickMenu(self, position):
        try:
            # print('dfdsfdsf')
            # a=(self.tableView.selectedIndexes()[0].data())
            menu = QMenu()

            saveColumnProfile = menu.addAction("Save New Col profile")
            restoreColumnProfile = menu.addAction("Open Col Profile")
            saveAsDefault = menu.addAction("SaveAs Defalt Col Profile")
            hideColumn = menu.addAction("Hide")
            reset = menu.addAction("Reset")

            # cancelAction = menu.addAction("Cancel")
            action = menu.exec_(self.tableView.horizontalHeader().mapToGlobal(position))
            if action == saveColumnProfile:
                self.saveColumnProfile()
            elif (action == restoreColumnProfile):
                self.openColumnProfile()
            elif (action == saveAsDefault):
                self.saveAsDefaultColumnProfile()
            elif (action == hideColumn):
                x = (self.tableView.horizontalHeader().logicalIndexAt(position))
                self.tableView.horizontalHeader().hideSection(x)

            elif (action == reset):
                if self.tableView.horizontalHeader().sectionsHidden():

                    count = self.tableView.horizontalHeader().count()
                    for i in range(count):
                        if self.tableView.horizontalHeader().isSectionHidden(i):
                            self.tableView.horizontalHeader().showSection(i)

        except:
            print(sys.exc_info()[1])
    def clearFields(self):
        # Add code here to clear the input fields in your window
        # self.cbVoucherType.setCurrentIndex(0)
        # self.cbDebitedAccount.setCurrentIndex(0)
        # self.model.removeRows(0, self.model.rowCount())
        self.table[ : self.last_serialno] = [0, 0, 0, 0, 0]
        self.model.removeRows(0, self.model.rowCount())
        

        self.model.DelRows(0, self.last_serialno)
        self.last_serialno = 0
        self.model.last_serialno = 0
        self.model.rowCount()
        ind = self.model.index(0, 0)
        ind1 = self.model.index(0, 1)
        self.model.dataChanged.emit(ind, ind1)
        # self.tableshow.cbCurrency.setCurrentIndex(0)
        self.leNarration.clear()
        self.lbCredit.clear()
        self.lbDebit.clear()
        self.lbCurrency.clear()



