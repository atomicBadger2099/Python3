# VARIABLES AREA
score = 0             #INITIALIZE SCORE
choice_1 = "unknown"  #INITIALIZE ANSWER 1
choice_2 = "unknown"  #INITIALIZE ANSWER 2
choice_3 = "unknown"  #INITIALIZE ANSWER 3


# EXECUTION AREA
print("\n")
print("WELCOME TO QUIZWORLD.")
print("\n")    
playChoice = input("Would you like to play a quiz game?\nPlease enter your response of yes or no AS A FULL WORD EXACTLY at the cursor.>>>")

if playChoice == 'no' or playChoice == 'NO' or playChoice == 'No':
    print("\n")
    print("You have chosen not to play. Have a nice day.")
    print("\n")
    exit()
elif playChoice == 'YES' or playChoice == 'yes' or playChoice == 'Yes':
    print("\n")
    print("You have chosen to play. Most Awesome!")
    print("\n")
else:
    print("\n")
    print("ERROR: some mistake has happened in input.")
    print("Please restart the program from the beginning.")
    print("\n")
    
    exit()

#QUESTION AREA 1

print("Question Number one.")
print("\n")
print("What does CPU stand for? Please choose from the following options.")
print("\n")
print("A. Chinese Pulmonary Unification")
print("B. Central Processing Unit")
print("C. Cerudine Prolific Underpinning")
print("\n")

choice_1 = input("Please enter your answer as A, B, or C at the cursor. Pick only one answer.  >>>")
print("\n")

if choice_1 == 'B' or choice_1 == 'b':
    print("your choice is correct.")
    score = score + 100
else:
    print("your choice is not correct.")
    score = score + 10

print("Your current score is:")
print(score)
print("Now on to question number two.")
print("\n")

#QUESTION AREA 2

print("Question number Two")
print("\n")
print("What does RAM stand for? Please choose from the following options.")
print("A. Retroactive Auxillary Movement")
print("B. Retentional Antoric Metachoice")
print("C. Random Access Memory")
print("\n")

choice_2 = input("Please enter your answer as A, B, or C at the cursor. Pick only one answer.  >>>")
print("\n")

if choice_2 == 'C' or choice_2 == 'c':
    print("your choice is correct.")
    score = score + 100
else:
    print("your choice is not correct.")
    score = score + 10

print("Your current score is:")
print(score)
print("Now on to question number three.")
print("\n")

#QUESTION AREA 3

print("Question Number three.")
print("\n")
print("What does GPU stand for? Please choose from the following options.")
print("\n")
print("A. Graphics processing unit")
print("B. Grand preparation understanding")
print("C. Geriatric pulmonary underpinning")
print("\n")

choice_3 = input("Please enter your answer as A, B, or C at the cursor. Pick only one answer.  >>>")
print("\n")

if choice_3 == 'A' or choice_3 == 'a':
    print("your choice is correct.")
    score = score + 100
else:
    print("your choice is not correct.")
    score = score + 10

print("Your final score is:")
print(score)
print("We hope you enjoyed this game. Have a nice day")
print("\n")

# END OF PROGRAM
exit()

