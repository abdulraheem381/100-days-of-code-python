import random

word_list = ["camel" , "bird", "lake", "germany" , "candle"]

chosen_word = random.choice(word_list)

print(chosen_word)

placeholder = ""

word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
    
print(placeholder)



# GUESS A LETTER 

guess = input("Guess a letter: ").lower()

display = ""

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)           
     
