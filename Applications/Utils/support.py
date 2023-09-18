import datetime
import json
import sqlite3
import traceback
import uuid
from functools import partial

import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from PyQt5.QtWidgets import *
from PyQt5.uic.properties import QtCore
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
from Applications.Views.TrialBalance.trial_balance import TrialBalanceWindow
from Applications.Views.Voucher.create_voucher import CreateVoucherWindow
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
    main.tableshow = Terminal()
    main.altergrouplist = AlterGroupListWindow()  # Group List Window For Alteration
    main.alterledger = AlterLedgerWindow()
    main.daybook = DayBookWindow()
    main.trialbalance = TrialBalanceWindow()



    ##################################### Gateway ###################################################

    main.gateway.fCreate.layout().addWidget(main.masterlist)
    main.gateway.fAlter.layout().addWidget(main.altermasterlist)
    main.gateway.fVouchers.layout().addWidget(main.createvoucher)
    main.gateway.fDayBook.layout().addWidget(main.daybook)
    # main.gateway.fBalanceSheet.layout().addWidget(main.masterlist)

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


#------------------------------------------- All Slots -----------------------------------------#
def allSlots(main):

    #-----------------------------------  Login Window ----------------------------------------------#

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
    # main.gateway.pbTrailBalance.clicked.connect(lambda: showTrialBalanceGroup(main))
    main.gateway.pbChangeCompany.clicked.connect(lambda: goToMainWindow(main))

    # -----------------------------------------------------------------------#
    main.gateway.pbCreateMaster.clicked.connect(main.gateway.showCreateFrame)
    main.gateway.pbAlterMaster.clicked.connect(main.gateway.showAlterFrame)
    main.gateway.pbDayBook.clicked.connect(main.gateway.showDayBookFrame)
    main.gateway.pbVouchers.clicked.connect(main.gateway.showVouchersFrame)
    main.gateway.pbBalanceSheet.clicked.connect(main.gateway.showBalanceSheetFrame)
    main.gateway.pbTrailBalance.clicked.connect(main.gateway.showTrialBalanceFrame)

    main.gateway.pbClose.clicked.connect(main.gateway.close)



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
    #####################################################################################
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
    main.createvoucher.pbAdd.clicked.connect(lambda: showTableView(main))
    main.createvoucher.pbBack.clicked.connect(main.createvoucher.hide)

    #----------------------------------- Table Window ---------------------------------------------#
    main.tableshow.pdAddRaw.clicked.connect(lambda: addRaw(main))

    #----------------------------------- Day Book Window ------------------------------------------#
    main.daybook.deDateEdit.dateChanged.connect(lambda: filterDataByDate(main))
    main.daybook.pbBack.clicked.connect(main.daybook.hide)

    # ------------------------------------- Trial Balance ------------------------------#
    main.trialbalance.pbBack.clicked.connect(main.trialbalance.hide)
    main.trialbalance.tableView.doubleClicked.connect(lambda:trialBalanceDoubleClicked(main))
    main.trialbalance.cbtrialbalance.activated.connect(lambda: trialBalanceComboBox(main))
    main.trialbalance.cbMonth.activated.connect(lambda: filterByMonth(main))
    # main.trialbalance.deFrom.dateChanged.connect(lambda: filterDataByMonth(main))



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

            # Insert data into the Company_table
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
                company_button.clicked.connect(lambda _, name=company_name,id=company_id: gateway(main, name ,id))


        except sqlite3.Error as e:
            print("Error executing query:", e)
        cursor.close()



    except:
        print(traceback.print_exc())


