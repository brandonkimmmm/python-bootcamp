from random import choices

from art import logo, vs
from game_data import data
from replit import clear

total_score = 0
is_wrong = False
is_running = True


def get_option_description(option):
    return f"{option['name']}, a {option['description']}, from {option['country']}."


def get_choices():
    return choices(data, k=2)


def get_correct_choice(options):
    if options[0]["follower_count"] > options[1]["follower_count"]:
        return "A"
    else:
        return "B"


def display_choices_and_compare(options):
    print(f"Compare A: {get_option_description(options[0])}")
    print(vs)
    print(f"Against B: {get_option_description(options[1])}")

    correct_guess = get_correct_choice(options)
    given_guess = input("Who has more followers? Type 'A' or 'B': ")

    while given_guess != "A" and given_guess != "B":
        given_guess = input("Invalid choice given! Type 'A' or 'B': ")

    if correct_guess == given_guess:
        global total_score
        total_score += 1
    else:
        global is_wrong
        is_wrong = True


def run_game():
    clear()
    print(logo)
    if not is_wrong:
        if total_score > 0:
            print(f"You're right! Current score {total_score}.")
        options = get_choices()
        display_choices_and_compare(options)
    else:
        print(f"Sorry, that's wrong. Final score: {total_score}.")
        global is_running
        is_running = False


while is_running:
    run_game()
