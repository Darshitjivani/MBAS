import json
import sqlite3
import traceback
from functools import partial
from PyQt5.QtCore import Qt

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


    except:
        print(traceback.print_exc())



def createCompany(main):

    ''' Execute the Quary for create company and save the data into database.'''

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
        #     return
        # Check if any of the required fields are empty
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
                main.gateway.show()
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

                # print(company_name)
                # item = QListWidgetItem(company_name)
                # main.listWidget.addItem(item)
                #
                # # Attach additional data (company ID) to the item
                # item.setData(Qt.UserRole, company_id)

        #         company_button = QPushButton(company_name)
        #         company_button.setStyleSheet("color: white;")
        #         layout.addWidget(company_button)
        # #
        # #
        #
        #         company_button.clicked.connect(lambda _, name=company_name,id=company_id: gateway(main, name ,id))


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
    except:
        print(traceback.print_exc())

def masterList(main):
    ''' This Function will show the Master list window for creation of ledger, group etc.'''
    try:
        # main_window = main.show()
        main.gateway.hide()
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




def creategrouppage(main):
    ''' This Function will show the Window for Create Group.'''
    try:
        main.creategroup.show()
        comapny_id = main.companyID
        print(comapny_id)
        company_name = main.companyName
        main.creategroup.lbCompanyName.setText(f"Welcome to {company_name}")

        # Get the list of group roles and groups created by the company
        group_roles = getGroupRoles(main)
        # print("group roles ",group_roles)
        company_groups = getGroupsCreatedByCompany(main)

        # Combine group roles and company groups into a single list
        role_names = [role[1] for role in group_roles]
        group_names = [group[1] for group in company_groups]
        all_items = role_names + group_names

        # Clear existing items from the drop-down button
        main.creategroup.comboBox.clear()

        # Populate the drop-down button with group role names
        main.creategroup.comboBox.addItems(all_items)

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
        selected_role_index = main.creategroup.comboBox.currentIndex()
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
                main.creategroup.comboBox.setCurrentIndex(-1)

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
        main.createledger.lbCompanyName.setText(f"Welcome to {company_name}")

        # Get the list of group roles and groups created by the company
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
        main.createledger.cbUnderGroup.clear()

        # Populate the drop-down button with group role names
        main.createledger.cbUnderGroup.addItems(all_items)
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


def showAlterMasterPage(main):
    '''This Function will show master list window for Alteration.'''
    try:
        main.gateway.hide()
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



def alterLedgerListpage(main):
    ''' This function will show the all ledger list which is created by that perticular company.'''
    try:
        main.altermasterlist.hide()
        main.alterledgerlist.show()
        # user = main.userID  # Assuming you store the logged-in user ID in main.userID
        # print(user)  # user= nisha@gmail.com
        company_id = main.companyID
        print(company_id)
        command = ''' SELECT * FROM AccountMaster_table WHERE CompanyID = ? '''

        cursor = main.db_connection.cursor()
        try:
            cursor.execute(command, (company_id,))
            # print(user)
            ledger_data = cursor.fetchall()
            main.listWidget.clear()
            for ledger in ledger_data:
                ledger_name = ledger[2]
                print(ledger_name)
                ledger_id = ledger[0]

                item = QListWidgetItem()
                ledger_button = QPushButton(ledger_name)
                ledger_button.setStyleSheet("color: Black;")
                ledger_button.clicked.connect(lambda _, name=ledger_name, id=ledger_id: alterLedgerPage(main, name, id))
                # company_button.clicked.connect(lambda _, name=company_name, id=company_id: gateway(main, name, id))
                item.setSizeHint(ledger_button.sizeHint())  # Set the size of the item to match the button's size
                main.alterledgerlist.listWidget.addItem(item)
                main.alterledgerlist.listWidget.setItemWidget(item, ledger_button)

                # Attach additional data (company ID) to the item
                item.setData(Qt.UserRole, ledger_id)
        except sqlite3.Error as e:
            print("Error executing query:", e)
        cursor.close()

    except:
        print(traceback.print_exc())


def alterLedgerPage(main,ledger_name,ledger_id):
    ''' This function will load the data of ledger page.'''
    try:
        main.ledgerID = ledger_id
        print(ledger_id)
        main.ledgerName = ledger_name
        print(ledger_name)
        main.createledger.show()
        try:
            cursor = main.db_connection.cursor()
            query = '''SELECT * FROM AccountMaster_table WHERE AcMasterID = ?'''
            cursor.execute(query, (ledger_id,))
            ledger_data = cursor.fetchone()

            if ledger_data:
                # Populate the fields in the "Create Ledger" form with the retrieved data
                main.createledger.leAcName.setText(ledger_data[2])  # Assuming ledger name is at index 4
                main.createledger.leMailingName.setText(ledger_data[4])  # Assuming mailing name is at index 6
                # Set the selected role in the comboBox
                selected_role = ledger_data[3]  # Assuming group role is at index 3
                main.createledger.cbUnderGroup.setCurrentText(selected_role)
                # main.createledger.cbUnderGroup.setText(ledger_data[3])
                # main.createledger.leMailingName.text()
                main.createledger.ptAddress.setPlainText(ledger_data[5])
                #state = main.createledger.leAcName.text()
                main.createledger.leCountry.setText(ledger_data[7])
                main.createledger.lePincode.setText(str(ledger_data[8]))
                #  main.createledger.leAcName.text()
                main.createledger.leBalance.setText(ledger_data[10])



        except sqlite3.Error as e:
            print("Error fetching ledger data:", e)
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