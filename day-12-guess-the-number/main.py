from random import randint

from art import logo

RANDOM_NUM = randint(1, 100)
attempts = 10
is_correct = False


def check_guess(num):
    global attempts
    global is_correct
    attempts -= 1

    if num > RANDOM_NUM:
        print("Too high.")
    elif num < RANDOM_NUM:
        print("Too low.")
    else:
        is_correct = True
        print(f"You got it! The answer was {RANDOM_NUM}.")

    if not is_correct:
        if attempts > 0:
            print("Guess again.")
        else:
            print("You've run out of guesses, you lose.")


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking fo a number between 1 and 100.")


difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
while difficulty != "easy" and difficulty != "hard":
    difficulty = input(
        "Invalid difficulty given! Choose a difficulty. Type 'easy' or 'hard': "
    )

if difficulty == "hard":
    attempts = 5

while not is_correct and attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    attempt = int(input("Make a guess: "))
    check_guess(attempt)
