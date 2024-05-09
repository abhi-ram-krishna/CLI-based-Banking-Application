"""Data Validation

This script allows the developer to validate format of account related data iteams when entered by the user.
This file can be imported as a module and contains the following functions:
    *validate_acno - validates account number entered by user
    *validate_pin - validates account PIN entered by user
    *validate_name - validates account holders name during registration
    *validate_dob - validates DOB of account holder during registration
    *validate_amt - validates amount entered during account transactions [Deposit/Withdrawal]
"""

import re

def validate_acno() -> str:
    pattern=r'^\d{10}$'
    while True:
        try:
            acno=input("ENTER YOUR 10 DIGIT ACCOUNT NUMBER:").strip()
            if re.match(pattern,acno):
                return acno
            else:
                raise ValueError
        except:
            print("Error: Invalid account number. Try again")

def validate_pin() -> str:
    pattern=r'^\d{4}$'
    while True:
        try:
            pin=input("ENTER YOUR 4 DIGIT SECRET PIN:").strip()
            if re.match(pattern,pin):
                return pin
            else:
                raise ValueError
        except:
            print("Error: Invalid pin. Try again")       

def validate_name() -> str:
    pattern=r'^([A-Z]+)([\s]+[A-Z]+)*([\s|\.]+[A-Z])*$'
    while True:
        try:
            name=input("ENTER YOUR NAME:").strip().upper()
            if re.match(pattern,name):
                return name
            else:
                raise ValueError
        except:
            print("Error: Name can only contain letters, period and/or white spaces")   

def validate_dob() -> str:
    pattern=r'^[0-9]{2}/[0-9]{2}/[0-9]{4}$'
    while True:
        try:
            dob=input("ENTER YOUR DATE OF BIRTH [dd/mm/yyyy]:").strip()
            if re.match(pattern,dob):
                return dob
            else:
                raise ValueError
        except:
            print("Error: Invalid dob format") 

def validate_amt() -> str:
    pattern=r'^\d+$'
    while True:
        try:
            amt=input("ENTER AMOUNT:").strip()
            if re.match(pattern,amt):
                return amt
            else:
                raise ValueError
        except:
            print("Error: Invalid amount. Try again")         

if __name__=='__main__':
    print("--ACCESS RESTRICTED--")