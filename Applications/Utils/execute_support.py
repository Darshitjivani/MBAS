import sqlite3
import sys
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


# ---------------------------------------- Imports For Files -----------------------------#
from Applications.Utils.support import *
from Applications.Views.CreateGroup.create_group import CreateGroupWindow
from Applications.Views.Ledger.alter_ledger_list import AlterLedgerListWindow
from Applications.Views.Ledger.ledger_create import CreateLedgerWindow
from Applications.Views.Login.login import LoginWindow
from Applications.Views.Home.home import HomeWindow
from Applications.Views.CompanyCreate.company_create import CompanyCreateWindow
from Applications.Views.Gateways.gateways import GatewaysWindow
from Applications.Views.MasterList.alter_master_list import AlterMasterListWindow
from Applications.Views.MasterList.master_list import MasterListWindow


def initialObjects(main):

    # -------------------- Path of Database --------------------------#
    loc1=os.getcwd().split('Application')
    db_path=os.path.join(loc1[0], 'Database', 'MBAS.db')
    main.db_connection = sqlite3.connect(db_path)



    main.login = LoginWindow()  # Login Window


def allObjects(main):


    main.gateway = GatewaysWindow() # Gateway Window
    main.companycreate = CompanyCreateWindow()  # Create Company Window
    # main.home = HomeWindow()
    main.masterlist = MasterListWindow()  # MaterList Window
    main.creategroup = CreateGroupWindow() # Create group Window
    main.createledger = CreateLedgerWindow() # Create Ledger Window
    main.altermasterlist = AlterMasterListWindow()  # Master List window For Alteration
    main.alterledgerlist = AlterLedgerListWindow() # Ledger List Window For Alteration

def intialSlots(main):

    # ------------------------------- Main Window --------------#

    main.pbCreateCompany.clicked.connect(lambda:createCompanyPage(main))
    main.pbListOfCompany.clicked.connect(lambda:listOfCompany(main))
    # main.cbListOfComapny.addItems(lambda:listOfCompany(main))
    # company_names = listOfCompany(main)
    # print("comapny names",company_names)
    #
    # main.cbListOfComapny.addItems(company_names)
    #
    # # Connect the dropdown signal to a function
    # main.cbListOfComapny.currentIndexChanged.connect(
    #     lambda index: displayCompanyDetails(main, index)
    # )

def allSlots(main):
    #-----------------------  Login Window ----------------------------------------------#
    main.login.pbLogin.clicked.connect(lambda:loginFunction(main))

    #------------------------------- Create Company Window --------------------------#
    main.companycreate.pbSubmit.clicked.connect(lambda: createCompany(main))

    #-------------------------------- Gateway Window -------------------------------#
    main.gateway.pbCreateMaster.clicked.connect(lambda: masterList(main))
    main.gateway.pbAlterMaster.clicked.connect(lambda: showAlterMasterPage(main))

    #-------------------------------- Master List Window -------------------------------#
    main.masterlist.pbCreateGroup.clicked.connect(lambda: creategrouppage(main))
    main.masterlist.pdCreateLedger.clicked.connect(lambda: createLedgerPage(main))
    # main.masterlist.pbChangeCompany.clicked.connect(main.home.show())

    # --------------------------------- Create Group Window --------------------------#
    main.creategroup.pbSubmit.clicked.connect(lambda: saveGroupData(main))

    #--------------------------------- Create Ledger Window -----------------------------#
    main.createledger.pbSubmit.clicked.connect(lambda: saveledger(main))
    main.createledger.pbDelete.clicked.connect(lambda: deleteLedger(main))

    #------------------------------ Alter Master List Window ---------------------------#
    main.altermasterlist.pbAlterLedger.clicked.connect(lambda: alterLedgerListpage(main))


    # main.creategroup.pbSubmit.clicked.connect(lambda: creategrouppage(main))
    # main.masterlist.pbChangeCompany.clicked.connect()








