from replit import clear
from  art import logo
#HINT: You can call clear() to clear the output in the console.

item_auction = input("What's the auction item ")
bidders = []

def add_bidders(bidder_name, bidder_bid):
    new_bidder = {}
    new_bidder["Name"] = bidder_name
    new_bidder["Bid"]  = bidder_bid
    bidders.append(new_bidder)

def highest_bidder(bid):
    higgest_bid = 0
    winner = ""
    for i in range(0, len(bid)):
        if bid[i]["Bid"] > higgest_bid:
            highest_bid = bid[i]["Bid"]
            winner = bid[i]["Name"]
            
    print(f"The highest bidder is {winner} with a bid of {highest_bid}")

def draw(bidder_draw):
    draw = []
    for bids in bidder_draw:
        save_bid = bidders[0]["Bid"]
        if bids["Bid"] == save_bid:
            save_bid = bids["Bid"]
            draw.append(bids["Name"])

    if len(draw) > 1:
        print(f"if {draw} appears as winner, please rebid")
            
another_bidder = True
while another_bidder is True:
    print(logo)
    print(f"Welcome to the Secret auction of a {item_auction}")
    name = input("what is your name?: ")
    bid = int(input("what is your bid?: $"))
    
    add_bidders(bidder_name = name, bidder_bid = bid )
    
    add_bids = input("type 'yes' if there's another bidder or 'No' to end bid: ").lower()
    if add_bids == "yes":
        another_bidder = True
        clear()
    else:
        another_bidder = False
        clear()

print(logo)
highest_bidder(bidders)
draw(bidders)
