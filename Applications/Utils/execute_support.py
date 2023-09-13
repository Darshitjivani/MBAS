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
from Applications.Views.Branch.alter_branch_list import AlterBranchListWindow
from Applications.Views.Branch.create_branch import BranchCreateWindow
from Applications.Views.CreateGroup.alter_group_list import AlterGroupListWindow
from Applications.Views.CreateGroup.create_group import CreateGroupWindow
from Applications.Views.DayBook.create_daybook import DayBookWindow
from Applications.Views.Home.home import HomeWindow
from Applications.Views.Ledger.alter_ledger_list import AlterLedgerListWindow
from Applications.Views.Ledger.alter_ledger_show import AlterLedgerWindow
from Applications.Views.Ledger.ledger_create import CreateLedgerWindow
# from Applications.Views.Login.login import LoginWindow
from Applications.Views.CompanyCreate.company_create import CompanyCreateWindow
from Applications.Views.Gateways.gateways import GatewaysWindow
from Applications.Views.Login.login import LoginWindow
from Applications.Views.MasterList.alter_master_list import AlterMasterListWindow
from Applications.Views.MasterList.master_list import MasterListWindow
from Applications.Views.TrialBalance.trial_balance import TrialBalanceWindow
from Applications.Views.Voucher.create_voucher import CreateVoucherWindow
from Applications.Views.Voucher.table import Terminal
from Applications.main import UIMain


def initialObjects(main):
    # -------------------- Path of Database --------------------------#
    loc1 = os.getcwd().split('Application')
    db_path = os.path.join(loc1[0], 'Database', 'MBAS.db')
    main.db_connection = sqlite3.connect(db_path)

    main.login = LoginWindow()  # Login Window



def intialSlots(main):
    # ------------------------------- Main Window --------------#

    # main.pbCreateCompany.clicked.connect(lambda: createCompanyPage(main))
    # main.pbListOfCompany.clicked.connect(lambda: listOfCompany(main))
    main.pbCreateCompany.clicked.connect(main.showCreateCompany)
    main.pbClose.clicked.connect(main.close)
    main.login.pbLogin.clicked.connect(lambda: loginFunction(main))
    ##-------------------- Connect the dropdown signal to a function -------------------------#
    # main.cbListOfComapny.currentIndexChanged.connect(lambda index: displayCompanyDetails(main, index)










