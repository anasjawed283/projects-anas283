import random 

#for user computer interface
number = random.randint(1, 50)#keeping it for natural numbers till 50...
times = 1
guess = int(input("Guess the number: "))

while(True):#looping until the user gets it correct
    if(guess>number):
        guess = int(input("Guess another number. This one is greater than required: "))
        times += 1
    elif(guess<number):
        guess = int(input("Guess another number. This one is smaller than required: "))
        times += 1

    else:
        print(f"Awesome that's the correct number! You guessed it right in {times} chances")
        break #ends the game when the user gets it correct if want to continue we must keep it in loop again.