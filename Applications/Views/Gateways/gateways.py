import layout
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
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent, QKeySequence
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

from Applications.Views.MasterList.master_list import MasterListWindow
from Themes.dt3 import dt3


# from model import ModelTS


class GatewaysWindow(QMainWindow):
    def __init__(self):
        super(GatewaysWindow, self).__init__()
        loc1 = os.getcwd().split('Application')
        ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'Gateways.ui')
        uic.loadUi(ui_login, self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.lbCompanyName = self.findChild(QLabel, 'lbCompanyName')# Attribute initialization
        self.masterlist = MasterListWindow()
        # self.showMaximized()
        self.createShortcuts()  # Create A shortcut

        #----------------------------------- For Window Movement ----------------------------------$
        self.dragging = False
        self.offset = None

        #------------------------------------- Maximize And Minimize -------------------------------#
        self.maxwin = True
        self.pbMaximized.clicked.connect(self.showmaxORnormal)
        self.pbMinimized.clicked.connect(self.showminimized)

        #-------------------------------------------- For MenuBar Hide -----------------------------------#
        self.pbMenubar.clicked.connect(self.menuHideShow)

        # Hide all frames initially
        self.hideAllFrames()
        self.setStyleSheet(dt3)

        #
        # self.lbChangeCompany.hide()
        # self.pbChangeCompany.clicked.connect(self.lbChangeCompany.show)
        # self.pbChangeCompany.setToolTip("Change Company")

    def menuHideShow(self):
        try:
            self.wMenubar.setVisible(not self.wMenubar.isVisible())
        except:
            print(traceback.print_exc())

    def showminimized(self):
        self.showMinimized()  # show the window in minimized screen

    def showmaxORnormal(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def createShortcuts(self):
        self.quitSc = QShortcut(QKeySequence('Esc'), self)
        self.quitSc.activated.connect(self.close)

    def hideAllFrames(self):
        self.fCreate.hide()
        self.fAlter.hide()
        self.fVouchers.hide()
        self.fDayBook.hide()
        self.fBalanceSheet.hide()
        self.fTrialBalance.hide()

    def showCreateFrame(self):
        self.hideAllFrames()
        self.fCreate.show()

    def showAlterFrame(self):
        self.hideAllFrames()
        self.fAlter.show()

    def showDayBookFrame(self):
        self.hideAllFrames()
        self.fDayBook.show()

    def showVouchersFrame(self):
        self.hideAllFrames()
        self.fVouchers.show()

    def showBalanceSheetFrame(self):
        self.hideAllFrames()
        self.fBalanceSheet.show()

    def showTrialBalanceFrame(self):
        self.hideAllFrames()
        self.fTrialBalance.show()

    def updateTitleLabel(self, company_name):
        self.lbCompanyName.setText(f"Welcome to {company_name}")


    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            # Calculate the offset between the mouse click and the window position
            self.offset = event.globalPos() - self.pos()
            self.dragging = True


    def mouseMoveEvent(self, event: QMouseEvent):
        if self.dragging:
            # Move the window with the mouse while dragging
            self.move(event.globalPos() - self.offset)


    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            # Stop dragging when the left mouse button is released
            self.dragging = False
            self.offset = None
