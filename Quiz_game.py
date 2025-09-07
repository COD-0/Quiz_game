#welcoming user
print("Welcome to our quiz game!")

#asking user if he she or ... want to play the game
play = input("Do you want to play the game? ").lower()
if play == "yes":
    print("ok,i hope you enjoy :) ")
elif play == "no":
    print("Okey then i hope see you soon young one :( ")
    quit()
else:
    print("please just answer with yes or no")  
    quit()

#asking questions and give score to user
score = 0
answer_1 = input("Where is the capital of persia? ").lower()
if answer_1 == "tehran":
    print("correct!")
    score += 1
else:
    print("incorrect!")
answer_2 = input("What's the khorshid meaning? ").lower()
if answer_2 == "sun":
    print("correct!")
    score += 1
else:
    print("incorrect")
if score > 0:    
    print("welldone!you did a graet job ;) this is youre score:", score)

else:
    print("try harder next time:) ") 
