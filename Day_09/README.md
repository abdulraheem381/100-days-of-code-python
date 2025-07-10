# 💰 Day 09 - Blind Bidding Program

This is the Day 09 project of my **#100DaysOfCode** Python journey: a **Blind Bidding Program** where multiple users can enter their bids anonymously, and the program determines the highest bidder.

---

## 🧠 Today's Learnings

- ✅ Python Dictionary  
- ✅ Nested Lists  
- ✅ Nested Dictionary  
- ✅ List inside a Dictionary  

---

## 🛠️ Project Description

This program simulates a blind auction. It allows multiple users to input their names and bid amounts. The highest bidder is determined at the end, and the winner is announced.

### ⚙️ Features

- Collects multiple bids without revealing previous entries  
- Uses dictionaries to store bid data  
- Finds the highest bidder using logic and loop  
- Clears the screen between each entry (simulated using `"\n" * 50`)

---

## 🖥️ How to Run

1. Make sure Python is installed.
2. Run the program:
   ```bash
   python blind_bid.py

---

🧑 Enter your name: Alice
💵 Enter your bid price: $300
❓ Anyone else want to bid? Type 'yes' or 'no': yes

🧑 Enter your name: Bob
💵 Enter your bid price: $350
❓ Anyone else want to bid? Type 'yes' or 'no': no

🏆 The winner is Bob with a bid of $350!
