import datetime
import json
import sqlite3
import traceback
import uuid
from datetime import datetime
from functools import partial

import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import QStandardItem, QDoubleValidator
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from PyQt5.QtWidgets import *
from PyQt5.uic.properties import QtCore

from Applications.Views.BalanceSheet.balancesheet import BalanceSheetWindow
from Applications.Views.DayBook.day_book import DayBookWindow
from Applications.Views.Branch.alter_branch_list import AlterBranchListWindow
from Applications.Views.Branch.create_branch import BranchCreateWindow
from Applications.Views.CompanyCreate.company_create import CompanyCreateWindow
from Applications.Views.CreateGroup.alter_group_list import AlterGroupListWindow
from Applications.Views.CreateGroup.create_group import CreateGroupWindow
from Applications.Views.DayBook.day_book import DayBookWindow
from Applications.Views.Gateways.gateways import GatewaysWindow
from Applications.Views.Home.home import HomeWindow
from Applications.Views.Ledger.alter_ledger_list import AlterLedgerListWindow
from Applications.Views.Ledger.alter_ledger_show import AlterLedgerWindow
from Applications.Views.Ledger.ledger_create import CreateLedgerWindow
from Applications.Views.MasterList.alter_master_list import AlterMasterListWindow
from Applications.Views.MasterList.master_list import MasterListWindow
from Applications.Views.TrialBalance.date_filter import DateFilterWindow
from Applications.Views.TrialBalance.trial_balance import TrialBalanceWindow
from Applications.Views.Voucher.create_voucher import CreateVoucherWindow
from Applications.Views.Voucher.currconv_entry import CurrConvEntryWindow
from Applications.Views.Voucher.payment_entry import PaymentEntryWindow
from Applications.Views.Voucher.purchase_entry import PurchaseEntryWindow
from Applications.Views.Voucher.reciept_entry import RecieptEntryWindow
from Applications.Views.Voucher.sales_entry import SalesEntryWindow
from Applications.Views.Voucher.table import Terminal



#---------------------------------------------------- All Objects ---------------------------------------------#
def allObjects(main):
    main.gateway = GatewaysWindow()  # Gateway Window
    main.companycreate = CompanyCreateWindow()  # Create Company Window
    main.masterlist = MasterListWindow()  # MaterList Window
    main.creategroup = CreateGroupWindow()  # Create group Window
    main.createledger = CreateLedgerWindow()  # Create Ledger Window
    main.altermasterlist = AlterMasterListWindow()  # Master List window For Alteration
    main.alterledgerlist = AlterLedgerListWindow() # Ledger List Window For Alteration
    main.alterbranchlist = AlterBranchListWindow()  #Ledger list Branch wise for Alteration
    main.createbranch = BranchCreateWindow() # Branch List Window For Alteration
    main.tableshow = Terminal()
    main.altergrouplist = AlterGroupListWindow()  # Group List Window For Alteration
    main.alterledger = AlterLedgerWindow()
    main.daybook = DayBookWindow()
    main.trialbalance = TrialBalanceWindow()
    main.datefilter = DateFilterWindow()
    main.balancesheet = BalanceSheetWindow()


    #-------------------------------------- Voucher Object --------------------------------
    main.createvoucher = CreateVoucherWindow()  # Create Voucher Window
    main.paymententry = PaymentEntryWindow()
    main.salesentry = SalesEntryWindow()
    main.purchaseentry = PurchaseEntryWindow()
    main.recieptentry = RecieptEntryWindow()
    main.currconventry = CurrConvEntryWindow()


    ##################################### Gateway ###################################################

    main.gateway.fCreate.layout().addWidget(main.masterlist)
    main.gateway.fAlter.layout().addWidget(main.altermasterlist)
    main.gateway.fVouchers.layout().addWidget(main.createvoucher)
    main.gateway.fDayBook.layout().addWidget(main.daybook)
    main.gateway.fBalanceSheet.layout().addWidget(main.balancesheet)
    main.gateway.fTrialBalance.layout().addWidget(main.trialbalance)

    ##################################### MasterList ###################################################
    main.masterlist.fGroup.layout().addWidget(main.creategroup)
    main.masterlist.fLedger.layout().addWidget(main.createledger)
    main.masterlist.fBranch.layout().addWidget(main.createbranch)

    ##################################### AlterMAsterList ##############################################
    main.altermasterlist.fAlterLedger.layout().addWidget(main.alterledgerlist)
    main.altermasterlist.fAlterGroup.layout().addWidget(main.altergrouplist)
    main.altermasterlist.fAlterBranch.layout().addWidget(main.alterbranchlist)
    ##################################### Company Create ###############################################
    main.fCreateCompany.layout().addWidget(main.companycreate)


#--------------------------------------------------------- All Slots -----------------------------------------#


def allSlots(main):
    #-----------------------  Login Window ----------------------------------------------#

    # main.creategroup.pbCreate
    # ------------------------------- Create Company Window --------------------------#
    main.companycreate.pbSubmit.clicked.connect(lambda: createCompany(main))
    main.companycreate.pbSubmit.clicked.connect(main.companycreate.hide)
    main.companycreate.pbClose.clicked.connect(main.companycreate.hide)
    main.pbCreateCompany.clicked.connect(main.companycreate.show)

    # Connect the "Add" button to the clear function
    # main.pbCreateCompany.clicked.connect(lambda: clearCompanyCreateFields(main))



    #-------------------------------- Gateway Window -------------------------------#
    main.gateway.pbCreateMaster.clicked.connect(main.gateway.showCreateFrame)
    main.gateway.pbCreateMaster.clicked.connect(lambda: masterList(main))

    main.gateway.pbAlterMaster.clicked.connect(main.gateway.showAlterFrame)
    main.gateway.pbAlterMaster.clicked.connect(lambda: showAlterMasterPage(main))

    main.gateway.pbDayBook.clicked.connect(main.gateway.showDayBookFrame)
    main.gateway.pbDayBook.clicked.connect(lambda: showDayBook(main))

    main.gateway.pbVouchers.clicked.connect(main.gateway.showVouchersFrame)
    main.gateway.pbVouchers.clicked.connect(lambda: showVoucherPage(main))

    main.gateway.pbTrailBalance.clicked.connect(main.gateway.showTrialBalanceFrame)
    main.gateway.pbTrailBalance.clicked.connect(lambda: showTrialBalance(main))


    # main.gateway.pbCreateMaster.clicked.connect(lambda: masterList(main))
    # main.gateway.pbAlterMaster.clicked.connect(lambda: showAlterMasterPage(main))
    main.gateway.pbBalanceSheet.clicked.connect(main.gateway.showBalanceSheetFrame)
    main.gateway.pbChangeCompany.clicked.connect(lambda: goToMainWindow(main))
    main.gateway.pbClose.clicked.connect(main.gateway.close)

    main.balancesheet.pbBack.clicked.connect(main.balancesheet.hide)

    # -------------------------------- Master List Window -------------------------------#
    main.masterlist.pbCreateGroup.clicked.connect(lambda: creategrouppage(main))
    main.masterlist.pdCreateLedger.clicked.connect(lambda: createLedgerPage(main))
    main.masterlist.pbCreateBranch.clicked.connect(lambda: createBranchpage(main))
    # main.masterlist.pbCreateBranch.clicked.connect(lambda: createBranchpage(main))


    main.masterlist.pbBack.clicked.connect(main.masterlist.hide)

    main.masterlist.pbCreateGroup.clicked.connect(main.masterlist.showCreateGroup)
    main.masterlist.pbCreateBranch.clicked.connect(main.masterlist.showCreateBranch)
    main.masterlist.pdCreateLedger.clicked.connect(main.masterlist.showCreateLadger)

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
    main.altermasterlist.pbBack.clicked.connect(main.altermasterlist.hide)

    main.altermasterlist.pbAlterGroup.clicked.connect(main.altermasterlist.showAlterGroup)
    main.altermasterlist.pbAlterLedger.clicked.connect(main.altermasterlist.showAlterLedger)
    main.altermasterlist.pbAlterBranch.clicked.connect(main.altermasterlist.showAlterBranch)
    main.alterledgerlist.pbClose.clicked.connect(main.alterledgerlist.hide)
    main.altergrouplist.pbClose.clicked.connect(main.altergrouplist.hide)

    #---------------------------- Create Branch Window ----------------------------------#

    main.createbranch.pbSubmit.clicked.connect(lambda: saveBranchData(main))
    main.alterledger.pbSubmit.clicked.connect(lambda: saveAlterLedgerData(main))
    # main.alterledger.pbSubmit.clicked.connect(main.alterledgerlist.hide)

    main.alterledger.pbDelete.clicked.connect(lambda: deleteLedger(main))
    main.alterledger.pbClose.clicked.connect(main.alterledger.close)

    # -------------------------Alter Branch Window----------------------------------------#

    main.alterbranchlist.pbClose.clicked.connect(main.alterbranchlist.close)

    # ------------------------------------- Create Voucher Window -------------------------------#

    main.createvoucher.pbSubmit.clicked.connect(lambda: saveVoucherData(main))
    main.createvoucher.pbPayment.clicked.connect(lambda: showPaymentEntry(main))
    main.createvoucher.pbSales.clicked.connect(lambda: showSalesEntry(main))
    main.createvoucher.pbPurchase.clicked.connect(lambda: showPurchaseEntry(main))
    main.createvoucher.pbReciept.clicked.connect(lambda: showRecieptEntry(main))
    main.createvoucher.pbCurConvsn.clicked.connect(lambda: showCurrConvEntry(main))
    main.createvoucher.pbBack.clicked.connect(main.createvoucher.hide)
    # main.createvoucher.pbAdd.clicked.connect(lambda: showTableView(main))
    # main.createvoucher.pbDelete.clicked.connect(lambda: deleteRows(main))

    #----------------------------------- Table Window ---------------------------------------------#
    # main.tableshow.pdAddRaw.clicked.connect(lambda: addRaw(main))

    #----------------------------------- Day Book Window ------------------------------------------#
    main.daybook.deDateEdit.dateChanged.connect(lambda: filterDataByDate(main))
    main.daybook.pbBack.clicked.connect(main.daybook.hide)


    # ------------------------------------- Trial Balance ------------------------------#
    main.trialbalance.pbBack_2.clicked.connect(main.trialbalance.hide)
    main.trialbalance.cbtrialbalance.activated.connect(lambda: trialBalanceComboBox(main))
    main.datefilter.deFrom.dateChanged.connect(lambda: filterbyDate(main))
    main.datefilter.deTo.dateChanged.connect(lambda: filterbyDate(main))
    main.datefilter.pbGetData.clicked.connect(main.datefilter.close)
    main.datefilter.pbCancel.clicked.connect(main.datefilter.close)
    # main.datefilter.pbCancel.clicked.connect(lambda:showTrialBalance(main))

    main.trialbalance.tableView.doubleClicked.connect(lambda:trialBalanceDoubleClicked(main))

    main.paymententry.pbcancel.clicked.connect(main.paymententry.hide)
    main.salesentry.pbcancel.clicked.connect(main.salesentry.hide)
    main.purchaseentry.pbcancel.clicked.connect(main.purchaseentry.hide)
    main.recieptentry.pbcancel.clicked.connect(main.recieptentry.hide)
    main.currconventry.pbcancel.clicked.connect(main.currconventry.hide)


    main.trialbalance.pbFilter.clicked.connect(lambda: filterbyDate(main))
    main.trialbalance.pbFilter.clicked.connect(lambda: filterClicked(main))


