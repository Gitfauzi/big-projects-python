# here we will store password in encrypted version
# you should not store password like that in real life

master_pwd =input("what is the master password? ")


def view():
    with open ('passwords.txt', 'r') as f:#a - is append, w is write , r is read 
        for line in f.readlines():
            print(line.rstrip())

def add():
    name = input("account name: ")
    pwd = input("password ")

    with open ('passwords.txt', 'a') as f:#a - is append, w is write , r is read 
        f.write(name + "|" + pwd + "\n")
while True:

    mode = input("would you like to add a new passowrd or view an existing one (view/add) ? ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode ")
        continue
