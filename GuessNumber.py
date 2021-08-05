import random
randNumber = random.randint(1,100)
userguess = None
guesses = 0
while(userguess != randNumber):
    userguess = int(input("Guess the number :"))
    guesses += 1
    if(userguess == randNumber):
        print("Your guess is right!!")
    else:
        if(userguess>randNumber):
            print("PLEASE GUESS THE SMALLER NUMBER THAN THAT..")
        else:
            print("PLEASE GUESS THE GRATER NUMBER THAN THAT..")

print(f"You guessed the number in {guesses} guesses")