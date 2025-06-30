print("Welcome to the roller coaster!")

height = int(input("Enter your height in cm: "))
bill = 0

if height >= 120:
    print("You can ride the roller coaster.")
    age = int(input("Enter your age: "))  

    if age < 12:
        print("Your ticket price is $5.")
        bill = 5
    elif age <= 18:
        print("Your ticket price is $7.")   
        bill = 7 
    else:
        print("Your ticket price is $12.")
        bill = 12

    photo = int(input("Do you want a photo? Type 1 for yes and 0 for no: "))
    if photo == 1:
        print("Photo charges are $3.")    
        bill += 3

    print(f"Your total bill is ${bill}.")
else:
    print("Sorry, you can't ride. Height must be at least 120 cm.")
