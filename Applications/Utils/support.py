import json
import sqlite3
import traceback
from functools import partial
from PyQt5.QtCore import *

from PyQt5.QtWidgets import *




def loginFunction(main):

    ''' It will Login through Username and Password and redirect to main Window.'''

    try:
        # print('login')
        user = main.login.leUserName.text()
        # print('user',user)
        password = main.login.lePassword.text()
        # print('password',password)

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
            main.show()
            print('Login Successful')
        else:
            print('Please check your Userid or password')

    except:
        print(traceback.print_exc())



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
                company_button.setStyleSheet("color: white;")
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
        # comapny_id = main.comapnyID
        # print(company_name)
        main.gateway.show()
        main.companyID = company_id
        main.companyName = company_name
        print(main.companyID)

        main.gateway.updateTitleLabel(company_name)



        def goToMainWindow():
            main.gateway.hide()  # Hide the gateway window
            main.show()  # Show the main window

        main.gateway.pbChangeCompany.clicked.connect(goToMainWindow)

    except:
        print(traceback.print_exc())


def masterList(main):
    ''' This Function will show the Master list window for creation of ledger, group etc.'''
    try:
        # main_window = main.show()
        # main.gateway.hide()
        main.masterlist.show()
        comapny_id = main.companyID
        company_name = main.companyName
        main.masterlist.lbCompanyName.setText(f"Welcome to {company_name}")

        def goToMainWindow():
            main.masterlist.hide()  # Hide the masterlist window
            main.show()  # Show the main window

        main.masterlist.pbChangeCompany.clicked.connect(goToMainWindow)
        # main.masterlist.pbChangeCompany.clicked.connect(main_window)

        # main.gateway.updateTitleLabel(comapny_id[1])

    except:
        print(traceback.print_exc())


def getGroupRoles(main):

    ''' This function will execute the query to get the group roles from Group role.'''
    try:
        cursor = main.db_connection.cursor()
        query = '''SELECT Group_roleID, Role_name FROM Group_role'''
        cursor.execute(query)
        groups = cursor.fetchall()
        print("groups:", groups)
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


def getBranch(main):

    ''' This function will execute the query to get the group roles from Group role.'''
    try:
        company_id = main.companyID
        cursor = main.db_connection.cursor()
        query = '''SELECT BranchID,Owner_name FROM Branch_table WHERE CompanyID = ?'''
        cursor.execute(query, (company_id,))
        branch = cursor.fetchall()
        print("groups:", branch)
        cursor.close()
        return branch
    except sqlite3.Error as e:
        print("Error fetching branch:", e)
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
    alterLedgerListpage(main)



def showAlterMasterPage(main):
    '''This Function will show master list window for Alteration.'''
    try:

        # main.gateway.hide()
        main.altermasterlist.show()
        comapny_id = main.companyID
        company_name = main.companyName
        # print(company_name)
        main.altermasterlist.lbCompanyName.setText(f"Welcome to {company_name}")
        # Get the list of group roles and groups created by the company
        group_roles = getGroupRoles(main)
        # print("group roles ", group_roles)
        company_groups = getGroupsCreatedByCompany(main)
        # print("company roles", company_groups)

        # Combine group roles and company groups into a single list
        role_names = [role[1] for role in group_roles]
        group_names = [group[1] for group in company_groups]
        all_items = role_names + group_names

        # Clear existing items from the drop-down button
        main.createledger.cbUnderGroup.clear()

        # Populate the drop-down button with group role names
        main.createledger.cbUnderGroup.addItems(all_items)

        def goToMainWindow():
            main.altermasterlist.hide()  # Hide the masterlist window
            main.show()  # Show the main window

        main.altermasterlist.pbChangeCompany.clicked.connect(goToMainWindow)
    except:
        print(traceback.print_exc())



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
                    ledger_button.setStyleSheet("color: Black;")
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
            # print("company roles", company_groups)

            # Combine group roles and company groups into a single list
            role_names = [role[1] for role in group_roles]
            group_names = [group[1] for group in company_groups]
            all_items = role_names + group_names
            # print(all_items)

            # Clear existing items from the drop-down button
            main.alterledger.cbUnderGroup.clear()

            # Populate the drop-down button with group role names
            main.alterledger.cbUnderGroup.addItems(all_items)

            if ledger_data:
                # Populate the fields in the "Create Ledger" form with the retrieved data
                main.alterledger.leAcName.setText(ledger_data[2])  # Assuming ledger name is at index 4
                main.alterledger.leMailingName.setText(ledger_data[4])  # Assuming mailing name is at index 6
                # Set the selected role in the comboBox
                selected_role = ledger_data[3]# Assuming group role is at index 3
                print("selected_role",selected_role)

                # main.alterledger.cbUnderGroup.addItem(selected_role)
                main.alterledger.cbUnderGroup.setCurrentText(selected_role)
                # main.createledger.cbUnderGroup.setText(ledger_data[3])
                # main.createledger.leMailingName.text()
                main.alterledger.ptAddress.setPlainText(ledger_data[5])
                #state = main.createledger.leAcName.text()
                main.alterledger.leCountry.setText(ledger_data[7])
                main.alterledger.lePincode.setText(str(ledger_data[8]))
                #  main.createledger.leAcName.text()
                main.alterledger.leBalance.setText(str(ledger_data[10]))

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


