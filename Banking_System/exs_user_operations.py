"""Existing User Operations

This script allows the user to perform operations permitted by the bank on opened accounts

This script requires modules 'account_info_manager' and 'data_validation' to be present within the same directory

This file can be imported as a module and contains the following functions:
    *login - authenticate and authorize user to perform further account related operations 
    *show_services - allows user to select from list of account related operations
    *check balance - allows user to check account balance
    *deposit - allows user to deposit an amount to the account
    *withdrawal - allows user to withdraw an amount from the account, if possible
"""

import sys
try:
	import account_info_manager as aim
	import data_validation as dv
except ImportError:
	print("--SOME ERROR OCCURED.TERMINATING PROGRAM--")
	sys.exit(0)
else:
	acc_manager=aim.AccountManager()
	accounts=acc_manager.get_acc_list()
	logged_account=None

	def check_balance() -> None:
		global logged_account
		print(f'Account No.: xxxxxx{logged_account.acc_no[-4:]}\nBalance:{logged_account.balance}')

	def deposit() -> None:
		amt=dv.validate_amt()
		global logged_account
		logged_account.balance=str(int(logged_account.balance)+int(amt))
		print("Deposit successful")
		print(f'Account No.: xxxxxx{logged_account.acc_no[-4:]}\nBalance:{logged_account.balance}')
		acc_manager.update_acc_list(logged_account)

	def withdrawal() -> None:
		amt=dv.validate_amt()
		global logged_account
		if logged_account.balance<amt:
			print("Insufficient Balance. Cannot perform withdrawal.")
		else:
			logged_account.balance=str(int(logged_account.balance)-int(amt))
			print("Withdrawal successful")
			print(f'Account No.: xxxxxx{logged_account.acc_no[-4:]}\nBalance:{logged_account.balance}')
			acc_manager.update_acc_list(logged_account)

	def login() -> None:
		acno=dv.validate_acno()
		pin=dv.validate_pin()
		for account in accounts:
			if account.acc_no==acno and account.pin==pin:
				global logged_account
				logged_account=account
				break

		if logged_account:
			print(f'\nWelcome {logged_account.cust_name}')
			show_services()
		else:
			print('\nError: Incorrect account number or PIN')


	def show_services() -> None:
		global logged_account
		while logged_account:
			print("\nSELECT AN OPTION FROM THE FOLLOWING MENU")
			print("CHOICE\t| OPTION\n----------------------")
			print("1\t| CHECK BALANCE")
			print("2\t| CASH DEPOSIT")
			print("3\t| CASH WITHDRAWAL")
			print("x\t| LOGOUT")
			choice=input("\nENTER YOUR CHOICE:").lower()

			if choice=='1':
				check_balance()
			elif choice=='2':
				deposit()
			elif choice=='3':
				withdrawal()
			elif choice=='x':
				print("----Logging out----")
				logged_account=None
				return
			else:
				print("Invalid Choice.")

if __name__=='__main__':
    print("--ACCESS RESTRICTED--")