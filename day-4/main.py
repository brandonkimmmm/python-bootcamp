import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hands = [rock, paper, scissors]

user_hand = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

print(f"{hands[user_hand]}")

computer_hand = random.randint(0, 2)

print(f"Computer choose:\n{hands[computer_hand]}")

if (user_hand == computer_hand):
    print("You draw")
elif (
    (user_hand == 0 and computer_hand == 1)
    or (user_hand == 1 and computer_hand == 2)
    or (user_hand == 2 and computer_hand == 0)
):
    print("You lose")
else:
    print("You win")