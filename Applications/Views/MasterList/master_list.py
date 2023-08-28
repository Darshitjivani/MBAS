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

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget, QWidget, QPushButton
from PyQt5.QtCore import Qt

class MasterListWindow(QMainWindow):
    def __init__(self):
        super(MasterListWindow, self).__init__()

        # Load your UI and set window flags
        loc1 = os.getcwd().split('Application')
        ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'MasterList.ui')
        uic.loadUi(ui_login, self)
#         self.setWindowFlag(Qt.FramelessWindowHint)
#         self.setGeometry(100, 100, 800, 600)
#
#         # Create a QDockWidget and add a close button
#         self.dock_widget = QDockWidget("My Dock Widget", self)
#         self.close_button = QPushButton("Close Dock", self)
#         self.dock_widget.setWidget(self.close_button)
#         self.addDockWidget(Qt.TopDockWidgetArea, self.dock_widget)
#
#         # Connect topLevelChanged signal to the custom slot
#         self.dock_widget.topLevelChanged.connect(self.dockWidgetTopLevelChanged)
#         self.dockWidget_8.clicked.connect(self.close)  # Close the main window when button clicked
#
#     def dockWidgetTopLevelChanged(self, isTopLevel):
#         if isTopLevel:
#             self.close()  # Close the main window if dock widget becomes a top-level window
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = GatewaysWindow()
#     window.show()
#     app.exec()


# class GatewaysWindow(QMainWindow):
#     def __init__(self):
#         super(GatewaysWindow, self).__init__()
#         loc1 = os.getcwd().split('Application')
#         ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'MasterList.ui')
#         uic.loadUi(ui_login, self)
#
#         self.setWindowFlag(Qt.FramelessWindowHint)
#         self.setGeometry(100, 100, 800, 600)
#         self.dockWidget_8.topLevelChanged.connect(self.close)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = GatewaysWindow()
#     window.show()
#     app.exec()


# class MyDockWidget(QDockWidget):
#     def __init__(self, *args, **kwargs):
#         super(MyDockWidget, self).__init__(*args, **kwargs)
#
#     def closeEvent(self, event):
#         # Close the entire main window
#         self.parent().close()

# class GatewaysWindow(QMainWindow):
#     def __init__(self):
#         super(GatewaysWindow, self).__init__()
#
#         loc1 = os.getcwd().split('Application')
#         ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'MasterList.ui')
#         uic.loadUi(ui_login, self)
        #
        # self.setWindowFlag(Qt.FramelessWindowHint)
        # self.setGeometry(100, 100, 800, 600)
        #
        # self.dockWidget_8 = MyDockWidget(self)  # Replace with your actual QDockWidget instance
        # self.addDockWidget(Qt.DockWidgetArea(4), self.dockWidget_8)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = GatewaysWindow()
#     window.show()
#     app.exec()