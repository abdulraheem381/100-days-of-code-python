import time
import sys

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____ 
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____ 
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')

print("🏴‍☠️ Welcome to *Treasure Island*! 🏝️")
time.sleep(1)
print("Your mission is simple: **Find the hidden treasure.** 💰")
time.sleep(1)

# Round 1
round_1 = input("\nYou're at a crossroad. Where do you want to go?\n👉 Type 'left' or 'right': ").lower()

if round_1 == 'right':
    print("💥 You fell into a hole. Game Over!")
    sys.exit()
elif round_1 == 'left':
    print("🌊 You arrive at a calm lake. There's an island in the middle.")
else:
    print("❌ Invalid choice. Try again next time.")
    sys.exit()

# Round 2
round_2 = input("\nDo you want to wait for a boat or swim across?\n👉 Type 'wait' or 'swim': ").lower()

if round_2 == 'swim':
    print("🐟 You were attacked by a school of trout. Game Over!")
    sys.exit()
elif round_2 == 'wait':
    print("⛵ You safely reach the island by boat.")
else:
    print("❌ Invalid choice. Try again next time.")
    sys.exit()

# Round 3
round_3 = input("\nYou see a house with 3 doors: 🔴 Red, 🟡 Yellow, 🔵 Blue.\nWhich door do you choose?\n👉 Type 'red', 'yellow' or 'blue': ").lower()

if round_3 == 'red':
    print("🔥 Burned by fire. Game Over!")
elif round_3 == 'blue':
    print("🧟 Eaten by beasts. Game Over!")
elif round_3 == 'yellow':
    print("🎉 Congratulations! You found the treasure. **YOU WIN!** 🏆")
else:
    print("❌ That door doesn't exist. Game Over.")
