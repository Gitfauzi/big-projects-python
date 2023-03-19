
def deposit():
    amount = input("what would you like to deposit? $")
    if amount.isdigit():
        amount = int(amount)
        if amount <= 0:
            print("please enter no greator than zero")

    else:
        print("enter a number")

    return amount

deposit()