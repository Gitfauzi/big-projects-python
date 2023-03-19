# 42:
# we made the game of rock paper scissor

import random

user_wins = 0
computer_wins = 0

options =["rock", "paper", "scissor"]

while True:
    user_input=input("type rock/paper/scissors or Q to quit the game ").lower()

    if user_input == "q" :
        break  # if the condition is not met than it will just go to the end of while loop and print("goodbye") 


    if user_input not in options:
        continue   # mtlb agar user_input not in options hai to yahan se code sidha while loop ke start par chala jayega

    random_number = random.randint(0,2)
    # rock is 0, paper is 1, scissor is 2
    computer_pick = options[random_number]
    print("computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick =="scissor":
        print("You won!!")
        user_wins +=1
        continue   # mtlb agar user_input ="rock " and computer_pick ="scissor " hai to yahan se code sidha while loop ke start par chala jayega

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!!")
        user_wins +=1
        continue # mtlb agar user_input ="paper " and computer_pick ="rock" hai to yahan se code sidha while loop ke start par chala jayega

    elif user_input == "scissor" and computer_pick == "paper":
        print("You won!!")
        user_wins +=1
        continue  # mtlb agar user_input ="scissor " and computer_pick ="paper " hai to yahan se code sidha while loop ke start par chala jayega

    else:
        print("You lost ")
        computer_wins += 1

print("You won", user_wins, "time")  # yahan par isne you won 0 times kyu nahi likha - 
print("goodbye")

