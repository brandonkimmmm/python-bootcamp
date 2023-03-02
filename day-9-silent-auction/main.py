from art import logo
from replit import clear

print(logo)
print("Welcome to the secret auction program.")

end_auction = False
bids = {}
highest_bidder = ""

while not end_auction:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    bids[name] = bid

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        end_auction = True
    clear()

for bidder in bids:
    if (highest_bidder == "" or bids[bidder] > bids[highest_bidder]):
        highest_bidder = bidder

print(f"The winner is {highest_bidder} with a bid of ${bids[highest_bidder]}.")