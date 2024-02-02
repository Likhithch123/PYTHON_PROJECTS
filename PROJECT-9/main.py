## Title of the project: BLIND-AUCTION OR SECRET AUCTION


import os
from art import logo

print(logo)
bidders_left = True
blind_auction_dict = {}


def find_highest_bidder(bidding_record):
    max_bid = 0
    winner = ""
    for bidder in bidding_record:
        if bidding_record[bidder] > max_bid:
            max_bid = bidding_record[bidder]
            winner = bidder
    print(f"{winner} won the auction with a bid of ₹{max_bid}")


while bidders_left:
    name = input("what is your name?\n")
    bidding_amount = int(input("Enter your bid: ₹"))
    blind_auction_dict[name] = bidding_amount
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if should_continue != 'yes':
        bidders_left = False
        find_highest_bidder(blind_auction_dict)
    else:
        os.system('cls')
