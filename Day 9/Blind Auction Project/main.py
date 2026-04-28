# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
dictionary_bid= {}
should_continue = True
import art

print(art.logo)

def get_winner(dictionary):
    highest_bid = 0
    winner =""
    for bidder in dictionary:
        bid_amount = dictionary[bidder]
        if highest_bid < int(bid_amount):
            highest_bid = int(bid_amount)
            winner = bidder
    #print("Using max:" + max(dictionary, key = dictionary.get))
    print("The winner is "+ winner + " with a bid of " + str(highest_bid))

# TODO-3: Whether if new bids need to be added
while should_continue:
    name = input("Enter your name: ")
    bid = input("Enter your bid: ")
    dictionary_bid[name] = bid
    other_biders = input("Are there any other biders: y/n ")
    if other_biders == "n":
        should_continue = False
        get_winner(dictionary_bid)

# TODO-4: Compare bids in dictionary

