"""Account Information Manager

This module  contains classes and functions to fetch, add or update account details
to the file act as account data store.
"""
#import os
#file_path=os.getcwd()+r'\\Banking_System\\customer_account_info.txt'

class Account:
    """
    A class used to represent an account and related details

    ...

    Attributes
    ----------
    acc_no : str
        The account number
    cust_name : str
        The name of the account holder
    balance : str
        The account balance
    dob : str
        The Date of Birth of account holder
    pin:
        The 4 digit pin for logging into the application
    acc_type:
        The account type [SAVINGS/CURRENT]
    """

    def __init__(self,acc_no:str,cust_name: str,balance: str,dob:str,pin: str,acc_type: str):
        self.acc_no=acc_no
        self.cust_name=cust_name
        self.balance=balance
        self.dob=dob
        self.pin=pin
        self.acc_type=acc_type


class AccountManager(Account):
    """
    A class containing methods to fetch and add or update file containing account details
    """

    def __init__(self):
        #import os
        #file_path=os.getcwd()+r'\Banking_System\customer_account_info.txt'
        #self.file_name=file_path
        self.file_name='d:\\Python_Files\\Entri_DSML\\Banking_System\\customer_account_info.txt'

    def get_acc_list(self):
        """Gets and passes the details of accounts in the bank

        Returns
        -------
        list
            A list of objects of Account class representing the account details
        """

        self.accounts=[]
        with open(self.file_name,'r') as fp:
            #generates list of objects of Account class containing details of each opened account and returns it
            for row in fp:
                vals=row.split(',')
                acc_obj=Account(vals[0],vals[1],int(vals[2]),vals[3],vals[4],vals[5])
                self.accounts.append(acc_obj)
            return self.accounts
    
    def update_acc_list(self,up_acc:Account):
        """Add or update account details to the file containing details of all accounts

        Parameters
        ----------
        up_acc : (class)Account
            The
        Returns
        -------
        None
        """
        #generates a string in desired format containing details regarding an account and adds or updates it to file
        upd_line=up_acc.acc_no+','+up_acc.cust_name+','+up_acc.balance+','+up_acc.dob+','+up_acc.pin+','+up_acc.acc_type
        with open(self.file_name,'r+') as fp:
            lines=fp.readlines()
            fp.seek(0)
            for line in lines:
                if line[:10] != upd_line[:10]:
                    fp.write(line)
            fp.write(upd_line)
            fp.truncate()

if __name__=='__main__':
    print("--ACCESS RESTRICTED--")
    