import platform
from PyQt5 import uic
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtWidgets import *
import qdarkstyle
import os
import numpy as np
from PyQt5.QtGui import QIcon, QKeySequence



class Terminal(QMainWindow):
    def __init__(self):

        super(Terminal, self).__init__()
        self.osType = platform.system()

        loc1 = os.getcwd().split('Application')
        ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'table.ui')
        uic.loadUi(ui_login, self)
        dark = qdarkstyle.load_stylesheet_pyqt5()
        self.lastSerialNo = 0

        osType = platform.system()

        if (osType == 'Darwin'):
            flags = Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        else:
            flags = Qt.WindowFlags(Qt.SubWindow | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)

        self.cancel.clicked.connect(self.hide)
        self.createShortcuts()

    def movWin(self, x, y):
        self.move(self.pos().x() + x, self.pos().y() + y)


    def createShortcuts(self):
        self.quitSc = QShortcut(QKeySequence('Esc'), self)
        self.quitSc.activated.connect(self.hide)

    def my_function(self):
        print("Button clicked and function called!")

#
# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     form = Terminal()
#     form.show()
#     sys.exit(app.exec_())
# #
# #
#
#









# import sys
# from PyQt5.QtWidgets import *
#
# class MyWidget(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle('Show Frame Example')
#         self.setGeometry(100, 100, 400, 300)
#
#         # Create a QVBoxLayout to arrange widgets vertically
#         layout = QVBoxLayout()
#
#         # Create a push button
#         self.show_button = QPushButton('Show Frame', self)
#         self.show_button.clicked.connect(self.show_frame)
#         layout.addWidget(self.show_button)
#
#         # Create a frame (you can replace this with any widget you want)
#         self.frame = QFrame(self)
#         self.frame.setFrameShape(QFrame.StyledPanel)
#         layout.addWidget(self.frame)
#         self.frame.hide()  # Initially hide the frame
#
#         # Set the layout for the main window
#         self.setLayout(layout)
#
#     def show_frame(self):
#         # Show or hide the frame when the button is clicked
#         self.frame.setVisible(not self.frame.isVisible())
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MyWidget()
#     window.show()
#     sys.exit(app.exec_())




# import tkinter as tk
#
# # Create the main window (root)
# root = tk.Tk()
# root.title("Main Window")
#
# # Create a frame within the main window
# frame = tk.Frame(root)
# frame.pack()
#
# # Create a button inside the frame
# button = tk.Button(frame, text="Show Window")
# button.pack()
#
# # Function to open a new window
# def open_window():
#     # Create a new window
#     new_window = tk.Toplevel(root)
#     new_window.title("New Window")
#
#     # Add widgets to the new window
#     label = tk.Label(new_window, text="This is a new window!")
#     label.pack()
#
# # Bind the button to open the new window
# button.config(command=open_window)
#
# # Start the main event loop
# root.mainloop()
