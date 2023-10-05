import datetime
import json
import sqlite3
import traceback
import uuid
from datetime import datetime
from collections import defaultdict
from functools import partial
from PyQt5.QtCore import QModelIndex
import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import QStandardItem, QDoubleValidator
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from PyQt5.QtWidgets import *
from PyQt5.uic.properties import QtCore

from Applications.Views.BalanceSheet.balancesheet import BalanceSheetWindow
# from Applications.Views.DayBook.date_filter_daybook import DateFilterInDayBookWindow
from Applications.Views.DayBook.day_book import DayBookWindow
from Applications.Views.Branch.alter_branch_list import AlterBranchListWindow
from Applications.Views.Branch.create_branch import BranchCreateWindow
from Applications.Views.CompanyCreate.company_create import CompanyCreateWindow
from Applications.Views.CreateGroup.alter_group_list import AlterGroupListWindow
from Applications.Views.CreateGroup.create_group import CreateGroupWindow
from Applications.Views.DayBook.day_book import DayBookWindow
from Applications.Views.Gateways.gateways import GatewaysWindow
from Applications.Views.Home.home import HomeWindow
from Applications.Views.LeadgerBalance.leadger_balance import LedgerBalanceWindow
from Applications.Views.Ledger.alter_ledger_list import AlterLedgerListWindow
from Applications.Views.Ledger.alter_ledger_show import AlterLedgerUpdateWindow
from Applications.Views.Ledger.ledger_create import CreateLedgerWindow
from Applications.Views.MasterList.alter_master_list import AlterMasterListWindow
from Applications.Views.MasterList.master_list import MasterListWindow
from Applications.Views.TrialBalance.date_filter import DateFilterWindow
from Applications.Views.TrialBalance.trial_balance import TrialBalanceWindow
from Applications.Views.Voucher.contra_entry import ContraEnteryWindow
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
    main.createbranch = BranchCreateWindow() # Branch List Window For Alteration
    main.createvoucher  = CreateVoucherWindow()  # Create Voucher Window
    main.alterbranchlist = AlterBranchListWindow()  #Ledger list Branch wise for Alteration
    main.createbranch = BranchCreateWindow() # Branch List Window For Alteration
    main.altergrouplist = AlterGroupListWindow()  # Group List Window For Alteration
    main.alterledger = AlterLedgerUpdateWindow()
    main.daybook = DayBookWindow()

    main.trialbalance = TrialBalanceWindow()
    main.datefilter = DateFilterWindow()
    main.balancesheet = BalanceSheetWindow()
    main.ledgerblance = LedgerBalanceWindow()


    #-------------------------------------- Voucher Object --------------------------------
    main.createvoucher = CreateVoucherWindow()  # Create Voucher Window
    main.paymententry = PaymentEntryWindow()
    main.salesentry = SalesEntryWindow()
    main.purchaseentry = PurchaseEntryWindow()
    main.recieptentry = RecieptEntryWindow()
    main.currconventry = CurrConvEntryWindow()
    main.contraentry = ContraEnteryWindow()



    ##################################### Gateway ###################################################

    main.gateway.fCreate.layout().addWidget(main.masterlist)
    main.gateway.fAlter.layout().addWidget(main.altermasterlist)
    main.gateway.fVouchers.layout().addWidget(main.createvoucher)
    main.gateway.fDayBook.layout().addWidget(main.daybook)
    main.gateway.fBalanceSheet.layout().addWidget(main.balancesheet)
    main.gateway.fTrialBalance.layout().addWidget(main.trialbalance)
    main.gateway.fLedgerBalance.layout().addWidget(main.ledgerblance)

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
    main.pbCreateCompany.clicked.connect(lambda: clearCompanyCreateFields(main))



    #-------------------------------- Gateway Window -------------------------------#
    main.gateway.pbCreateMaster.clicked.connect(lambda: masterList(main))
    main.gateway.pbAlterMaster.clicked.connect(lambda: showAlterMasterPage(main))
    main.gateway.pbDayBook.clicked.connect(lambda: showDayBook(main))
    main.gateway.pbVouchers.clicked.connect(lambda: showVoucherPage(main))
    main.gateway.pbTrailBalance.clicked.connect(lambda: showTrialBalance(main))
    main.gateway.pbLedgerBalance.clicked.connect(lambda: showLedgerBalance(main))
    main.gateway.pbCreateMaster.clicked.connect(main.gateway.showCreateFrame)
    main.gateway.pbAlterMaster.clicked.connect(main.gateway.showAlterFrame)
    main.gateway.pbDayBook.clicked.connect(main.gateway.showDayBookFrame)
    main.gateway.pbVouchers.clicked.connect(main.gateway.showVouchersFrame)
    main.gateway.pbBalanceSheet.clicked.connect(main.gateway.showBalanceSheetFrame)
    main.gateway.pbTrailBalance.clicked.connect(main.gateway.showTrialBalanceFrame)
    main.gateway.pbLedgerBalance.clicked.connect(main.gateway.showLedgerBalanceFrame)
    main.gateway.pbChangeCompany.clicked.connect(lambda: goToMainWindow(main))
    main.gateway.pbClose.clicked.connect(main.gateway.close)
    main.balancesheet.pbBack.clicked.connect(main.balancesheet.hide)

    # -------------------------------- Master List Window -------------------------------#
    main.masterlist.pbCreateGroup.clicked.connect(lambda: creategrouppage(main))
    main.masterlist.pdCreateLedger.clicked.connect(lambda: createLedgerPage(main))
    main.masterlist.pbCreateBranch.clicked.connect(lambda: createBranchpage(main))
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
    #####################################################################################
    main.altermasterlist.pbAlterBranch.clicked.connect(main.altermasterlist.showAlterBranch)
    main.alterledgerlist.pbClose.clicked.connect(main.alterledgerlist.hide)
    main.altergrouplist.pbClose.clicked.connect(main.altergrouplist.hide)

    #---------------------------- Create Branch Window ----------------------------------#
    main.createbranch.pbSubmit.clicked.connect(lambda: saveBranchData(main))
    main.alterledger.pbSubmit.clicked.connect(lambda: saveAlterLedgerData(main))
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
    main.createvoucher.pbContra.clicked.connect(lambda: showContraEntry(main))
    main.createvoucher.pbDeleteRaw.clicked.connect(lambda: deleteRows(main))
    main.createvoucher.pbDelete.clicked.connect(lambda : deleteVoucher(main))
    main.createvoucher.pbPayment.clicked.connect(lambda: setVoucherType(main))
    main.createvoucher.pbSales.clicked.connect(lambda: setVoucherType(main))
    main.createvoucher.pbPurchase.clicked.connect(lambda: setVoucherType(main))
    main.createvoucher.pbReciept.clicked.connect(lambda: setVoucherType(main))
    main.createvoucher.pbCurConvsn.clicked.connect(lambda: setVoucherType(main))
    main.createvoucher.pbContra.clicked.connect(lambda : setVoucherType(main))
    main.createvoucher.pbCreateLedger.clicked.connect(lambda :createLedger(main))
    main.createvoucher.pbBack.clicked.connect(main.createvoucher.hide)
    main.currconventry.pbcancel.clicked.connect(main.currconventry.hide)

        #-----------------------------        Contra Window ----------------------------#
    main.contraentry.pdAddRaw.clicked.connect(lambda: addRawInContra(main))
    main.contraentry.pbcancel.clicked.connect(main.contraentry.hide)

        #--------------------------------------- Receipt Window ------------------------------#
    main.recieptentry.pdAddRaw.clicked.connect(lambda: addRawInReciept(main))
    main.recieptentry.pbcancel.clicked.connect(main.recieptentry.hide)

        #------------------------------------  Payment Window ------------------------------#
    main.paymententry.pdAddRaw.clicked.connect(lambda: addRawInPayment(main))
    main.paymententry.pbcancel.clicked.connect(main.paymententry.hide)

        #------------------------------------  Sales Window ------------------------------#
    main.salesentry.pdAddRaw.clicked.connect(lambda: addRawInSales(main))
    main.salesentry.pbcancel.clicked.connect(main.salesentry.hide)


    #------------------------------------  Purchase Window ------------------------------#
    main.purchaseentry.pdAddRaw.clicked.connect(lambda: addRawInPurchase(main))
    main.purchaseentry.pbcancel.clicked.connect(main.purchaseentry.hide)


    #----------------------------------- Day Book Window ------------------------------------------#
    main.daybook.leAccount.textChanged.connect(lambda: filterDataByAccountName(main))
    main.daybook.tableView.doubleClicked.connect(lambda : dayBookDoubleClicked(main))
    main.daybook.pbGetData.clicked.connect(lambda: filterDataByDateRange(main))
    main.daybook.tableView.doubleClicked.connect(lambda: dayBookDoubleClicked(main))
    main.daybook.pbBack.clicked.connect(main.daybook.hide)

    # ------------------------------------- Trial Balance ------------------------------#

    main.trialbalance.cbtrialbalance.activated.connect(lambda: trialBalanceComboBox(main))
    main.datefilter.deFrom.dateChanged.connect(lambda: filterbyDate(main))
    main.datefilter.deTo.dateChanged.connect(lambda: filterbyDate(main))
    main.gateway.pbTrailBalance.clicked.connect(lambda: showTrialBalance(main))
    main.datefilter.pbCancel.clicked.connect(lambda:showTrialBalance(main))
    main.trialbalance.tableView.doubleClicked.connect(lambda:trialBalanceDoubleClicked(main))
    main.trialbalance.pbFilter.clicked.connect(lambda: filterbyDate(main))
    main.trialbalance.pbFilter.clicked.connect(lambda: filterClicked(main))
    main.datefilter.pbGetData.clicked.connect(main.datefilter.close)
    main.datefilter.pbCancel.clicked.connect(main.datefilter.close)
    main.trialbalance.pbBack.clicked.connect(main.trialbalance.hide)

    # ------------------------------------- Ledger Balance ------------------------------#
    main.ledgerblance.pbBack.clicked.connect(main.ledgerblance.close)
    main.ledgerblance.pbGetData.clicked.connect(lambda: filterDataByDateInLedgerBalance(main))


# ------------------------------------ For Login Function ---------------------------------------

def loginFunction(main):

    try:
        user = main.login.leUserName.text()
        password = main.login.lePassword.text()
        command = ''' SELECT * FROM User_table WHERE username= ? AND password = ? '''
        cursor = main.db_connection.cursor()
        ############################### Alert for user name and password ##############################
        if not user:
            QMessageBox.warning(main, 'Warning', 'Please Fill The Username ')
            return
        if not password:
            QMessageBox.warning(main, 'Warning', 'Please Fill The Password.')
            return

        try:
            cursor.execute(command,(user, password))

            main.db_connection.commit()
        except sqlite3.Error as e:
            print("Error executing query:", e)

        user_data = cursor.fetchone()
        cursor.close()

        print(user_data)
        if user_data!=[]:
            main.userID=user_data[0]
            main.login.hide()
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
        main.companycreate.show()
        main.hide()

    except:
        print(traceback.print_exc())
    listOfCompany(main)