# ------------------------------------ For Login Function ---------------------------------------


def loginFunction(main):

    ''' It will Login through Username and Password and redirect to main Window.'''

    try:
        user = main.login.leUserName.text()
        password = main.login.lePassword.text()
        command = ''' SELECT * FROM User_table WHERE username= ? AND password = ? '''
        cursor = main.db_connection.cursor()

        ############################### Alert for user name and password ##############################
        # if not user:
        #     QMessageBox.warning(main, 'Warning', 'Please Fill The Username ')
        #     return
        # if not password:
        #     QMessageBox.warning(main, 'Warning', 'Please Fill The Password.')
        #     return



        try:
            cursor.execute(command,(user, password))

            main.db_connection.commit()
        except sqlite3.Error as e:
            print("Error executing query:", e)

        user_data = cursor.fetchone()
        cursor.close()
        # print(user_data)

        print(user_data)
        if user_data!=[]:

            main.userID=user_data[0]

            main.login.hide()
            # main.show()
            main.showMaximized()
            allObjects(main)
            allSlots(main)
            print('Login Successful')
        else:
            print('Please check your Userid or password')

    except:
        print(traceback.print_exc())


# ------------------------------------ For Company Create ---------------------------------------


def createCompanyPage(main):
    ''' Show the Form for Create Company Page'''


    try:
        # main.hide()
        main.companycreate.show()
        main.hide()


    except:
        print(traceback.print_exc())
    listOfCompany(main)


