#
## Guess Game
### Created by Yseeva
##
#

import random
print("||||| ______ WELCOME ______||||")
print("it is a guess game . I have a number between 0-20 and you guess it!")
given=int(input("Enter the number I am thinking of :"))
randnum=random.randint(0,20)
count=1
while 1 :
    if given==randnum:
        print(f"Corroct it is {given} with {count} guesses")
        break
    elif given>randnum:
        print(f"it is lower than {given}")
        given=int(input("Enter the number I am thinking of :"))
        count+=1
    elif given<randnum:
        print(f"it is upper than {given}")
        given=int(input("Enter the number I am thinking of :"))
        count+=1
        