# ------------------------------------ For Gateway ---------------------------------------
def gateway(main, company_name, company_id):
    ''' This Function will show the Gatway Window.'''
    # try:
    #     # Clear the existing content of widget_2
    #     for i in reversed(range(main.widget_2.layout().count())):
    #         main.widget_2.layout().itemAt(i).widget().deleteLater()
    #
    #     # Create the content of the gateway window as widgets
    #     label = QLabel("Gateway Window Content for Company ID: " + str(company_id))
    #     back_button = QPushButton("Back to Company List")
    #     back_button.clicked.connect(lambda: listOfCompany(main))  # Go back to the company list
    #
    #     # Add the widgets to the layout
    #     main.widget_2.layout().addWidget(label)
    #     main.widget_2.layout().addWidget(back_button)
    #
    # except:
    #     print(traceback.print_exc())
    try:
        main.hide()
        main.gateway.showMaximized()
        # main.showMaximized()
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
        # main_window = main.show()
        # main.gateway.hide()
        main.masterlist.show()
        comapny_id = main.companyID
        company_name = main.companyName
        # main.masterlist.lbCompanyName.setText(f"Welcome to {company_name}")

        # def goToMainWindow():
        #     main.masterlist.hide()  # Hide the masterlist window
        #     main.show()  # Show the main window
        #
        # main.masterlist.pbChangeCompany.clicked.connect(goToMainWindow)
        # main.masterlist.pbChangeCompany.clicked.connect(main_window)

        # main.gateway.updateTitleLabel(comapny_id[1])

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

        # def goToMainWindow():
        #     main.altermasterlist.hide()  # Hide the masterlist window
        #     main.show()  # Show the main window

        # main.altermasterlist.pbChangeCompany.clicked.connect(goToMainWindow)
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
        # main.creategroup.lbCompanyName.setText(f"Welcome to {company_name}")

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

       # Connect the submit button's clicked signal to a function

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

        # Find the index of the selected branch name in the branch_name list
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
            command = ''' SELECT * FROM AccountMaster_table WHERE CompanyID = ? '''
            cursor = main.db_connection.cursor()

            try:
                cursor.execute(command, (company_id,))
                ledger_data = cursor.fetchall()
                main.listWidget.clear()

                for ledger in ledger_data:
                    ledger_name = ledger[2]
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
    '''This Function will execute the Query to save the data of ledger into database.'''
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
            else:
                insert_query = '''INSERT INTO AccountMaster_table (CompanyID,Ac_name,Under_groupName, Mailing_name,Address
                                ,Country,Pincode,Balance)
                                          VALUES (?,?,?,?,?,?,?,?)'''
                values = (main.companyID,name,selected_role,mailing_name,address,country,pincode,balance)
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
                branch_data = cursor.fetchall()
                main.alterbranchlist.listWidget.clear()
                for branch in branch_data:
                    branch_name = branch[2]
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
        main.branchID = branch_id
        main.branchName = branch_name

        # main.createledger.show()
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
def showVoucherPage(main):
    try:
        company_id = main.companyID

        main.createvoucher.show()
        company_name = main.companyName

        voucher_type = getVoucherType(main)
        account = getAccountMaster(main)

        # Combine group roles and company groups into a single list
        role_names = [role[1] for role in voucher_type]
        account_name = [name[2] for name in account]
        # group_names = [group[1] for group in company_groups]
        # all_items = role_names + group_names

        main.account = account

        # Clear existing items from the drop-down button
        main.createvoucher.cbVoucherType.clear()
        main.createvoucher.cbDebitedAccount.clear()

        # Populate the drop-down button with group role names
        main.createvoucher.cbVoucherType.addItems(role_names)
        main.createvoucher.cbDebitedAccount.addItems(account_name)

        main.tableshow.cbAccountName.addItems(account_name)

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

def saveVoucherData(main):
    try:
        try:
            company_id = main.companyID
            voucher_type = main.createvoucher.cbVoucherType.currentText()
            debit_account = main.createvoucher.cbDebitedAccount.currentText()
            narration = main.createvoucher.leNarration.text()
            date = main.createvoucher.deDate.text()
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
            print("selecetd account index:", selected_account_index)
            if selected_account_index is None:
                print("Selected branch not found in the branchs list.")
                return
            try:
                # Insert a new voucher record and store the data table ID
                cursor = main.db_connection.cursor()
                cursor.execute(
                    "INSERT INTO voucher_table (CompanyID,AccountMasterID, VoucherType, DebitAccount,Date, Narration, DebitAmount, CreditAmount , DataTableID) "
                    "VALUES (?, ?, ?, ?, ?, ?,?,?,?)", (
                    company_id, selected_account_index, voucher_type, debit_account, date, narration, debit_amount,
                    credit_amount, data_table_id))
                main.db_connection.commit()

                # Insert data from main.createvoucher.table into the data table
                for row in main.createvoucher.table[:main.createvoucher.last_serialno]:
                    cursor.execute(
                        f"INSERT INTO Data_table (Type, Perticular,CreditAmount,DebitAmount, Currency, VoucherID) VALUES (?,?, ?,?, ?, ?)",
                        (row[0],row[1],row[2],row[3],row[4],data_table_id))
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

                    main.createvoucher.close()
                    # main.gateway.updateTitleLabel(company_ name)


                else:

                    # User chose not to continue, clear the company creation UI

                    main.createvoucher.clearFields()

            except sqlite3.Error as e:
                print("Error fetchig branch:", e)


            main.tableshow.cbAccountName.clear()
            # main.tableview.cbDrCr.clear()
            main.tableshow.leAmount.clear()
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


def showTableView(main):
    try:
        main.tableshow.show()
        # account = getAccountMaster(main)
        # account_name = [name[2] for name in account]
        # main.tableshow.cbAccountName.addItems(account_name)

    except:
        print(traceback.print_exc())


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


        # Determine the column to update based on "Cr/Dr" selection
        if dr_cr == "Cr":
            indexlist=[0,1,3,4]
            # column_index = 2  # Credit Amount Column
        elif dr_cr == "Dr":
            indexlist = [0, 1, 2, 4]
            # column_index = 3  # Debit Amount Column
        else:
            return  # Invalid selection


        # Update the table with the values
        main.createvoucher.table[main.createvoucher.last_serialno,indexlist] = [dr_cr, account_name, amount,currency ]

        # Increment the last_serialno
        main.createvoucher.last_serialno += 1
        main.createvoucher.model.last_serialno += 1
        main.createvoucher.model.insertRows()
        main.createvoucher.model.rowCount() # print(main.createvoucher.model.rowCount())
        ind = main.createvoucher.model.index(0, 0)
        ind1 = main.createvoucher.model.index(0, 1)
        main.createvoucher.model.dataChanged.emit(ind, ind1)

        print(main.createvoucher.table[:main.createvoucher.last_serialno],type(main.createvoucher.table[:main.createvoucher.last_serialno]))
        debitSum = main.createvoucher.table[:main.createvoucher.last_serialno,2].sum()
        main.createvoucher.lbDebit.setText(str(debitSum))

        creditSum = main.createvoucher.table[:main.createvoucher.last_serialno,3].sum()
        main.createvoucher.lbCredit.setText(str(creditSum))