def alterGroupListpage(main):

    try:
        main.altergrouplist.show()
    except:
        print(traceback.print_exc())


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




def createBranchpage(main):
    try:
        main.createbranch.show()
        comapny_id = main.companyID
        print(comapny_id)
        company_name = main.companyName
        main.createbranch.lbCompanyName.setText(f"Welcome to {company_name}")
    except:
        print(traceback.print_exc())

def saveBranchData(main):
    try:
        name = main.createbranch.leOwnerName.text()
        print(name)
        # company_name = main.createbranch.leCompanyName.text()
        cursor = main.db_connection.cursor()
        try:
            insert_query = '''INSERT INTO Branch_table (CompanyID,Owner_name)
                                                      VALUES (?,?)'''
            values = (main.companyID, name)
            print("vaues:", values)
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

                # User chose to continue, show the gateway window

                # main.gateway(main, company_name)

                main.createbranch.close()
                # main.alterledgerlist.hide()
                # main.masterlist.show()

                # main.gateway.updateTitleLabel(company_ name)


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
        ############################### hide master list ############################
        main.altermasterlist.hide()
        company_id = main.companyID
        print(company_id)
        # main.alterledgerlist.show()

        # user = main.userID  # Assuming you store the logged-in user ID in main.userID
        # print(user)  # user= nisha@gmail.com
        if  not main.alterledgerlist.isVisible():
            main.alterledgerlist.show()

            command = ''' SELECT * FROM Branch_table WHERE CompanyID = ? '''

            cursor = main.db_connection.cursor()
            try:
                cursor.execute(command, (company_id,))
                # print(user)
                branch_data = cursor.fetchall()
                main.listWidget.clear()
                for branch in branch_data:
                    branch_name = branch[2]
                    print(branch_name)
                    branch_id = branch[1]

                    item = QListWidgetItem()
                    branch_button = QPushButton(branch_name)
                    branch_button.setStyleSheet("color: Black;")
                    branch_button.clicked.connect(lambda _, name=branch_name, id=branch_id: branchPageList(main, name, id))
                    # company_button.clicked.connect(lambda _, name=company_name, id=company_id: gateway(main, name, id))
                    item.setSizeHint(branch_button.sizeHint())  # Set the size of the item to match the button's size
                    main.alterledgerlist.listWidget.addItem(item)
                    main.alterledgerlist.listWidget.setItemWidget(item, branch_button)

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
                print("Branch Id:",branch_id)

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
                item = QListWidgetItem()
                branch_combo = QComboBox()
                branch_combo.addItem(branch_name)
                # You can add more items to the combo box if needed

                item.setSizeHint(branch_combo.sizeHint())  # Set the size of the item to match the combo box's size
                main.alterledgerlist.listWidget.addItem(item)
                main.alterledgerlist.listWidget.setItemWidget(item, branch_combo)



                # Attach additional data (company ID) to the item
                item.setData(Qt.UserRole, branch_id)
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

#
# def createComboBoxDelegate(parent):
#     combo_box = QComboBox(parent)
#     combo_box.addItems(['cell11', 'cell12', 'cell13', 'cell14', 'cell15'])
#
#     delegate = QStyledItemDelegate()
#     delegate.setItemEditorFactory(lambda parent, option, index: combo_box)
#
#     return delegate

def showVoucherPage(main):
    try:
        # accountNamesReady = pyqtSignal(list)  # Define a signal
        company_id = main.companyID

        main.createvoucher.show()
        company_name = main.companyName
        main.createvoucher.lbCompanyName.setText(f"Welcome to {company_name}")

        voucher_type = getVoucherType(main)
        account = getAccountMaster(main)
        print(account)
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

def saveVoucherData(main,data):
    print("hello voucher")
    print(data)
    try:
        try:

            company_id = main.companyID
            voucher_type = main.createvoucher.cbVoucherType.currentText()
            debit_account = main.createvoucher.cbDebitedAccount.currentText()
            narration = main.createvoucher.leNarration.text()
            date = main.createvoucher.leDate.text()
            # You can retrieve other data as needed from voucher window widgets

            cursor = main.db_connection.cursor()

            # Insert voucher data into the database
            cursor.execute("INSERT INTO voucher_table (CompanyID, VoucherType, DebitAccount, Narration, Date) "
                           "VALUES (?, ?, ?, ?, ?)", (company_id, voucher_type, debit_account, narration, date))

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

        # print(account_name)
        # main.tableview.cbAccountName.clear()
        user_id = main.tableview.line1.text()
        print(user_id)
        perticular = main.tableview.line3.text()
        # perticular = main.tableview.cbAccountName.currentText()
        # print(perticular)
        debit = main.tableview.line3.text()
        credit = main.tableview.line4.text()

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
        main.tableview.line1.clear()
        main.tableview.line2.clear()
        main.tableview.line3.clear()
        main.tableview.line4.clear()
    except:
        print(traceback.print_exc())

