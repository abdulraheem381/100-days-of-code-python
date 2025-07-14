# Tip calculator
print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))  # <- float for cents

tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

split_bill = int(input("How many people to split the bill? "))

total_with_tip = bill + (bill * tip / 100)
per_person = total_with_tip / split_bill

print(f"Each person should pay: ${per_person:.2f}")
