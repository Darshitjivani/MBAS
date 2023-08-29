import os

from PyQt5 import uic
from PyQt5 import *
import qdarkstyle
import traceback
import numpy as np
# from model import ModelTS

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget, QWidget, QPushButton
from PyQt5.QtCore import Qt

class CreateLedgerWindow(QMainWindow):
    def __init__(self):
        super(CreateLedgerWindow, self).__init__()

        # Load your UI and set window flags
        loc1 = os.getcwd().split('Application')
        ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'LedgerCreate.ui')
        uic.loadUi(ui_login, self)