def createCompany(main):

    ''' Execute the Quary for create company and save the data into database.'''

    # main.widget_2.show(createCompany)


    try:

        company_name = main.companycreate.leComapnyName.text()
        mailing_name = main.companycreate.leMailingName.text()
        address = main.companycreate.ptAddress.toPlainText()
        state = main.companycreate.leState.text()
        country = main.companycreate.leCountry.text()
        pincode = main.companycreate.lePincode.text()
        mobile = main.companycreate.leMobile.text()
        fax = main.companycreate.leFax.text()
        email = main.companycreate.leEmail.text()
        website = main.companycreate.leWebsite.text()
        currency_symbol = main.companycreate.leCurrencySymbol.text()
        formal_name_currency = main.companycreate.leFormalName.text()
        fy_date = main.companycreate.deFYDate.text()
        book_date = main.companycreate.deBookYear.text()

        # Check if a company with the same name already exists in the database
        # cursor = main.db_connection.cursor()
        # check_query = "SELECT COUNT(*) FROM Company_table WHERE Company_name = ?"
        # cursor.execute(check_query, (company_name,))
        # existing_count_tuple = cursor.fetchone()
        # cursor.close()
        #
        # existing_count = existing_count_tuple[0] if existing_count_tuple else 0
        #
        # if existing_count > 0:
        #     QMessageBox.warning(main, 'Warning', 'A company with the same name already exists.')
        # return
    #     # Check if any of the required fields are empty
        main.companycreate.show()

        if (
                not company_name
                or not mailing_name
                or not address
                or not state
                or not country
                or not pincode
                or not mobile
                or not email
                or not currency_symbol
                or not formal_name_currency
                or not fy_date
                or not book_date
        ):
            QMessageBox.warning(main, 'Warning', 'Please fill in all required fields.')
            return

        cursor = main.db_connection.cursor()
        try:
            # print(cursor)

            # Insert data into the Company_table
            insert_query = '''INSERT INTO Company_table (UserID, Company_name, Mailing_name, Address, State, Country, Pincode,
                                    Mobile, Fax, E_mail, Website, Currency_smb, Formal_name, fy_date, book_date)
                                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

            # print(main.userID, company_name, mailing_name, address, state, country, pincode, mobile, fax,
            #           email, website, currency_symbol, formal_name_currency, fy_date, book_date)
            values = (main.userID, company_name, mailing_name, address, state, country, pincode, mobile, fax,
                      email, website, currency_symbol, formal_name_currency, fy_date, book_date)
            # print(values)
            cursor.execute(insert_query, values)
            main.db_connection.commit()

            # Close the database connection
            cursor.close()
            QMessageBox.information(main, 'Success', 'Company entry created successfully!')

            clearCompanyCreateFields(main) # clear the all fields in company create

            # Show a confirmation dialog
            reply = QMessageBox.question(
                main,
                'Confirmation',
                'Company entry created successfully!\nDo you want to continue?',
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )

            if reply == QMessageBox.Yes:

                # User chose to continue, show the gateway window
                # main.gateway(main, company_name)
                # main.gateway.show()
                main.gateway.updateTitleLabel(company_name)
                clearCompanyCreateFields(main)

            else:
                # User chose not to continue, clear the company creation UI
                main.companycreate.clearFields()

            # QMessageBox.information(main, 'Success', 'Company entry created successfully!')
            # main.showConfirmationDialog()

        except sqlite3.Error as e:
            print("Error executing query:", e)
            QMessageBox.critical(main, 'Error', 'Error creating company entry.')
    except:
        print(traceback.print_exc())
    listOfCompany(main)


def clearCompanyCreateFields(main):
    main.companycreate.leComapnyName.clear()
    main.companycreate.leMailingName.clear()
    main.companycreate.ptAddress.clear()
    main.companycreate.leState.clear()
    main.companycreate.leCountry.clear()
    main.companycreate.lePincode.clear()
    main.companycreate.leMobile.clear()
    main.companycreate.leFax.clear()
    main.companycreate.leEmail.clear()
    main.companycreate.leWebsite.clear()
    main.companycreate.leCurrencySymbol.clear()
    main.companycreate.leFormalName.clear()
    main.companycreate.deFYDate.clear()
    main.companycreate.deBookYear.clear()


def listOfCompany(main):

    ''' Show the List of Comapny When clicked on 'List Of Company' button.'''

    try:

        user = main.userID  # Assuming you store the logged-in user ID in main.userID
        print(user) # user= nisha@gmail.com
        command = ''' SELECT * FROM Company_table WHERE UserID = ? '''

        cursor = main.db_connection.cursor()

        try:
            cursor.execute(command, (user,))
            # print(user)
            company_data = cursor.fetchall()
            main.listWidget.clear()

            # Create a QPushButton for each company and add it to the layout
            for company in company_data:
                company_name = company[2]
                company_id = company[1]


                item = QListWidgetItem()
                company_button = QPushButton(company_name)

                company_button.setStyleSheet("QPushButton {"
                             "    background-color: #ffffff;"
                             "  border-radius: 4px;"
                             "    color: #000000;"
                             "   font: 63 11pt Segoe UI Semibold;"
                             "   padding: 5px;"
                              "outline: none;"
                              "margin: 6px;"
                               "text-align:center;"
                             "}"
                                          "QPushButton:selected {"
                                      "background: #1464A0;"
                                      "color: #19232d;"
                                                    "}"
                             "QPushButton:hover {"
                            "border-radius: 4px;"
                             "color: #ffffff;"
                             "   font: 63 11pt Segoe UI Semibold;"
                              "outline: none;"

                            " padding: 5px;"
                             "    background-color: #9BA4B5;"
                             "}")
                # button.clicked.connect(lambda _, name=company_name, id=company_id: gateway(main, name, id))
                company_button.clicked.connect(lambda _, name=company_name, id=company_id: gateway(main, name, id))
                item.setSizeHint(company_button.sizeHint())  # Set the size of the item to match the button's size
                main.listWidget.addItem(item)
                main.listWidget.setItemWidget(item, company_button)

                # Attach additional data (company ID) to the item
                item.setData(Qt.UserRole, company_id)
                # company_button.clicked.connect(lambda _, name=company_name,id=company_id: gateway(main, name ,id))


        except sqlite3.Error as e:
            print("Error executing query:", e)
        cursor.close()



    except:
        print(traceback.print_exc())


# ------------------------------------ For Gateway ---------------------------------------


def gateway(main, company_name, company_id):
    ''' This Function will show the Gatway Window.'''
    try:
        main.hide()
        # comapny_id = main.comapnyID
        main.gateway.showMaximized()
        # main.showMaximized()
        main.companyID = company_id
        main.companyName = company_name
        print(main.companyID)

        main.gateway.updateTitleLabel(company_name)
    except:
        print(traceback.print_exc())


def goToMainWindow(main):
    main.gateway.hide()  # Hide the gateway window
    main.show()  # Show the main window

# ------------------------------------ For Masters ---------------------------------------


def masterList(main):
    ''' This Function will show the Master list window for creation of ledger, group etc.'''
    try:
        # main_window = main.show()
        # main.gateway.hide()
        main.masterlist.show()
        comapny_id = main.companyID
        company_name = main.companyName

    except:
        print(traceback.print_exc())


def showAlterMasterPage(main):
    '''This Function will show master list window for Alteration.'''
    try:

        # main.gateway.hide()
        main.altermasterlist.show()
        comapny_id = main.companyID
        company_name = main.companyName
        # main.altermasterlist.lbCompanyName.setText(f"Welcome to {company_name}")
        # Get the list of group roles and groups created by the company
        group_roles = getGroupRoles(main)
        company_groups = getGroupsCreatedByCompany(main)

        # Combine group roles and company groups into a single list
        role_names = [role[1] for role in group_roles]
        group_names = [group[1] for group in company_groups]
        all_items = role_names + group_names

        # Clear existing items from the drop-down button
        main.createledger.cbUnderGroup.clear()

        # Populate the drop-down button with group role names
        main.createledger.cbUnderGroup.addItems(all_items)


    except:
        print(traceback.print_exc())
    # alterLedgerListpage(main)


# ------------------------------------ For Groups ---------------------------------------

def getGroupRoles(main):

    ''' This function will execute the query to get the group roles from Group role.'''
    try:
        cursor = main.db_connection.cursor()
        query = '''SELECT Group_roleID, Role_name FROM Group_role'''
        cursor.execute(query)
        groups = cursor.fetchall()
        cursor.close()
        return groups
    except sqlite3.Error as e:
        print("Error fetching groups:", e)
        return []


def getGroupsCreatedByCompany(main):

    '''This function will execute the query to get group which is created by that perticular company.'''

    try:
        company_id = main.companyID
        cursor = main.db_connection.cursor()
        query = '''SELECT GroupID, Group_name FROM Group_table WHERE CompanyID = ?'''
        cursor.execute(query, (company_id,))
        groups = cursor.fetchall()
        cursor.close()
        return groups
    except sqlite3.Error as e:
        print("Error fetching groups:", e)
        return []


def creategrouppage(main):
    ''' This Function will show the Window for Create Group.'''
    try:
        main.creategroup.show()
        comapny_id = main.companyID
        print(comapny_id)
        company_name = main.companyName
        # main.creategroup.lbCompanyName.setText(f"Welcome to {company_name}")

        # Get the list of group roles and groups created by the company
        group_roles = getGroupRoles(main)
        # print("group roles ",group_roles)
        company_groups = getGroupsCreatedByCompany(main)

        # Combine group roles and company groups into a single list
        role_names = [role[1] for role in group_roles]
        print("roles name", role_names)
        group_names = [group[1] for group in company_groups]
        print("grous name", group_names)
        all_items = role_names + group_names
        print(all_items)

        # Clear existing items from the drop-down button
        main.creategroup.cbUnderGroup.clear()

        # Populate the drop-down button with group role names
        main.creategroup.cbUnderGroup.addItems(all_items)

       # Connect the submit button's clicked signal to a function

    except:
        print(traceback.print_exc())


def saveGroupData(main):

    ''' This function will execute the query to save the created group into database.'''
    try:
        comapny_id = main.companyID
        # print(comapny_id)
        group_name = main.creategroup.lineEdit.text()
        # print("group_name:",group_name)
        selected_role_index = main.creategroup.cbUnderGroup.currentIndex()
        # print("selected_role_index",selected_role_index)

        # Get the list of group roles
        group_roles = getGroupRoles(main)
        # print("group roles:", group_roles)

        if selected_role_index >= 0 and selected_role_index < len(group_roles):
            selected_group_role_id = group_roles[selected_role_index][0]
            # print("slected group index:", selected_group_role_id)

            # Perform the database insert operation
            cursor = main.db_connection.cursor()
            try:
                insert_query = '''INSERT INTO Group_table (Group_roleID,CompanyID, Group_name)
                                  VALUES (?, ?,?)'''
                values = (selected_group_role_id,comapny_id, group_name)
                # print("vaues:", values)
                cursor.execute(insert_query, values)
                main.db_connection.commit()
                cursor.close()

                QMessageBox.information(
                    main.creategroup, 'Success', 'Group created successfully!'
                )
                reply = QMessageBox.question(
                    main,
                    'Confirmation',
                    'Company entry created successfully!\nDo you want to continue?',
                    QMessageBox.Yes | QMessageBox.No,
                    QMessageBox.No
                )

                if reply == QMessageBox.Yes:
                    print("hello")
                    # User chose to continue, show the gateway window
                    # main.gateway(main, company_name)
                    main.creategroup.hide()
                    main.masterlist.show()
                    # main.gateway.updateTitleLabel(company_name)

                else:
                    # User chose not to continue, clear the company creation UI
                    main.companycreate.clearFields()

            except sqlite3.Error as e:
                print("Error executing query:", e)
                QMessageBox.critical(main, 'Error', 'Error creating company entry.')


                # Clear the input fields
                main.creategroup.lineEdit.clear()
                main.creategroup.cbUnderGroup.setCurrentIndex(-1)

        else:
            QMessageBox.warning(
                main.creategroup, 'Warning', 'Please select a valid group role.'
            )

    except sqlite3.Error as e:
        print("Error creating group:", e)
        QMessageBox.critical(main.creategroup, 'Error', 'Error creating group.')
    # alterGroupListpage(main)


group_list_shown = False
def alterGroupListpage(main):

    ''' This function will show the all ledger list which is created by that particular company.'''
    global group_list_shown  # Declare the flag variable as global
    # Check if the ledger list is already shown, and show it only if it's not shown
    if not group_list_shown:
        try:
            # Show the ledger list
            company_id = main.companyID
            command = ''' SELECT * FROM Group_table WHERE CompanyID = ? '''
            cursor = main.db_connection.cursor()

            try:
                cursor.execute(command, (company_id,))
                group_data = cursor.fetchall()
                main.listWidget.clear()

                for group in group_data:
                    group_name = group[3]
                    group_id = group[0]
                    item = QListWidgetItem()
                    group_button = QPushButton(group_name)
                    # group_button.clicked.connect(
                    #     lambda _, name=group_name, id=group_id: alterLedgerPage(main, name, id))
                    item.setSizeHint(group_button.sizeHint())
                    main.altergrouplist.listwidget.addItem(item)
                    main.altergrouplist.listwidget.setItemWidget(item, group_button)
                    item.setData(Qt.UserRole, group_id)
                    # ledger_button.clicked.connect(main.alterledgerlist.showAlterLedgerFrame)

                # Set the flag to True, indicating that the ledger list is now shown
                group_list_shown = True
            except sqlite3.Error as e:
                print("Error executing query:", e)
            cursor.close()
        except:
            print(traceback.print_exc())
    else:
        # If the ledger list is already shown, you can choose to do nothing or handle it differently
        pass
    main.altergrouplist.show()


# ------------------------------------ For Ledger ---------------------------------------


def createLedgerPage(main):

    '''This Function will show the window for creating ledger.'''

    try:
        main.createledger.show()
        comapny_id = main.companyID
        # print(comapny_id)
        company_name = main.companyName
        # main.createledger.lbCompanyName.setText(f"Welcome to {company_name}")

        # Get the list of group roles and groups created by the company
        group_roles = getGroupRoles(main)
        # print("group roles ", group_roles)
        company_groups = getGroupsCreatedByCompany(main)
        # print("company roles", company_groups)
        branches = getBranch(main)
        print("Branch name:", branches)

        # Combine group roles and company groups into a single list
        role_names = [role[1] for role in group_roles]
        group_names = [group[1] for group in company_groups]
        all_items = role_names + group_names
        # print(all_items)

        branch_name = [branch[1] for branch in branches]
        print(branch_name)



        # Clear existing items from the drop-down button
        main.createledger.cbUnderGroup.clear()
        main.createledger.cbUnderBranch.clear()
        # Populate the drop-down button with group role names
        main.createledger.cbUnderGroup.addItems(all_items)
        main.createledger.cbUnderBranch.addItems(branch_name)

        main.branches = branches


    except:
        print(traceback.print_exc())


def saveledger(main):
    '''This Function will execute the Query to save the data of ledger into database.'''
    try:
        name = main.createledger.leAcName.text()
        print(name)
        mailing_name = main.createledger.leMailingName.text()
        address = main.createledger.ptAddress.toPlainText()
        # state = main.createledger.leAcName.text()
        country = main.createledger.leCountry.text()
        pincode = main.createledger.lePincode.text()
        # date = main.createledger.leAcName.text()
        balance = main.createledger.leBalance.text()


        selected_role = main.createledger.cbUnderGroup.currentText()
        print("selected_role", selected_role)
        # selected_branch_index = main.createledger.cbUnderBranch.currentText()
        # print("selected_branch_text", selected_branch_index)
        selected_branch_text = main.createledger.cbUnderBranch.currentText()
        print("selected_branch_text", selected_branch_text)

        # Find the index of the selected branch name in the branch_name list
        # selected_branch_index = branch_name.index(selected_branch_text)
        # print("selected_branch_index:",selected_branch_index)
        selected_branch_index = None
        for branch in main.branches:
            if branch[1] == selected_branch_text:
                selected_branch_index = branch[0]
                break
        print("selecetd branch index:", selected_branch_index)
        if selected_branch_index is None:
            print("Selected branch not found in the branchs list.")
            return

        # Get the list of group roles
        # group_roles = getGroupRoles(main)
        # print("group roles:", group_roles)
        #
        # if selected_role_index >= 0 and selected_role_index < len(group_roles):
        #     selected_group_role_id = group_roles[selected_role_index][0]
        #     print("slected group index:", selected_group_role_id)

            # Perform the database insert operation
        cursor = main.db_connection.cursor()
        try:
            if hasattr(main, 'ledgerID') and main.ledgerID is not None:
                # If a ledger ID is available (i.e., editing an existing ledger), perform an update
                update_query = '''UPDATE AccountMaster_table SET Ac_name=?,Under_groupName=?, Mailing_name=?,Address=?,
                                Country=?,Pincode=?,Balance=? WHERE AcMasterID=?'''
                update_values = (name,selected_role,mailing_name,address,country,pincode,balance,main.ledgerID)
                print("update values:",update_values)
                cursor.execute(update_query, update_values)
            else:
                insert_query = '''INSERT INTO AccountMaster_table (CompanyID,Ac_name,Under_groupName,Under_branchName, Mailing_name,Address
                                ,Country,Pincode,Balance,BranchID)
                                          VALUES (?,?,?,?,?,?,?,?,?,?)'''
                values = (main.companyID,name,selected_role,selected_branch_text,mailing_name,address,country,pincode,balance,selected_branch_index)
                print("vaues:", values)
                cursor.execute(insert_query, values)
            main.db_connection.commit()
            cursor.close()

            QMessageBox.information(

                main.creategroup, 'Success', 'Ledger created successfully!'

            )

            reply = QMessageBox.question(

                main,

                'Confirmation',

                'Company entry created successfully!\nDo you want to continue?',

                QMessageBox.Yes | QMessageBox.No,

                QMessageBox.No

            )

            if reply == QMessageBox.Yes:

                # User chose to continue, show the gateway window

                # main.gateway(main, company_name)

                main.createledger.hide()

                main.masterlist.show()

                # main.gateway.updateTitleLabel(company_name)


            else:

                # User chose not to continue, clear the company creation UI

                main.companycreate.clearFields()


        except sqlite3.Error as e:

            print("Error executing query:", e)

            QMessageBox.critical(main, 'Error', 'Error creating Ledger entry.')
    except:
        print(traceback.print_exc())
    # alterLedgerListpage(main)
    updateLedgerList(main)


ledger_list_shown = False
def alterLedgerListpage(main):
    ''' This function will show the all ledger list which is created by that particular company.'''
    global ledger_list_shown  # Declare the flag variable as global

    # Check if the ledger list is already shown, and show it only if it's not shown
    if not ledger_list_shown:
        try:
            # Show the ledger list

            company_id = main.companyID
            print(company_id)
            command = ''' SELECT * FROM AccountMaster_table WHERE CompanyID = ? '''
            cursor = main.db_connection.cursor()

            try:
                cursor.execute(command, (company_id,))
                ledger_data = cursor.fetchall()
                main.listWidget.clear()

                for ledger in ledger_data:
                    ledger_name = ledger[2]
                    # print(ledger_name)
                    ledger_id = ledger[0]

                    item = QListWidgetItem()
                    ledger_button = QPushButton(ledger_name)
                    ledger_button.clicked.connect(
                        lambda _, name=ledger_name, id=ledger_id: alterLedgerPage(main, name, id))
                    item.setSizeHint(ledger_button.sizeHint())
                    main.alterledgerlist.listWidget.addItem(item)
                    main.alterledgerlist.listWidget.setItemWidget(item, ledger_button)
                    item.setData(Qt.UserRole, ledger_id)
                    # ledger_button.clicked.connect(main.alterledgerlist.showAlterLedgerFrame)

                # Set the flag to True, indicating that the ledger list is now shown
                # global ledger_list_shown
                ledger_list_shown = True
            except sqlite3.Error as e:
                print("Error executing query:", e)
            cursor.close()
        except:
            print(traceback.print_exc())
    else:
        # If the ledger list is already shown, you can choose to do nothing or handle it differently
        pass
    main.alterledgerlist.show()
    # alterLedgerListpage(main)
    # saveledger(main)
    # createLedgerPage(main)
    updateLedgerList(main)


def alterLedgerPage(main,ledger_name,ledger_id):
    ''' This function will load the data of ledger page.'''

    try:
        main.ledgerID = ledger_id
        print("alter ledger",ledger_id)
        main.ledgerName = ledger_name
        print(ledger_name)
        main.alterledger.show()


        try:
            cursor = main.db_connection.cursor()
            query = '''SELECT * FROM AccountMaster_table WHERE AcMasterID = ?'''
            cursor.execute(query, (ledger_id,))
            ledger_data = cursor.fetchone()
            group_roles = getGroupRoles(main)
            # print("group roles ", group_roles)
            company_groups = getGroupsCreatedByCompany(main)
            branches = getBranch(main)

            # Combine group roles and company groups into a single list
            role_names = [role[1] for role in group_roles]
            group_names = [group[1] for group in company_groups]
            all_items = role_names + group_names
            branch_name = [branch[1] for branch in branches]

            # Clear existing items from the drop-down button
            main.alterledger.cbUnderGroup.clear()
            main.createledger.cbUnderBranch.clear()

            # Populate the drop-down button with group role names
            main.alterledger.cbUnderGroup.addItems(all_items)
            main.alterledger.cbUnderBranch.addItems(branch_name)

            if ledger_data:
                # Populate the fields in the "Create Ledger" form with the retrieved data
                main.alterledger.leAcName.setText(ledger_data[2])  # Assuming ledger name is at index 4
                main.alterledger.leMailingName.setText(ledger_data[6])  # Assuming mailing name is at index 6
                # Set the selected role in the comboBox
                selected_role = ledger_data[3]  # Assuming group role is at index 3
                # main.alterledger.cbUnderGroup.addItem(selected_role)
                main.alterledger.cbUnderGroup.setCurrentText(selected_role)
                # main.createledger.cbUnderGroup.setText(ledger_data[3])
                # main.createledger.leMailingName.text()
                main.alterledger.ptAddress.setPlainText(ledger_data[5])
                # state = main.createledger.leAcName.text()
                main.alterledger.leCountry.setText(ledger_data[7])
                main.alterledger.lePincode.setText(str(ledger_data[8]))
                #  main.createledger.leAcName.text()
                main.alterledger.leBalance.setText(str(ledger_data[10]))
                selected_branch = ledger_data[12]
                main.alterledger.cbUnderBranch.setCurrentText(str(selected_branch))

        except sqlite3.Error as e:
            print("Error fetching ledger data:", e)


    except:
        print(traceback.print_exc())


def saveAlterLedgerData(main):
    '''This Function will execute the Query to save the data of ledger into database.'''
    try:
        name = main.alterledger.leAcName.text()
        print(name)
        mailing_name = main.alterledger.leMailingName.text()
        address = main.alterledger.ptAddress.toPlainText()
        # state = main.alterledger.leAcName.text()
        country = main.alterledger.leCountry.text()
        pincode = main.alterledger.lePincode.text()
        # date = main.alterledger.leAcName.text()
        balance = main.alterledger.leBalance.text()


        selected_role = main.alterledger.cbUnderGroup.currentText()
        print("selected_role_index", selected_role)
        # Get the list of group roles
        group_roles = getGroupRoles(main)
        print("group roles:", group_roles)
        #
        # if selected_role_index >= 0 and selected_role_index < len(group_roles):
        #     selected_group_role_id = group_roles[selected_role_index][0]
        #     print("slected group index:", selected_group_role_id)

            # Perform the database insert operation
        cursor = main.db_connection.cursor()
        try:
            if hasattr(main, 'ledgerID') and main.ledgerID is not None:
                # If a ledger ID is available (i.e., editing an existing ledger), perform an update
                update_query = '''UPDATE AccountMaster_table SET Ac_name=?,Under_groupName=?, Mailing_name=?,Address=?,
                                Country=?,Pincode=?,Balance=? WHERE AcMasterID=?'''
                update_values = (name,selected_role,mailing_name,address,country,pincode,balance,main.ledgerID)
                print("update values:",update_values)
                cursor.execute(update_query, update_values)
            else:
                insert_query = '''INSERT INTO AccountMaster_table (CompanyID,Ac_name,Under_groupName, Mailing_name,Address
                                ,Country,Pincode,Balance)
                                          VALUES (?,?,?,?,?,?,?,?)'''
                values = (main.companyID,name,selected_role,mailing_name,address,country,pincode,balance)
                print("vaues:", values)
                cursor.execute(insert_query, values)
            main.db_connection.commit()
            cursor.close()




            QMessageBox.information(

                main.creategroup, 'Success', ' Ledger Changes successfully!'

            )

            reply = QMessageBox.question(

                main,

                'Confirmation',

                'Company entry created successfully!\nDo you want to continue?',

                QMessageBox.Yes | QMessageBox.No,

                QMessageBox.No

            )

            if reply == QMessageBox.Yes:

                # User chose to continue, show the gateway window

                # main.gateway(main, company_name)

                main.alterledger.close()

                # main.masterlist.show()

                # main.gateway.updateTitleLabel(company_name)


            else:

                # User chose not to continue, clear the company creation UI

                main.companycreate.clearFields()

        except sqlite3.Error as e:

            print("Error executing query:", e)

            QMessageBox.critical(main, 'Error', 'Error creating Ledger entry.')

    except:
        print(traceback.print_exc())
    # alterLedgerListpage(main)


def deleteLedger(main):
    '''This function will delete '''
    try:
        if hasattr(main, 'ledgerID') and main.ledgerID is not None:
            cursor = main.db_connection.cursor()
            delete_query = '''DELETE FROM AccountMaster_table WHERE AcMasterID=?'''
            cursor.execute(delete_query, (main.ledgerID,))
            main.db_connection.commit()
            cursor.close()

            QMessageBox.information(
                main.createledger, 'Success', 'Ledger deleted successfully!'
            )
            # Hide the ledger form after deletion
            main.createledger.hide()
        else:
            QMessageBox.warning(
                main.createledger, 'Warning', 'No ledger selected for deletion!'
            )
    except sqlite3.Error as e:
        print("Error executing query:", e)
        QMessageBox.critical(main, 'Error', 'Error deleting Ledger entry.')
    main.alterledger.close()


def updateLedgerList(main):
    try:
        # Clear the existing items in the list widget
        main.listWidget.clear()

        # Fetch the updated ledger data from the database
        cursor = main.db_connection.cursor()
        query = '''SELECT AcMasterID, Ac_name FROM AccountMaster_table'''
        cursor.execute(query)
        ledger_data = cursor.fetchall()
        cursor.close()

        # Populate the list widget with the ledger data
        for item in ledger_data:
            ledger_id, ledger_name = item
            list_item = QListWidgetItem(ledger_name)
            list_item.setData(Qt.UserRole, ledger_id)  # Store the ledger ID as user data
            main.listWidget.addItem(list_item)

    except sqlite3.Error as e:
        print("Error updating ledger list:", e)


# ------------------------------------ For Branch ---------------------------------------


def createBranchpage(main):
    try:
        main.createbranch.show()
        comapny_id = main.companyID
        print(comapny_id)
        company_name = main.companyName
        # main.createbranch.lbCompanyName.setText(f"Welcome to {company_name}")
    except:
        print(traceback.print_exc())


def getBranch(main):

    ''' This function will execute the query to get the group roles from Group role.'''
    try:
        company_id = main.companyID
        cursor = main.db_connection.cursor()
        query = '''SELECT BranchID,Owner_name FROM Branch_table WHERE CompanyID = ?'''
        cursor.execute(query, (company_id,))
        branch = cursor.fetchall()
        cursor.close()
        return branch
    except sqlite3.Error as e:
        print("Error fetching branch:", e)
        return []


def saveBranchData(main):
    try:
        name = main.createbranch.leOwnerName.text()
        # company_name = main.createbranch.leCompanyName.text()
        cursor = main.db_connection.cursor()
        try:
            insert_query = '''INSERT INTO Branch_table (CompanyID,Owner_name)
                                                      VALUES (?,?)'''
            values = (main.companyID, name)
            cursor.execute(insert_query, values)
            main.db_connection.commit()
            cursor.close()

            QMessageBox.information(

                main.creategroup, 'Success', 'Branch created successfully!'

            )
            reply = QMessageBox.question(

                main,

                'Confirmation',

                'Company entry created successfully!\nDo you want to continue?',

                QMessageBox.Yes | QMessageBox.No,

                QMessageBox.No

            )

            if reply == QMessageBox.Yes:

                main.createbranch.close()

            else:

                # User chose not to continue, clear the company creation UI

                main.createbranch.clearFields()

        except sqlite3.Error as e:

            print("Error executing query:", e)

            QMessageBox.critical(main, 'Error', 'Error creating Branch entry.')


    except:
        print(traceback.print_exc())


def alterBranchList(main):
    try:
        company_id = main.companyID
        # main.alterledgerlist.show()

        # user = main.userID  # Assuming you store the logged-in user ID in main.userID
        if  not main.alterbranchlist.isVisible():
            main.alterbranchlist.show()

            command = ''' SELECT * FROM Branch_table WHERE CompanyID = ? '''

            cursor = main.db_connection.cursor()
            try:
                cursor.execute(command, (company_id,))
                # print(user)
                branch_data = cursor.fetchall()
                main.alterbranchlist.listWidget.clear()
                for branch in branch_data:
                    branch_name = branch[2]
                    print(branch_name)
                    branch_id = branch[1]

                    item = QListWidgetItem()
                    branch_button = QPushButton(branch_name)
                    branch_button.clicked.connect(lambda _, name=branch_name, id=branch_id: branchPageList(main, name, id))
                    # company_button.clicked.connect(lambda _, name=company_name, id=company_id: gateway(main, name, id))
                    item.setSizeHint(branch_button.sizeHint())  # Set the size of the item to match the button's size
                    main.alterbranchlist.listWidget.addItem(item)
                    main.alterbranchlist.listWidget.setItemWidget(item, branch_button)

                    # Attach additional data (company ID) to the item
                    item.setData(Qt.UserRole, branch_id)
            except sqlite3.Error as e:
                print("Error executing query:", e)
            cursor.close()
        else:
            pass

    except:
        print(traceback.print_exc())


def branchPageList(main, branch_name,branch_id):
    try:
        # main.alterbranchledgerlist.show()
        company_id = main.companyID
        print(company_id)
        main.branchID = branch_id
        print(branch_id)
        main.branchName = branch_name
        print(branch_name)

        # main.createledger.show()
        command = ''' SELECT * FROM AccountMaster_table WHERE BranchID = ? '''

        cursor = main.db_connection.cursor()
        try:
            cursor.execute(command, (branch_id,))
            # print(user)
            branch_data = cursor.fetchall()
            print("branch data:", branch_data)
            main.listWidget.clear()
            for branch in branch_data:
                branch_name = branch[2]
                print(branch_name)
                branch_id = branch[12]

        except sqlite3.Error as e:
            print("Error executing query:", e)
        cursor.close()

    except:
        print(traceback.print_exc())


def createComboBoxDelegate(parent):
    combo_box = QComboBox(parent)
    combo_box.addItems(['cell11', 'cell12', 'cell13', 'cell14', 'cell15'])

    delegate = QStyledItemDelegate()

    def setComboBoxEditor(model, index):
        return combo_box

    delegate.createEditor = setComboBoxEditor

    return delegate


# ------------------------------------ For Voucher ---------------------------------------

def updateDayName(main, date):
    day_name = date.toString("dddd")
    main.createvoucher.leDay.setText(day_name)


def showVoucherPage(main):
    try:
        # accountNamesReady = pyqtSignal(list)  # Define a signal
        company_id = main.companyID

        main.createvoucher.show()
        company_name = main.companyName
        # main.createvoucher.lbCompanyName.setText(f"Welcome to {company_name}")

        voucher_type = getVoucherType(main)
        account = getAccountMaster(main)
        # print("group roles ",group_roles)
        # company_groups = getGroupsCreatedByCompany(main)

        # Combine group roles and company groups into a single list
        role_names = [role[1] for role in voucher_type]
        account_name = [name[2] for name in account]
        # group_names = [group[1] for group in company_groups]
        # all_items = role_names + group_names

        main.account = account

        # Clear existing items from the drop-down button
        # main.createvoucher.cbVoucherType.clear()
        # main.createvoucher.cbDebitedAccount.clear()


        current_date = QDate.currentDate()

        # Set the current date for the QDateEdit widget
        main.createvoucher.deDate.setDate(current_date)
        # Get the day of the current date as an integer (e.g., 2 for Tuesday)
        current_day = current_date.dayOfWeek()

        # Map the integer day of the week to its name
        day_name = current_date.toString("dddd")

        # Set the day name as text in your QLineEdit widget
        # main.createvoucher.leDay.setText(day_name)
        # Connect the slot to the dateChanged signal
        # main.createvoucher.deDate.dateChanged.connect(lambda date: updateDayName(main, date))
        # Populate the drop-down button with group role names
        # main.createvoucher.cbVoucherType.addItems(role_names)
        # main.createvoucher.cbDebitedAccount.addItems(account_name)

        main.tableshow.cbAccountName.addItems(account_name)


        # In your CreateVoucherWindow constructor or initialization code
        main.createvoucher.tableView.selectionModel().selectionChanged.connect(lambda :updateSumsOnSelectionChange(main))

        # main.createvoucher.tableView.setItemDelegateForColumn(1, main.combo_delegate)

        # main.createvoucher.cbCreditedAccount.addItems(account_name)
        # main.createvoucher.cbAccountName.addItems(account_name)

    except:
        print(traceback.print_exc())


def getVoucherType(main):

    ''' This function will execute the query to get the group roles from Group role.'''
    try:
        company_id = main.companyID
        cursor = main.db_connection.cursor()
        query = '''SELECT VoucherTypeID,Voucher_name FROM VoucherType_table'''
        cursor.execute(query)
        voucher = cursor.fetchall()
        print("groups:", voucher)
        cursor.close()
        return voucher
    except sqlite3.Error as e:
        print("Error fetching branch:", e)
        return []


def getAccountMaster(main):
    print("hello")

    try:
        company_id = main.companyID
        # print("company id",company_id)
        cursor = main.db_connection.cursor()

        command = ''' SELECT * FROM AccountMaster_table WHERE CompanyID = ? '''
        cursor.execute(command, (company_id,))
        # print(user)
        ledger_data = cursor.fetchall()
        # print("ledger data:", ledger_data)
        cursor.close()
        return ledger_data

    except sqlite3.Error as e:
        print("Error fetchig branch:", e)
        return []


################################################ Voucher Data #################################################

def saveVoucherData(main):
    print("hello voucher")
    # print(data)
    try:
        try:
            company_id = main.companyID
            voucher_type = main.createvoucher.cbVoucherType.currentText()
            debit_account = main.createvoucher.cbDebitedAccount.currentText()
            narration = main.createvoucher.leNarration.text()
            # Create a QDate object for the current date
            selected_date = main.createvoucher.deDate.date()
            selected_date_str = selected_date.toString("dd-MM-yyyy")
            # Update the "day" field in your GUI
            day = main.createvoucher.leDay.text()

            debit_amount = main.createvoucher.lbDebit.text()

            credit_amount = main.createvoucher.lbCredit.text()


            # Generate a unique identifier for the data table
            data_table_id = str(uuid.uuid4())  # Use uuid to generate a unique ID
            debit_amount = main.createvoucher.lbDebit.text()
            print("sum of debit amount", debit_amount)
            credit_amount = main.createvoucher.lbCredit.text()
            print("sum of credit amount:", credit_amount)
            # print("debit sum:",main.debitAmount)
            # print("Credit sum:", main.creditAmount)

            selected_account_index = None
            for account in main.account:
                if account[2] == debit_account:
                    selected_account_index = account[0]
                    break

            if selected_account_index is None:
                print("Selected branch not found in the branchs list.")
                return
            # print("debit sum:",main.debitAmount)
            # print("Credit sum:", main.creditAmount)
            selected_account_index = None
            for account in main.account:
                if account[2] == debit_account:
                    selected_account_index = account[0]
                    break

            if selected_account_index is None:
                return

            selected_accountt_index = None
            for account in main.account:
                if account[2] == main.account_name:
                    selected_accountt_index = account[0]
                    break

            if selected_accountt_index is None:
                return

            try:
                # Insert a new voucher record and store the data table ID
                cursor = main.db_connection.cursor()
                cursor.execute(
                    "INSERT INTO voucher_table (CompanyID,AccountMasterID, VoucherType, DebitAccount,Date,Day, Narration, DebitAmount, CreditAmount , DataTableID) "
                    "VALUES (?, ?, ?, ?,?, ?, ?,?,?,?)", (
                    company_id, selected_account_index, voucher_type, debit_account, selected_date_str,day, narration, debit_amount,
                    credit_amount, data_table_id))
                main.db_connection.commit()

                for row in main.createvoucher.table[:main.createvoucher.last_serialno]:

                    cursor.execute(
                        f"INSERT INTO Data_table (Type, Perticular,CreditAmount,DebitAmount, Currency, VoucherID, CompanyID, AccountMasterID) VALUES (?,?,?, ?,?,?, ?, ?)",
                        (row[0],row[1],row[2],row[3],row[4],data_table_id,company_id,selected_accountt_index))
                    main.db_connection.commit()

                QMessageBox.information(

                    main.createvoucher, 'Success', 'Voucher created successfully!'

                )
                reply = QMessageBox.question(

                    main,

                    'Confirmation',

                    'Company entry created successfully!\nDo you want to continue?',

                    QMessageBox.Yes | QMessageBox.No,

                    QMessageBox.No

                )

                if reply == QMessageBox.Yes:

                    # User chose to continue, show the gateway window

                    # main.gateway(main, company_name)

                    main.createvoucher.clearFields()
                    main.createvoucher.close()
                    main.tableshow.clear()
                    # main.alterledgerlist.hide()
                    # main.masterlist.show()

                    # main.gateway.updateTitleLabel(company_ name)


                else:

                    # User chose not to continue, clear the company creation UI

                    main.createvoucher.clearFields()

            except sqlite3.Error as e:
                print("Error fetchig branch:", e)


            # main.tableshow.cbAccountName.clear()
            # main.tableview.cbDrCr.clear()
            # main.tableshow.leAmount.clear()
            # main.tableview.leAmount.clear()

        except:
            print(traceback.print_exc())


    except:
        print(traceback.print_exc())


def createVoucherpage(main):
    try:
        company_id = main.companyID
        # branch_id = main.branchID

    except:
        print(traceback.print_exc())

def showPaymentEntry(main):
    try:
        main.paymententry.show()
    except:
        print(traceback.print_exc())


def showSalesEntry(main):
    try:
        main.salesentry.show()
    except:
        print(traceback.print_exc())


def showPurchaseEntry(main):
    try:
        main.purchaseentry.show()
    except:
        print(traceback.print_exc())


def showRecieptEntry(main):
    try:
        main.recieptentry.show()
    except:
        print(traceback.print_exc())


def showCurrConvEntry(main):
    try:
        main.currconventry.show()
    except:
        print(traceback.print_exc())

#------------------------------------- Add Raw In TableView -------------------------------
#--------------------------------------Vocher Window ------------------------------
def showTableView(main):
    try:
        main.tableshow.show()
        # Create a QDoubleValidator
        validator = QDoubleValidator()
        # Set the validator to allow only numbers and decimals
        validator.setDecimals(2)
        main.tableshow.leAmount.setValidator(validator)

        # # Connect the signal for cbDrCr combobox
        main.tableshow.cbDrCr.activated.connect(lambda: updateCrDrComboBox(main))


    except:
        print(traceback.print_exc())


def updateCrDrComboBox(main):
    # Check the "Dr" or "Cr" selection and call the appropriate function to refresh the combobox
    main.dr_cr = main.tableshow.cbDrCr.currentText()
    if main.dr_cr == "Dr":
        refreshComboBoxForDr(main)
    elif main.dr_cr == "Cr":
        refreshComboBoxForCr(main)


def updateSumsOnSelectionChange(main):
    try:

        # Calculate and update the sums here
        # Convert the values in the column to integers before summing
        debitSum = np.sum(main.createvoucher.table[:, 2].astype(int))
        print("debit sum", debitSum)
        main.createvoucher.lbDebit.setText(str(debitSum))

        creditSum = np.sum(main.createvoucher.table[:, 3].astype(int))
        main.createvoucher.lbCredit.setText(str(creditSum))

        main.createvoucher.pbSubmit.setVisible(debitSum == creditSum)

    except:
        print(traceback.print_exc())


# Initialize a dictionary to store selected account names for "Dr" and "Cr"
selected_account_names = {"Dr": [], "Cr": []}
# Function to refresh the combobox with account names for "Dr"
def refreshComboBoxForDr(main):
    try:
        account_name = [name[2] for name in main.account]

        # Clear existing items from the drop-down button
        main.tableshow.cbAccountName.clear()

        # Populate the drop-down button with account names that haven't been selected as "Cr"
        available_account_names = [name for name in account_name if name not in selected_account_names["Cr"]]
        # print("available account in dr", available_account_names)
        main.tableshow.cbAccountName.addItems(available_account_names)

    except Exception as e:
        print(traceback.print_exc())


# Function to refresh the combobox with all account names for "Cr"
def refreshComboBoxForCr(main):
    try:
        account_name = [name[2] for name in main.account]

        # Clear existing items from the drop-down button
        main.tableshow.cbAccountName.clear()

        # Populate the drop-down button with account names that haven't been selected as "Cr"
        available_account_names = [name for name in account_name if name not in selected_account_names["Dr"]]
        # print("available account in Cr", available_account_names)


        # Populate the drop-down button with all account names
        main.tableshow.cbAccountName.addItems(available_account_names)

    except Exception as e:
        print(traceback.print_exc())


def addEntary(main):
    # Calculate the sum of amounts in the "Cr" and "Dr" columns
    total_cr = sum(row[3] for row in main.createvoucher.table if row[0] == "Cr")
    total_dr = sum(row[2] for row in main.createvoucher.table if row[0] == "Dr")
    if main.dr_cr == "Cr":
        amount_needed = total_dr - total_cr - main.amount
        print("amount needed in cr", amount_needed)
        if amount_needed > 0:
            # Add a new row with the calculated "Dr" amount
            main.createvoucher.table[main.createvoucher.last_serialno, [0, 1, 3, 4]] = ["Cr", main.account_name,
                                                                                        amount_needed,
                                                                                        main.currency]
            main.createvoucher.last_serialno += 1
            main.createvoucher.model.last_serialno += 1
            main.createvoucher.model.insertRows()

    elif main.dr_cr == "Dr":
        amount_needed = total_cr - total_dr - main.amount
        print("amount needed in dr", amount_needed)
        if amount_needed > 0:
            # Add a new row with the calculated "Cr" amount
            main.createvoucher.table[main.createvoucher.last_serialno, [0, 1, 2, 4]] = ["Dr", main.account_name,
                                                                                        amount_needed,
                                                                                        main.currency]
            main.createvoucher.last_serialno += 1

            main.createvoucher.model.last_serialno += 1
            main.createvoucher.model.insertRows()

    else:
        return  # Invalid selection


def addRaw(main):
    try:
        company_id = main.companyID

        # print(account_name)
        # main.tableview.cbAccountName.clear()
        account_name = main.tableshow.cbAccountName.currentText()
        dr_cr = main.tableshow.cbDrCr.currentText()
        amount =float(main.tableshow.leAmount.text())
        currency = main.tableshow.cbCurrency.currentText()

#----------------------- disable other currency option after selected -----------------------------

        if currency=="INR":
            main.tableshow.cbCurrency.setCurrentIndex(0)  # Set it to INR
            main.tableshow.cbCurrency.setEnabled(False)  # Disable the combobox
        elif currency=="USD":
            main.tableshow.cbCurrency.setCurrentIndex(1)  # Set it to USD
            main.tableshow.cbCurrency.setEnabled(False)
        else:
            main.tableshow.cbCurrency.setEnabled(True)

        main.account_name = main.tableshow.cbAccountName.currentText()
        main.dr_cr = main.tableshow.cbDrCr.currentText()
        # Add the selected account name to the appropriate list
        selected_account_names[main.dr_cr].append(main.account_name)
        main.amount =float(main.tableshow.leAmount.text())

        main.currency = main.tableshow.cbCurrency.currentText()

        # Calculate the sum of amounts in the "Cr" and "Dr" columns
        total_cr = sum(row[3] for row in main.createvoucher.table if row[0] == "Cr")
        total_dr = sum(row[2] for row in main.createvoucher.table if row[0] == "Dr")

        # Disable other currency options if INR is selected in the first row
        if main.currency == "INR":
            main.tableshow.cbCurrency.setCurrentIndex(0)  # Set it to INR
            main.tableshow.cbCurrency.setEnabled(False)  # Disable the combobox
        elif main.currency == "USD":
            main.tableshow.cbCurrency.setCurrentIndex(1)  # Set it to USD
            main.tableshow.cbCurrency.setEnabled(False)



        # Determine the column to update based on "Cr/Dr" selection
        # Determine the column to update based on "Cr/Dr" selection
        if dr_cr == "Cr":
            indexlist=[0,1,3,4]
            # column_index = 2  # Credit Amount Column
        elif dr_cr == "Dr":
            indexlist = [0, 1, 2, 4]
            # column_index = 3  # Debit Amount Column
        else:
            return  # Invalid selection

        # addEntary(main)

        # Update the table with the values
        main.createvoucher.table[main.createvoucher.last_serialno,indexlist] = [main.dr_cr, main.account_name, main.amount,main.currency]


        #
        # # Increment the last_serialno
        main.createvoucher.last_serialno += 1
        main.createvoucher.model.last_serialno += 1
        main.createvoucher.model.insertRows()
        main.createvoucher.model.rowCount() # print(main.createvoucher.model.rowCount())

        # Emit dataChanged signal for the modified row
        ind = main.createvoucher.model.index(0, 0)
        ind1 = main.createvoucher.model.index(0, 1)
        main.createvoucher.model.dataChanged.emit(ind, ind1)

        print(main.createvoucher.table[:main.createvoucher.last_serialno],type(main.createvoucher.table[:main.createvoucher.last_serialno]))
        debitSum = main.createvoucher.table[:main.createvoucher.last_serialno,3].sum()
        main.debitAmount =  main.createvoucher.lbDebit.setText(str(debitSum))
        print("debit Sum Amount")

        creditSum = main.createvoucher.table[:main.createvoucher.last_serialno,2].sum()
        main.creditAmount = main.createvoucher.lbCredit.setText(str(creditSum))

        # print(main.createvoucher.table[:main.createvoucher.last_serialno],type(main.createvoucher.table[:main.createvoucher.last_serialno]))
        updateSumsOnSelectionChange(main)
        # refreshComboBoxes(main, main.dr_cr)
        ############### Clear the input widgets after adding data#################
        # main.tableshow.cbAccountName.setCurrentIndex(0)
        main.tableshow.cbDrCr.setCurrentIndex(0)
        main.tableshow.leAmount.clear()
        # main.tableshow.cbCurrency.setCurrentIndex(0)
        main.tableshow.hide()

    except:
        print(traceback.print_exc())


def deleteRows(main):
    try:
        main.createvoucher.last_serialno -= 1
        main.createvoucher.model.last_serialno -= 1
        main.createvoucher.model.DelRows()
        main.createvoucher.model.rowCount()

        # Recalculate the sums after deleting the row
        updateSumsOnSelectionChange(main)

        ind = main.createvoucher.model.index(0, 0)
        ind1 = main.createvoucher.model.index(0, 1)
        main.createvoucher.model.dataChanged.emit(ind, ind1)
    except:
        print(traceback.print_exc())


#------------------------------------------- Day Book ------------------------------------------


def fetchDayBookData(main):
    try:
        cursor = main.db_connection.cursor()
        command = "SELECT Date,DebitAccount, VoucherType, DebitAmount , CreditAmount FROM Voucher_table Where CompanyID = ?"
        cursor.execute(command, (main.companyID,))
        data = cursor.fetchall()
        # print("data:", data)
        for row in data:
            main.daybook.table[main.daybook.last_serialno] = list(row)
            print(main.daybook.table[main.daybook
                  .last_serialno])
            main.daybook.last_serialno += 1
            main.daybook.model.last_serialno += 1
            main.daybook.model.insertRows()
            main.daybook.model.rowCount()

            # Emit dataChanged signal for the modified row
            ind = main.daybook.model.index(0, 0)
            ind1 = main.daybook.model.index(0, 1)
            main.daybook.model.dataChanged.emit(ind, ind1)

    except:
        print(traceback.print_exc())


def showDayBook(main):
    try:
        main.daybook.show()
        fetchDayBookData(main)
    except:
        print(traceback.print_exc())


def filterDataByDate(main):
    try:
        selectedDate = main.daybook.deDateEdit.date()
        # Convert the selectedDate to a string in the required format
        selectedTextDate = selectedDate.toString("dd-MM-yyyy")
        print("selected date", selectedTextDate)
        main.selectdate = selectedTextDate

        # proxy_model = main.daybook.smodel  # Get the QSortFilterProxyModel

        # Set the filter string to match the selected date
        main.daybook.smodel.setFilterFixedString(main.selectdate)
        print("day book data", main.daybook.smodel.setFilterFixedString(main.selectdate))
        # Notify the view to update
        # main.daybook.smodel.invalidateFilter()

    except:
        print(traceback.print_exc())


# ------------------------------------ For Trial Balance ---------------------------------------


def fetchTrialBalanceData(main,fromdate='01-04-2023',enddate=datetime.today().strftime('%d-%m-%Y')):
    try:
        print(enddate)

        main.trialbalance.table[0:main.trialbalance.last_serialno] =[0,0,0,0]

        main.trialbalance.model.DelRows(0,main.trialbalance.last_serialno)
        main.trialbalance.last_serialno=0
        main.trialbalance.model.last_serialno=0
        main.trialbalance.model.rowCount()
        ind = main.trialbalance.model.index(0, 0)
        ind1 = main.trialbalance.model.index(0, 1)
        main.trialbalance.model.dataChanged.emit(ind, ind1)




        cursor = main.db_connection.cursor()
        command = """
                    SELECT
                        AccountMaster_table.Ac_name,
                        SUM(Voucher_table.DebitAmount) AS TotalDebit,
                        SUM(Voucher_table.CreditAmount) AS TotalCredit
                    FROM
                        AccountMaster_table
                    JOIN
                        Voucher_table ON AccountMaster_table.AcMasterID = Voucher_table.AccountMasterID
                    WHERE
                        AccountMaster_table.CompanyID = ? 
                        AND  Voucher_table.Date BETWEEN  ? AND ?
                    GROUP BY
                        AccountMaster_table.AcMasterID,
                        AccountMaster_table.Ac_name
                    """
        cursor.execute(command, (main.companyID,fromdate,enddate,))

        data = cursor.fetchall()

        # LEFT JOIN Voucher_table AS Voucher_table ON AccountMaster_table.AcMasterID = Voucher_table.AccountMasterID
        # LEFT JOIN Data_table AS Data_table ON AccountMaster_table.AcMasterID = Data_table.AccountMasterID

        for row in data:
            main.trialbalance.table[main.trialbalance.last_serialno,[0,1,2]] = list(row)
            print(main.trialbalance.table[main.trialbalance
                  .last_serialno])
            main.trialbalance.last_serialno += 1
            main.trialbalance.model.last_serialno += 1
            main.trialbalance.model.insertRows()
            main.trialbalance.model.rowCount()


            ind = main.trialbalance.model.index(0, 0)
            ind1 = main.trialbalance.model.index(0, 1)
            main.trialbalance.model.dataChanged.emit(ind, ind1)

        total_debit = sum(row[1] if row[1] is not None else 0 for row in data)
        total_credit = sum(row[2] if row[2] is not None else 0 for row in data)

        # lbCredit and lbDebit with the sum
        main.trialbalance.lbdebitINR.setText(str(total_debit))
        main.trialbalance.lbcreditINR.setText(str(total_credit))

        # main.trialbalance.lbdebitINR.setText(f"{total_debit} INR")
        # main.trialbalance.lbcreditINR.setText(f"{total_credit} INR")


    except:
        print(traceback.print_exc())


def showTrialBalance(main):
    try:
        current_date = QDate.currentDate()
        current_date_str = current_date.toString("dd-MM-yyyy")
        main.trialbalance.lbDate.setText(current_date_str)

        date = main.datefilter.deFrom.date()
        fromdate = date.toString("dd-MM-yyyy")
        print('dateeeee',fromdate)

        main.trialbalance.show()
        fetchTrialBalanceData(main)
    except:
        print(traceback.print_exc())


def fetchTrialBalanceGroup(main,fromdate='01-04-2023',enddate=datetime.today().strftime('%d-%m-%Y')):
    try:

        main.trialbalance.table[0:main.trialbalance.last_serialno] = [0, 0, 0, 0]

        main.trialbalance.model.DelRows(0, main.trialbalance.last_serialno)
        main.trialbalance.last_serialno = 0
        main.trialbalance.model.last_serialno = 0
        main.trialbalance.model.rowCount()
        ind = main.trialbalance.model.index(0, 0)
        ind1 = main.trialbalance.model.index(0, 1)
        main.trialbalance.model.dataChanged.emit(ind, ind1)

        cursor = main.db_connection.cursor()

        # cursor.execute("SELECT AccountMaster_table.Under_groupname,Voucher_table.CreditAmount, Voucher_table.DebitAmount FROM AccountMaster_table JOIN Voucher_table ON AccountMaster_table.AcMasterID = Voucher_table.AccountMasterID;")
        command = """
                    SELECT 
                        AccountMaster_table.Under_groupname,
                        SUM(Voucher_table.DebitAmount) AS TotalDebit, 
                        SUM(Voucher_table.CreditAmount) AS TotalCredit
                    FROM 
                        AccountMaster_table
                    JOIN 
                        Voucher_table ON AccountMaster_table.AcMasterID = Voucher_table.AccountMasterID
                    WHERE
                        AccountMaster_table.CompanyID = ?
                       AND Voucher_table.Date BETWEEN  ? AND ?
                    GROUP BY 
                        AccountMaster_table.Under_groupname
                """
        cursor.execute(command, (main.companyID,fromdate,enddate,))
        data = cursor.fetchall()

        for row in data:
            main.trialbalance.table[main.trialbalance.last_serialno, [0, 1, 2]] = list(row)
            print(main.trialbalance.table[main.trialbalance
                  .last_serialno])
            main.trialbalance.last_serialno += 1
            main.trialbalance.model.last_serialno += 1
            main.trialbalance.model.insertRows()
            main.trialbalance.model.rowCount()

            ind = main.trialbalance.model.index(0, 0)
            ind1 = main.trialbalance.model.index(0, 1)
            main.trialbalance.model.dataChanged.emit(ind, ind1)

        total_debit = sum(row[1] if row[1] is not None else 0 for row in data)
        total_credit = sum(row[2] if row[2] is not None else 0 for row in data)

        # Update the lbCredit and lbDebit QLable widgets with the calculated sums
        main.trialbalance.lbdebitINR.setText(str(total_debit))
        main.trialbalance.lbcreditINR.setText(str(total_credit))

    except:
        print(traceback.print_exc())


def fetchTrialBalanceBranch(main,fromdate='01-04-2023',enddate=datetime.today().strftime('%d-%m-%Y')):
    try:

        main.trialbalance.table[0:main.trialbalance.last_serialno] = [0, 0, 0, 0]

        main.trialbalance.model.DelRows(0, main.trialbalance.last_serialno)
        main.trialbalance.last_serialno = 0
        main.trialbalance.model.last_serialno = 0
        main.trialbalance.model.rowCount()
        ind = main.trialbalance.model.index(0, 0)
        ind1 = main.trialbalance.model.index(0, 1)
        main.trialbalance.model.dataChanged.emit(ind, ind1)

        cursor = main.db_connection.cursor()
        # cursor.execute("SELECT AccountMaster_table.under_branchname, Voucher_table.CreditAmount, Voucher_table.DebitAmount FROM AccountMaster_table AS AccountMaster_table JOIN Voucher_table AS Voucher_table ON AccountMaster_table.AcMasterID = Voucher_table.AccountMasterID; ")
        command = """
                    SELECT 
                        AccountMaster_table.under_branchname,
                        SUM(Voucher_table.DebitAmount) AS TotalDebit, 
                        SUM(Voucher_table.CreditAmount) AS TotalCredit 
                    FROM 
                        AccountMaster_table
                    JOIN 
                        Voucher_table ON AccountMaster_table.AcMasterID = Voucher_table.AccountMasterID
                    WHERE
                        AccountMaster_table.CompanyID = ?
                        AND Voucher_table.Date BETWEEN  ? AND ?
                    GROUP BY 
                        AccountMaster_table.under_branchname
                 """
        cursor.execute(command, (main.companyID,fromdate,enddate,))
        data = cursor.fetchall()

        # main.trialbalance.model.beginResetModel()  # Reset the model
        for row in data:
            main.trialbalance.table[main.trialbalance.last_serialno, [0, 1, 2]] = list(row)
            print(main.trialbalance.table[main.trialbalance
                  .last_serialno])
            main.trialbalance.last_serialno += 1
            main.trialbalance.model.last_serialno += 1
            main.trialbalance.model.insertRows()
            main.trialbalance.model.rowCount()

            ind = main.trialbalance.model.index(0, 0)
            ind1 = main.trialbalance.model.index(0, 1)
            main.trialbalance.model.dataChanged.emit(ind, ind1)

        total_debit = sum(row[1] if row[1] is not None else 0 for row in data)
        total_credit = sum(row[2] if row[2] is not None else 0 for row in data)

        # Update the lbCredit and lbDebit QLable widgets with the calculated sums
        main.trialbalance.lbdebitINR.setText(str(total_debit))
        main.trialbalance.lbcreditINR.setText(str(total_credit))

    except:
        print(traceback.print_exc())


def trialBalanceComboBox(main):
    try:

        main.trialbalance.model.clear()
        main.trialbalance.last_serialno = 0
        main.trialbalance.model.last_serialno = 0

        selcted_item = main.trialbalance.cbtrialbalance.currentText()
        print(selcted_item)
        main.is_filtered = False
        print("44444444444444444444444444444444444444444444444444444444444444444444444")
        if selcted_item ==("Ledger-Wise"):
            fetchTrialBalanceData(main)
        elif selcted_item ==("Group-Wise"):
            fetchTrialBalanceGroup(main)
        else:
            fetchTrialBalanceBranch(main)

    except:
        print(traceback.print_exc())


def filterClicked(main):
    try:
        main.trialbalance.model.clear()
        main.trialbalance.last_serialno = 0
        main.trialbalance.model.last_serialno = 0

        selcted_item = main.trialbalance.cbtrialbalance.currentText()
        main.is_filtered = True
        print("66666655555555555555555555555555555555555555555555555555555555")
        if selcted_item ==("Ledger-Wise"):
            main.datefilter.pbGetData.clicked.connect(lambda: fetchTrialBalanceData(main, main.selectdateFrom, main.selectdateTo))

        elif selcted_item ==("Group-Wise"):
            main.datefilter.pbGetData.clicked.connect(lambda :fetchTrialBalanceGroup(main,main.selectdateFrom,main.selectdateTo))

        else:
            main.datefilter.pbGetData.clicked.connect(lambda :fetchTrialBalanceBranch(main,main.selectdateFrom,main.selectdateTo))


    except:
        print(traceback.print_exc())


def trialBalanceDoubleClicked(main):
    try:
        idy = main.trialbalance.cbtrialbalance.currentText()

        if main.is_filtered :

            print("22222222222222222222222222222222222222222222222222222222222222")

            if idy=="Ledger-Wise":
                cursor = main.db_connection.cursor()
                command = """SELECT Date, DebitAccount, VoucherType,DebitAmount,CreditAmount
                                  FROM Voucher_table
                                  WHERE Voucher_table.Date BETWEEN  ? AND ?"""

                cursor.execute(command, (main.selectdateFrom, main.selectdateTo))
                data = cursor.fetchall()
                idx = main.trialbalance.tableView.selectedIndexes()[0].data()
                filtered_data = [row for row in data if row[1] == idx]
            elif idy=="Group-Wise":
                cursor = main.db_connection.cursor()
                command = """SELECT
                                 Voucher_table.Date,
                                 Voucher_table.DebitAccount,
                                 Voucher_table.VoucherType,
                                 Voucher_table.DebitAmount,
                                 Voucher_table.CreditAmount,
                                 AccountMaster_table.Under_groupName
                              FROM
                                 AccountMaster_table
                              JOIN
                                 Voucher_table ON AccountMaster_table.AcMasterID = Voucher_table.AccountMasterID
                              WHERE
                                 AccountMaster_table.CompanyID = ?
                                 AND Voucher_table.Date BETWEEN  ? AND ?"""

                cursor.execute(command, (main.companyID,main.selectdateFrom, main.selectdateTo,))
                data = cursor.fetchall()
                idx = main.trialbalance.tableView.selectedIndexes()[0].data()
                filtered_data = [row for row in data if row[5] == idx]
            else:
                cursor = main.db_connection.cursor()
                command = """SELECT
                                 Voucher_table.Date,
                                 Voucher_table.DebitAccount,
                                 Voucher_table.VoucherType,
                                 Voucher_table.DebitAmount,
                                 Voucher_table.CreditAmount,
                                 AccountMaster_table.under_branchname
                              FROM
                                 AccountMaster_table
                              JOIN
                                 Voucher_table ON AccountMaster_table.AcMasterID = Voucher_table.AccountMasterID
                              WHERE
                                 AccountMaster_table.CompanyID = ?
                                 AND Voucher_table.Date BETWEEN  ? AND ?"""

                cursor.execute(command, (main.companyID,main.selectdateFrom, main.selectdateTo,))
                data = cursor.fetchall()
                idx = main.trialbalance.tableView.selectedIndexes()[0].data()
                filtered_data = [row for row in data if row[5] == idx]
            main.is_filtered = True

        else:
            print("333333333333333333333333333333333333333333333333333333333333")

            if idy == "Ledger-Wise":
                cursor = main.db_connection.cursor()
                command = """SELECT Date, DebitAccount, VoucherType,DebitAmount,CreditAmount
                                  FROM Voucher_table"""

                cursor.execute(command, )
                data = cursor.fetchall()
                idx = main.trialbalance.tableView.selectedIndexes()[0].data()
                filtered_data = [row for row in data if row[1] == idx]
            elif idy == "Group-Wise":
                cursor = main.db_connection.cursor()
                command = """SELECT
                                 Voucher_table.Date,
                                 Voucher_table.DebitAccount,
                                 Voucher_table.VoucherType,
                                 Voucher_table.DebitAmount,
                                 Voucher_table.CreditAmount,
                                 AccountMaster_table.Under_groupName
                              FROM
                                 AccountMaster_table
                              JOIN
                                 Voucher_table ON AccountMaster_table.AcMasterID = Voucher_table.AccountMasterID
                              WHERE
                                 AccountMaster_table.CompanyID = ?"""

                cursor.execute(command, (main.companyID,))
                data = cursor.fetchall()
                idx = main.trialbalance.tableView.selectedIndexes()[0].data()
                filtered_data = [row for row in data if row[5] == idx]
            else:
                cursor = main.db_connection.cursor()
                command = """SELECT
                                 Voucher_table.Date,
                                 Voucher_table.DebitAccount,
                                 Voucher_table.VoucherType,
                                 Voucher_table.DebitAmount,
                                 Voucher_table.CreditAmount,
                                 AccountMaster_table.under_branchname
                              FROM
                                 AccountMaster_table
                              JOIN
                                 Voucher_table ON AccountMaster_table.AcMasterID = Voucher_table.AccountMasterID
                              WHERE
                                 AccountMaster_table.CompanyID = ?"""

                cursor.execute(command, (main.companyID,))
                data = cursor.fetchall()
                idx = main.trialbalance.tableView.selectedIndexes()[0].data()
                filtered_data = [row for row in data if row[5] == idx]



        print('idx', idx)
        # print("filtered_data",filtered_data)

         # Create a QDialog to display the data in a table view
        dialog = QDialog(main)
        dialog.setWindowTitle("Data Details")
        dialog.setGeometry(580, 300, 450, 350)

        # Create a QTableView and set the data model
        table_view = QTableView()
        model = QStandardItemModel()
        model.setColumnCount(5)
        model.setHorizontalHeaderLabels(["Date","Perticulars", "Voucher Type", "Debit Amount INR", "Credit Amount INR","banchName"])


        for row in filtered_data:
            # model.appendRow([QStandardItem(str(item)) for item in row])
            items = [QStandardItem(str(item)) for item in row]
            for item in items:
                item.setFlags(item.flags() ^ Qt.ItemIsEditable)  # Make cells non-editable
            model.appendRow(items)

        table_view.setModel(model)
        table_view.horizontalHeader().setStretchLastSection(True)
        table_view.setSelectionBehavior(QTableView.SelectRows)

        # Hide the 6th column (index 5)
        table_view.setColumnHidden(5, True)

        layout = QVBoxLayout()
        layout.addWidget(table_view)
        dialog.setLayout(layout)

        # Show the dialog
        dialog.exec_()

    except Exception as e:
        print(traceback.print_exc())


# --------------------------------------- Filtered By From to To -------------------------------

def filterbyDate(main):
    try:

        current_date = QDate.currentDate()
        # current_date_str = current_date.toString("dd-MM-yyyy")
        main.datefilter.deTo.setDate(current_date)

        main.datefilter.show()

        selectedDateFrom = main.datefilter.deFrom.date()
        selectedTextDateFrom = selectedDateFrom.toString("dd-MM-yyyy")
        main.selectdateFrom = selectedTextDateFrom
        # print("9416515", main.selectdateFrom, selectedTextDateFrom)

        selectedDateTo = main.datefilter.deTo.date()
        selectedTextDateTo = selectedDateTo.toString("dd-MM-yyyy")
        main.selectdateTo = selectedTextDateTo
        # print("4515151", main.selectdateTo, selectedTextDateTo)



    except Exception as e:
        # print(traceback.print_exc())
        print(e)



