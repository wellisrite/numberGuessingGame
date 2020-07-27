import random as rand
import time

start_time = time.time()

solved = False
MAX_LIMIT = 10000

number = rand.randint(0, MAX_LIMIT)

guess = rand.randint(0, MAX_LIMIT)

guessStatus = ""

def guessNextNumber(guessStatus, guess):
    if (guessStatus == "smaller"):
        return rand.randint(0, guess)
    else:
        return rand.randint(guess, MAX_LIMIT)


while(not solved):
    if (guess == number):
        solved = True
        continue

    guessStatus = "bigger" if (guess < number) else "smaller"

    print(f"Wrong Number: The number is {guessStatus} than {guess}")
    
    guess = guessNextNumber(guessStatus, guess)


print("solved the number is", number)
execTime = time.time() - start_time
print(f"It took {execTime} to search for the number")