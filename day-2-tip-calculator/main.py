print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100
split_num = int(input("How many people to split the bill? "))

total_bill *= tip_percentage + 1

result = "{:.2f}".format(round(total_bill / split_num, 2))
print(f"Each person should pay: ${result}")
