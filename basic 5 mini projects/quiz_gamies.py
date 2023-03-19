print("Welcome to our computer quiz")

playing = input("do you wanted to play a quiz? ")
print(playing)


if playing.lower() != "yes":
    quit()

print("okay! Let's play the quiz :")

Score = 0
answer = input("what does cpu stand for? ")
if answer.lower() == "central processing unit":
    print("correct")
    Score += 1
else:
    print("sorry but its incorrect!")    

answer = input("What does gpu stands for ? ")
if answer.lower() == "graphics processing unit":
    print("correct")
    Score += 1
else:
    print("sorry but its incorrect!")    

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("correct")
    Score += 1
else:
    print("sorry but its incorrect!")  

answer = input("What does psu stands for ? ")
if answer.lower() == "power supply unit":
    print("correct")
    Score += 1
else:
    print("sorry but its incorrect!") 

print("You got " + str(Score) + " questions correct out of 4 questions.")   
print("You got " + str((Score/4)*100) + " %.")   