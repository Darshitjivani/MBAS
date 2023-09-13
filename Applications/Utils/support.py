import json
import sqlite3
import traceback
from functools import partial
from PyQt5.QtCore import *

from PyQt5.QtWidgets import *

from Applications.Views.Branch.alter_branch_list import AlterBranchListWindow
from Applications.Views.Branch.create_branch import BranchCreateWindow
from Applications.Views.CompanyCreate.company_create import CompanyCreateWindow
from Applications.Views.CreateGroup.alter_group_list import AlterGroupListWindow
from Applications.Views.CreateGroup.create_group import CreateGroupWindow
from Applications.Views.DayBook.create_daybook import DayBookWindow
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


def allObjects(main):
    main.gateway = GatewaysWindow()  # Gateway Window
    main.companycreate = CompanyCreateWindow()  # Create Company Window
    main.home = HomeWindow() # Homewindow
    main.masterlist = MasterListWindow()  # MaterList Window
    main.creategroup = CreateGroupWindow()  # Create group Window
    main.createledger = CreateLedgerWindow()  # Create Ledger Window
    main.altermasterlist = AlterMasterListWindow()  # Master List window For Alteration
    main.alterledgerlist = AlterLedgerListWindow() # Ledger List Window For Alteration
    main.createbranch = BranchCreateWindow() # Branch List Window For Alteration
    main.createvoucher  = CreateVoucherWindow()  # Create Voucher Window
    main.alterbranchlist = AlterBranchListWindow()  #Ledger list Branch wise for Alteration
    main.tableview = Terminal()
    main.altergrouplist = AlterGroupListWindow()  # Group List Window For Alteration
    main.alterledger = AlterLedgerWindow()
    main.trialbalance = TrialBalanceWindow()
    main.daybook = DayBookWindow()


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


