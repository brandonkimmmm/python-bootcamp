import os

import pandas

data = pandas.read_csv(f"{os.path.dirname(__file__)}/nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (_, row) in data.iterrows()}
word = input("Enter a word: ").upper()
print([phonetic_dict[char] for char in word])
