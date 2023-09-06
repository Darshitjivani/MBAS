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
from Applications.Views.Branch.alter_branch_company_list import AlterBranchLedgerListWindow
from Applications.Views.Branch.create_branch import BranchCreateWindow
from Applications.Views.CreateGroup.alter_group_list import AlterGroupListWindow
from Applications.Views.CreateGroup.create_group import CreateGroupWindow
from Applications.Views.Ledger.alter_ledger_list import AlterLedgerListWindow
from Applications.Views.Ledger.alter_ledger_show import AlterLedgerWindow
from Applications.Views.Ledger.ledger_create import CreateLedgerWindow
from Applications.Views.Login.login import LoginWindow
from Applications.Views.Home.home import HomeWindow
from Applications.Views.CompanyCreate.company_create import CompanyCreateWindow
from Applications.Views.Gateways.gateways import GatewaysWindow
from Applications.Views.MasterList.alter_master_list import AlterMasterListWindow
from Applications.Views.MasterList.master_list import MasterListWindow
from Applications.Views.Voucher.create_voucher import CreateVoucherWindow
from Applications.Views.Voucher.table import Terminal
from Applications.main import UIMain


def initialObjects(main):
    # -------------------- Path of Database --------------------------#
    loc1 = os.getcwd().split('Application')
    db_path = os.path.join(loc1[0], 'Database', 'MBAS.db')
    main.db_connection = sqlite3.connect(db_path)

    main.login = LoginWindow()  # Login Window


def allObjects(main):
    main.gateway = GatewaysWindow()  # Gateway Window
    main.companycreate = CompanyCreateWindow()  # Create Company Window
    # main.home = HomeWindow() # Homewindow
    main.masterlist = MasterListWindow()  # MaterList Window
    main.creategroup = CreateGroupWindow()  # Create group Window
    main.createledger = CreateLedgerWindow()  # Create Ledger Window
    main.altermasterlist = AlterMasterListWindow()  # Master List window For Alteration
    main.alterledgerlist = AlterLedgerListWindow() # Ledger List Window For Alteration
    main.createbranch = BranchCreateWindow() # Branch List Window For Alteration
    main.createvoucher  = CreateVoucherWindow()  # Create Voucher Window
    main.alterbranchlist = AlterBranchLedgerListWindow()  #Ledger list Branch wise for Alteration
    # main.combo_delegate = ComboBoxDelegate()
    main.tableview = Terminal()
    # main.alterledgerlist = AlterLedgerListWindow()  # Ledger List Window For Alteration
    main.altergrouplist = AlterGroupListWindow()  # Group List Window For Alteration
    # main.homewindow = HomeWindow() #home window
    # main.backwindow = goToMasterList
    main.alterledger = AlterLedgerWindow()



    ##################################### Gateway ###################################################

    main.gateway.fCreate.layout().addWidget(main.masterlist)
    main.gateway.fAlter.layout().addWidget(main.altermasterlist)
    # main.gateway.fVouchers.layout().addWidget(main.masterlist)
    # main.gateway.fDayBook.layout().addWidget(main.masterlist)
    # main.gateway.fBalanceSheet.layout().addWidget(main.masterlist)
    # main.gateway.fTrailBalance.layout().addWidget(main.masterlist)

    ##################################### MasterList ###################################################
    main.masterlist.fGroup.layout().addWidget(main.creategroup)
    main.masterlist.fLedger.layout().addWidget(main.createledger)

    ##################################### AlterMAsterList ##############################################
    main.altermasterlist.fAlterLedger.layout().addWidget(main.alterledgerlist)
    main.altermasterlist.fAlterGroup.layout().addWidget(main.altergrouplist)
    ##################################### Company Create ###############################################
    main.fCreateCompany.layout().addWidget(main.companycreate)



def intialSlots(main):
    # ------------------------------- Main Window --------------#

    # main.pbCreateCompany.clicked.connect(lambda: createCompanyPage(main))
    # main.pbListOfCompany.clicked.connect(lambda: listOfCompany(main))
    main.pbCreateCompany.clicked.connect(main.showCreateCompany)
    main.pbClose.clicked.connect(main.close)

    ##-------------------- Connect the dropdown signal to a function -------------------------#
    # main.cbListOfComapny.currentIndexChanged.connect(lambda index: displayCompanyDetails(main, index)