def allSlots(main):
    #-----------------------  Login Window ----------------------------------------------#


    # main.creategroup.pbCreate
    # ------------------------------- Create Company Window --------------------------#
    main.companycreate.pbSubmit.clicked.connect(lambda: createCompany(main))
    main.companycreate.pbSubmit.clicked.connect(main.companycreate.hide)
    main.companycreate.pbClose.clicked.connect(main.companycreate.hide)

    main.pbCreateCompany.clicked.connect(main.companycreate.show)
    # main.pbCreateCompany.clicked.connect(main.companycreate.showCreateCompany)

    # Connect the "Add" button to the clear function
    main.pbCreateCompany.clicked.connect(lambda: clearCompanyCreateFields(main))



    #-------------------------------- Gateway Window -------------------------------#
    main.gateway.pbCreateMaster.clicked.connect(lambda: masterList(main))
    main.gateway.pbAlterMaster.clicked.connect(lambda: showAlterMasterPage(main))
    main.gateway.pbVouchers.clicked.connect(lambda: showVoucherPage(main))

    # -------------------------------- Gateway Window -------------------------------#
    # main.gateway.pbCreateMaster.clicked.connect(lambda: masterList(main))
    # main.gateway.pbAlterMaster.clicked.connect(lambda: showAlterMasterPage(main))
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
    main.masterlist.pbBack.clicked.connect(main.masterlist.hide)


    main.masterlist.pbCreateGroup.clicked.connect(main.masterlist.showCreateGroup)
    main.masterlist.pbCreateBranch.clicked.connect(main.masterlist.showCreateBranch)
    main.masterlist.pdCreateLedger.clicked.connect(main.masterlist.showCreateLadger)

    # main.masterlist.pbChangeCompany.clicked.connect(main.home.show())
    # main.masterlist.pbClose.clicked.connect(main.masterlist.hide)
    # main.masterlist.pbChangeCompany.clicked.connect(main.show)

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
    main.alterledger.pbSubmit.clicked.connect(lambda:saveAlterLedgerData(main))
    # main.alterledger.pbSubmit.clicked.connect(main.alterledgerlist.hide)


    main.alterledger.pbDelete.clicked.connect(lambda: deleteLedger(main))
    main.alterledger.pbClose.clicked.connect(main.alterledger.close)


    #-------------------------Alter Branch Window----------------------------------------#


    main.alterbranchlist.pbClose.clicked.connect(main.alterbranchlist.close)

    #------------------------------------- Create Voucher Window -------------------------------#
    main.createvoucher.pbSubmit.clicked.connect(lambda: saveVoucherData(main))
    main.createvoucher.pbAdd.clicked.connect(lambda: showTableView(main))
    main.createvoucher.pbBack.clicked.connect(main.createvoucher.hide)


    #----------------------------------- Table Window ---------------------------------------------#
    main.tableview.pdAddRaw.clicked.connect(lambda: addRaw(main))

    #----------------------------------- Day Book -------------------------------------#
    # main.gateway.pbDayBook.clicked.connect(main.gateway.showDayBookFrame)
    main.daybook.pbBack.clicked.connect(main.daybook.hide)

    main.trialbalance.pbBack.clicked.connect(main.trialbalance.hide)


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

            # print(main.userID, company_name, mailing_name, address, state, country, pincode, mobile, fax,
            #           email, website, currency_symbol, formal_name_currency, fy_date, book_date)
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
    try:
        main.hide()
        # comapny_id = main.comapnyID
        main.gateway.showMaximized()
        # main.showMaximized()
        main.companyID = company_id
        main.companyName = company_name

        main.gateway.updateTitleLabel(company_name)



        def goToMainWindow():
            main.gateway.hide()  # Hide the gateway window
            main.show()  # Show the main window

        main.gateway.pbChangeCompany.clicked.connect(goToMainWindow)

    except:
        print(traceback.print_exc())


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
    # alterGroupListpage(main)


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
                    group_button.setStyleSheet("QPushButton {"
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
                    group_button.clicked.connect(
                        lambda _, name=group_name, id=group_id: alterLedgerPage(main, name, id))
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
        # main.createledger.lbCompanyName.setText(f"Welcome to {company_name}")

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
    # alterLedgerListpage(main)


def saveledger(main):
    '''This Function will execute the Query to save the data of ledger into database.'''
    try:
        name = main.createledger.leAcName.text()
        mailing_name = main.createledger.leMailingName.text()
        address = main.createledger.ptAddress.toPlainText()
        # state = main.createledger.leAcName.text()
        country = main.createledger.leCountry.text()
        pincode = main.createledger.lePincode.text()
        # date = main.createledger.leAcName.text()
        balance = main.createledger.leBalance.text()


        selected_role = main.createledger.cbUnderGroup.currentText()
        # selected_branch_index = main.createledger.cbUnderBranch.currentText()
        selected_branch_text = main.createledger.cbUnderBranch.currentText()
        # Find the index of the selected branch name in the branch_name list
        # selected_branch_index = branch_name.index(selected_branch_text)
        selected_branch_index = None
        for branch in main.branches:
            if branch[1] == selected_branch_text:
                selected_branch_index = branch[0]
                break
        if selected_branch_index is None:
            print("Selected branch not found in the branchs list.")
            return

        # Get the list of group roles
        # group_roles = getGroupRoles(main)
        #
        # if selected_role_index >= 0 and selected_role_index < len(group_roles):
        #     selected_group_role_id = group_roles[selected_role_index][0]

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
                # main.createledger.clearFields()
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
                    ledger_button.setStyleSheet("QPushButton {"
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
                                      # "background: #1464A0;"
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
        mailing_name = main.alterledger.leMailingName.text()
        address = main.alterledger.ptAddress.toPlainText()
        # state = main.alterledger.leAcName.text()
        country = main.alterledger.leCountry.text()
        pincode = main.alterledger.lePincode.text()
        # date = main.alterledger.leAcName.text()
        balance = main.alterledger.leBalance.text()


        selected_role = main.alterledger.cbUnderGroup.currentText()
        # Get the list of group roles
        group_roles = getGroupRoles(main)
        #
        # if selected_role_index >= 0 and selected_role_index < len(group_roles):
        #     selected_group_role_id = group_roles[selected_role_index][0]

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
                branch_data = cursor.fetchall()
                main.alterbranchlist.listWidget.clear()
                for branch in branch_data:
                    branch_name = branch[2]
                    branch_id = branch[1]

                    item = QListWidgetItem()
                    branch_button = QPushButton(branch_name)

                    branch_button.setStyleSheet("QPushButton {"
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
                                                 # "background: #1464A0;"
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

                # branch_combo = QComboBox()  # Create a QComboBox for each branch
                # item = QListWidgetItem()

                # Create a QPushButton for the branch item and set it as a delegate
                # delegate_button = QPushButton(branch_name)
                # delegate_button.setStyleSheet("color: Black;")
                # branch_combo.addItem("")
                # branch_combo.setItemDelegate(ButtonDelegate(delegate_button))  # Set custom delegate
                #
                # item.setSizeHint(branch_combo.sizeHint())  # Set the size of the item to match the combo box's size
                # main.alterledgerlist.listWidget.addItem(item)
                # main.alterledgerlist.listWidget.setItemWidget(item, branch_combo)
                # #


                # item = QListWidgetItem()
                # branch_combo = QComboBox()
                # branch_combo.addItem(branch_name)
                # # You can add more items to the combo box if needed
                #
                # item.setSizeHint(branch_combo.sizeHint())  # Set the size of the item to match the combo box's size
                # main.alterbranchlist.listWidget.addItem(item)
                # main.alterbranchlist.listWidget.setItemWidget(item, branch_combo)
                #
                #
                #
                # # Attach additional data (company ID) to the item
                # item.setData(Qt.UserRole, branch_id)

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

        # Clear existing items from the drop-down button
        main.createvoucher.cbVoucherType.clear()
        main.createvoucher.cbDebitedAccount.clear()
        # main.createvoucher.cbCreditedAccount.clear()
        # main.createvoucher.cbAccountName.clear()
        main.createvoucher.tableWidget.setColumnCount(4)  # Assuming you have 4 columns
        main.createvoucher.tableWidget.setHorizontalHeaderLabels(["UserID", "Perticular", "Debit", "Credit"])

        # Connect the custom signal to the ComboBoxDelegate's updateComboBox method
        # main.createvoucher.accountNamesReady.connect(main.combo_delegate.updateComboBox)
        # main.createvoucher.accountNamesReady.emit(account_name)

        # Populate the drop-down button with group role names
        main.createvoucher.cbVoucherType.addItems(role_names)
        main.createvoucher.cbDebitedAccount.addItems(account_name)
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
            # date = main.createvoucher.leDate.text()
            # You can retrieve other data as needed from voucher window widgets

            cursor = main.db_connection.cursor()

            # Insert voucher data into the database
            cursor.execute("INSERT INTO voucher_table (CompanyID, VoucherType, DebitAccount, Narration) "
                           "VALUES (?, ?, ?, ?)", (company_id, voucher_type, debit_account, narration))

            main.db_connection.commit()
            cursor.close()
        except sqlite3.Error as e:
            print("Error fetchig branch:", e)
            # return []


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
        main.tableview.show()
        account = getAccountMaster(main)
        # account_name = [name[2] for name in account]
        # main.createvoucher.cbVoucherType.clear()
        # main.tableview.cbAccountName.addItems(account_name)

    except:
        print(traceback.print_exc())


def addRaw(main):
    try:
        company_id = main.companyID

        # main.tableview.cbAccountName.clear()
        user_id = main.tableview.leUserid.text()
        perticular = main.tableview.lePerticular.text()
        # perticular = main.tableview.cbAccountName.currentText()
        debit = main.tableview.leDebit.text()
        credit = main.tableview.leCredit.text()

        # Create a new row in the QTableWidget
        current_row = main.createvoucher.tableWidget.rowCount()
        main.createvoucher.tableWidget.insertRow(current_row)

        # Populate the new row with the data
        main.createvoucher.tableWidget.setItem(current_row, 0, QTableWidgetItem(user_id))
        main.createvoucher.tableWidget.setItem(current_row, 1, QTableWidgetItem(perticular))
        main.createvoucher.tableWidget.setItem(current_row, 2, QTableWidgetItem(debit))
        main.createvoucher.tableWidget.setItem(current_row, 3, QTableWidgetItem(credit))
        cursor = main.db_connection.cursor()


        cursor.execute("INSERT INTO data_table (Type, Perticular, Debit, Credit) VALUES (?, ?, ?, ?)",
                       (user_id, perticular, debit, credit))
        main.db_connection.commit()
        cursor.close()

        # Clear the QLineEdit widgets for the next entry
        main.tableview.leUserid.clear()
        main.tableview.lePerticular.clear()
        main.tableview.leDebit.clear()
        main.tableview.leCredit.clear()
    except:
        print(traceback.print_exc())