def createCompany(main):
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

        # if existing_count > 0:
        #     QMessageBox.warning(main, 'Warning', 'A company with the same name already exists.')
        # return
        # Check if any of the required fields are empty
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
            insert_query = '''INSERT INTO Company_table (UserID, Company_name, Mailing_name, Address, State, Country, Pincode,
                                    Mobile, Fax, E_mail, Website, Currency_smb, Formal_name, fy_date, book_date)
                                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            values = (main.userID, company_name, mailing_name, address, state, country, pincode, mobile, fax,
                      email, website, currency_symbol, formal_name_currency, fy_date, book_date)
            cursor.execute(insert_query, values)
            main.db_connection.commit()

            # Close the database connection
            cursor.close()
            QMessageBox.information(main, 'Success', 'Company entry created successfully!')


            # Show a confirmation dialog
            reply = QMessageBox.question(
                main,
                'Confirmation',
                'Company entry created successfully!\nDo you want to continue?',
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )

            if reply == QMessageBox.Yes:
                main.gateway.updateTitleLabel(company_name)
                clearCompanyCreateFields(main)  # clear the all fields in company create
                main.companycreate.pbSubmit.clicked.connect(main.companycreate.hide)


            else:
                pass
                clearCompanyCreateFields(main)  # clear the all fields in company create

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
            company_data = cursor.fetchall()
            main.listWidget.clear()

            # Create a QPushButton for each company and add it to the layout
            for company in company_data:
                company_name = company[2]
                company_id = company[1]

                item = QListWidgetItem()
                company_button = QPushButton(company_name)
                company_button.setStyleSheet( "QPushButton {" "width: 150px;"
                                                "cursor: pointer;"
                                                "height: 30px;"
                                                "font: 63 11pt Segoe UI Semibold;"
                                                "background-color: #293241;"
                                                "color: #FFFFFF;"
                                                "border: none;"
                                                "text-align: center;"
                                                "text-decoration: none;"
                                                "display: inline-block;"
                                                "font-size: 16px;"
                                                "margin: 8px;"
                                                "border-radius: 5px;""}"
                                                "QPushButton:hover {"
                                                "background-color: #f0f0f0;"
                                                "color: #000000;""}");

                company_button.clicked.connect(lambda _, name=company_name, id=company_id: gateway(main, name, id))
                item.setSizeHint(company_button.sizeHint())  # Set the size of the item to match the button's size
                main.listWidget.addItem(item)
                main.listWidget.setItemWidget(item, company_button)

                # Attach additional data (company ID) to the item
                item.setData(Qt.UserRole, company_id)

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
        main.gateway.showMaximized()
        main.companyID = company_id
        main.companyName = company_name
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
        main.masterlist.show()
        comapny_id = main.companyID
        company_name = main.companyName

    except:
        print(traceback.print_exc())


def showAlterMasterPage(main):
    '''This Function will show master list window for Alteration.'''
    try:

        main.altermasterlist.show()
        comapny_id = main.companyID
        company_name = main.companyName
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
        company_name = main.companyName

        # Get the list of group roles and groups created by the company
        group_roles = getGroupRoles(main)
        company_groups = getGroupsCreatedByCompany(main)

        # Combine group roles and company groups into a single list
        role_names = [role[1] for role in group_roles]
        group_names = [group[1] for group in company_groups]
        all_items = role_names + group_names
        # Clear existing items from the drop-down button
        main.creategroup.cbUnderGroup.clear()

        # Populate the drop-down button with group role names
        main.creategroup.cbUnderGroup.addItems(all_items)

    except:
        print(traceback.print_exc())



def saveGroupData(main):

    ''' This function will execute the query to save the created group into database.'''
    try:
        comapny_id = main.companyID
        group_name = main.creategroup.lineEdit.text()
        selected_role_index = main.creategroup.cbUnderGroup.currentIndex()

        # Get the list of group roles
        group_roles = getGroupRoles(main)

        if selected_role_index >= 0 and selected_role_index < len(group_roles):
            selected_group_role_id = group_roles[selected_role_index][0]

            # Perform the database insert operation
            cursor = main.db_connection.cursor()
            try:
                insert_query = '''INSERT INTO Group_table (Group_roleID,CompanyID, Group_name)
                                  VALUES (?, ?,?)'''
                values = (selected_group_role_id,comapny_id, group_name)
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
                    main.creategroup.hide()
                    main.masterlist.show()

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


group_list_shown = False
def alterGroupListpage(main):
    try:

        ''' This function will show the all ledger list which is created by that particular company.'''
        global group_list_shown  # Declare the flag variable as global
        # Check if the ledger list is already shown, and show it only if it's not shown
        company_groups = getGroupsCreatedByCompany(main)

        if not group_list_shown:
            try:
                # Show the ledger list
                company_id = main.companyID
                command = ''' SELECT * FROM Group_role WHERE CompanyID = ? '''
                cursor = main.db_connection.cursor()

                try:
                    cursor.execute(command, (company_id,))
                    role_names = cursor.fetchall()
                    group_data = role_names + company_groups
                    main.listWidget.clear()

                    for group in group_data:
                        group_name = group[1]
                        group_id = group[0]
                        item = QListWidgetItem()
                        group_button = QPushButton(group_name)
                        item.setSizeHint(group_button.sizeHint())
                        main.altergrouplist.listwidget.addItem(item)
                        main.altergrouplist.listwidget.setItemWidget(item, group_button)
                        item.setData(Qt.UserRole, group_id)

                    # Set the flag to True, indicating that the ledger list is now shown
                    group_list_shown = True
                except sqlite3.Error as e:
                    print("Error executing query:", e)
                cursor.close()
            except:
                print(traceback.print_exc())
        else:
            pass
        main.altergrouplist.show()
    except:
        print(traceback.print_exc())


# ------------------------------------ For Ledger ---------------------------------------


def createLedgerPage(main):

    '''This Function will show the window for creating ledger.'''

    try:
        main.createledger.show()
        comapny_id = main.companyID
        company_name = main.companyName
        # Get the list of group roles and groups created by the company
        group_roles = getGroupRoles(main)
        company_groups = getGroupsCreatedByCompany(main)
        branches = getBranch(main)

        # Combine group roles and company groups into a single list
        role_names = [role[1] for role in group_roles]
        group_names = [group[1] for group in company_groups]
        all_items = role_names + group_names

        branch_name = [branch[1] for branch in branches]

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
        mailing_name = main.createledger.leMailingName.text()
        address = main.createledger.ptAddress.toPlainText()
        country = main.createledger.leCountry.text()
        pincode = main.createledger.lePincode.text()
        balance = main.createledger.leBalance.text()

        selected_role = main.createledger.cbUnderGroup.currentText()
        selected_branch_text = main.createledger.cbUnderBranch.currentText()

        selected_branch_index = None
        for branch in main.branches:
            if branch[1] == selected_branch_text:
                selected_branch_index = branch[0]
                break
        if selected_branch_index is None:
            return

            # Perform the database insert operation
        cursor = main.db_connection.cursor()
        try:
            if hasattr(main, 'ledgerID') and main.ledgerID is not None:
                # If a ledger ID is available (i.e., editing an existing ledger), perform an update
                update_query = '''UPDATE AccountMaster_table SET Ac_name=?,Under_groupName=?, Mailing_name=?,Address=?,
                                Country=?,Pincode=?,Balance=? WHERE AcMasterID=?'''
                update_values = (name,selected_role,mailing_name,address,country,pincode,balance,main.ledgerID)
                cursor.execute(update_query, update_values)
            else:
                insert_query = '''INSERT INTO AccountMaster_table (CompanyID,Ac_name,Under_groupName,Under_branchName, Mailing_name,Address
                                ,Country,Pincode,Balance,BranchID)
                                          VALUES (?,?,?,?,?,?,?,?,?,?)'''
                values = (main.companyID,name,selected_role,selected_branch_text,mailing_name,address,country,pincode,balance,selected_branch_index)
                cursor.execute(insert_query, values)
            main.db_connection.commit()
            cursor.close()

            QMessageBox.information(

                main.creategroup, 'Success', 'Ledger created successfully!'
            )

            reply = QMessageBox.question(
                main,
                'Confirmation',
                'Account Master  entry created successfully!\nDo you want to continue?',
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )

            if reply == QMessageBox.Yes:
                # User chose to continue, show the gateway window
                main.createledger.hide()
                main.masterlist.show()

            else:
                # User chose not to continue, clear the company creation UI
                main.companycreate.clearFields()

        except sqlite3.Error as e:
            print("Error executing query:", e)
            QMessageBox.critical(main, 'Error', 'Error creating Ledger entry.')
    except:
        print(traceback.print_exc())
    updateLedgerList(main)


ledger_list_shown = False
def alterLedgerListpage(main):
    global ledger_list_shown  # Declare the flag variable as global

    # Check if the ledger list is already shown, and show it only if it's not shown
    if not ledger_list_shown:
        try:
            company_id = main.companyID
            command = ''' SELECT * FROM AccountMaster_table WHERE CompanyID = ? '''
            cursor = main.db_connection.cursor()

            try:
                cursor.execute(command, (company_id,))
                ledger_data = cursor.fetchall()

                main.listWidget.clear()

                for ledger in ledger_data:
                    ledger_name = ledger[1]
                    ledger_id = ledger[0]

                    item = QListWidgetItem()
                    ledger_button = QPushButton(ledger_name)
                    ledger_button.clicked.connect(
                        lambda _, name=ledger_name, id=ledger_id: alterLedgerPage(main, name, id))
                    item.setSizeHint(ledger_button.sizeHint())
                    main.alterledgerlist.listWidget.addItem(item)
                    main.alterledgerlist.listWidget.setItemWidget(item, ledger_button)
                    item.setData(Qt.UserRole, ledger_id)

                # Set the flag to True, indicating that the ledger list is now shown
                ledger_list_shown = True
            except sqlite3.Error as e:
                print("Error executing query:", e)
            cursor.close()
        except:
            print(traceback.print_exc())
    else:
        pass
    main.alterledgerlist.show()
    updateLedgerList(main)


def alterLedgerPage(main,ledger_name,ledger_id):

     # This function will load the data of ledger page.
    try:
        main.ledgerID = ledger_id
        main.ledgerName = ledger_name
        main.alterledger.show()

        try:
            cursor = main.db_connection.cursor()
            query = '''SELECT * FROM AccountMaster_table WHERE AcMasterID = ?'''
            cursor.execute(query, (ledger_id,))
            ledger_data = cursor.fetchone()
            group_roles = getGroupRoles(main)
            company_groups = getGroupsCreatedByCompany(main)
            branches = getBranch(main)

            # Combine group roles and company groups into a single list
            role_names = [role[1] for role in group_roles]
            group_names = [group[1] for group in company_groups]
            all_items = role_names + group_names
            branch_name = [branch[1] for branch in branches]

            # Clear existing items from the drop-down button
            main.alterledger.cbUnderGroup.clear()
            main.alterledger.cbUnderBranch.clear()

            # Populate the drop-down button with group role names
            main.alterledger.cbUnderGroup.addItems(all_items)
            main.alterledger.cbUnderBranch.addItems(branch_name)

            if ledger_data:
                # Populate the fields in the "Create Ledger" form with the retrieved data
                main.alterledger.leAcName.setText(ledger_data[1])  # Assuming ledger name is at index 1
                main.alterledger.leMailingName.setText(ledger_data[4])  # Assuming mailing name is at index 4
                # Set the selected role in the comboBox
                selected_role = ledger_data[3]  # Assuming group role is at index 3
                main.alterledger.cbUnderGroup.setCurrentText(selected_role)
                main.alterledger.ptAddress.setPlainText(ledger_data[5])
                main.alterledger.leCountry.setText(ledger_data[7])
                main.alterledger.lePincode.setText(str(ledger_data[8]))
                main.alterledger.leBalance.setText(str(ledger_data[10]))
                selected_branch = ledger_data[12]
                main.alterledger.cbUnderBranch.setCurrentText(str(selected_branch))

        except sqlite3.Error as e:
            print("Error fetching ledger data:", e)


    except:
        print(traceback.print_exc())


def saveAlterLedgerData(main):
    try:
        name = main.alterledger.leAcName.text()
        mailing_name = main.alterledger.leMailingName.text()
        address = main.alterledger.ptAddress.toPlainText()
        country = main.alterledger.leCountry.text()
        pincode = main.alterledger.lePincode.text()
        balance = main.alterledger.leBalance.text()


        selected_role = main.alterledger.cbUnderGroup.currentText()
        # Get the list of group roles
        group_roles = getGroupRoles(main)


            # Perform the database insert operation
        cursor = main.db_connection.cursor()
        try:
            if hasattr(main, 'ledgerID') and main.ledgerID is not None:
                # If a ledger ID is available (i.e., editing an existing ledger), perform an update
                update_query = '''UPDATE AccountMaster_table SET Ac_name=?,Under_groupName=?, Mailing_name=?,Address=?,
                                Country=?,Pincode=?,Balance=? WHERE AcMasterID=?'''
                update_values = (name,selected_role,mailing_name,address,country,pincode,balance,main.ledgerID)
                cursor.execute(update_query, update_values)

                reply = QMessageBox.question(
                    main,
                    'Confirmation',
                    'Ledger Update successfully!\nDo you want to continue?',
                    QMessageBox.Yes | QMessageBox.No,
                    QMessageBox.No
                )
            else:
                QMessageBox.information(
                    main.creategroup, 'Success', ' Ledger Changes successfully!'
                )

                insert_query = '''INSERT INTO AccountMaster_table (CompanyID,Ac_name,Under_groupName, Mailing_name,Address
                                ,Country,Pincode,Balance)
                                          VALUES (?,?,?,?,?,?,?,?)'''
                values = (main.companyID,name,selected_role,mailing_name,address,country,pincode,balance)
                cursor.execute(insert_query, values)

                reply = QMessageBox.question(
                    main,
                    'Confirmation',
                    'Ledger entry created successfully!\nDo you want to continue?',
                    QMessageBox.Yes | QMessageBox.No,
                    QMessageBox.No
                )
            main.db_connection.commit()
            cursor.close()

            if reply == QMessageBox.Yes:
                main.alterledger.close()

            else:
                main.alterledger.clearFields()

        except sqlite3.Error as e:
            print("Error executing query:", e)
            QMessageBox.critical(main, 'Error', 'Error creating Ledger entry.')

    except:
        print(traceback.print_exc())


def deleteLedger(main):
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
        main.db_connection.commit()
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
        company_name = main.companyName
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
                main.createbranch.clearFields()

        except sqlite3.Error as e:
            print("Error executing query:", e)
            QMessageBox.critical(main, 'Error', 'Error creating Branch entry.')
    except:
        print(traceback.print_exc())


def alterBranchList(main):
    try:
        company_id = main.companyID
        # user = main.userID  # Assuming you store the logged-in user ID in main.userID
        if  not main.alterbranchlist.isVisible():
            main.alterbranchlist.show()

            command = ''' SELECT * FROM Branch_table WHERE CompanyID = ? '''

            cursor = main.db_connection.cursor()
            try:
                cursor.execute(command, (company_id,))
                branch_data = cursor.fetchall()
                main.alterbranchlist.listWidget.clear()
                for branch in branch_data:
                    branch_name = branch[1]
                    branch_id = branch[1]

                    item = QListWidgetItem()
                    branch_button = QPushButton(branch_name)
                    branch_button.clicked.connect(lambda _, name=branch_name, id=branch_id: branchPageList(main, name, id))
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
        company_id = main.companyID
        main.branchID = branch_id
        main.branchName = branch_name

        command = ''' SELECT * FROM AccountMaster_table WHERE BranchID = ? '''

        cursor = main.db_connection.cursor()
        try:
            cursor.execute(command, (branch_id,))
            branch_data = cursor.fetchall()
            main.listWidget.clear()
            for branch in branch_data:
                branch_name = branch[2]
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

voucher_numbers = {}
def getVoucherNumber(main):
    try:
        voucher_type = main.createvoucher.cbVoucherType.currentText()

        # Check if voucher type is in the dictionary, if not, initialize it with 1
        if voucher_type not in voucher_numbers:
            voucher_numbers[voucher_type] = 1
        else:
            # Increment the voucher number for this voucher type
            voucher_numbers[voucher_type] += 1

        # Set the voucher number in the "No." box
        main.createvoucher.leNoVoucher.setText(str(voucher_numbers[voucher_type]))
    except:
        print(traceback.print_exc())

def setVoucherType(main):
    try:
        # Get the text of the clicked button and set it as the voucher type
        sender_button = main.sender()
        if sender_button:
            main.createvoucher.lbVoucherType.setText(sender_button.text())
    except:
        print(traceback.print_exc())


def generate_new_voucher_number(main):
    try:
        cursor = main.db_connection.cursor()

        # Query to retrieve the maximum voucher number
        cursor.execute("SELECT MAX(VoucherNO) FROM Voucher_Master")
        max_voucher_no = cursor.fetchone()[0]

        # Check if max_voucher_no is None (i.e., no existing vouchers)
        if max_voucher_no is None:
            new_voucher_no = "Voucher_0001"
        else:
            # Extract the numeric part from the maximum voucher number
            numeric_part = int(max_voucher_no.split("_")[1])
            # Increment the numeric part by 1
            numeric_part += 1
            # Combine the prefix and incremented numeric part
            new_voucher_no = f"Voucher_{numeric_part:04d}"
        return new_voucher_no

    except Exception as e:
        print("Error generating new voucher number:", str(e))
        return None


def showVoucherPage(main):
    try:
        main.createvoucher.show()
        main.createvoucher.clearFields()
        new_voucher_number = generate_new_voucher_number(main)
        main.createvoucher.leVoucherNo.setText(new_voucher_number)
        main.createvoucher.pbDelete.setVisible(False)

        account = getAccountMaster(main)
        account_name = [name[1] for name in account]
        main.account = account

        current_date = QDate.currentDate()
        main.createvoucher.deDate.setDate(current_date)

        main.createvoucher.pbSubmit.setVisible(False)
        main.createvoucher.model.dataChanged.connect(lambda: updateSumsOnSelectionChange(main))
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
        cursor.close()
        return voucher
    except sqlite3.Error as e:
        print("Error fetching branch:", e)
        return []


def getAccountMaster(main):

    try:
        company_id = main.companyID
        cursor = main.db_connection.cursor()

        command = ''' SELECT * FROM AccountMaster_table WHERE CompanyID = ? '''
        cursor.execute(command, (company_id,))
        ledger_data = cursor.fetchall()
        cursor.close()
        return ledger_data

    except sqlite3.Error as e:
        print("Error fetchig branch:", e)
        return []

################################################ Voucher Data #################################################

def saveVoucherData(main):
    try:
        try:
            company_id = main.companyID
            main.voucherNo = main.createvoucher.leVoucherNo.text()

            voucher_type = main.createvoucher.lbVoucherType.text()

            narration = main.createvoucher.leNarration.text()
            selected_date = main.createvoucher.deDate.date()
            selected_date_str = selected_date.toString("dd-MM-yyyy")  # Convert QDate to string in the format "YYYY-MM-DD"
            main.selected_date_str = selected_date.toString(
                "dd-MM-yyyy")  # Convert QDate to string in the format "YYYY-MM-DD"

            # Generate a unique identifier for the data table
            data_table_id = str(uuid.uuid4())  # Use uuid to generate a unique ID
            debit_amount = main.createvoucher.lbDebit.text()
            credit_amount = main.createvoucher.lbCredit.text()
            currency = main.createvoucher.lbCurrency.text()
            #
            try:
                # Insert a new voucher record and store the data table ID
                cursor = main.db_connection.cursor()

                if hasattr(main, 'voucherNo') and main.voucherNo is not None:
                    # A voucher number is available, so we can check for an existing voucher
                    query = '''SELECT VoucherID FROM Voucher_Master WHERE VoucherNO = ?'''
                    cursor.execute(query, (main.voucherNo,))
                    existing_voucher_id = cursor.fetchone()
                else:
                    # Handle the case where main.voucherNo is not defined (e.g., set a default voucher number)
                    # You can use a default voucher number or prompt the user to enter one
                    # default_voucher_no = "DEFAULT_VOUCHER_NO"  # Replace with your default value or logic
                    # main.voucherNo = default_voucher_no
                    existing_voucher_id = None

                num_rows = main.createvoucher.last_serialno

                # Count the current number of "Cr" and "Dr" rows
                num_cr_rows = sum(1 for row in main.createvoucher.table if row[0] == "Cr")
                num_dr_rows = sum(1 for row in main.createvoucher.table if row[0] == "Dr")
                if existing_voucher_id:

                    # If a ledger ID is available (i.e., editing an existing ledger), perform an update
                    update_query = '''UPDATE Voucher_Master SET CompanyID=?, VoucherType=?,Date=?,
                                    Narration=?,DebitAmount=?,CreditAmount=?,Currency=? WHERE VoucherID=? AND VoucherNO=?'''
                    update_values = (
                        company_id, voucher_type, main.selected_date_str, narration, debit_amount,
                        credit_amount, currency,existing_voucher_id[0], main.voucherNo)
                    cursor.execute(update_query, update_values)

                    query = '''SELECT VoucherID FROM Voucher_details
                                                          WHERE VoucherID=? '''
                    cursor.execute(query, (existing_voucher_id[0],))
                    existing_entry = cursor.fetchone()

                    if existing_entry:
                        if num_rows == 2:
                            update_query = '''UPDATE Voucher_details
                                             SET DebitSideAccount=?, CreditSideAccount=?, DebitAmount=? , 
                                             CreditAmount=? , Currency=?
                                             WHERE VoucherID=? '''
                            update_values = (
                            main.createvoucher.table[0, 1], main.createvoucher.table[1, 1], main.createvoucher.table[0, 2],
                            main.createvoucher.table[1, 3]
                            , main.createvoucher.table[0, 4], existing_voucher_id[0])
                            cursor.execute(update_query, update_values)
                            # Insert corresponding entries in Ledger_table
                            updateLedgerEntries(main, main.createvoucher.table[0, 1], main.createvoucher.table[1, 1],
                                                main.createvoucher.table[0, 2], main.createvoucher.table[0, 4]
                                                )
                        else:
                            if num_cr_rows == 1 and num_dr_rows >= 2:
                                # Save data for multiple debit rows and a single credit row
                                debit_rows = [row for row in main.createvoucher.table if row[0] == "Dr"]
                                credit_row = [row for row in main.createvoucher.table if row[0] == "Cr"][0]

                                for debit_row in debit_rows:

                                     updated_query_dr = '''UPDATE Voucher_details
                                                 SET DebitSideAccount=? , CreditSideAccount=?,DebitAmount=? , 
                                                 CreditAmount=? , Currency=?
                                                 WHERE VoucherID=? AND  DebitSideAccount=? AND CreditSideAccount=?'''


                                     updated_value_dr =  (debit_row[1], credit_row[1],debit_row[2], debit_row[2], debit_row[4],
                                                        existing_voucher_id[0],debit_row[1], credit_row[1])
                                     cursor.execute(updated_query_dr, updated_value_dr)


                                    # Insert corresponding entries in Ledger_table
                                     updateLedgerEntries(main, debit_row[1], credit_row[1], debit_row[2], debit_row[4])


                            elif num_dr_rows == 1 and num_cr_rows >= 2:
                                # Save data for multiple credit rows and a single debit row
                                credit_rows = [row for row in main.createvoucher.table if row[0] == "Cr"]
                                debit_row = [row for row in main.createvoucher.table if row[0] == "Dr"][0]

                                voucher_master_id = cursor.lastrowid  # Assuming you have the master voucher ID

                                for credit_row in credit_rows:

                                    updated_query_cr = '''UPDATE Voucher_details
                                                        SET DebitSideAccount=? ,CreditSideAccount=?,DebitAmount=? , 
                                                        CreditAmount=? , Currency=?
                                                        WHERE VoucherID=? AND DebitSideAccount=? AND CreditSideAccount=?'''
                                    updated_value_cr = (debit_row[1],credit_row[1],credit_row[3], credit_row[3], debit_row[4],
                                         existing_voucher_id[0],debit_row[1],credit_row[1])
                                    cursor.execute(updated_query_cr, updated_value_cr)



                                    # Insert corresponding entries in Ledger_table
                                    updateLedgerEntries(main, debit_row[1], credit_row[1], credit_row[3], debit_row[4]
                                                        )

                    main.db_connection.commit()

                    reply = QMessageBox.question(
                        main,
                        'Confirmation',
                        'Voucher Updated successfully!\nDo you want to continue?',
                        QMessageBox.Yes | QMessageBox.No,
                        QMessageBox.No
                    )
                else:

                    QMessageBox.information(
                        main.createvoucher, 'Success', 'Voucher created successfully!'
                    )

                    insert_query = '''INSERT INTO Voucher_Master (CompanyID,VoucherNO,VoucherType,Date, Narration, DebitAmount, CreditAmount, Currency)
                        VALUES (?, ?, ?, ?,?, ?,?,?)'''


                    value = (
                        company_id,main.voucherNo,voucher_type, main.selected_date_str, narration, debit_amount,
                        credit_amount,currency)
                    cursor.execute(insert_query, value)
                    main.db_connection.commit()
                    if num_rows == 2:
                        voucher_master_id = cursor.lastrowid

                        cursor.execute(
                            f"INSERT INTO Voucher_details (DebitSideAccount, CreditSideAccount,DebitAmount,CreditAmount, Currency, VoucherID) VALUES (?,?,?, ?,?,?)",
                            (main.createvoucher.table[0, 1], main.createvoucher.table[1, 1], main.createvoucher.table[0, 2],
                             main.createvoucher.table[1, 3], main.createvoucher.table[0, 4], voucher_master_id))
                        main.db_connection.commit()

                        # Insert corresponding entries in Ledger_table
                        insertLedgerEntries(main, main.createvoucher.table[0, 1], main.createvoucher.table[1, 1],
                                            main.createvoucher.table[0, 2], main.createvoucher.table[0, 4]
                                            )
                    else:
                        if num_cr_rows == 1 and num_dr_rows >= 2:
                            # Save data for multiple debit rows and a single credit row
                            debit_rows = [row for row in main.createvoucher.table if row[0] == "Dr"]
                            credit_row = [row for row in main.createvoucher.table if row[0] == "Cr"][0]

                            voucher_master_id = cursor.lastrowid  # Assuming you have the master voucher ID

                            for debit_row in debit_rows:
                                cursor.execute(
                                    "INSERT INTO Voucher_details (DebitSideAccount, CreditSideAccount, DebitAmount, CreditAmount, Currency, VoucherID) VALUES (?, ?, ?, ?, ?, ?)",
                                    (debit_row[1], credit_row[1], debit_row[2], debit_row[2], debit_row[4],
                                     voucher_master_id))
                                main.db_connection.commit()

                                # Insert corresponding entries in Ledger_table
                                insertLedgerEntries(main, debit_row[1], credit_row[1], debit_row[2], debit_row[4]
                                                    )

                        elif num_dr_rows == 1 and num_cr_rows >= 2:
                            # Save data for multiple credit rows and a single debit row
                            credit_rows = [row for row in main.createvoucher.table if row[0] == "Cr"]
                            debit_row = [row for row in main.createvoucher.table if row[0] == "Dr"][0]
                            voucher_master_id = cursor.lastrowid  # Assuming you have the master voucher ID

                            for credit_row in credit_rows:

                                cursor.execute(
                                    "INSERT INTO Voucher_details (DebitSideAccount, CreditSideAccount, DebitAmount, CreditAmount, Currency, VoucherID) VALUES (?, ?, ?, ?, ?, ?)",
                                    (debit_row[1], credit_row[1], credit_row[3], credit_row[3], debit_row[4],
                                     voucher_master_id))
                                main.db_connection.commit()

                                # Insert corresponding entries in Ledger_table
                                insertLedgerEntries(main, debit_row[1], credit_row[1], credit_row[3], debit_row[4]
                                                    )

                    reply = QMessageBox.question(

                        main,
                        'Confirmation',
                        'Voucher entry created successfully!\nDo you want to continue?',
                        QMessageBox.Yes | QMessageBox.No,
                        QMessageBox.No
                    )

                closingBalanceIdea(main)

                if reply == QMessageBox.Yes:

                    # User chose to continue, show the gateway window
                    main.createvoucher.table[0: main.createvoucher.last_serialno] = [0, 0, 0, 0, 0]

                    main.createvoucher.model.DelRows(0, main.createvoucher.last_serialno)
                    main.createvoucher.last_serialno = 0
                    main.createvoucher.model.last_serialno = 0
                    main.createvoucher.model.rowCount()

                    ind = main.createvoucher.model.index(0, 0)
                    ind1 = main.createvoucher.model.index(0, 1)
                    main.createvoucher.model.dataChanged.emit(ind, ind1)


                    main.createvoucher.lbCredit.clear()
                    main.createvoucher.leNarration.clear()
                    main.createvoucher.lbDebit.clear()
                    main.createvoucher.lbCurrency.clear()


                    setVoucherType(main)
                    new_voucher_number = generate_new_voucher_number(main)
                    main.createvoucher.leVoucherNo.setText(new_voucher_number)

                    main.recieptentry.cbCurrency.setEnabled(True)
                    main.salesentry.cbCurrency.setEnabled(True)
                    main.purchaseentry.cbCurrency.setEnabled(True)
                    main.paymententry.cbCurrency.setEnabled(True)
                    main.contraentry.cbCurrency.setEnabled(True)

                    main.recieptentry.cbAccountName.clear()
                    main.salesentry.cbAccountName.clear()
                    main.purchaseentry.cbAccountName.clear()
                    main.paymententry.cbAccountName.clear()
                    main.contraentry.cbAccountName.clear()

                else:
                    main.createvoucher.clearFields()

            except :
                print("Error fetchig voucher:", traceback.print_exc())
        except:
            print(traceback.print_exc())
    except:
        print(traceback.print_exc())

def updateLedgerEntries(main,debit_account, credit_account, amount, currency):
    try:
        voucher_no = main.voucherNo
        date = main.selected_date_str
        cursor = main.db_connection.cursor()

        if hasattr(main, 'voucherNo') and main.voucherNo is not None:
            # A voucher number is available, so we can check for an existing voucher
            query = '''SELECT LedgerID  FROM Ledger_table WHERE VoucherNO = ? AND  LedgerName=? AND  Perticulars=? '''
            cursor.execute(query, (main.voucherNo,debit_account,credit_account,))
            existing_ledger_id_dr = cursor.fetchone()
        else:
            existing_ledger_id_dr = None
        if existing_ledger_id_dr:
            update_query = '''UPDATE Ledger_table
                               SET Date=?,
                               Currency=?, Debit=?
                               WHERE  VoucherNo=? AND Credit=0'''
            value = (date,  currency, amount, main.voucherNo)
            cursor.execute(update_query, value)
        else:
            pass
        if hasattr(main, 'voucherNo') and main.voucherNo is not None:
            # A voucher number is available, so we can check for an existing voucher
            query = '''SELECT LedgerID  FROM Ledger_table WHERE VoucherNO = ? AND  LedgerName=? AND  Perticulars=? '''
            cursor.execute(query, (main.voucherNo, credit_account, debit_account,))
            existing_ledger_id_cr = cursor.fetchone()
        else:
            existing_ledger_id_cr = None

        if existing_ledger_id_cr:
            update_query2 = '''UPDATE Ledger_table
                               SET Date=?,
                               Currency=?,Credit=?
                               WHERE VoucherNo=? AND Debit=0 '''
            value2 = ( date, currency, amount, main.voucherNo)
            cursor.execute(update_query2, value2)
        else:
            pass
        main.db_connection.commit()
    except:
        print(traceback.print_exc())

def insertLedgerEntries(main, debit_account, credit_account, amount, currency):
    try:
        voucher_no = main.voucherNo
        date = main.selected_date_str
        cursor = main.db_connection.cursor()

        if hasattr(main, 'voucherNo') and main.voucherNo is not None:
            # A voucher number is available, so we can check for an existing voucher
            query = '''SELECT LedgerID  FROM Ledger_table WHERE VoucherNO = ? AND  LedgerName=? AND  Perticulars=? '''
            cursor.execute(query, (main.voucherNo,debit_account,credit_account,))
            existing_ledger_id_dr = cursor.fetchone()
        else:
            existing_ledger_id_dr = None

        if hasattr(main, 'voucherNo') and main.voucherNo is not None:
            # A voucher number is available, so we can check for an existing voucher
            query = '''SELECT LedgerID  FROM Ledger_table WHERE VoucherNO = ? AND  LedgerName=? AND  Perticulars=? '''
            cursor.execute(query, (main.voucherNo, credit_account, debit_account,))
            existing_ledger_id_cr = cursor.fetchone()
        else:
            existing_ledger_id_cr = None


        if existing_ledger_id_dr:
            update_query = '''UPDATE Ledger_table
                               SET LedgerName=? , Perticulars=?, Date=?,
                               Currency=?, Debit=?
                               WHERE  VoucherNo=? AND Credit=0'''
            value = (debit_account,credit_account,date,  currency, amount, main.voucherNo)
            cursor.execute(update_query, value)


        elif existing_ledger_id_cr:
            update_query2 = '''UPDATE Ledger_table
                               SET  LedgerName=? , Perticulars=?, Date=?,
                               Currency=?,Credit=?
                               WHERE VoucherNo=? AND Debit=0 '''
            value2 = (credit_account, debit_account,date, currency, amount, main.voucherNo)
            cursor.execute(update_query2, value2)


        else:
            # Insert debit side entry
            cursor.execute("""
                INSERT INTO Ledger_table (LedgerName, Perticulars, Currency, Debit, Credit, VoucherNo, Date)
                VALUES (?, ?, ?, ?, ?, ?,?)
            """, (debit_account, credit_account, currency, amount, 0, voucher_no,date))
            # Insert credit side entry
            cursor.execute("""
                INSERT INTO Ledger_table (LedgerName, Perticulars, Currency, Debit, Credit, VoucherNo , Date)
                VALUES (?, ?, ?, ?, ?, ?,?)
            """, (credit_account, debit_account, currency, 0, amount, voucher_no,date))

        main.db_connection.commit()


    except:
        print(traceback.print_exc())

def createLedgerEntries(main):
    try:
        cursor = main.db_connection.cursor()

        debit_account = main.createvoucher.table[0,1]
        date = main.selected_date_str
        credit_account = main.createvoucher.table[1,1]
        voucher_no = main.voucherNo
        currency = main.createvoucher.table[0,4]
        debit_amount = main.createvoucher.table[0,2]
        credit_amount = main.createvoucher.table[1,3]

        if hasattr(main, 'voucherNo') and main.voucherNo is not None:
            # A voucher number is available, so we can check for an existing voucher
            query = '''SELECT LedgerID  FROM Ledger_table WHERE VoucherNO = ?'''
            cursor.execute(query, (main.voucherNo,))
            existing_ledger_id = cursor.fetchone()
        else:
            existing_ledger_id = None

        if existing_ledger_id:
            update_query = '''UPDATE Ledger_table
                            SET LedgerName=?, Date=?, Perticulars=? , 
                            Currency=?, Debit=?
                            WHERE  VoucherNo=? AND Credit=0'''
            value = (debit_account, date, credit_account, currency, debit_amount,main.voucherNo)
            cursor.execute(update_query,value)

            update_query2 = '''UPDATE Ledger_table
                            SET LedgerName=?, Date=?, Perticulars=? , 
                            Currency=?,Credit=?
                            WHERE VoucherNo=? AND Debit=0 '''
            value2 = (credit_account, date, debit_account,  currency, credit_amount,main.voucherNo)
            cursor.execute(update_query2, value2)
            main.db_connection.commit()
            closingBalance(main)



        else:
            # Insert debit side entry
            cursor.execute("""
                INSERT INTO Ledger_table (LedgerName, Date, Perticulars, VoucherNo, Currency, Debit, Credit)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (debit_account, date, credit_account, voucher_no, currency, debit_amount, 0))

            # Insert credit side entry
            cursor.execute("""
                INSERT INTO Ledger_table (LedgerName, Date, Perticulars, VoucherNo, Currency, Debit, Credit)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (credit_account, date, debit_account, voucher_no, currency, 0, credit_amount))

            main.db_connection.commit()
            closingBalance(main)


    except:
        print(traceback.print_exc())


def closingBalanceIdea(main):
    try:
        cursor = main.db_connection.cursor()

        # Iterate through each unique account in the voucher details table
        unique_accounts = {row[1] for row in main.createvoucher.table if row[1] != 0}
        currency = main.createvoucher.table[0, 4]
        if currency=='INR':
            for account in unique_accounts:
                for row in main.createvoucher.table:
                    if row[1] == account and row[0]=='Dr':
                        debit_account = account

                        # Find LedgerID for the debit account
                        query_debit = '''SELECT LedgerID FROM Ledger_table WHERE LedgerName = ? AND Perticulars = ? AND Currency = 'INR' '''
                        cursor.execute(query_debit, (debit_account, "Closing Balance"))
                        debit_ledger_id = cursor.fetchone()

                        query_debit_closing_balance = '''SELECT sum(Credit) - sum(Debit) FROM Ledger_table WHERE LedgerName = ? AND Currency = 'INR' AND Perticulars != 'Closing Balance' '''
                        cursor.execute(query_debit_closing_balance, (debit_account,))
                        debit_closing_balance = cursor.fetchone()
                        debit_closing_balance = debit_closing_balance[0]

                        if debit_ledger_id is not None:
                            if debit_closing_balance < 0:
                                update_query = '''UPDATE Ledger_table
                                                SET Debit=?,Credit=?,
                                                Date='31-03-2024', VoucherNo=''
                                                WHERE  LedgerName=? AND Perticulars='Closing Balance' AND Currency='INR' '''
                                value = (0, abs(debit_closing_balance), debit_account)
                                cursor.execute(update_query, value)
                            else:
                                update_query = '''UPDATE Ledger_table
                                                SET Debit=?,Credit=?,
                                                Date='31-03-2024', VoucherNo=''
                                                WHERE  LedgerName=? AND Perticulars='Closing Balance' AND Currency='INR'  '''
                                value = (abs(debit_closing_balance), 0, debit_account)
                                cursor.execute(update_query, value)
                        else:
                            if debit_closing_balance is not None and debit_closing_balance < 0:
                                # Insert debit side entry
                                cursor.execute("""
                                                INSERT INTO Ledger_table (LedgerName,Date, Perticulars,VoucherNo,Currency, Debit, Credit)
                                                VALUES (?, ?, ?, ?, ?,?,?)
                                            """, (debit_account, '31-03-2024', 'Closing Balance', '', currency, 0,
                                                  abs(debit_closing_balance)))
                            else:
                                # Insert debit side entry
                                cursor.execute("""
                                               INSERT INTO Ledger_table (LedgerName,Date, Perticulars,VoucherNo,Currency, Debit, Credit)
                                               VALUES (?, ?, ?, ?, ?,?,?)
                                           """, (
                                debit_account, '31-03-2024', 'Closing Balance', '', currency, abs(debit_closing_balance),
                                0))


                    elif row[1] == account and row[0]=='Cr':
                        credit_account = account

                        # Find LedgerID for the credit account
                        query_credit = '''SELECT LedgerID FROM Ledger_table WHERE LedgerName = ? AND Perticulars = ? AND Currency = 'INR' '''
                        cursor.execute(query_credit, (credit_account, "Closing Balance"))
                        credit_ledger_id = cursor.fetchone()

                        query_credit_closing_balance = '''SELECT sum(Credit) - sum(Debit) FROM Ledger_table WHERE LedgerName = ? AND Currency = 'INR'  AND Perticulars != 'Closing Balance' '''
                        cursor.execute(query_credit_closing_balance, (credit_account,))
                        credit_closing_balance = cursor.fetchone()
                        credit_closing_balance = credit_closing_balance[0]

                        if credit_ledger_id is not None:
                            if credit_closing_balance < 0:
                                update_query = '''UPDATE Ledger_table
                                                            SET Debit=?,Credit=?,
                                                            Date='31-03-2024', VoucherNo=''
                                                            WHERE  LedgerName=? AND Perticulars='Closing Balance' AND Currency= 'INR'  '''
                                value = (0, abs(credit_closing_balance), credit_account)
                                cursor.execute(update_query, value)
                            else:
                                update_query = '''UPDATE Ledger_table
                                                            SET Debit=?,Credit=? ,
                                                            Date='31-03-2024', VoucherNo=''  
                                                            WHERE  LedgerName=? AND Perticulars='Closing Balance' AND Currency='INR'  '''
                                value = (abs(credit_closing_balance), 0, credit_account)
                                cursor.execute(update_query, value)

                        else:
                            if credit_closing_balance is not None and credit_closing_balance < 0:
                                # Insert credit side entry
                                cursor.execute("""
                                                           INSERT INTO Ledger_table (LedgerName,Date,Perticulars,VoucherNo, Currency, Debit, Credit)
                                                           VALUES (?, ?, ?, ?, ?,?,?)
                                                       """, (
                                credit_account, '31-03-2024', 'Closing Balance', '', currency, 0,
                                abs(credit_closing_balance)))
                            else:
                                # Insert credit side entry
                                cursor.execute("""
                                               INSERT INTO Ledger_table (LedgerName, Date,Perticulars, VoucherNo,Currency, Debit, Credit)
                                               VALUES (?, ?, ?, ?, ?,?,?)
                                                           """,
                                               (credit_account, '31-03-2024', 'Closing Balance', '', currency,
                                                abs(credit_closing_balance), 0))
        else:
            for account in unique_accounts:
                for row in main.createvoucher.table:
                    if row[1] == account and row[0]=='Dr':
                        debit_account = account

                        # Find LedgerID for the debit account
                        query_debit_usd = '''SELECT LedgerID FROM Ledger_table WHERE LedgerName = ? AND Perticulars = ? AND Currency = 'USD' '''
                        cursor.execute(query_debit_usd, (debit_account, "Closing Balance"))
                        debit_ledger_id_usd = cursor.fetchone()

                        query_debit_closing_balance_usd = '''SELECT sum(Credit) - sum(Debit) FROM Ledger_table WHERE LedgerName = ? AND Currency = 'USD' AND Perticulars != 'Closing Balance' '''
                        cursor.execute(query_debit_closing_balance_usd, (debit_account,))
                        debit_closing_balance_usd = cursor.fetchone()
                        debit_closing_balance_usd = debit_closing_balance_usd[0]

                        if debit_ledger_id_usd is not None:
                            if debit_closing_balance_usd < 0:
                                update_query = '''UPDATE Ledger_table
                                                   SET Debit=?,Credit=? ,
                                                   Date='31-03-2024', VoucherNo=''
                                                   WHERE  LedgerName=? AND Perticulars='Closing Balance' AND Currency='USD' '''
                                value = (0, abs(debit_closing_balance_usd), debit_account)
                                cursor.execute(update_query, value)
                            else:
                                update_query = '''UPDATE Ledger_table
                                                   SET Debit=?,Credit=? ,
                                                   Date='31-03-2024', VoucherNo=''
                                                   WHERE  LedgerName=? AND Perticulars='Closing Balance' AND Currency='USD' '''
                                value = (abs(debit_closing_balance_usd), 0, debit_account)
                                cursor.execute(update_query, value)
                        else:
                            if debit_closing_balance_usd is not None and debit_closing_balance_usd < 0:
                                # Insert debit side entry
                                cursor.execute("""
                                                   INSERT INTO Ledger_table (LedgerName, Date,Perticulars,VoucherNo,Currency, Debit, Credit)
                                                   VALUES (?, ?, ?, ?, ?,?,?)
                                               """, (debit_account, '31-03-2024', 'Closing Balance', '', currency, 0,
                                                     abs(debit_closing_balance_usd)))
                            elif debit_closing_balance_usd is None:
                                pass
                            else:
                                # Insert debit side entry
                                cursor.execute("""
                                              INSERT INTO Ledger_table (LedgerName,Date, Perticulars,VoucherNo,Currency, Debit, Credit)
                                              VALUES (?, ?, ?, ?, ?,?,?)
                                                              """,
                                               (debit_account, '31-03-2024', 'Closing Balance', '', currency,
                                                abs(debit_closing_balance_usd), 0))

                    elif row[1] == account and row[0] == 'Cr':
                        credit_account = account

                        # Find LedgerID for the credit account
                        query_credit_usd = '''SELECT LedgerID FROM Ledger_table WHERE LedgerName = ? AND Perticulars = ? AND Currency = 'USD' '''
                        cursor.execute(query_credit_usd, (credit_account, "Closing Balance"))
                        credit_ledger_id_usd = cursor.fetchone()

                        query_credit_closing_balance_usd = '''SELECT sum(Credit) - sum(Debit) FROM Ledger_table WHERE LedgerName = ? AND Currency = 'USD' AND Perticulars != 'Closing Balance' '''
                        cursor.execute(query_credit_closing_balance_usd, (credit_account,))
                        credit_closing_balance_usd = cursor.fetchone()
                        credit_closing_balance_usd = credit_closing_balance_usd[0]

                        if credit_ledger_id_usd is not None:
                            if credit_closing_balance_usd < 0:
                                update_query = '''UPDATE Ledger_table
                                                    SET Debit=?,Credit=? ,
                                                    Date='31-03-2024', VoucherNo=''
                                                    WHERE  LedgerName=? AND Perticulars='Closing Balance' AND Currency='USD' '''
                                value = (0, abs(credit_closing_balance_usd), credit_account)
                                cursor.execute(update_query, value)
                            else:
                                update_query = '''UPDATE Ledger_table
                                                    SET Debit=?,Credit=?,
                                                    Date='31-03-2024', VoucherNo='' 

                                                    WHERE  LedgerName=? AND Perticulars='Closing Balance'  AND Currency='USD' '''
                                value = (abs(credit_closing_balance_usd), 0, credit_account)
                                cursor.execute(update_query, value)


                        else:
                            if credit_closing_balance_usd is not None and credit_closing_balance_usd < 0:
                                # Insert credit side entry
                                cursor.execute("""
                                                   INSERT INTO Ledger_table (LedgerName,Date, Perticulars, VoucherNo,Currency, Debit, Credit)
                                                   VALUES (?, ?, ?, ?, ?,?,?)
                                               """, (credit_account, '31-03-2024', 'Closing Balance', '', currency, 0,
                                                     abs(credit_closing_balance_usd)))
                            elif credit_closing_balance_usd is None:
                                pass
                            else:
                                # Insert credit side entry
                                cursor.execute("""
                                                   INSERT INTO Ledger_table (LedgerName, Date,Perticulars,VoucherNo, Currency, Debit, Credit)
                                                   VALUES (?, ?, ?, ?, ?,?,?)
                                                               """,
                                               (credit_account, '31-03-2024', 'Closing Balance', '', currency,
                                                abs(credit_closing_balance_usd), 0))

        main.db_connection.commit()

    except:
        print(traceback.print_exc())


def closingBalance(main):
    try:
        debit_account = main.createvoucher.table[0, 1]
        currency = main.createvoucher.table[0, 4]
        credit_account = main.createvoucher.table[1, 1]

        cursor = main.db_connection.cursor()

        if currency == 'INR':
            ########################################### INR ################################################################

            # Find LedgerID for the debit account
            query_debit = '''SELECT LedgerID FROM Ledger_table WHERE LedgerName = ? AND Perticulars = ? AND Currency = 'INR' '''
            cursor.execute(query_debit, (debit_account, "Closing Balance"))
            debit_ledger_id = cursor.fetchone()

            # Find LedgerID for the credit account
            query_credit = '''SELECT LedgerID FROM Ledger_table WHERE LedgerName = ? AND Perticulars = ? AND Currency = 'INR' '''
            cursor.execute(query_credit, (credit_account, "Closing Balance"))
            credit_ledger_id = cursor.fetchone()

            query_debit_closing_balance = '''SELECT sum(Credit) - sum(Debit) FROM Ledger_table WHERE LedgerName = ? AND Currency = 'INR' AND Perticulars != 'Closing Balance' '''
            cursor.execute(query_debit_closing_balance, (debit_account,))
            debit_closing_balance = cursor.fetchone()
            debit_closing_balance = debit_closing_balance[0]

            query_credit_closing_balance = '''SELECT sum(Credit) - sum(Debit) FROM Ledger_table WHERE LedgerName = ? AND Currency = 'INR'  AND Perticulars != 'Closing Balance' '''
            cursor.execute(query_credit_closing_balance, (credit_account,))
            credit_closing_balance = cursor.fetchone()
            credit_closing_balance = credit_closing_balance[0]

            if debit_ledger_id is not None:
                if debit_closing_balance <0 :
                    update_query = '''UPDATE Ledger_table
                                    SET Debit=?,Credit=?,
                                    Date='31-03-2024', VoucherNo=''
                                    WHERE  LedgerName=? AND Perticulars='Closing Balance' AND Currency='INR' '''
                    value = (0,abs(debit_closing_balance),debit_account)
                    cursor.execute(update_query, value)
                else:
                    update_query = '''UPDATE Ledger_table
                                    SET Debit=?,Credit=?,
                                    Date='31-03-2024', VoucherNo=''
                                    WHERE  LedgerName=? AND Perticulars='Closing Balance' AND Currency='INR'  '''
                    value = (abs(debit_closing_balance), 0, debit_account)
                    cursor.execute(update_query, value)

            else:
                if debit_closing_balance < 0:
                    # Insert debit side entry
                    cursor.execute("""
                                    INSERT INTO Ledger_table (LedgerName,Date, Perticulars,VoucherNo,Currency, Debit, Credit)
                                    VALUES (?, ?, ?, ?, ?,?,?)
                                """, (debit_account,'31-03-2024','Closing Balance','',currency,0, abs(debit_closing_balance)))
                else:
                    # Insert debit side entry
                    cursor.execute("""
                                   INSERT INTO Ledger_table (LedgerName,Date, Perticulars,VoucherNo,Currency, Debit, Credit)
                                   VALUES (?, ?, ?, ?, ?,?,?)
                               """, (debit_account,'31-03-2024', 'Closing Balance','', currency, abs(debit_closing_balance) , 0))


            if credit_ledger_id is not None:
                if credit_closing_balance <0:
                    update_query = '''UPDATE Ledger_table
                                     SET Debit=?,Credit=?,
                                     Date='31-03-2024', VoucherNo=''
                                     WHERE  LedgerName=? AND Perticulars='Closing Balance' AND Currency= 'INR'  '''
                    value = (0, abs(credit_closing_balance), credit_account)
                    cursor.execute(update_query, value)
                else:
                    update_query = '''UPDATE Ledger_table
                                     SET Debit=?,Credit=? ,
                                     Date='31-03-2024', VoucherNo=''  
                                     WHERE  LedgerName=? AND Perticulars='Closing Balance' AND Currency='INR'  '''
                    value = (abs(credit_closing_balance),0, credit_account)
                    cursor.execute(update_query, value)


            else:
                if credit_closing_balance <0:
                    # Insert credit side entry
                    cursor.execute("""
                                    INSERT INTO Ledger_table (LedgerName,Date,Perticulars,VoucherNo, Currency, Debit, Credit)
                                    VALUES (?, ?, ?, ?, ?,?,?)
                                """, (credit_account, '31-03-2024','Closing Balance','', currency, 0,abs(credit_closing_balance)))
                else:
                    # Insert credit side entry
                    cursor.execute("""
                                    INSERT INTO Ledger_table (LedgerName, Date,Perticulars, VoucherNo,Currency, Debit, Credit)
                                    VALUES (?, ?, ?, ?, ?,?,?)
                                                """,
                                   (credit_account, '31-03-2024','Closing Balance', '',currency, abs(credit_closing_balance), 0))

    ################################################################## USD #########################################
        else:
            # Find LedgerID for the debit account
            query_debit_usd = '''SELECT LedgerID FROM Ledger_table WHERE LedgerName = ? AND Perticulars = ? AND Currency = 'USD' '''
            cursor.execute(query_debit_usd, (debit_account, "Closing Balance"))
            debit_ledger_id_usd = cursor.fetchone()

            # Find LedgerID for the credit account
            query_credit_usd = '''SELECT LedgerID FROM Ledger_table WHERE LedgerName = ? AND Perticulars = ? AND Currency = 'USD' '''
            cursor.execute(query_credit_usd, (credit_account, "Closing Balance"))
            credit_ledger_id_usd = cursor.fetchone()

            query_debit_closing_balance_usd = '''SELECT sum(Credit) - sum(Debit) FROM Ledger_table WHERE LedgerName = ? AND Currency = 'USD' AND Perticulars != 'Closing Balance' '''
            cursor.execute(query_debit_closing_balance_usd, (debit_account,))
            debit_closing_balance_usd = cursor.fetchone()
            debit_closing_balance_usd = debit_closing_balance_usd[0]


            query_credit_closing_balance_usd = '''SELECT sum(Credit) - sum(Debit) FROM Ledger_table WHERE LedgerName = ? AND Currency = 'USD' AND Perticulars != 'Closing Balance' '''
            cursor.execute(query_credit_closing_balance_usd, (credit_account,))
            credit_closing_balance_usd = cursor.fetchone()
            credit_closing_balance_usd = credit_closing_balance_usd[0]


            if debit_ledger_id_usd is not None:
                if debit_closing_balance_usd < 0:
                    update_query = '''UPDATE Ledger_table
                                       SET Debit=?,Credit=? ,
                                       Date='31-03-2024', VoucherNo=''
                                        
                                       WHERE  LedgerName=? AND Perticulars='Closing Balance' AND Currency='USD' '''
                    value = (0, abs(debit_closing_balance_usd), debit_account)
                    cursor.execute(update_query, value)
                else:
                    update_query = '''UPDATE Ledger_table
                                       SET Debit=?,Credit=? ,
                                       Date='31-03-2024', VoucherNo=''
                                 
                                       WHERE  LedgerName=? AND Perticulars='Closing Balance' AND Currency='USD' '''
                    value = (abs(debit_closing_balance_usd), 0, debit_account)
                    cursor.execute(update_query, value)

            else:
                if debit_closing_balance_usd is not None and debit_closing_balance_usd < 0:
                    # Insert debit side entry
                    cursor.execute("""
                                       INSERT INTO Ledger_table (LedgerName, Date,Perticulars,VoucherNo,Currency, Debit, Credit)
                                       VALUES (?, ?, ?, ?, ?,?,?)
                                   """, (debit_account,'31-03-2024', 'Closing Balance','', currency, 0, abs(debit_closing_balance_usd)))
                elif credit_closing_balance_usd is None:
                    pass
                else:
                    # Insert debit side entry
                    cursor.execute("""
                                  INSERT INTO Ledger_table (LedgerName,Date, Perticulars,VoucherNo,Currency, Debit, Credit)
                                  VALUES (?, ?, ?, ?, ?,?,?)
                                                  """,
                                   (debit_account, '31-03-2024','Closing Balance', '',currency, abs(debit_closing_balance_usd), 0))

            if credit_ledger_id_usd is not None:
                if credit_closing_balance_usd < 0:
                    update_query = '''UPDATE Ledger_table
                                        SET Debit=?,Credit=? ,
                                        Date='31-03-2024', VoucherNo=''
                                        WHERE  LedgerName=? AND Perticulars='Closing Balance' AND Currency='USD' '''
                    value = (0, abs(credit_closing_balance_usd), credit_account)
                    cursor.execute(update_query, value)

                else:
                    update_query = '''UPDATE Ledger_table
                                        SET Debit=?,Credit=?,
                                        Date='31-03-2024', VoucherNo='' 
                                        
                                        WHERE  LedgerName=? AND Perticulars='Closing Balance'  AND Currency='USD' '''
                    value = (abs(credit_closing_balance_usd), 0, credit_account)
                    cursor.execute(update_query, value)



            else:
                if credit_closing_balance_usd is not None and  credit_closing_balance_usd < 0:
                    # Insert credit side entry
                    cursor.execute("""
                                       INSERT INTO Ledger_table (LedgerName,Date, Perticulars, VoucherNo,Currency, Debit, Credit)
                                       VALUES (?, ?, ?, ?, ?,?,?)
                                   """, (credit_account, '31-03-2024','Closing Balance', '',currency, 0, abs(credit_closing_balance_usd)))
                elif credit_closing_balance_usd is None:
                    pass
                else:
                    # Insert credit side entry
                    cursor.execute("""
                                       INSERT INTO Ledger_table (LedgerName, Date,Perticulars,VoucherNo, Currency, Debit, Credit)
                                       VALUES (?, ?, ?, ?, ?,?,?)
                                                   """,
                                   (credit_account, '31-03-2024','Closing Balance','', currency, abs(credit_closing_balance_usd), 0))

        main.db_connection.commit()

    except:
        print(traceback.print_exc())

def createLedger(main):

    try:
        main.gateway.fVouchers.hide()
        main.gateway.fCreate.show()
        main.masterlist.fLedger.show()
        createLedgerPage(main)
        main.createledger.pbSubmit.clicked.connect(lambda : goToVoucherCreate(main))
    except:
        print(traceback.print_exc())

def goToVoucherCreate(main):
    try:
        main.masterlist.fLedger.hide()
        main.gateway.fCreate.hide()
        main.gateway.fVouchers.show()
        showVoucherPage(main)
    except:
        print(traceback.print_exc())

######################################################  Payment Entry - Voucher #########################################
def showPaymentEntry(main):
    try:

        account_name = [name[1] for name in main.account]
        main.paymententry.cbAccountName.clear()
        main.paymententry.cbAccountName.addItems(account_name)
        main.paymententry.show()
        # Create a QDoubleValidator
        validator = QDoubleValidator()
        # Set the validator to allow only numbers and decimals
        validator.setDecimals(2)
        main.paymententry.leAmount.setValidator(validator)
        main.paymententry.cbDrCr.activated.connect(lambda: updateCrDrComboBoxInPayment(main))
        main.paymententry.cbDrCr.activated.connect(lambda: addEntaryInPayment(main))

    except:
        print(traceback.print_exc())

def updateCrDrComboBoxInPayment(main):
    # Check the "Dr" or "Cr" selection and call the appropriate function to refresh the combobox
    main.dr_cr = main.paymententry.cbDrCr.currentText()
    refreshComboBoxForDrInPayment(main)
    if main.dr_cr == "Dr":
        refreshComboBoxForDrInPayment(main)
    elif main.dr_cr == "Cr":
        refreshComboBoxForCrInPayment(main)
    else:
        refreshComboBoxForDrInPayment(main)


# Initialize a dictionary to store selected account names for "Dr" and "Cr"
selected_account_names_in_payment = {"Dr": [], "Cr": []}
# Function to refresh the combobox with account names for "Dr"
def refreshComboBoxForDrInPayment(main):
    try:
        account_name = [name[1] for name in main.account]
        # Clear existing items from the drop-down button
        main.paymententry.cbAccountName.clear()
        # Populate the drop-down button with account names that haven't been selected as "Cr"
        available_account_names = [name for name in account_name if name not in selected_account_names_in_payment["Cr"]]
        main.paymententry.cbAccountName.addItems(available_account_names)

    except Exception as e:
        print(traceback.print_exc())

# Function to refresh the combobox with all account names for "Cr"
def refreshComboBoxForCrInPayment(main):
    try:
        account_name = [name[1] for name in main.account]

        # Clear existing items from the drop-down button
        main.paymententry.cbAccountName.clear()

        # Populate the drop-down button with account names that haven't been selected as "Cr"
        available_account_names = [name for name in account_name if name not in selected_account_names_in_payment["Dr"]]

        # Populate the drop-down button with all account names
        main.paymententry.cbAccountName.addItems(available_account_names)

    except Exception as e:
        print(traceback.print_exc())

def addEntaryInPayment(main):
    try:
        main.dr_cr = main.paymententry.cbDrCr.currentText()
        # Calculate the sum of amounts in the "Cr" and "Dr" columns
        total_cr = sum(row[3] for row in main.createvoucher.table if row[0] == "Cr")
        total_dr = sum(row[2] for row in main.createvoucher.table if row[0] == "Dr")
        if main.dr_cr == "Cr":
            amount_needed = total_dr - total_cr
            if amount_needed > 0:
                main.paymententry.leAmount.setText(str(amount_needed))

        elif main.dr_cr == "Dr":
            amount_needed = total_cr - total_dr
            if amount_needed > 0:
                # Add a new row with the calculated "Cr" amount
                main.paymententry.leAmount.setText(str(amount_needed))
        else:
            return  # Invalid selection
    except:
        print(traceback.print_exc())


def addRawInPayment(main):
    try:
        company_id = main.companyID
        main.account_name = main.paymententry.cbAccountName.currentText()
        main.dr_cr = main.paymententry.cbDrCr.currentText()
        # Add the selected account name to the appropriate list
        selected_account_names_in_payment[main.dr_cr].append(main.account_name)
        main.amount = float(main.paymententry.leAmount.text())

        main.currency = main.paymententry.cbCurrency.currentText()
    #----------------------- disable other currency option after selected -----------------------------

        if main.currency=="INR":
            main.paymententry.cbCurrency.setCurrentIndex(0)  # Set it to INR
            main.paymententry.cbCurrency.setEnabled(False)  # Disable the combobox
            main.createvoucher.lbCurrency.setText(main.currency)
        elif main.currency=="USD":
            main.paymententry.cbCurrency.setCurrentIndex(1)  # Set it to USD
            main.paymententry.cbCurrency.setEnabled(False)
            main.createvoucher.lbCurrency.setText(main.currency)
        else:
            main.paymententry.cbCurrency.setEnabled(True)
        num_cr_rows = sum(1 for row in main.createvoucher.table if row[0] == "Cr")
        num_dr_rows = sum(1 for row in main.createvoucher.table if row[0] == "Dr")

        # Check if adding a new row is allowed based on the current counts
        if (main.dr_cr == "Cr" and num_dr_rows >= 2) or (main.dr_cr == "Dr" and num_cr_rows >= 2):
            return  #

        # new_row = [main.dr_cr, main.account_name, main.amount, main.currency]
        if main.dr_cr == "Cr":
            indexlist=[0,1,2,3,4]
            # Find the index of the last "Cr" row
            last_cr_index = next((i for i, row in enumerate(main.createvoucher.table) if row[0] == "Cr"), -1)
            last_cr_inndex = next((i for i, row in enumerate(main.createvoucher.table) if row[0] == "Cr"and row[1] == main.account_name), -1)

            if last_cr_index >= 0:
                if last_cr_inndex >= 0:
                # Insert the new "Dr" row after the last "Cr" row
                    main.createvoucher.table[last_cr_index, 3] += main.amount
                    updateSumsOnSelectionChange(main)
                    ind = main.createvoucher.model.index(0, 0)
                    ind1 = main.createvoucher.model.index(0, 1)
                    main.createvoucher.model.dataChanged.emit(ind, ind1)
                    main.paymententry.leAmount.clear()
                    main.paymententry.hide()
                else:
                    insert_index = last_cr_index + 1

            else:
                # There are no "Cr" rows, insert at the end
                insert_index = main.createvoucher.last_serialno

            # Shift all rows below the insert_index one index below
            main.createvoucher.table[insert_index + 1:] = main.createvoucher.table[insert_index:-1]

            # Update the table with the values at the insert_index
            main.createvoucher.table[insert_index, indexlist] = [main.dr_cr, main.account_name, 0,main.amount,
                                                                 main.currency]
            # Increment the last_serialno
            main.createvoucher.last_serialno += 1
            main.createvoucher.model.last_serialno += 1
            main.createvoucher.model.insertRows()
            main.createvoucher.model.rowCount() # print(main.createvoucher.model.rowCount())




        elif main.dr_cr == "Dr":
            indexlist = [0, 1, 2, 3, 4]
            # Find the index of the last "Cr" row
            main.createvoucher.last_serialno = 0
            last_dr_index = next(
                (i for i, row in enumerate(main.createvoucher.table) if row[0] == "Dr"),
                -1)

            last_dr_inndex = next(
                (i for i, row in enumerate(main.createvoucher.table) if row[0] == "Dr" and row[1] == main.account_name),
                -1)

            if last_dr_index >= 0:
                if last_dr_inndex >= 0:
                # Insert the new "Dr" row after the last "Cr" row
                    main.createvoucher.table[last_dr_index, 2] += main.amount
                    updateSumsOnSelectionChange(main)
                    ind = main.createvoucher.model.index(0, 0)
                    ind1 = main.createvoucher.model.index(0, 1)
                    main.createvoucher.model.dataChanged.emit(ind, ind1)
                    main.paymententry.leAmount.clear()
                    main.paymententry.hide()
                else:
                    insert_index = last_dr_index + 1

            else:
                # There are no "Cr" rows, insert at the end
                insert_index = main.createvoucher.last_serialno
            # Shift all rows below the insert_index one index below
            main.createvoucher.table[insert_index + 1:] = main.createvoucher.table[insert_index:-1]

            # Update the table with the values at the insert_index
            main.createvoucher.table[insert_index, indexlist] = [main.dr_cr, main.account_name, main.amount,0,
                                                                 main.currency]

            # # # Increment the last_serialno
            main.createvoucher.last_serialno += 1
            main.createvoucher.model.last_serialno += 1
            main.createvoucher.model.insertRows()
            main.createvoucher.model.rowCount()  # print(main.createvoucher.model.rowCount())

        # Emit dataChanged signal for the modified row
        ind = main.createvoucher.model.index(0, 0)
        ind1 = main.createvoucher.model.index(0, 1)
        main.createvoucher.model.dataChanged.emit(ind, ind1)

        debitSum = main.createvoucher.table[:main.createvoucher.last_serialno,3].sum()
        main.debitAmount =  main.createvoucher.lbDebit.setText(str(debitSum))

        creditSum = main.createvoucher.table[:main.createvoucher.last_serialno,2].sum()
        main.creditAmount = main.createvoucher.lbCredit.setText(str(creditSum))

        updateSumsOnSelectionChange(main)
        ############### Clear the input widgets after adding data#################
        main.paymententry.cbDrCr.setCurrentIndex(0)
        main.paymententry.leAmount.clear()
        main.paymententry.hide()

    except:
        print(traceback.print_exc())


##############################################   Sales Entry - Voucher ##############################################
def showSalesEntry(main):
    try:
        main.salesentry.show()
        account_name = [name[1] for name in main.account]
        main.salesentry.cbAccountName.clear()
        main.salesentry.cbAccountName.addItems(account_name)
        main.salesentry.rbCash.clicked.connect(lambda :setVisibilityForCashInSales(main))
        main.salesentry.rbCredit.clicked.connect(lambda : setVisibilityForDebitInSales(main))
    except:
        print(traceback.print_exc())

def setVisibilityForCashInSales(main):
    try:
        main.salesentry.cbAccountName.setVisible(False)
        main.salesentry.label.setVisible(False)
        main.salesentry.label_4.setVisible(False)
        main.salesentry.label_5.setVisible(False)
        main.salesentry.lineEdit.setVisible(False)
    except:
        print(traceback.print_exc())

def setVisibilityForDebitInSales(main):
    try:
        main.salesentry.cbAccountName.setVisible(True)
        main.salesentry.label.setVisible(True)
        main.salesentry.label_4.setVisible(True)
        main.salesentry.label_5.setVisible(True)
        main.salesentry.lineEdit.setVisible(True)
    except:
        print(traceback.print_exc())

def addRawInSales(main):
    try:
        if main.salesentry.rbCash.isChecked():
            addRawInSalesForCash(main)
        elif main.salesentry.rbCredit.isChecked():
            addRawInSalesForDebit(main)

    except:
        print(traceback.print_exc())


def addRawInSalesForDebit(main):
    try:
        main.account_name = main.salesentry.cbAccountName.currentText()
        main.amount = float(main.salesentry.leAmount.text())
        main.currency = main.salesentry.cbCurrency.currentText()
        # ----------------------- disable other currency option after selected -----------------------------

        if main.currency == "INR":
            main.salesentry.cbCurrency.setCurrentIndex(0)  # Set it to INR
            main.salesentry.cbCurrency.setEnabled(False)  # Disable the combobox
            main.createvoucher.lbCurrency.setText(main.currency)
        elif main.currency == "USD":
            main.salesentry.cbCurrency.setCurrentIndex(1)  # Set it to USD
            main.salesentry.cbCurrency.setEnabled(False)
            main.createvoucher.lbCurrency.setText(main.currency)
        else:
            main.salesentry.cbCurrency.setEnabled(True)
        # Count the current number of "Cr" and "Dr" rows
        num_cr_rows = sum(1 for row in main.createvoucher.table if row[0] == "Cr")
        num_dr_rows = sum(1 for row in main.createvoucher.table if row[0] == "Dr")

        indexlist = [0, 1, 2, 3, 4]
        num_rows = main.createvoucher.last_serialno

        # to add "Dr" raw
        first_column_values = [row[0] for row in main.createvoucher.table]
        if num_rows<2:
            main.createvoucher.table[main.createvoucher.last_serialno, indexlist] = ["Dr",main.account_name,
                                                                                     main.amount, 0, main.currency]
            main.createvoucher.last_serialno += 1
            main.createvoucher.model.last_serialno += 1
            main.createvoucher.model.insertRows()
            main.createvoucher.model.rowCount()

            # to add "Cr" raw
            main.createvoucher.table[main.createvoucher.last_serialno, indexlist] = ["Cr", "Stock", 0,
                                                                                     main.amount, main.currency]

            main.createvoucher.last_serialno += 1
            main.createvoucher.model.last_serialno += 1
            main.createvoucher.model.insertRows()
            main.createvoucher.model.rowCount()


        else:
            cr_row = next((i for i, row in enumerate(main.createvoucher.table) if row[0] == "Cr"), None)
            if cr_row is not None:
                # Update the "Cr" row's debit and credit amounts
                main.createvoucher.table[cr_row][2] = 0  # Update debit amount
                main.createvoucher.table[cr_row][3] += main.amount  # Update credit amount


            existing_dr_row = next(
                (i for i, row in enumerate(main.createvoucher.table) if row[0] == "Dr" and row[1] == main.account_name),
                None)

            if existing_dr_row is not None:
                # Update the existing "Dr" row's debit amount
                main.createvoucher.table[existing_dr_row][2] += main.amount
            else:
                indexlist = [0, 1, 2, 3, 4]

                # Find the index of the last "Cr" row
                last_cr_index = max((i for i, row in enumerate(main.createvoucher.table) if row[0] == "Cr"), default=-1)

                if last_cr_index >= 0:
                    # Insert the new "Dr" row before the last "Cr" row
                    insert_index = last_cr_index
                else:
                    # There are no "Cr" rows, insert at the end
                    insert_index = main.createvoucher.last_serialno

                # Shift all rows below the insert_index one index below
                main.createvoucher.table[insert_index + 1:] = main.createvoucher.table[insert_index:-1]

                # Add a new "Dr" row at the insert_index
                main.createvoucher.table[insert_index, indexlist] = ["Dr", main.account_name, main.amount, 0,
                                                                     main.currency]

                main.createvoucher.last_serialno += 1
                main.createvoucher.model.last_serialno += 1
                main.createvoucher.model.insertRows()
                main.createvoucher.model.rowCount()



        # Emit dataChanged signal for the modified rows
        ind = main.createvoucher.model.index(0, 0)
        ind1 = main.createvoucher.model.index(0, 1)
        main.createvoucher.model.dataChanged.emit(ind, ind1)

        updateSumsOnSelectionChange(main)
        main.salesentry.leAmount.clear()
        main.salesentry.hide()

    except:
        print(traceback.print_exc())


def addRawInSalesForCash(main):
    try:

        main.amount = float(main.salesentry.leAmount.text())

        main.currency = main.salesentry.cbCurrency.currentText()
        # ----------------------- disable other currency option after selected -----------------------------

        if main.currency == "INR":
            main.salesentry.cbCurrency.setCurrentIndex(0)  # Set it to INR
            main.salesentry.cbCurrency.setEnabled(False)  # Disable the combobox
            main.createvoucher.lbCurrency.setText(main.currency)
        elif main.currency == "USD":
            main.salesentry.cbCurrency.setCurrentIndex(1)  # Set it to USD
            main.salesentry.cbCurrency.setEnabled(False)
            main.createvoucher.lbCurrency.setText(main.currency)
        else:
            main.salesentry.cbCurrency.setEnabled(True)

        # Count the current number of "Cr" and "Dr" rows
        num_cr_rows = sum(1 for row in main.createvoucher.table if row[0] == "Cr")
        num_dr_rows = sum(1 for row in main.createvoucher.table if row[0] == "Dr")

        indexlist = [0, 1, 2, 3, 4]

        # to add "Dr" raw
        main.createvoucher.table[main.createvoucher.last_serialno, indexlist] = ["Dr","Cash",
                                                                                 main.amount, 0, main.currency]
        main.createvoucher.last_serialno += 1
        main.createvoucher.model.last_serialno += 1
        main.createvoucher.model.insertRows()
        main.createvoucher.model.rowCount()

        # to add "Cr" raw
        main.createvoucher.table[main.createvoucher.last_serialno, indexlist] = ["Cr", "Stock", 0,
                                                                                 main.amount, main.currency]

        main.createvoucher.last_serialno += 1
        main.createvoucher.model.last_serialno += 1
        main.createvoucher.model.insertRows()
        main.createvoucher.model.rowCount()

        # Emit dataChanged signal for the modified rows
        ind = main.createvoucher.model.index(0, 0)
        ind1 = main.createvoucher.model.index(0, 1)
        main.createvoucher.model.dataChanged.emit(ind, ind1)

        updateSumsOnSelectionChange(main)
        main.salesentry.leAmount.clear()
        main.salesentry.hide()

    except:
        print(traceback.print_exc())

##############################################  Purchase Entry -Voucher ############################################
def showPurchaseEntry(main):
    try:
        main.purchaseentry.show()
        account_name = [name[1] for name in main.account]
        main.purchaseentry.cbAccountName.clear()
        main.purchaseentry.cbAccountName.addItems(account_name)
        main.purchaseentry.rbCash.clicked.connect(lambda: setVisibilityForCashInPurchase(main))
        main.purchaseentry.rbCredit.clicked.connect(lambda: setVisibilityForCreditInPurchase(main))
    except:
        print(traceback.print_exc())


def setVisibilityForCashInPurchase(main):
    try:

        main.purchaseentry.cbAccountName.setVisible(False)
        main.purchaseentry.label.setVisible(False)
        main.purchaseentry.label_4.setVisible(False)
        main.purchaseentry.label_5.setVisible(False)
        main.purchaseentry.lineEdit.setVisible(False)
    except:
        print(traceback.print_exc())

def setVisibilityForCreditInPurchase(main):
    try:

        main.purchaseentry.cbAccountName.setVisible(True)
        main.purchaseentry.label.setVisible(True)
        main.purchaseentry.label_4.setVisible(True)
        main.purchaseentry.label_5.setVisible(True)
        main.purchaseentry.lineEdit.setVisible(True)
    except:
        print(traceback.print_exc())

def addRawInPurchase(main):
    try:
        if main.purchaseentry.rbCash.isChecked():
            addRawInPurchaseForCash(main)
        elif main.purchaseentry.rbCredit.isChecked():
            addRawInPurchaseForCredit(main)

    except:
        print(traceback.print_exc())


def addRawInPurchaseForCredit(main):
    try:
        main.account_name = main.purchaseentry.cbAccountName.currentText()
        main.amount = float(main.purchaseentry.leAmount.text())
        main.currency = main.purchaseentry.cbCurrency.currentText()
        # ----------------------- disable other currency option after selected -----------------------------

        if main.currency == "INR":
            main.purchaseentry.cbCurrency.setCurrentIndex(0)  # Set it to INR
            main.purchaseentry.cbCurrency.setEnabled(False)  # Disable the combobox
            main.createvoucher.lbCurrency.setText(main.currency)
        elif main.currency == "USD":
            main.purchaseentry.cbCurrency.setCurrentIndex(1)  # Set it to USD
            main.purchaseentry.cbCurrency.setEnabled(False)
            main.createvoucher.lbCurrency.setText(main.currency)
        else:
            main.purchaseentry.cbCurrency.setEnabled(True)
        # Count the current number of "Cr" and "Dr" rows
        num_cr_rows = sum(1 for row in main.createvoucher.table if row[0] == "Cr")
        num_dr_rows = sum(1 for row in main.createvoucher.table if row[0] == "Dr")

        indexlist = [0, 1, 2, 3, 4]
        num_rows = main.createvoucher.last_serialno

        # # to add "Dr" raw
        first_column_values = [row[0] for row in main.createvoucher.table]
        if num_rows < 2:

            # to add "Dr" raw
            main.createvoucher.table[main.createvoucher.last_serialno, indexlist] = ["Dr","Stock",
                                                                                     main.amount, 0, main.currency]
            main.createvoucher.last_serialno += 1
            main.createvoucher.model.last_serialno += 1
            main.createvoucher.model.insertRows()
            main.createvoucher.model.rowCount()

            # to add "Cr" raw
            main.createvoucher.table[main.createvoucher.last_serialno, indexlist] = ["Cr", main.account_name, 0,
                                                                                     main.amount, main.currency]

            main.createvoucher.last_serialno += 1
            print("last serial number in cr", main.createvoucher.last_serialno)
            main.createvoucher.model.last_serialno += 1
            main.createvoucher.model.insertRows()
            main.createvoucher.model.rowCount()  # print(main.createvoucher.model.rowCount())
        else:
            dr_row = next((i for i, row in enumerate(main.createvoucher.table) if row[0] == "Dr"), None)
            if dr_row is not None:
                # Update the "Cr" row's debit and credit amounts
                main.createvoucher.table[dr_row][3] = 0  # Update debit amount
                main.createvoucher.table[dr_row][2] += main.amount  # Update credit amount

            existing_cr_row = next(
                (i for i, row in enumerate(main.createvoucher.table) if row[0] == "Cr" and row[1] == main.account_name),
                None)

            if existing_cr_row is not None:
                # Update the existing "Dr" row's debit amount
                main.createvoucher.table[existing_cr_row][3] += main.amount
            else:
                indexlist = [0, 1, 2, 3, 4]

                # # Shift all rows below the insert_index one index below
                # main.createvoucher.table[main.createvoucher.last_serialno + 1:] = main.createvoucher.table[
                #                                                                   main.createvoucher.last_serialno:-1]
                # Add a new "Dr" row at the current last_serialno position
                main.createvoucher.table[main.createvoucher.last_serialno, indexlist] = ["Cr", main.account_name,0,
                                                                                         main.amount,  main.currency]
                main.createvoucher.last_serialno += 1
                main.createvoucher.model.last_serialno += 1
                main.createvoucher.model.insertRows()
                main.createvoucher.model.rowCount()

        main.createvoucher.last_serialno += 1
        main.createvoucher.model.last_serialno += 1
        main.createvoucher.model.insertRows()
        main.createvoucher.model.rowCount()

        # Emit dataChanged signal for the modified rows
        ind = main.createvoucher.model.index(0, 0)
        ind1 = main.createvoucher.model.index(0, 1)
        main.createvoucher.model.dataChanged.emit(ind, ind1)

        updateSumsOnSelectionChange(main)
        main.purchaseentry.leAmount.clear()
        main.purchaseentry.hide()

    except:
        print(traceback.print_exc())


def addRawInPurchaseForCash(main):
    try:
        main.amount = float(main.purchaseentry.leAmount.text())
        main.currency = main.purchaseentry.cbCurrency.currentText()
        # ----------------------- disable other currency option after selected -----------------------------

        if main.currency == "INR":
            main.purchaseentry.cbCurrency.setCurrentIndex(0)  # Set it to INR
            main.purchaseentry.cbCurrency.setEnabled(False)  # Disable the combobox
            main.createvoucher.lbCurrency.setText(main.currency)
        elif main.currency == "USD":
            main.purchaseentry.cbCurrency.setCurrentIndex(1)  # Set it to USD
            main.purchaseentry.cbCurrency.setEnabled(False)
            main.createvoucher.lbCurrency.setText(main.currency)
        else:
            main.purchaseentry.cbCurrency.setEnabled(True)
        # Count the current number of "Cr" and "Dr" rows
        num_cr_rows = sum(1 for row in main.createvoucher.table if row[0] == "Cr")
        num_dr_rows = sum(1 for row in main.createvoucher.table if row[0] == "Dr")

        indexlist = [0, 1, 2, 3, 4]

        # to add "Dr" raw
        main.createvoucher.table[main.createvoucher.last_serialno, indexlist] = ["Dr","Stock",
                                                                                 main.amount, 0, main.currency]
        main.createvoucher.last_serialno += 1
        main.createvoucher.model.last_serialno += 1
        main.createvoucher.model.insertRows()
        main.createvoucher.model.rowCount()

        # to add "Cr" raw
        main.createvoucher.table[main.createvoucher.last_serialno, indexlist] = ["Cr", "Cash", 0,
                                                                                 main.amount, main.currency]

        main.createvoucher.last_serialno += 1
        main.createvoucher.model.last_serialno += 1
        main.createvoucher.model.insertRows()
        main.createvoucher.model.rowCount()

        # Emit dataChanged signal for the modified rows
        ind = main.createvoucher.model.index(0, 0)
        ind1 = main.createvoucher.model.index(0, 1)
        main.createvoucher.model.dataChanged.emit(ind, ind1)

        updateSumsOnSelectionChange(main)
        main.purchaseentry.leAmount.clear()
        main.purchaseentry.hide()

    except:
        print(traceback.print_exc())

##########################################  Receipt Entry - Voucher ##############################################
def showRecieptEntry(main):
    try:
        account_name = [name[1] for name in main.account]
        main.recieptentry.cbAccountName.clear()
        main.recieptentry.cbAccountName.addItems(account_name)
        main.recieptentry.show()

        # Create a QDoubleValidator
        validator = QDoubleValidator()
        # Set the validator to allow only numbers and decimals
        validator.setDecimals(2)
        main.recieptentry.leAmount.setValidator(validator)

        main.recieptentry.cbDrCr.activated.connect(lambda: updateCrDrComboBoxInReciet(main))
        main.recieptentry.cbDrCr.activated.connect(lambda: addEntaryInReceipt(main))

    except:
        print(traceback.print_exc())


def updateCrDrComboBoxInReciet(main):
    # Check the "Dr" or "Cr" selection and call the appropriate function to refresh the combobox
    main.dr_cr = main.recieptentry.cbDrCr.currentText()
    refreshComboBoxForDrInReceipt(main)
    if main.dr_cr == "Dr":
        refreshComboBoxForDrInReceipt(main)
    elif main.dr_cr == "Cr":
        refreshComboBoxForCrInReceipt(main)
    else:
        refreshComboBoxForDrInReceipt(main)



# Initialize a dictionary to store selected account names for "Dr" and "Cr"
selected_account_names_in_receipt = {"Dr": [], "Cr": []}
# Function to refresh the combobox with account names for "Dr"
def refreshComboBoxForDrInReceipt(main):
    try:
        account_name = [name[1] for name in main.account]

        # Clear existing items from the drop-down button
        main.recieptentry.cbAccountName.clear()

        # Populate the drop-down button with account names that haven't been selected as "Cr"
        available_account_names = [name for name in account_name if name not in selected_account_names_in_receipt["Cr"]]
        main.recieptentry.cbAccountName.addItems(available_account_names)

    except Exception as e:
        print(traceback.print_exc())

# Function to refresh the combobox with all account names for "Cr"
def refreshComboBoxForCrInReceipt(main):
    try:
        account_name = [name[1] for name in main.account]
        # Clear existing items from the drop-down button
        main.recieptentry.cbAccountName.clear()

        # Populate the drop-down button with account names that haven't been selected as "Cr"
        available_account_names = [name for name in account_name if name not in selected_account_names_in_receipt["Dr"]]

        # Populate the drop-down button with all account names
        main.recieptentry.cbAccountName.addItems(available_account_names)

    except Exception as e:
        print(traceback.print_exc())

def addEntaryInReceipt(main):
    try:
        main.dr_cr = main.recieptentry.cbDrCr.currentText()
        # Calculate the sum of amounts in the "Cr" and "Dr" columns
        total_cr = sum(row[3] for row in main.createvoucher.table if row[0] == "Cr")
        total_dr = sum(row[2] for row in main.createvoucher.table if row[0] == "Dr")
        if main.dr_cr == "Cr":
            amount_needed = total_dr - total_cr
            if amount_needed > 0:
                main.recieptentry.leAmount.setText(str(amount_needed))

        elif main.dr_cr == "Dr":
            amount_needed = total_cr - total_dr
            if amount_needed > 0:
                # Add a new row with the calculated "Cr" amount
                main.recieptentry.leAmount.setText(str(amount_needed))

        else:
            return  # Invalid selection
    except:
        print(traceback.print_exc())


def addRawInReciept(main):
    try:
        company_id = main.companyID

        main.account_name = main.recieptentry.cbAccountName.currentText()
        main.dr_cr = main.recieptentry.cbDrCr.currentText()
        # Add the selected account name to the appropriate list
        selected_account_names_in_receipt[main.dr_cr].append(main.account_name)
        main.amount = float(main.recieptentry.leAmount.text())

        main.currency = main.recieptentry.cbCurrency.currentText()
    #----------------------- disable other currency option after selected -----------------------------

        if main.currency=="INR":
            main.recieptentry.cbCurrency.setCurrentIndex(0)  # Set it to INR
            main.recieptentry.cbCurrency.setEnabled(False)  # Disable the combobox
            main.createvoucher.lbCurrency.setText(main.currency)
        elif main.currency=="USD":
            main.recieptentry.cbCurrency.setCurrentIndex(1)  # Set it to USD
            main.recieptentry.cbCurrency.setEnabled(False)
            main.createvoucher.lbCurrency.setText(main.currency)
        else:
            main.recieptentry.cbCurrency.setEnabled(True)

        # Count the current number of "Cr" and "Dr" rows
        num_cr_rows = sum(1 for row in main.createvoucher.table if row[0] == "Cr")
        num_dr_rows = sum(1 for row in main.createvoucher.table if row[0] == "Dr")

        # Check if adding a new row is allowed based on the current counts
        if (main.dr_cr == "Cr" and num_dr_rows >= 2) or (main.dr_cr == "Dr" and num_cr_rows >= 2):
            return
        if main.dr_cr == "Cr":
            indexlist=[0,1,2,3,4]
            # Find the index of the last "Cr" row
            last_cr_index = next((i for i, row in enumerate(main.createvoucher.table) if row[0] == "Cr"), -1)
            last_cr_inndex = next((i for i, row in enumerate(main.createvoucher.table) if row[0] == "Cr"and row[1] == main.account_name), -1)

            if last_cr_index >= 0:
                if last_cr_inndex >= 0:
                # Insert the new "Dr" row after the last "Cr" row
                    main.createvoucher.table[last_cr_index, 3] += main.amount
                    updateSumsOnSelectionChange(main)
                    ind = main.createvoucher.model.index(0, 0)
                    ind1 = main.createvoucher.model.index(0, 1)
                    main.createvoucher.model.dataChanged.emit(ind, ind1)
                    main.contraentry.leAmount.clear()
                    main.contraentry.hide()
                else:
                    insert_index = last_cr_index + 1

            else:
                # There are no "Cr" rows, insert at the end
                insert_index = main.createvoucher.last_serialno

            main.createvoucher.table[insert_index + 1:] = main.createvoucher.table[insert_index:-1]

            # Update the table with the values at the insert_index
            main.createvoucher.table[insert_index, indexlist] = [main.dr_cr, main.account_name, 0,main.amount,
                                                                 main.currency]

            main.createvoucher.last_serialno += 1
            main.createvoucher.model.last_serialno += 1
            main.createvoucher.model.insertRows()
            main.createvoucher.model.rowCount()

        elif main.dr_cr == "Dr":
            indexlist = [0, 1, 2, 3, 4]
            # Find the index of the last "Cr" row
            main.createvoucher.last_serialno = 0
            last_dr_index = next(
                (i for i, row in enumerate(main.createvoucher.table) if row[0] == "Dr"),
                -1)

            last_dr_inndex = next(
                (i for i, row in enumerate(main.createvoucher.table) if row[0] == "Dr" and row[1] == main.account_name),
                -1)

            if last_dr_index >= 0:
                if last_dr_inndex >= 0:
                # Insert the new "Dr" row after the last "Cr" row
                    main.createvoucher.table[last_dr_index, 2] += main.amount
                    updateSumsOnSelectionChange(main)
                    ind = main.createvoucher.model.index(0, 0)
                    ind1 = main.createvoucher.model.index(0, 1)
                    main.createvoucher.model.dataChanged.emit(ind, ind1)
                    main.recieptentry.leAmount.clear()
                    main.recieptentry.hide()
                else:
                    insert_index = last_dr_index + 1

            else:
                # There are no "Cr" rows, insert at the end
                insert_index = main.createvoucher.last_serialno
            # Shift all rows below the insert_index one index below
            main.createvoucher.table[insert_index + 1:] = main.createvoucher.table[insert_index:-1]

            # Update the table with the values at the insert_index
            main.createvoucher.table[insert_index, indexlist] = [main.dr_cr, main.account_name, main.amount,0,
                                                                 main.currency]

            main.createvoucher.last_serialno += 1
            main.createvoucher.model.last_serialno += 1
            main.createvoucher.model.insertRows()
            main.createvoucher.model.rowCount()

        # Emit dataChanged signal for the modified row
        ind = main.createvoucher.model.index(0, 0)
        ind1 = main.createvoucher.model.index(0, 1)
        main.createvoucher.model.dataChanged.emit(ind, ind1)

        debitSum = main.createvoucher.table[:main.createvoucher.last_serialno,3].sum()
        main.debitAmount =  main.createvoucher.lbDebit.setText(str(debitSum))

        creditSum = main.createvoucher.table[:main.createvoucher.last_serialno,2].sum()
        main.creditAmount = main.createvoucher.lbCredit.setText(str(creditSum))

        updateSumsOnSelectionChange(main)
        ############### Clear the input widgets after adding data#################
        main.recieptentry.cbDrCr.setCurrentIndex(0)
        main.recieptentry.leAmount.clear()
        main.recieptentry.hide()

    except:
        print(traceback.print_exc())

##################################################### Contra Entry ################################################

def showContraEntry(main):
    try:
        main.contraentry.show()
        validator = QDoubleValidator()
        # Set the validator to allow only numbers and decimals
        validator.setDecimals(2)
        main.contraentry.leAmount.setValidator(validator)

        account_name = [name[1] for name in main.account]
        main.contraentry.cbAccountName.clear()
        main.contraentry.cbAccountName.addItems(account_name)


        # # Connect the signal for cbDrCr combobox
        main.contraentry.cbDrCr.activated.connect(lambda: updateCrDrComboBox(main))
        main.contraentry.cbDrCr.activated.connect(lambda: addEntary(main))

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
        validator = QDoubleValidator()
        # Set the validator to allow only numbers and decimals
        validator.setDecimals(2)
        main.tableshow.leAmount.setValidator(validator)

        # # Connect the signal for cbDrCr combobox
        main.tableshow.cbDrCr.activated.connect(lambda: updateCrDrComboBox(main))
        main.tableshow.cbDrCr.activated.connect(lambda: addEntary(main))

    except:
        print(traceback.print_exc())


def updateCrDrComboBox(main):
    # Check the "Dr" or "Cr" selection and call the appropriate function to refresh the combobox
    main.dr_cr = main.contraentry.cbDrCr.currentText()

    if main.dr_cr == "Dr":
        refreshComboBoxForDr(main)
    elif main.dr_cr == "Cr":
        refreshComboBoxForCr(main)
    else:
        refreshComboBoxForDr(main)


def updateSumsOnSelectionChange(main):
    try:

        main.debitSum = np.sum(main.createvoucher.table[:, 2].astype(float))
        debitSumFormatted = "{:.2f}".format(main.debitSum)  # Format the float with 2 decimal places
        main.createvoucher.lbDebit.setText(debitSumFormatted)

        main.creditSum = np.sum(main.createvoucher.table[:, 3].astype(float))
        creditSumFormatted = "{:.2f}".format(main.creditSum)  # Format the float with 2 decimal places
        main.createvoucher.lbCredit.setText(creditSumFormatted)
        main.createvoucher.pbSubmit.setVisible(main.debitSum == main.creditSum)

    except:
        print(traceback.print_exc())

# Initialize a dictionary to store selected account names for "Dr" and "Cr"
selected_account_names = {"Dr": [], "Cr": []}
# Function to refresh the combobox with account names for "Dr"
def refreshComboBoxForDr(main):
    try:
        account_name = [name[1] for name in main.account]

        # Clear existing items from the drop-down button
        main.contraentry.cbAccountName.clear()

        # Populate the drop-down button with account names that haven't been selected as "Cr"
        available_account_names = [name for name in account_name if name not in selected_account_names["Cr"]]
        main.contraentry.cbAccountName.addItems(available_account_names)

    except Exception as e:
        print(traceback.print_exc())

# Function to refresh the combobox with all account names for "Cr"
def refreshComboBoxForCr(main):
    try:
        account_name = [name[1] for name in main.account]

        # Clear existing items from the drop-down button
        main.contraentry.cbAccountName.clear()

        # Populate the drop-down button with account names that haven't been selected as "Cr"
        available_account_names = [name for name in account_name if name not in selected_account_names["Dr"]]
        # Populate the drop-down button with all account names
        main.contraentry.cbAccountName.addItems(available_account_names)

    except Exception as e:
        print(traceback.print_exc())

def addEntary(main):
    try:
        main.dr_cr = main.contraentry.cbDrCr.currentText()
        # Calculate the sum of amounts in the "Cr" and "Dr" columns
        total_cr = sum(row[3] for row in main.createvoucher.table if row[0] == "Cr")
        total_dr = sum(row[2] for row in main.createvoucher.table if row[0] == "Dr")
        if main.dr_cr == "Cr":
            amount_needed = total_dr - total_cr
            if amount_needed > 0:
                main.contraentry.leAmount.setText(str(amount_needed))
        elif main.dr_cr == "Dr":
            amount_needed = total_cr - total_dr
            if amount_needed > 0:
                # Add a new row with the calculated "Cr" amount
                main.contraentry.leAmount.setText(str(amount_needed))

        else:
            return  # Invalid selection
    except:
        print(traceback.print_exc())


def addRawInContra(main):
    try:
        company_id = main.companyID

        main.account_name = main.contraentry.cbAccountName.currentText()
        main.dr_cr = main.contraentry.cbDrCr.currentText()
        # Add the selected account name to the appropriate list
        selected_account_names[main.dr_cr].append(main.account_name)
        main.amount = float(main.contraentry.leAmount.text())

        main.currency = main.contraentry.cbCurrency.currentText()
    #----------------------- disable other currency option after selected -----------------------------

        if main.currency=="INR":
            main.contraentry.cbCurrency.setCurrentIndex(0)  # Set it to INR
            main.contraentry.cbCurrency.setEnabled(False)  # Disable the combobox
            main.createvoucher.lbCurrency.setText(main.currency)
        elif main.currency=="USD":
            main.contraentry.cbCurrency.setCurrentIndex(1)  # Set it to USD
            main.contraentry.cbCurrency.setEnabled(False)
            main.createvoucher.lbCurrency.setText(main.currency)
        else:
            main.contraentry.cbCurrency.setEnabled(True)
        # Count the current number of "Cr" and "Dr" rows
        num_cr_rows = sum(1 for row in main.createvoucher.table if row[0] == "Cr")
        num_dr_rows = sum(1 for row in main.createvoucher.table if row[0] == "Dr")

        # Check if adding a new row is allowed based on the current counts
        if (main.dr_cr == "Cr" and num_dr_rows >= 2) or (main.dr_cr == "Dr" and num_cr_rows >= 2):
            return
        if main.dr_cr == "Cr":
            indexlist=[0,1,2,3,4]
            # Find the index of the last "Cr" row
            last_cr_index = next((i for i, row in enumerate(main.createvoucher.table) if row[0] == "Cr"), -1)
            last_cr_inndex = next((i for i, row in enumerate(main.createvoucher.table) if row[0] == "Cr"and row[1] == main.account_name), -1)

            if last_cr_index >= 0:
                if last_cr_inndex >= 0:
                # Insert the new "Dr" row after the last "Cr" row
                    main.createvoucher.table[last_cr_index, 3] += main.amount
                    updateSumsOnSelectionChange(main)
                    ind = main.createvoucher.model.index(0, 0)
                    ind1 = main.createvoucher.model.index(0, 1)
                    main.createvoucher.model.dataChanged.emit(ind, ind1)
                    main.contraentry.leAmount.clear()
                    main.contraentry.hide()
                else:
                    insert_index = last_cr_index + 1

            else:
                # There are no "Cr" rows, insert at the end
                insert_index = main.createvoucher.last_serialno
            # Shift all rows below the insert_index one index below
            main.createvoucher.table[insert_index + 1:] = main.createvoucher.table[insert_index:-1]

            # Update the table with the values at the insert_index
            main.createvoucher.table[insert_index, indexlist] = [main.dr_cr, main.account_name, 0,main.amount,
                                                                 main.currency]

            # # # Increment the last_serialno
            main.createvoucher.last_serialno += 1
            main.createvoucher.model.last_serialno += 1
            main.createvoucher.model.insertRows()
            main.createvoucher.model.rowCount()




        elif main.dr_cr == "Dr":
            indexlist = [0, 1, 2, 3, 4]
            # Find the index of the last "Cr" row
            main.createvoucher.last_serialno = 0
            last_dr_index = next(
                (i for i, row in enumerate(main.createvoucher.table) if row[0] == "Dr"),
                -1)

            last_dr_inndex = next(
                (i for i, row in enumerate(main.createvoucher.table) if row[0] == "Dr" and row[1] == main.account_name),
                -1)

            if last_dr_index >= 0:
                if last_dr_inndex >= 0:
                # Insert the new "Dr" row after the last "Cr" row
                    main.createvoucher.table[last_dr_index, 2] += main.amount
                    updateSumsOnSelectionChange(main)
                    ind = main.createvoucher.model.index(0, 0)
                    ind1 = main.createvoucher.model.index(0, 1)
                    main.createvoucher.model.dataChanged.emit(ind, ind1)
                    main.tableshow.leAmount.clear()
                    main.tableshow.hide()
                else:
                    insert_index = last_dr_index + 1

            else:
                # There are no "Cr" rows, insert at the end
                insert_index = main.createvoucher.last_serialno

            # Shift all rows below the insert_index one index below
            main.createvoucher.table[insert_index + 1:] = main.createvoucher.table[insert_index:-1]

            # Update the table with the values at the insert_index
            main.createvoucher.table[insert_index, indexlist] = [main.dr_cr, main.account_name, main.amount,0,
                                                                 main.currency]

            main.createvoucher.last_serialno += 1
            main.createvoucher.model.last_serialno += 1
            main.createvoucher.model.insertRows()
            main.createvoucher.model.rowCount()

        # Emit dataChanged signal for the modified row
        ind = main.createvoucher.model.index(0, 0)
        ind1 = main.createvoucher.model.index(0, 1)
        main.createvoucher.model.dataChanged.emit(ind, ind1)

        debitSum = main.createvoucher.table[:main.createvoucher.last_serialno,3].sum()
        main.debitAmount =  main.createvoucher.lbDebit.setText(str(debitSum))

        creditSum = main.createvoucher.table[:main.createvoucher.last_serialno,2].sum()
        main.creditAmount = main.createvoucher.lbCredit.setText(str(creditSum))
        updateSumsOnSelectionChange(main)
        ############### Clear the input widgets after adding data#################

        main.contraentry.cbDrCr.setCurrentIndex(0)
        main.contraentry.leAmount.clear()
        main.contraentry.hide()

    except:
        print(traceback.print_exc())


########################################### Currency Conversion - Voucher #######################################

def showCurrConvEntry(main):
    try:
        main.currconventry.show()
    except:
        print(traceback.print_exc())


######################################### Add Raw In TableView #####################################################

def deleteRows(main):
    try:
        if main.createvoucher.last_serialno > 0:
            main.createvoucher.last_serialno -= 1
            main.createvoucher.model.last_serialno -= 1
            main.createvoucher.model.DelRows()
            main.createvoucher.model.rowCount()

            main.createvoucher.table[main.createvoucher.last_serialno] = [0, 0, 0, 0, 0]

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
        # Check if data has already been fetched, if yes, return without fetching again

        cursor = main.db_connection.cursor()
        command = """
        SELECT 
        a.Date,
        a.VoucherNO,a.VoucherType,b.DebitSideAccount as 'Debit Acc',
        b.CreditSideAccount as 'Credit Acc',b.DebitAmount as 'Amount',b.Currency,a.Narration
        FROM Voucher_Master a left join Voucher_details b on a.VoucherID = b.VoucherID
        Where CompanyID = ?
        ORDER BY a.Date ASC
        """
        cursor.execute(command, (main.companyID,))
        data = cursor.fetchall()
        main.daybook.table[0:main.ledgerblance.last_serialno]=[0,0,0,0,0,0,0,0]
        main.daybook.model.DelRows(0,main.daybook.model.last_serialno)
        main.daybook.last_serialno = 0
        main.daybook.model.last_serialno = 0
        if data:
            # Populate the model only if there is data available
            for row in data:
                main.daybook.table[main.daybook.last_serialno] = list(row)
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
        main.daybook.leAccount.clear()
        current_date = QDate.currentDate()
        # Your string date
        date_str = '01-04-2023'

        # Parse the string date into day, month, and year components
        day, month, year = map(int, date_str.split('-'))

        # Create a QDate object
        date = QDate(year, month, day)

        # Set the date in your QDateEdit widget
        main.daybook.deFrom.setDate(date)
        main.daybook.deTo.setDate(current_date)
        main.gateway.showDayBookFrame()
    except:
        print(traceback.print_exc())


def filterDataByAccountName(main):
    try:
        selecteAccount = main.daybook.leAccount.text()

        # Set the filter to show only rows where Debit Acc or Credit Acc match the selected account
        main.daybook.smodel.setFilterKeyColumn(-1)  # Match against all columns
        main.daybook.smodel.setFilterRegExp(selecteAccount)

    except:
      print(traceback.print_exc())


def dayBookDoubleClicked(main):
    try:
        idx = main.daybook.tableView.selectedIndexes()[0].data()


        indexes = main.daybook.tableView.selectedIndexes()
        index = indexes[0]  # Get the first selected index
        row = index.row()
        col = index.column()

        if col == 1:
            name = index.sibling(index.row(), col).data()

            showAlterVoucher(main, name)

        if col == 3 or col == 4:
            main.ledgerID = idx
            try:

                cursor = main.db_connection.cursor()
                query = '''SELECT * FROM AccountMaster_table WHERE Ac_name = ?'''
                cursor.execute(query, (idx,))
                ledger_data = cursor.fetchone()
                group_roles = getGroupRoles(main)
                company_groups = getGroupsCreatedByCompany(main)
                branches = getBranch(main)
                # Combine group roles and company groups into a single list
                role_names = [role[1] for role in group_roles]
                group_names = [group[1] for group in company_groups]
                all_items = role_names + group_names
                branch_name = [branch[1] for branch in branches]

                # Clear existing items from the drop-down button
                main.alterledger.cbUnderGroup.clear()
                main.alterledger.cbUnderBranch.clear()

                # Populate the drop-down button with group role names
                main.alterledger.cbUnderGroup.addItems(all_items)
                main.alterledger.cbUnderBranch.addItems(branch_name)

                if ledger_data:
                    # Populate the fields in the "Create Ledger" form with the retrieved data
                    main.alterledger.leAcName.setText(ledger_data[1])  # Assuming ledger name is at index 1
                    main.alterledger.leMailingName.setText(ledger_data[4])  # Assuming mailing name is at index 4
                    # Set the selected role in the comboBox
                    selected_role = ledger_data[3]  # Assuming group role is at index 3
                    main.alterledger.cbUnderGroup.setCurrentText(ledger_data[2])
                    main.alterledger.ptAddress.setPlainText(ledger_data[5])
                    main.alterledger.leCountry.setText(ledger_data[7])
                    main.alterledger.lePincode.setText(str(ledger_data[8]))
                    main.alterledger.leBalance.setText(str(ledger_data[10]))
                    selected_branch = ledger_data[12]
                    main.alterledger.cbUnderBranch.setCurrentText(str(selected_branch))

            except sqlite3.Error as e:
                print("Error fetching ledger data:", e)

    except:
        print(traceback.print_exc())


def filterDataByDateRange(main):
    try:
        # Get the selected "From" and "To" dates
        fromDate = main.daybook.deFrom.date()
        toDate = main.daybook.deTo.date()

        # Convert dates to strings in the required format
        fromDateStr = fromDate.toString("dd-MM-yyyy")
        toDateStr = toDate.toString("dd-MM-yyyy")

        # Use SQL query to fetch data within the date range
        cursor = main.db_connection.cursor()
        command = """
        SELECT 
        a.Date,
        a.VoucherNO,a.VoucherType,b.DebitSideAccount as 'Debit Acc',
        b.CreditSideAccount as 'Credit Acc',a.DebitAmount as 'Amount',b.Currency,a.Narration
        FROM Voucher_Master a left join Voucher_details b on a.VoucherID = b.VoucherID
        WHERE CompanyID = ? AND Date BETWEEN ? AND ?
        ORDER BY a.Date ASC 
        """
        cursor.execute(command, (main.companyID, fromDateStr, toDateStr))
        data = cursor.fetchall()

        # Clear the existing data in the model
        main.daybook.model.DelRows(0, main.daybook.model.last_serialno)
        main.daybook.last_serialno = 0
        main.daybook.model.last_serialno = 0

        if data:
            # Populate the model with the filtered data
            for row in data:
                main.daybook.table[main.daybook.last_serialno] = list(row)
                main.daybook.last_serialno += 1
                main.daybook.model.last_serialno += 1
                main.daybook.model.insertRows()
        main.daybook.deFrom.clear()
    except Exception as e:
        print("Error filtering data by date range:", str(e))



def showAlterVoucher(main , voucherNo):
    try:

        main.createvoucher.pbDelete.setVisible(True)
        main.voucherNo = voucherNo
        main.gateway.fDayBook.hide()
        main.gateway.fVouchers.show()
        main.createvoucher.show()

        main.createvoucher.table[0: main.createvoucher.last_serialno] = [0, 0, 0, 0, 0]
        # self.model.removeRows(0, self.model.rowCount())

        main.createvoucher.model.DelRows(0, main.createvoucher.last_serialno)
        main.createvoucher.last_serialno = 0
        main.createvoucher.model.last_serialno = 0
        main.createvoucher.model.rowCount()

        ind = main.createvoucher.model.index(0, 0)
        ind1 = main.createvoucher.model.index(0, 1)
        main.createvoucher.model.dataChanged.emit(ind, ind1)


        main.createvoucher.clearFields()
        cursor = main.db_connection.cursor()


        query = '''
                   SELECT vm.*, vd.*
                   FROM Voucher_Master vm
                   LEFT JOIN Voucher_details vd ON vm.VoucherID = vd.VoucherID
                   WHERE vm.VoucherNO = ?
               '''
        cursor.execute(query, (voucherNo,))
        voucher_data = cursor.fetchone()

        account = getAccountMaster(main)
        main.account = account


        account_name = [name[1] for name in account]
        main.contraentry.cbAccountName.addItems(account_name)
        main.paymententry.cbAccountName.addItems(account_name)
        main.createvoucher.model.dataChanged.connect(lambda: updateSumsOnSelectionChange(main))

        if voucher_data:
            main.createvoucher.leVoucherNo.setText(voucher_data[1])
            main.createvoucher.lbVoucherType.setText(voucher_data[2])
            # Assuming voucher_data[3] contains a date string in the format 'YYYY-MM-DD'
            date_str = voucher_data[3]
            date_obj = datetime.strptime(date_str, '%d-%m-%Y').date()
            # Create dictionaries to store consolidated data
            dr_accounts = defaultdict(float)
            cr_accounts = defaultdict(float)
            for raw in voucher_data:
                print("alter voucher")
                main.createvoucher.leVoucherNo.setText(raw[1])
                main.createvoucher.lbVoucherType.setText(raw[2])
                # Assuming voucher_data[3] contains a date string in the format 'YYYY-MM-DD'
                date_str = raw[3]
                date_obj = datetime.strptime(date_str, '%d-%m-%Y').date()

                # Now you can set the date in your QDateEdit widget
                main.createvoucher.deDate.setDate(date_obj)
                main.createvoucher.leNarration.setText(raw[4])


                debit_amount = raw[5]  # Assuming voucher_data[5] is a float
                debit_amount_str = "{:.2f}".format(debit_amount)  # Format the float with 2 decimal places
                main.createvoucher.lbDebit.setText(debit_amount_str)  # Set the formatted string as text


                credit_amount = raw[6]  # Assuming voucher_data[5] is a float
                credit_amount_str = "{:.2f}".format(credit_amount)  # Format the float with 2 decimal places
                main.createvoucher.lbCredit.setText(credit_amount_str)  # Set the formatted string as text


                # main.createvoucher.lbCredit.setText(voucher_data[6])
                main.createvoucher.lbCurrency.setText(str(raw[9]))




            ##############TABLE Entries########################

                DRAccount=raw[11]
                CRAccount=raw[12]
                DRAmt=raw[13]
                CRAmt=raw[14]
                Currency=raw[15]
                print("Dr Account_____________________", DRAccount)
                print("Cr Account_____________________", CRAccount)


                # Update consolidated amounts
                if DRAccount:
                    dr_accounts[DRAccount] += DRAmt
                    print("dr account-------------", dr_accounts[DRAccount])
                if CRAccount:
                    cr_accounts[CRAccount] += CRAmt
                    print("cr account-------------", cr_accounts[CRAccount])
            print("dr account items----------------", dr_accounts.items())
            # Update the table with consolidated data
            for account, amount in dr_accounts.items():
                main.createvoucher.table[main.createvoucher.last_serialno,] = ['Dr', account, amount, 0,
                                                                               Currency]
                main.createvoucher.last_serialno += 1
                main.createvoucher.model.last_serialno += 1
                main.createvoucher.model.insertRows()
            print("cr account items----------------",  cr_accounts.items())
            for account, amount in cr_accounts.items():
                main.createvoucher.table[main.createvoucher.last_serialno,] = ['Cr', account, 0, amount,
                                                                               Currency]
                main.createvoucher.last_serialno += 1
                main.createvoucher.model.last_serialno += 1
                main.createvoucher.model.insertRows()
            print("alter voucher table--------------", main.createvoucher.table)
            ind = main.createvoucher.model.index(0, 0)
            ind1 = main.createvoucher.model.index(0, 1)
            main.createvoucher.model.dataChanged.emit(ind, ind1)



    except:
        print(traceback.print_exc())

def deleteVoucher(main):
    try:
        if main.voucherNo:
            confirmation = QMessageBox.question(
                main,
                'Delete Voucher',
                f'Do you want to delete voucher {main.voucherNo}?',
                QMessageBox.Yes | QMessageBox.No
            )

            if confirmation == QMessageBox.Yes:
                # Perform the deletion in the database
                cursor = main.db_connection.cursor()
                # Retrieve the VoucherID associated with the voucher number
                cursor.execute("SELECT VoucherID FROM Voucher_Master WHERE VoucherNO = ?", (main.voucherNo,))
                voucher_id = cursor.fetchone()[0]

                if voucher_id:
                    # Delete from Voucher_details table
                    cursor.execute("DELETE FROM Voucher_details WHERE VoucherID = ?", (voucher_id,))

                    # Delete from Ledger_table where VoucherNo matches
                    cursor.execute("DELETE FROM Ledger_table WHERE VoucherNo = ?", (main.voucherNo,))

                    # Delete from Voucher_Master table
                    cursor.execute("DELETE FROM Voucher_Master WHERE VoucherNO = ?", (main.voucherNo,))

            main.db_connection.commit()

            # Optionally, clear the fields or update the UI to reflect the deletion
            main.createvoucher.clearFields()  # Implement this function to clear/reset UI fields
            QMessageBox.information(main, 'Voucher Deleted', f'Voucher {main.voucherNo} has been deleted.')
        else:
            QMessageBox.warning(main, 'Missing Voucher Number', 'Please enter a voucher number to delete.')

    except:
        print(traceback.print_exc())

# ------------------------------------ For Trial Balance ---------------------------------------

def fetchTrialBalanceData(main,fromdate='01-04-2023',enddate=datetime.today().strftime('%d-%m-%Y')):
    try:
        print(enddate)
        main.trialbalance.table[0:main.trialbalance.last_serialno] =[0,0,0,0,0,0]
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
                        Date,LedgerName, Currency ,Debit ,Credit  
                    FROM 
                        Ledger_table 
                    WHERE 
                        Perticulars == 'Closing Balance'
                    """
        cursor.execute(command, )

        data = cursor.fetchall()

        for row in data:
            index_list = [0, 1, 2, 3, 4, 5]

            if row[2]=='INR':
                main.trialbalance.table[main.trialbalance.last_serialno,index_list] = [row[0],row[1],row[3],row[4],0,0]
                main.trialbalance.last_serialno += 1
                main.trialbalance.model.last_serialno += 1
                main.trialbalance.model.insertRows()
                main.trialbalance.model.rowCount()

                # Emit dataChanged signal for the modified row
                ind = main.trialbalance.model.index(0, 0)
                ind1 = main.trialbalance.model.index(0, 1)
                main.trialbalance.model.dataChanged.emit(ind, ind1)
            elif row[2]=='USD':
                main.trialbalance.table[main.trialbalance.last_serialno, index_list] = [row[0], row[1],0,0,
                                                                                        row[3],
                                                                                        row[4]]
                main.trialbalance.last_serialno += 1
                main.trialbalance.model.last_serialno += 1
                main.trialbalance.model.insertRows()
                main.trialbalance.model.rowCount()

                # Emit dataChanged signal for the modified row
                ind = main.trialbalance.model.index(0, 0)
                ind1 = main.trialbalance.model.index(0, 1)
                main.trialbalance.model.dataChanged.emit(ind, ind1)

        totalSumInTrialBalance(main)

    except:
        print(traceback.print_exc())

def totalSumInTrialBalance(main):
    try:

        condition = main.trialbalance.table[:main.trialbalance.last_serialno, 1] != 'Closing Balance'

        ###################################### INR SUm ###########################################################

        debitSumInr = np.sum(main.trialbalance.table[:main.trialbalance.last_serialno, 2][condition].astype(float))
        debitSumFormattedInr = "{:.2f}".format(debitSumInr)  # Format the float with 2 decimal places
        main.trialbalance.lbdebitINR.setText(debitSumFormattedInr)

        creditSumInr = np.sum(main.trialbalance.table[:main.trialbalance.last_serialno, 3][condition].astype(float))
        creditSumFormattedInr = "{:.2f}".format(creditSumInr)  # Format the float with 2 decimal places
        main.trialbalance.lbcreditINR.setText(creditSumFormattedInr)

        ######################################### USD Sum #################################################

        debitSumUsd = np.sum(main.trialbalance.table[:main.trialbalance.last_serialno, 4][condition].astype(float))
        debitSumFormattedUsd = "{:.2f}".format(debitSumUsd)  # Format the float with 2 decimal places
        main.trialbalance.lbdebitUSD.setText(debitSumFormattedUsd)

        creditSumUsd = np.sum(main.trialbalance.table[:main.trialbalance.last_serialno, 5][condition].astype(float))
        creditSumFormattedUsd = "{:.2f}".format(creditSumUsd)  # Format the float with 2 decimal places
        main.trialbalance.lbcreditUSD.setText(creditSumFormattedUsd)


    except:
        print(traceback.print_exc())


def showTrialBalance(main):
    try:
        current_date = QDate.currentDate()
        current_date_str = current_date.toString("dd-MM-yyyy")
        main.trialbalance.lbDate.setText(current_date_str)

        date = main.datefilter.deFrom.date()
        fromdate = date.toString("dd-MM-yyyy")

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

        for row in data:
            main.trialbalance.table[main.trialbalance.last_serialno, [0, 1, 2]] = list(row)

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
        main.is_filtered = False
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

            if idy=="Ledger-Wise":
                cursor = main.db_connection.cursor()
                command = """SELECT 
                                 Date,Perticulars ,Debit ,Credit ,Currency 
                            FROM 
                                 Ledger_table """

                cursor.execute(command,)
                data = cursor.fetchall()
                idx = main.trialbalance.tableView.selectedIndexes()[1].data()
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

            if idy == "Ledger-Wise":
                cursor = main.db_connection.cursor()
                command = """SELECT 
                        Date,Perticulars ,Debit ,Credit, Currency 
                    FROM 
                        Ledger_table """

                cursor.execute(command, )
                data = cursor.fetchall()
                idx = main.trialbalance.tableView.selectedIndexes()[1].data()
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


         # Create a QDialog to display the data in a table view
        dialog = QDialog(main)
        dialog.setWindowTitle("Data Details")
        dialog.setGeometry(580, 300, 450, 350)

        # Create a QTableView and set the data model
        table_view = QTableView()
        model = QStandardItemModel()
        model.setColumnCount(5)
        model.setHorizontalHeaderLabels(["Date","Perticulars", "Debit Amount INR", "Credit Amount INR","Currency"])


        for row in filtered_data:
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
        main.datefilter.deTo.setDate(current_date)
        main.datefilter.show()
        selectedDateFrom = main.datefilter.deFrom.date()
        selectedTextDateFrom = selectedDateFrom.toString("dd-MM-yyyy")
        main.selectdateFrom = selectedTextDateFrom

        selectedDateTo = main.datefilter.deTo.date()
        selectedTextDateTo = selectedDateTo.toString("dd-MM-yyyy")
        main.selectdateTo = selectedTextDateTo

    except:
        print(traceback.print_exc())



#--------------------------------------  Ledger Balance -----------------------------------------------#


def showLedgerBalance(main):
    try:
        main.ledgerblance.show()
        populate_account_combobox(main)

        current_date = QDate.currentDate()
        # Your string date
        date_str = '01-04-2023'

        # Parse the string date into day, month, and year components
        day, month, year = map(int, date_str.split('-'))

        # Create a QDate object
        date = QDate(year, month, day)

        # Set the date in your QDateEdit widget
        main.ledgerblance.deFrom.setDate(date)
        main.ledgerblance.deTo.setDate(current_date)

        # Connect the currentIndexChanged signal to the slot function
        main.ledgerblance.cbAccount.activated.connect(lambda : loadLedgerData(main))
        # main.ledgerblance.cbAccount.activated.connect(lambda : totalClosingBalance(main))
        main.ledgerblance.cbAccount.activated.connect(lambda : totalSumInLedger(main))

    except:
        print(traceback.print_exc())


# Function to populate the QComboBox with distinct account names from both tables
def populate_account_combobox(main):
    try:
        cursor = main.db_connection.cursor()
        cursor.execute("""
                   
                    SELECT DISTINCT LedgerName
                    FROM Ledger_table
                    WHERE LedgerName IS NOT NULL
                """)

        account_names = cursor.fetchall()

        # Clear existing items in the combobox
        main.ledgerblance.cbAccount.clear()

        # Add fetched account names to the combobox
        for account_name in account_names:
            main.ledgerblance.cbAccount.addItem(account_name[0])

    except Exception as e:
        print("Error fetching account names:", str(e))


def filterDataByDateInLedgerBalance(main):
    try:
        # Get the selected "From" and "To" dates
        fromDate = main.ledgerblance.deFrom.date()
        toDate = main.ledgerblance.deTo.date()

        # Convert dates to strings in the required format
        fromDateStr = fromDate.toString("dd-MM-yyyy")
        toDateStr = toDate.toString("dd-MM-yyyy")

        selected_account = main.ledgerblance.cbAccount.currentText()
        # Use SQL query to fetch data within the date range
        cursor = main.db_connection.cursor()
        command = """
              
              SELECT date, Perticulars, VoucherNO, Currency, Debit, Credit
            FROM Ledger_table
            WHERE LedgerName = ?  AND Date BETWEEN ? AND ?
            
               """
        cursor.execute(command, (selected_account, fromDateStr, toDateStr))
        data = cursor.fetchall()

        # Clear the existing data in the model
        main.ledgerblance.table[0:main.ledgerblance.last_serialno] = [0, 0, 0, 0, 0, 0, 0]
        main.ledgerblance.model.DelRows(0, main.ledgerblance.model.last_serialno)
        main.ledgerblance.last_serialno = 0
        main.ledgerblance.model.last_serialno = 0

        # print("data:", data)
        index_list = [0, 1, 2, 3, 4, 5, 6]
        # Populate the model only if there is data available
        for row in data:
            if row[3] == 'INR':
                # print("ledger data",[row[0],row[1],row[2],f"{row[4]}  {row[3]}",f"{row[5]}  {row[3]}",0,0])
                main.ledgerblance.table[main.ledgerblance.last_serialno, index_list] = [row[0], row[1], row[2], row[4],
                                                                                        row[5], 0, 0]
                main.ledgerblance.last_serialno += 1
                main.ledgerblance.model.last_serialno += 1
                main.ledgerblance.model.insertRows()
                main.ledgerblance.model.rowCount()

                # Emit dataChanged signal for the modified row
                ind = main.ledgerblance.model.index(0, 0)
                ind1 = main.ledgerblance.model.index(0, 1)
                main.ledgerblance.model.dataChanged.emit(ind, ind1)
            elif row[3] == 'USD':
                # print("ledger data", [row[0], row[1], row[2], f"{row[4]}  {row[3]}", f"{row[5]}  {row[3]}", 0, 0])
                main.ledgerblance.table[main.ledgerblance.last_serialno, index_list] = [row[0], row[1], row[2], 0, 0,
                                                                                        row[4],
                                                                                        row[5]]
                main.ledgerblance.last_serialno += 1
                main.ledgerblance.model.last_serialno += 1
                main.ledgerblance.model.insertRows()
                main.ledgerblance.model.rowCount()

                # Emit dataChanged signal for the modified row
                ind = main.ledgerblance.model.index(0, 0)
                ind1 = main.ledgerblance.model.index(0, 1)
                main.ledgerblance.model.dataChanged.emit(ind, ind1)

        main.ledgerblance.deFrom.clear()
        totalSumInLedger(main)
    except:
        print(traceback.print_exc())



def loadLedgerData(main):
    try:

        current_date = QDate.currentDate()
        # Your string date
        date_str = '01-04-2023'

        # Parse the string date into day, month, and year components
        day, month, year = map(int, date_str.split('-'))

        # Create a QDate object
        date = QDate(year, month, day)

        # Set the date in your QDateEdit widget
        main.ledgerblance.deFrom.setDate(date)
        # Get the selected account name from the combobox
        selected_account = main.ledgerblance.cbAccount.currentText()

        # Execute the SQL query based on the selected account name
        cursor = main.db_connection.cursor()
        cursor.execute("""
            SELECT date, Perticulars, VoucherNO, Currency, Debit, Credit
            FROM Ledger_table
            WHERE LedgerName = ? 
            ORDER BY Date ASC;
        """, (selected_account,))

        # Fetch the query results
        ledger_data = cursor.fetchall()

        main.ledgerblance.table[0:main.ledgerblance.last_serialno]=[0,0,0,0,0,0,0]
        main.ledgerblance.model.DelRows(0, main.ledgerblance.model.last_serialno)
        main.ledgerblance.last_serialno = 0
        main.ledgerblance.model.last_serialno = 0
        index_list = [0, 1, 2, 3, 4,5,6]
        # Populate the model only if there is data available
        for row in ledger_data:
            if row[3]=='INR':
                main.ledgerblance.table[main.ledgerblance.last_serialno,index_list] = [row[0],row[1],row[2],row[4],row[5],0,0]
                main.ledgerblance.last_serialno += 1
                main.ledgerblance.model.last_serialno += 1
                main.ledgerblance.model.insertRows()
                main.ledgerblance.model.rowCount()

                # Emit dataChanged signal for the modified row
                ind = main.ledgerblance.model.index(0, 0)
                ind1 = main.ledgerblance.model.index(0, 1)
                main.ledgerblance.model.dataChanged.emit(ind, ind1)
            elif row[3]=='USD':
                main.ledgerblance.table[main.ledgerblance.last_serialno, index_list] = [row[0], row[1], row[2],0,0,
                                                                                        row[4],
                                                                                        row[5]]
                main.ledgerblance.last_serialno += 1
                main.ledgerblance.model.last_serialno += 1
                main.ledgerblance.model.insertRows()
                main.ledgerblance.model.rowCount()

                # Emit dataChanged signal for the modified row
                ind = main.ledgerblance.model.index(0, 0)
                ind1 = main.ledgerblance.model.index(0, 1)
                main.ledgerblance.model.dataChanged.emit(ind, ind1)

        totalSumInLedger(main)
    except Exception as e:
        print("Error loading ledger data:", str(e))


def totalSumInLedger(main):
    try:

        condition = main.ledgerblance.table[:main.ledgerblance.last_serialno, 1] != 'Closing Balance'

        ###################################### INR SUm ###########################################################

        debitSumInr = np.sum(main.ledgerblance.table[:main.ledgerblance.last_serialno, 3][condition].astype(float))
        debitSumFormattedInr = "{:.2f}".format(debitSumInr)  # Format the float with 2 decimal places
        # print("debit sum", debitSumFormatted)
        main.ledgerblance.lbtotalDebitINR.setText(f"{debitSumFormattedInr} INR")

        creditSumInr = np.sum(main.ledgerblance.table[:main.ledgerblance.last_serialno, 4][condition].astype(float))
        creditSumFormattedInr = "{:.2f}".format(creditSumInr)  # Format the float with 2 decimal places
        main.ledgerblance.lbtotalCreditINR.setText(f"{creditSumFormattedInr} INR")


        closingNalanceInr = creditSumInr - debitSumInr
        print("sum of closing inr",closingNalanceInr )
        if closingNalanceInr <0:
            main.ledgerblance.lbClosingBalanceCreditINR.setText(f"{abs(closingNalanceInr)} INR")
            main.ledgerblance.lbClosingBalanceDebitINR.setText(f"{0} INR")
        else:
            main.ledgerblance.lbClosingBalanceDebitINR.setText(f"{abs(closingNalanceInr)} INR")
            main.ledgerblance.lbClosingBalanceCreditINR.setText(f"{0} INR")



        ######################################### USD Sum #################################################

        debitSumUsd = np.sum(main.ledgerblance.table[:main.ledgerblance.last_serialno, 5][condition].astype(float))
        debitSumFormattedUsd = "{:.2f}".format(debitSumUsd)  # Format the float with 2 decimal places
        main.ledgerblance.lbtotalDebitUSD.setText(debitSumFormattedUsd)

        creditSumUsd = np.sum(main.ledgerblance.table[:main.ledgerblance.last_serialno, 6][condition].astype(float))
        creditSumFormattedUsd = "{:.2f}".format(creditSumUsd)  # Format the float with 2 decimal places
        main.ledgerblance.lbtotalCreditUSD.setText(f"{creditSumFormattedUsd} USD")


        closingNalanceUsd = creditSumUsd - debitSumUsd
        print("sum of closing inr", closingNalanceInr)
        if closingNalanceUsd < 0:
            main.ledgerblance.lbClosingBalanceCreditUSD.setText(f"{abs(closingNalanceUsd)} USD")
            main.ledgerblance.lbClosingBalanceDebitUSD.setText(f"{0} USD")
        else:
            main.ledgerblance.lbClosingBalanceDebitUSD.setText(f"{abs(closingNalanceUsd)} USD")
            main.ledgerblance.lbClosingBalanceCreditUSD.setText(f"{0} USD")


    except:
        print(traceback.print_exc())

def totalClosingBalance(main):

    try:

        main.ledgerblance.lbClosingBalanceCreditUSD.clear()
        main.ledgerblance.lbClosingBalanceDebitUSD.clear()
        main.ledgerblance.lbClosingBalanceCreditINR.clear()
        main.ledgerblance.lbClosingBalanceDebitINR.clear()

        selected_account = main.ledgerblance.cbAccount.currentText()

        # Execute the SQL query based on the selected account name
        cursor = main.db_connection.cursor()
        cursor.execute("""
                    SELECT Debit, Credit , Currency
                    FROM Ledger_table
                    WHERE LedgerName = ? AND Perticulars = 'Closing Balance'
                    ORDER BY Date ASC;
                """, (selected_account,))
        ledger_data = cursor.fetchall()
        closing_credit_inr = ledger_data[0][1]
        closing_debit_inr = ledger_data[0][0]
        currency_inr = ledger_data[0][2]
        main.ledgerblance.lbClosingBalanceDebitINR.setText(f"{closing_debit_inr} {currency_inr}")
        main.ledgerblance.lbClosingBalanceCreditINR.setText(f"{closing_credit_inr} {currency_inr}")

        if len(ledger_data) >= 2:
            closing_debit_usd = ledger_data[1][0]

            closing_credit_usd = ledger_data[1][1]
            currency_usd = ledger_data[1][2]

            main.ledgerblance.lbClosingBalanceDebitUSD.setText(f"{closing_debit_usd} {currency_usd}")
            main.ledgerblance.lbClosingBalanceCreditUSD.setText(f"{closing_credit_usd} {currency_usd}")
        else:
            pass


    except:
        print(traceback.print_exc())
