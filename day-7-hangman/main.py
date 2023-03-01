import random

from hangman_art import logo, stages
from hangman_words import word_list
from replit import clear

wrong_guesses = 0
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []

for _ in range(word_length):
    display.append('_')

def is_done():
    if '_'in display and wrong_guesses < 6:
        return False
    else:
        return True

def result():
    if '_' not in display and wrong_guesses < 6:
        return "You win."
    else:
        return "You lose."

print(logo)

while not is_done():
    guess = input("Guess a letter: ").lower()

    clear()

    if guess in chosen_word:
        if guess in display:
            print(f"You've already guessed {guess}")
        else:
            for index in range(word_length):
                if guess == chosen_word[index]:
                    display[index] = guess
    else:
        wrong_guesses += 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
    print(f"{' '.join(display)}\n{stages[wrong_guesses]}\n")

print(result())