# ------------------------------------------------------------------------------------------------------

        new_currency = main.tableshow.cbCurrency.currentText()

        # Replace lbCurrency with the new currency
        main.createvoucher.lbCurrency.setText(new_currency)



        ############### Clear the input widgets after adding data#################
        main.tableshow.cbAccountName.setCurrentIndex(0)
        main.tableshow.cbDrCr.setCurrentIndex(0)
        main.tableshow.leAmount.clear()
        # main.tableshow.cbCurrency.setCurrentIndex(0)
        main.tableshow.hide()

    except:
        print(traceback.print_exc())


# ------------------------------------ For Day Book ---------------------------------------
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
        main.selectdate = selectedTextDate

        # Set the filter string to match the selected date
        main.daybook.smodel.setFilterFixedString(main.selectdate)
        print("day book data", main.daybook.smodel.setFilterFixedString(main.selectdate))
        # Notify the view to update
        # main.daybook.smodel.invalidateFilter()

    except:
        print(traceback.print_exc())



# ------------------------------------ For Trial Balance ---------------------------------------


def fetchTrialBalanceData(main):
    try:
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
                        
                    GROUP BY
                        AccountMaster_table.AcMasterID,
                        AccountMaster_table.Ac_name
                    """
        cursor.execute(command, (main.companyID,))

        data = cursor.fetchall()

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

        # Update the lbCredit and lbDebit QLable widgets with the calculated sums
        main.trialbalance.lbdebitINR.setText(str(total_debit))
        main.trialbalance.lbcreditINR.setText(str(total_credit))

        # main.trialbalance.lbdebitINR.setText(f"{total_debit} INR")
        # main.trialbalance.lbcreditINR.setText(f"{total_credit} INR")


    except:
        print(traceback.print_exc())


def showTrialBalance(main):
    try:

        main.trialbalance.show()
        fetchTrialBalanceData(main)

    except:
        print(traceback.print_exc())


def filterByMonth(main):
    try:
        selcted_item = main.trialbalance.cbMonth.currentText()
        print(selcted_item)
        # start_month_number = datetime.datetime.strptime(selcted_item, '%B').month
        # print(start_month_number)
        main.trialbalance.smodel.setFilterFixedString(selcted_item)

    except:
        print(traceback.print_exc())





# def filterDataByMonth(main):
#     try:
#         fromDate = main.trialbalance.deFrom.date()
# #         toDate = main.trialbalance.deTo.date()
# #
# #         # Convert the selectedDate to a string in the required format
#         fromTextDate = fromDate.toString("dd-MM-yyyy")
#         # print("852",fromTextDate)
#         main.fromDate = fromTextDate
# #         toTextDate = toDate.toString("dd-MM-yyyy")
# #         # print("963", toTextDate)
# #         main.toDate = toTextDate
# #
# #         # Set the filter string to match the selected date
#         main.trialbalance.smodel.setFilterFixedString(main.fromDate)
#         print("trial balance23", main.trialbalance.smodel.setFilterFixedString(main.fromDate))
# #
# #         main.trialbalance.smodel.setFilterFixedString(main.toDate)
# #         print("trial balance09", main.trialbalance.smodel.setFilterFixedString(main.toDate))
# #
#     except:
#         print(traceback.print_exc())


def fetchTrialBalanceGroup(main):
    try:
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
                    GROUP BY 
                        AccountMaster_table.Under_groupname
                """
        cursor.execute(command, (main.companyID,))
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


def fetchTrialBalanceBranch(main):
    try:
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
                    GROUP BY 
                        AccountMaster_table.under_branchname
                 """
        cursor.execute(command, (main.companyID,))
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
        if selcted_item ==("Ledger-Wise"):
            fetchTrialBalanceData(main)
        elif selcted_item ==("Group-Wise"):
            fetchTrialBalanceGroup(main)
        else:
            fetchTrialBalanceBranch(main)

    except:
        print(traceback.print_exc())


def trialBalanceDoubleClicked(main):
    try:

        idy = main.trialbalance.cbtrialbalance.currentText()

        if idy=="Ledger-Wise":
            cursor = main.db_connection.cursor()
            cursor.execute("SELECT Date, DebitAccount, VoucherType,DebitAmount,CreditAmount FROM Voucher_table")
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

