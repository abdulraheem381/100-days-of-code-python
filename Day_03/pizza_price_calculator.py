print("🍕 Welcome to Python Pizza Deliveries!")

# User input with normalization
size = input("What size of pizza would you like? (S/M/L): ").strip().upper()
pepperoni = input("Would you like pepperoni? (Y/N): ").strip().upper()
extra_cheese = input("Would you like extra cheese? (Y/N): ").strip().upper()

bill = 0

# Pizza pricing logic
if size == 'S':
    bill = 15
    if pepperoni == 'Y':
        bill += 2
        print("🧀 Small pizza: $15 + $2 for pepperoni.")
    else:
        print("🧀 Small pizza: $15.")
elif size == 'M':
    bill = 20
    if pepperoni == 'Y':
        bill += 3
        print("🍕 Medium pizza: $20 + $3 for pepperoni.")
    else:
        print("🍕 Medium pizza: $20.")
elif size == 'L':
    bill = 25
    if pepperoni == 'Y':
        bill += 3
        print("🍕 Large pizza: $25 + $3 for pepperoni.")
    else:
        print("🍕 Large pizza: $25.")
else:
    print("❌ Invalid size selected. Please try again.")
    exit()

# Cheese option
if extra_cheese == 'Y':
    bill += 1
    print("🧀 Added extra cheese: +$1")

# Final bill
print(f"💵 Your total bill is: ${bill}")
