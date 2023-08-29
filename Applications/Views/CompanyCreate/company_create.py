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
from Applications.Views.Gateways.gateways import GatewaysWindow
import sqlite3

class CompanyCreateWindow(QMainWindow):
    def __init__(self):
        super(CompanyCreateWindow, self).__init__()
        loc1 = os.getcwd().split('Application')
        ui_login = os.path.join(loc1[0], 'Resources', 'UI', 'CompanyCreate.ui')
        uic.loadUi(ui_login, self)
        # self.setWindowFlag(Qt.FramelessWindowHint)


        # hide company window after creating company
        self.pbSubmit.clicked.connect(self.hide)



        # db_loc = os.path.join(loc1[0], 'Database', 'MBAS.db')
        #
        # self.db_connection = sqlite3.connect(db_loc)
        #
        # self.line_edit_fields = [
        #     self.cmp_name, self.mail_name,
        #     self.state, self.country, self.pincode, self.mobile,
        #     self.fax, self.e_mail, self.website, self.cry_symbol, self.formal_name
        #     # Add other QLineEdit instances here
        # ]
        # self.address.textChanged.connect(self.checkFieldsAndShowConfirmation)
        #
        # # Connect returnPressed signals of QLineEdit fields using a loop
        # for line_edit in self.line_edit_fields:
        #     line_edit.returnPressed.connect(self.checkFieldsAndShowConfirmation)

    # def checkFieldsAndShowConfirmation(self):
    #
    #     try:
    #         company_name = self.cmp_name.text()
    #         mailing_name = self.mail_name.text()
    #         address = self.address.toPlainText()
    #         state = self.state.text()
    #         country = self.country.text()
    #         pincode = int(self.pincode.text())
    #         mobile = int(self.mobile.text())
    #         fax = self.fax.text()
    #         email = self.e_mail.text()
    #         website = self.website.text()
    #         currency_symbol = self.cry_symbol.text()
    #         formal_name_currency = self.formal_name.text()
    #         fy_date = self.fy_date.text()
    #         book_date = self.book_date.text()
    #     except Exception as e:
    #         print(e)
    #
    #     # Check if a company with the same name already exists in the database
    #     cursor = self.db_connection.cursor()
    #     check_query = "SELECT COUNT(*) FROM Company_table WHERE Company_name = ?"
    #     cursor.execute(check_query, (company_name,))
    #     existing_count = cursor.fetchone()[0]
    #     cursor.close()
    #
    #     if existing_count > 0:
    #         QMessageBox.warning(self, 'Warning', 'A company with the same name already exists.')
    #         return
    #
    #     try:
    #         cursor = self.db_connection.cursor()
    #
    #         # Insert data into the Company_table
    #         insert_query = '''INSERT INTO Company_table (UserID, Company_name, Mailing_name, Address, State, Country, Pincode,
    #                                 Mobile, Fax, E_mail, Website, Currency_smb, Formal_name, fy_date, book_date)
    #                                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    #         values = (self.UserID, company_name, mailing_name, address, state, country, pincode, mobile, fax,
    #                   email, website, currency_symbol, formal_name_currency, fy_date, book_date)
    #
    #         cursor.execute(insert_query, values)
    #         self.db_connection.commit()
    #
    #         # Close the database connection
    #         cursor.close()
    #
    #         QMessageBox.information(self, 'Success', 'Company entry created successfully!')
    #
    #     except sqlite3.Error as e:
    #         print("Error executing query:", e)
    #         QMessageBox.critical(self, 'Error', 'Error creating company entry.')
    #     all_fields_filled = all(line_edit.text() for line_edit in self.line_edit_fields) and self.address.toPlainText()
    #
    #     if all_fields_filled:
    #         self.showConfirmationDialog()

    # def showConfirmationDialog(self):
    #     # Create a confirmation dialog
    #     reply = QMessageBox.question(
    #         self,
    #         'Confirmation',
    #         'Do you want to continue?',
    #         QMessageBox.Yes | QMessageBox.No,
    #         QMessageBox.No
    #     )
    #
    #     if reply == QMessageBox.Yes:
    #         # User chose to continue, handle accordingly
    #         self.createGateway()
    #     else:
    #         # User chose not to continue, clear the current line edit
    #         sender = self.sender()  # Get the sender of the signal
    #         if isinstance(sender, QLineEdit):
    #             sender.clear()
    #
    # def createGateway(self):
    #     gateway = GatewaysWindow()
    #     self.setCentralWidget(gateway)


# self.line_edit_fields = [
#             self.cmp_name, self.mail_name,
#             self.state, self.country, self.pincode, self.mobile,
#             self.fax, self.e_mail, self.website, self.cry_symbol, self.formal_name
#             # Add other QLineEdit instances here
#         ]
#         self.address.textChanged.connect(self.checkFieldsAndShowConfirmation)
#
#         # Connect returnPressed signals of QLineEdit fields using a loop
#         for line_edit in self.line_edit_fields:
#             line_edit.returnPressed.connect(self.checkFieldsAndShowConfirmation)
#
#     def checkFieldsAndShowConfirmation(self):
#         company_name = self.cmp_name.text()
#         mailing_name = self.mail_name.text()
#         address = self.address.text()
#         state = self.state.text()
#         country = self.country.text()
#         pincode = int(self.pincode.text())
#         mobile = int(self.mobile.text())
#         fax = self.fax.text()
#         email = self.e_mail.text()
#         website = self.website.text()
#         currency_symbol = self.cry_symbol.text()
#         formal_name_currency = self.formal_name.text()
#         fy_date = self.fy_date.text()
#         book_date = self.book_date.text()
#
#         try:
#             cursor = self.db_connection.cursor()
#
#             # Insert data into the Company_table
#             insert_query = '''INSERT INTO Company_table (UserID, Company_name, Mailing_name, Address, State, Country, Pincode,
#                                     Mobile, Fax, E_mail, Website, Currency_smb, Formal_name, fy_date, book_date)
#                                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
#             values = (self.UserID, company_name, mailing_name, address, state, country, pincode, mobile, fax,
#                       email, website, currency_symbol, formal_name_currency, fy_date, book_date)
#
#             cursor.execute(insert_query, values)
#             self.db_connection.commit()
#
#             # Close the database connection
#             cursor.close()
#
#             QMessageBox.information(self, 'Success', 'Company entry created successfully!')
#
#         except sqlite3.Error as e:
#             print("Error executing query:", e)
#             QMessageBox.critical(self, 'Error', 'Error creating company entry.')