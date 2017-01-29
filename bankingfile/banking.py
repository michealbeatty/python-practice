#!/usr/bin/env python3


import sys
# Prompt user to enter a file name prefix
# Generate two files prefix.old.txt and prefix.new.txt
# catch file read errors



# for each record in old master file
# display customer information
# account is 6 characters [0:6]
# balance is 10 characters [7:17]
# name is 27 at longest but can't use length [18:]
# prompt for transaction related to customer
# write the customer record to the new master file

# program will recognize following transactions
# deposit
# withdrawal
# close
# advance to next customer

def get_number(one_line):
    # returns the account number
    return one_line[:6]

def get_balance(one_line):
    # returns the account balance as a float
    if len(one_line) > 17:
        return float(one_line[7:17].lstrip())
    else:
        return 0.00

def get_name(one_line):
    # returns the account holder's name as a string
    if len(one_line) > 19:
        return one_line[18:].rstrip()
    else:
        return "(No Name)"

def equal_floats(x, y):
    if x == y:
        return True
    else:
        return False

def main():
    file_prefix = input("Enter file name prefix: ")

    infile = open("sample.master.old.txt")
    line = infile.readline()
    print("{} ({}) ${}".format(get_name(line), get_number(line), get_balance(line)))
    
    while True:
        trans_code = input("Enter a command (a, c, d, w) ")

        if trans_code == 'd':
            deposit = input("Deposit amount: ")
            new_balance = get_balance(line) + float(deposit)
            print("New balance is ", new_balance)
        if trans_code == 'w':
            withdrawal = input("Withdrawal amount: ")
            new_balance = get_balance(line) - float(withdrawal)
            print("New balance is ", new_balance)
        if trans_code == 'c':
            if get_balance(line) == 0:
                print("Closing Account")
            else:
                print("Account has a balance. Cannot close.")
        if trans_code == 'a':
            line = infile.readline()
            if get_number(line) == "999999":
                print("End of File. Closing...")
                sys.exit(0)
            print("{} ({}) ${}".format(get_name(line), get_number(line), get_balance(line)))
            continue

    infile.close()


if __name__ == '__main__':
    main()