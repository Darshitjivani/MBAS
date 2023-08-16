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

from Applications.Views.Login.login import LoginWindow



def initialObjects(main):
     main.login = LoginWindow()


def allObjects(main):
    pass
    # main.home = HomeWindow()

def intialSlots(main):
    pass

def allSlots(main):
    pass


