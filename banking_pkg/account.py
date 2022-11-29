import sys


def show_balance(balance):
    print(f"Your balance is ${float(balance)}.")


def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    print(f"You have successfully deposited ${amount} into your account.")
    return balance + amount


def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    print(f"You have successfully withdrawn ${amount} from your account.")
    while balance - amount < 0:
        print(f"Your balance is ${float(balance)}. Please try again.")
        withdraw(balance)
    return balance - amount


def logout(name):
    print(f"Goodbye, {name}!")


def embezzle(balance, stan_alive):

    #    stan_alive = 1
    while stan_alive == 1:
        amount = float(input(
            "It's not how much you make, it's how much you take home! No one asked WHAT you would be taking home! How much would you like to embezzle? $"))
        choice = input(
            "To keep this just between you and Stan in accounting, please press 1 to give Stan a 20% cut and all identifiable information will be taken off this transfer.")
        if choice == "1":
            print(
                "This is Susan in accounting. For an extra 5% I'll bump off Stan and keep this quiet.")
            next_choice = input(
                "Please press 1 to keep this between you and Susan. ")
            if next_choice == "1":
                print("There's a good lad.")
                stan_alive = 0
                return balance + (amount * .75), stan_alive
            else:
                print("You're not that bright, are you? Please wait for the police to arrive. Resisting arrest will only add to your trouble.")
                break
        else:
            print(
                "It's just gone up by 10%. I'll be calling the police if you get stupid.")
            alt_choice = input("Please press 1 to accept giving Stan 30%. ")
            if alt_choice == "1":
                print("This is Susan in accounting. It looks like Stan really has you over a barrel. Please press 1 to signal that you'd like him bumped off in exchange for giving Susan a 40% cut. You're not getting out of this without giving a little something. ")
                susan = input("What will it be? ")
                if susan == "1":
                    print("There's a good lad.")
                    stan_alive = 0
                    return balance + (amount * .6), stan_alive
            else:
                print("You're not that bright, are you? Please wait for the police to arrive. Resisting arrest will only add to your trouble.")
                sys.exit()
    while stan_alive == 0:
        amount = float(input(
            "It's not how much you make, it's how much you take home! No one asked WHAT you would be taking home! How much would you like to embezzle? $"))
        choice = input(
            "It's just you and Susan now, sweetie. Please press 1 to give Susan half. ")
        if choice == "1":
            print(
                "There's a good lad. We've got a nice litte arrangement, now, don't we?")
            stan_alive = 0
            return balance + (amount * .6), stan_alive
            break
        else:
            print("Look, you had a chance to indulge your greed. You're done here. Please wait for the police to arrive. They'll have complete printouts of this exchange. Minus, of course, my bit. I've also framed you for Stan's murder. It was your fault, anyway. You did tell me to kill him.")
            sys.exit()
