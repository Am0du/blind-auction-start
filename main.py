from replit import clear
from  art import logo


item_auction = input("What's the auction item ")
bidders = []

#Adds the bidder
def add_bidders(bidder_name, bidder_bid):
    new_bidder = {}
    new_bidder["Name"] = bidder_name
    new_bidder["Bid"]  = bidder_bid
    bidders.append(new_bidder)

#Finds the highest bidder
def highest_bidder(bid):
    higgest_bid = 0
    winner = ""
    for i in range(0, len(bid)):
        if bid[i]["Bid"] > higgest_bid:
            highest_bid = bid[i]["Bid"]
            winner = bid[i]["Name"]
            
    print(f"The highest bidder is {winner} with a bid of {highest_bid}")

#checks if there's a draw in the bid
def draw(bidder_draw):
    draw = []
    for bids in bidder_draw:
        save_bid = bidders[0]["Bid"]
        if bids["Bid"] == save_bid:
            save_bid = bids["Bid"]
            draw.append(bids["Name"])

    if len(draw) > 1:
        print(f"if {draw} appears as winner, please rebid")

#Loops to check if there's another user for bidding 
another_bidder = True
while another_bidder is True:
    print(logo)
    print(f"Welcome to the Secret Auction of a {item_auction}")
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

#calls the function and outputs the results
print(logo)
highest_bidder(bidders)
draw(bidders)
