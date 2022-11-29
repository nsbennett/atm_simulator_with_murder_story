from banking_pkg import account
import sys


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automated Teller Machine ===          ")


def name_length():
    while True:
        name = input("Enter name to register: ")
        if len(name) > 0 and len(name) < 11:
            return name
            break
        elif len(name) == 0:
            print("Please enter a user name.")
        else:
            print("User name must be no longer than 10 characters! Please try again!")


def pin_length():
    while True:
        pin = input("Enter PIN: ")
        if len(pin) > 0 and len(pin) < 5:
            return pin
            break
        elif len(pin) == 0:
            print("Please enter a PIN.")
        else:
            print("User name must be no longer than 10 characters! Please try again!")


name = name_length()
pin = pin_length()
balance = 0

while True:
    name_to_validate = name
    pin_to_validate = pin
    print("LOGIN")
    login_name = input("Enter name: ")
    login_pin = input("Enter PIN: ")

    if login_name == name_to_validate and login_pin == pin_to_validate:
        print("Login successful! Please hold still!")
        break
    else:
        print("Login unsuccessful! Please hold still!")


stan_alive = 1
while True:
    atm_menu(name)
    option = input("Please choose an option, type 1, 2, 3, or 4: ")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
    elif option == "3":
        balance = account.withdraw(balance)
    elif option == "4":
        account.logout(name)
        print("""
        CRITICAL SYSTEM FAILURE
        ALL USER INFORMATION LOST
        ALL BALANCES LOST
        PLEASE TAKE A SECOND JOB
        YOU WILL NEED IT
        """)
        sys.exit()
    elif option == "5":
        results = account.embezzle(balance, stan_alive)
        balance = float(results[0])
        stan_alive = results[1]
