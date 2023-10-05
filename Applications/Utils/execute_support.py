import os


# ---------------------------------------- Imports For Files -----------------------------#
from Applications.Utils.support import *
from Applications.Views.Login.login import LoginWindow



def initialObjects(main):
    # -------------------- Path of Database --------------------------#
    loc1 = os.getcwd().split('Application')
    db_path = os.path.join(loc1[0], 'Database', 'MBAS1.db')
    main.db_connection = sqlite3.connect(db_path)

    main.login = LoginWindow()  # Login Window

def initVariables(main):
    try:
        main.is_filtered = False
    except:
        print(traceback.print_exc())

def intialSlots(main):
    # ------------------------------- Main Window --------------#

    main.pbCreateCompany.clicked.connect(main.showCreateCompany)
    main.pbClose.clicked.connect(main.close)
    main.login.pbLogin.clicked.connect(lambda: loginFunction(main))










