import json
import os
import sys
import traceback

import numpy as np
from PyQt5 import uic

from Applications.Views.TrialBalance.modeltrialbal import ModelTB
from Themes.dt3 import dt3
from PyQt5.QtCore import Qt, QSortFilterProxyModel, QDate, QDateTime
from PyQt5.QtWidgets import QMainWindow, QMenu, QFileDialog, QApplication, QTableView


class TrialBalanceWindow(QMainWindow):
    def __init__(self, lbDate=None):
        super(TrialBalanceWindow, self).__init__()

        # Load your UI and set window flags
        loc1 = os.getcwd().split('Application')
        ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'TrialBalance.ui')
        uic.loadUi(ui_login, self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet(dt3)

        self.last_serialno = 0
        # self.initUI()
        self.tables_details_TWM()
        self.defaultColumnProfile()

    def tables_details_TWM(self):
        try:

            self.heads = ['Date','Perticular', 'Debit Amount INR', 'Credit Amount INR', 'Debit Amount USD', 'Credit Amount USD']
            self.visibleColumns = len(self.heads)
            print('len(self.heads)',len(self.heads))
            self.table = np.zeros((2000, len(self.heads)), dtype=object)

            self.model = ModelTB(self.table, self.heads)
            self.smodel = QSortFilterProxyModel()
            self.smodel.setSourceModel(self.model)
            self.tableView.setModel(self.smodel)
            self.tableView.setSelectionBehavior(QTableView.SelectRows)

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



            self.tableView.horizontalHeader().setContextMenuPolicy(Qt.CustomContextMenu)
            self.tableView.horizontalHeader().customContextMenuRequested.connect(self.headerRightClickMenu)

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

            # loc = os.getcwd().split('Application')[0]
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
            # pathDetails= json.load(f1)
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
            # a = pathDetails['TrialBal']['lastSavedColumnProfile']
            a = save
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

