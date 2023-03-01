import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D' 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

total_length = num_letters + num_symbols + num_numbers

password = []

for num in range(0, total_length):
    password.append(num)

for letter in range(0, num_letters):
    letter_pos = random.randint(0, len(password) - 1)
    while (password[letter_pos] == "letter"):
        letter_pos = random.randint(0, len(password) - 1)
    password[letter_pos] = "letter"

for symbol in range(0, num_symbols):
    symbol_pos = random.randint(0, len(password) - 1)
    while (password[symbol_pos] == "symbol" or password[symbol_pos] == "letter"):
        symbol_pos = random.randint(0, len(password) - 1)
    password[symbol_pos] = "symbol"

for char_pos in range(0, len(password)):
    if (password[char_pos] == "letter"):
        password[char_pos] = letters[random.randint(0, len(letters) - 1)]
    elif (password[char_pos] == "symbol"):
        password[char_pos] = symbols[random.randint(0, len(symbols) - 1)]
    else:
        password[char_pos] = numbers[random.randint(0, len(numbers) - 1)]

print(f"Here is your password: {''.join(password)}")

