"""New User Operations

This script allows the user to open a new account in the bank

This script requires modules 'account_info_manager' and 'data_validation' to be present within the same directory

This file can be imported as a module and contains the following function:
    *register - accepts details to open a new account and updates the same in the accounts information file
"""

import sys
try:
	import re
	import account_info_manager as aim
	import data_validation as dv
except ImportError:
	print("--SOME ERROR OCCURED.TERMINATING PROGRAM--")
	sys.exit(0)
else:
	def register():
		print("Enter your details to create new account")
		acc_manager=aim.AccountManager()
		accounts=acc_manager.get_acc_list()

		acc_nos=[]
		for account in accounts:
			acc_nos.append(account.acc_no)
		acc_nos.sort()

		acc_no='\n'+str(int(acc_nos[-1])+1)
		cust_name=dv.validate_name()
		balance='0'
		dob=dv.validate_dob()
		acc_type=''

		pattern=r'^[0-9]{4}$'
		print("SET A 4 DIGIT PIN TO LOGIN TO E-ACCOUNT")
		while True:
			e_pin=input("ENTER PIN:").strip()
			c_pin=input("CONFIRM PIN:").strip()
			if re.match(pattern,e_pin) and re.match(pattern,c_pin):
				if e_pin==c_pin:
					pin=e_pin
					print("PIN SET SUCCESSFULLY")
					break
				else:
					print("Error : please confirm entered PIN")
			else:
				print("Error: Invalid PIN or confirm PIN")

		while True:
			type=input("Enter account type ['s' for savings 'c' for current]:").strip().lower()
			if type=='s':
				acc_type='SAVINGS'
				break
			elif type=='c':
				acc_type='CURRENT'
			else:
				print("Error: Invalid choice")
		
		ac_obj=aim.account(acc_no,cust_name,balance,dob,pin,acc_type)
		acc_manager.update_acc_list(ac_obj)
		print('ACCOUNT CREATION SUCCESSFUL')
		print(f'\n{cust_name} your account number is {acc_no}')
		print('\nPLEASE LOGIN USING CREDENTIALS TO PERFORM TRANSACTIONS')
		
if __name__=='__main__':
    print("--ACCESS RESTRICTED--")