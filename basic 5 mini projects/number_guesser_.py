# here we will just generate random no. and see in how many times the user is able to guess it

import random
top_of_range=input("type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <=0:
        print("please type a no. greater than 0")
        quit()
else:
    print("please write a no. ")
    quit()

random_number=random.randint(0, top_of_range)
print(random_number)

guesses=0

while True:
    guesses+=1    

    user_guess =input("made a guess ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("enter a no. please")
        continue
            
    if user_guess == random_number:
        print("congrats! your guess is correct")
        break
        
    elif user_guess > random_number:
            print("Your guess is greator than the no. ")
    else:
            print("you are below the no. ")


print("You got it in", guesses, "gueses")

