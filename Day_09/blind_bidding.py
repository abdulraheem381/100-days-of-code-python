# ASCII Art Banner
banner = '''
  ____  _     _           _     _       _     _             
 | __ )(_) __| | ___ _ __(_)___| | __ _| |__ | | ___  _ __  
 |  _ \| |/ _` |/ _ \ '__| / __| |/ _` | '_ \| |/ _ \| '_ \ 
 | |_) | | (_| |  __/ |  | \__ \ | (_| | |_) | | (_) | | | |
 |____/|_|\__,_|\___|_|  |_|___/_|\__,_|_.__/|_|\___/|_| |_|

             💰 Day 09: Blind Bidding Program 💰
'''
print(banner)

# Store all bids
bids = {}

# Function to find and announce the highest bidder
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"\n🏆 The winner is {winner} with a bid of ${highest_bid}!\n")

# Start bidding loop
bidding_finished = False

while not bidding_finished:
    name = input("🧑 Enter your name: ")
    bid_price = int(input("💵 Enter your bid price: $"))
    bids[name] = bid_price

    more_bidder = input("❓ Anyone else want to bid? Type 'yes' or 'no': ").lower()

    if more_bidder == 'no':
        bidding_finished = True
        print("\n" * 50)
        find_highest_bidder(bids)
    else:
        print("\n" * 50)
