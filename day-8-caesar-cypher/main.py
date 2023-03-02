from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
continue_program = True

def caesar_cypher(direction, text, shift):
    result = ""

    if shift >= len(alphabet):
        shift %= 26

    if direction == "decode":
        shift *= -1

    for char in text:
        if char in alphabet:
            char_index = alphabet.index(char)
            char_index += shift

            if char_index >= len(alphabet) or char_index < 0:
                char_index %= len(alphabet)

            char = alphabet[char_index]
        result += char

    print(f"The {direction}d text is {result}")

print(logo)

while continue_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if direction != "encode" and direction != "decode":
        print("Wrong direction given.")
        exit()

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar_cypher(direction, text, shift)

    result = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n")
    if result == "no":
        continue_program = False

print("Goodbye")