import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = [ '0', '1', '2', '3', '4', '5', '6', '7','8','9']
symbols = ['!', '#', '$', '%','&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many Letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like\n"))


password_choice = []

# letters choice

for i in range(nr_letters):
    random_letter = random.choice(letters)
    password_choice.append(random_letter)

# numbers choice 

for i in range(nr_numbers):
    random_number = random.choice(numbers)
    password_choice.append(random_number)

# symbols choice

for i in range(nr_symbols):
    random_symbols = random.choice(symbols)
    password_choice.append(random_symbols)

# Shuffle the paswword choice list to make it more strong
random.shuffle(password_choice)

# joining into a string

password = "".join(password_choice)

print(f"Your Generated password is {password}")
print("Thanks for using PyPassword Generator. Stay secure! 🔐")



