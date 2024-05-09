"""Banking System

This script allows the user to carry out services provided by the bank.

This script requires modules 'exs_user_operations' and 'new_user_operations' to be present within the same directory
"""

import sys
try:    
    import exs_user_operations as eops
    import new_user_operations as nops
except ImportError:
    print("--SOME ERROR OCCURED.TERMINATING PROGRAM--")
    sys.exit(0)
else:
    print("Kerala Bank e-Service Portal\n============================")

    while True:
        print("\nSELECT AN OPTION FROM THE FOLLOWING MENU")
        print("CHOICE\t| OPTION\n----------------------")
        print("1\t| EXISTING CUSTOMER (LOGIN)")
        print("2\t| NEW CUSTOMER (CREATE ACCOUNT)")
        print("x\t| EXIT APPLICATION")
        choice=input("\nENTER YOUR CHOICE:").lower()
        if choice=='1':
            eops.login()
        elif choice=='2':
            nops.register()
        elif choice=='x':
            print('---Thank you for visiting Kerala Bank e-portal----')
            break
        else:
            print("Error: Invalid choice")
