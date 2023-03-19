import random

def gamewin(computer,you):

    if computer == you:
        None

    elif computer == ("s"):
        if you == ("w"):
            return False
        elif you == ("g"):
            return True

    elif computer == ("w"):
        if you == ("g"):
            return False
        elif you == ("s"):
            return True
            
    elif computer == ("g"):
        if you == ("s"):
            return False
        elif you == ("w"):
            return True

   


computer = ("Computer's turn : Snake(s),Water(w) or Gun(g)")
you = input("your turn : Snake(s),Water(w) or Gun(g) ")
randno = random.randint(1,3)

if randno == 1:
    computer = "s"
elif randno == 2:
    computer = "w"
else:
    computer = "g"



computerchoice = print(f"computer chose {computer}")
yourchoice = print(f"you chose {you}")

a = gamewin(computer,you)

if a is True:
    print("you won")
elif a is False:
    print("you lose")
elif a is None:
    print("tie")
    

gamewin(computer,you)






