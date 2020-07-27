import random as rand
import time

start_time = time.time()

solved = False
MAX_LIMIT = 10000000

number = rand.randint(0, MAX_LIMIT)

guess = rand.randint(0, MAX_LIMIT)

guessStatus = ""

min_treshold = 0

max_treshold = MAX_LIMIT

def guessNextNumber(guessStatus, guess):
    global min_treshold, max_treshold
    if (guessStatus == "smaller"):
        if (guess < max_treshold):
            max_treshold = guess
        return rand.randint(min_treshold, guess)
    else:
        if (guess > min_treshold):
            min_treshold = guess
        return rand.randint(guess, max_treshold)


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