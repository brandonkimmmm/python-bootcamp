from os import path

DIRNAME = path.dirname(__file__)

with open(f"{DIRNAME}/Input/Letters/starting_letter.txt") as starting_letter_file:
    starting_letter = starting_letter_file.read()

with open(f"{DIRNAME}/Input/Names/invited_names.txt") as names_file:
    content = names_file.read()
    names = content.splitlines()

    for name in names:
        letter = starting_letter.replace("[name]", name)
        with open(
            f"{DIRNAME}/Output/ReadyToSend/letter_for_{name.replace(' ', '_')}.txt",
            mode="w",
        ) as write_file:
            write_file.write(letter)
