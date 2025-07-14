# Caesar Cipher - Day 8 Project (Angela Yu 100 Days of Code)

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
             'n','o','p','q','r','s','t','u','v','w','x','y','z']

# Banner
def show_banner():
    print("""
   _____                                _____  _       _               
  / ____|                              / ____|| |     | |              
 | |     __ _ ___  ___ ___  ___  ___ | |     | |_   _| |__   ___ _ __ 
 | |    / _` / __|/ __/ _ \/ __|/ _ \| |     | | | | | '_ \ / _ \ '__|
 | |___| (_| \__ \ (_| (_) \__ \  __/| |____ | | |_| | |_) |  __/ |   
  \_____\__,_|___/\___\___/|___/\___| \_____||_|\__,_|_.__/ \___|_|   

    Caesar Cipher Tool | Day 8 - 100 Days of Code
    """)

def caesar_cipher(text, shift, direction):
    result = ""

    for char in text:
        if char in alphabets:
            index = alphabets.index(char)
            if direction == "encode":
                new_index = (index + shift) % 26
            elif direction == "decode":
                new_index = (index - shift) % 26
            result += alphabets[new_index]
        else:
            result += char  # Keep spaces and punctuation

    print(f"\nThe {direction}d text is: {result}\n")

# Run program in loop
show_banner()
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar_cipher(text=text, shift=shift, direction=direction)

    again = input("Do you want to go again? Type 'yes' or 'no':\n").lower()
    if again != 'yes':
        should_continue = False
        print("Goodbye 👋 Keep coding!")
