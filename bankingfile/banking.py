#!/usr/bin/env python3

import os
import sys

def get_number(one_line):
    """returns the account number"""
    return one_line[:6]

def get_balance(one_line):
    """returns the account balance as a float"""
    if len(one_line) > 17:
        return float(one_line[7:17].lstrip())
    else:
        return 0.00

def get_name(one_line):
    """returns the account holder's name as a string"""
    if len(one_line) > 19:
        return one_line[18:].rstrip()
    else:
        return "(No Name)"

def equal_floats(x, y):
    """Compares two floats and returns boolean"""
    if x == y:
        return True
    else:
        return False

def main():
    file_prefix = input("Enter file name prefix: ")
    old_file = file_prefix + ".old.txt"
    new_file = file_prefix + ".new.txt"

    if os.path.isfile(old_file):
        print("File exists")

        infile = open(old_file, 'r')
        ofile = open(new_file, 'w')
    else:
        print("{} does not exist".format(old_file))
        sys.exit(0)

    line = infile.readline()
    print("{} ({}) ${}".format(get_name(line), get_number(line), get_balance(line)))
    new_balance = get_balance(line)
    while True:
        trans_code = input("Enter a command (a, c, d, w) ")

        if trans_code == 'd':
            deposit = input("Deposit amount: ")
            new_balance = new_balance + float(deposit)
            print("New balance is ", new_balance)
        if trans_code == 'w':
            withdrawal = input("Withdrawal amount: ")
            new_balance = new_balance - float(withdrawal)
            print("New balance is ", new_balance)
        if trans_code == 'c':
            if new_balance == 0:
                print("Closing Account")
            else:
                print("Account has a balance. Cannot close.")
        if trans_code == 'a':
            new_entry = "{} {:.2f} {}\n".format(get_number(line), new_balance, get_name(line))
            ofile.write(new_entry)
            line = infile.readline()
            new_balance = get_balance(line)
            if get_number(line) == "999999":
                print("End of File. Closing...")
                sys.exit(0)
            print("{} ({}) ${}".format(get_name(line), get_number(line), get_balance(line)))
            continue

    infile.close()
    ofile.close()


if __name__ == '__main__':
    main()