def allSlots(main):
    #-----------------------  Login Window ----------------------------------------------#
    main.login.pbLogin.clicked.connect(lambda:loginFunction(main))

    # main.creategroup.pbCreate
    # ------------------------------- Create Company Window --------------------------#
    main.companycreate.pbSubmit.clicked.connect(lambda: createCompany(main))
    main.companycreate.pbSubmit.clicked.connect(main.companycreate.hide)
    main.companycreate.pbClose.clicked.connect(main.companycreate.hide)
    main.pbCreateCompany.clicked.connect(main.companycreate.show)

    # Connect the "Add" button to the clear function
    main.pbCreateCompany.clicked.connect(lambda: clearCompanyCreateFields(main))



    #-------------------------------- Gateway Window -------------------------------#
    main.gateway.pbCreateMaster.clicked.connect(lambda: masterList(main))
    main.gateway.pbAlterMaster.clicked.connect(lambda: showAlterMasterPage(main))
    main.gateway.pbVouchers.clicked.connect(lambda: showVoucherPage(main))
    # -------------------------------- Gateway Window -------------------------------#
    # main.gateway.pbCreateMaster.clicked.connect(lambda: masterList(main))
    # main.gateway.pbAlterMaster.clicked.connect(lambda: showAlterMasterPage(main))
    main.gateway.pbCreateMaster.clicked.connect(main.gateway.showCreateFrame)
    main.gateway.pbAlterMaster.clicked.connect(main.gateway.showAlterFrame)
    main.gateway.pbDayBook.clicked.connect(main.gateway.showDayBookFrame)
    main.gateway.pbVouchers.clicked.connect(main.gateway.showVouchersFrame)
    main.gateway.pbBalanceSheet.clicked.connect(main.gateway.showBalanceSheetFrame)
    main.gateway.pbTrailBalance.clicked.connect(main.gateway.showTrailBalanceFrame)

    main.gateway.pbClose.clicked.connect(main.gateway.close)

    # -------------------------------- Master List Window -------------------------------#
    main.masterlist.pbCreateGroup.clicked.connect(lambda: creategrouppage(main))
    main.masterlist.pbCreateGroup.clicked.connect(main.masterlist.showCreateGroup)

    main.masterlist.pdCreateLedger.clicked.connect(lambda: createLedgerPage(main))
    main.masterlist.pbCreateBranch.clicked.connect(lambda: createBranchpage(main))

    # main.masterlist.pbChangeCompany.clicked.connect(main.home.show())
    main.masterlist.pdCreateLedger.clicked.connect(main.masterlist.showCreateLadger)
    # main.masterlist.pbClose.clicked.connect(main.masterlist.hide)
    # main.masterlist.pbChangeCompany.clicked.connect(main.show)

    # --------------------------------- Create Group Window --------------------------#
    main.creategroup.pbSubmit.clicked.connect(lambda: saveGroupData(main))
    main.creategroup.pbClose.clicked.connect(main.creategroup.close)

    # --------------------------------- Create Ledger Window -----------------------------#
    main.createledger.pbSubmit.clicked.connect(lambda: saveledger(main))
    main.createledger.pbDelete.clicked.connect(lambda: deleteLedger(main))
    main.createledger.pbClose.clicked.connect(main.createledger.close)

    # ------------------------------ Alter Master List Window ---------------------------#
    main.altermasterlist.pbAlterGroup.clicked.connect(lambda: alterGroupListpage(main))
    main.altermasterlist.pbAlterLedger.clicked.connect(lambda: alterLedgerListpage(main))
    main.altermasterlist.pbAlterBranch.clicked.connect(lambda: alterBranchList(main))

    main.altermasterlist.pbAlterGroup.clicked.connect(main.altermasterlist.showAlterGroup)

    # main.altermasterlist.pbAlterLedger.clicked.connect(lambda: alterLedgerPage(main))
    main.altermasterlist.pbAlterLedger.clicked.connect(main.altermasterlist.showAlterLedger)
    # main.alterledgerlist.pbClose.clicked.connect(main.alterledgerlist.hide)
    main.altergrouplist.pbClose.clicked.connect(main.altergrouplist.hide)

    #---------------------------- Create Branch Window ----------------------------------#
    main.createbranch.pbSubmit.clicked.connect(lambda: saveBranchData(main))
    main.alterledger.pbSubmit.clicked.connect(lambda:saveAlterLedgerData(main))
    # main.alterledger.pbSubmit.clicked.connect(main.alterledgerlist.hide)
    main.alterledger.pbDelete.clicked.connect(lambda: deleteLedger(main))
    main.alterledger.pbClose.clicked.connect(main.alterledger.close)

    #------------------------------------- Create Voucher Window -------------------------------#
    main.createvoucher.pbSubmit.clicked.connect(lambda: saveVoucherData(main))
    main.createvoucher.pbAdd.clicked.connect(lambda: showTableView(main))


    #----------------------------------- Table Window ---------------------------------------------#
    main.tableview.pdAddRaw.clicked.connect(lambda: addRaw(main))


    # main.alterledgerlist.pbClose.clicked.connect(goToMasterList)


    # main.altermasterlist.pbAlterLedger.clicked.disconnect()
    # main.creategroup.pbSubmit.clicked.connect(lambda: creategrouppage(main))
    # main.masterlist.pbChangeCompany.clicked.connect()








