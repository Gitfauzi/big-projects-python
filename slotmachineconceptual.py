MAX_LINES = 3
def deposit():
    while True:
        amount = input("what would you like to deposit? $")
        if amount.isdigit():  # is digit --  only for positive integer
            amount = int(amount)
            if amount >0:
                break
            else:
                print("amount must be greator than zero")
        else:
            print("please enter a number")

    return amount


deposit()

def get_number_of_lines():

def main():
    balance = deposit()
main()