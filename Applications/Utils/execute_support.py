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
from Applications.Views.Login.login import LoginWindow



def initialObjects(main):
    # -------------------- Path of Database --------------------------#
    loc1 = os.getcwd().split('Application')
    db_path = os.path.join(loc1[0], 'Database', 'MBAS.db')
    main.db_connection = sqlite3.connect(db_path)

    main.login = LoginWindow()  # Login Window



def initVariables(main):
    try:
        main.is_filtered = False
    except:
        print(traceback.print_exc())

def intialSlots(main):
    # ------------------------------- Main Window --------------#

    # main.pbCreateCompany.clicked.connect(lambda: createCompanyPage(main))
    # main.pbListOfCompany.clicked.connect(lambda: listOfCompany(main))
    main.pbCreateCompany.clicked.connect(main.showCreateCompany)
    main.pbClose.clicked.connect(main.close)
    main.login.pbLogin.clicked.connect(lambda: loginFunction(main))
    ##-------------------- Connect the dropdown signal to a function -------------------------#
    # main.cbListOfComapny.currentIndexChanged.connect(lambda index: displayCompanyDetails(main, index)










