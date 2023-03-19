# choosing game 
# 58:

name = input("type your name")
print(f"welcome {name} to this adventure")

answer =input("you are on a dirt road, it has come to an end and you can left or right, where do you want to go ?").lower()

if answer == "left":
    answer =input("you come to a river, you can walk or swim across. type walk to move around and swim to swim across. ")
    if answer == "swim":
        print("you swim across and were eaten by the aligators")
    elif answer == "walk":
        print("you walk for many miles ran out of water you lose")
    else:
        print("please enter a valid statement")

elif answer == "right":
    answer = input("Now you come to bridge and it looks wobly, do you want to cross it or head back (cross/back)? ")
    if answer == "back":
        print("you go to back, lose    ")
    elif answer == "cross":
        print("you can cross bridge")
        answer =input("You cross the bridge you met a stranger would you like to talk to him, (yes/no)? ")
        if answer == "yes":
            answer = input("now you become friend to him and you can go with him in his journey or go another direction ? you want to go with him (yes/no)?")
        if answer == "no":
            print("now you don't know way out of it , you lose")
    else:
        print("please enter a valid statement")



else:
    print("not a valid option")