#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard
import pyperclip, re

pass_check = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}')

def passCheck():
    typePass = input("Enter hard to break password")
    mo = pass_check.search(typePass)
    if (not mo):
        print("Not Good")
        return False
    else:
        print("Good")
        return True

passCheck()
