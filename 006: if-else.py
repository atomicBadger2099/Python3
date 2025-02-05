#THIS PROGRAM DEMONSTRATES A SIMPLE USE OF AN IF-ELSE DECISION

print("\n")
print("This program demonstrates how a choice is used in Python 3.13")
print("\n")

print("What does CPU stand for?")
print("\n")
print("    your choices include:\n")
print("\n")
print("    A. Charlie's Precise Underline\n")          
print("    B. Central Processing Unit\n")
print("    C. Cognitive Potential Unchained\n")
print("\n")


#STANDARD IF-ELSE LOOP IMPLEMENTS A CHOICE AND RESULT

choice_x = input("please enter your response as A, B, or C and hit <ENTER> at the current prompt  >>> ")
print("\n")

if choice_x == 'B' or choice_x == 'b':
    print("your choice is correct.")
else:
    print("your choice is not correct.")

print("\n")
print("Thank you for your response.")
print("\n")

exit()
