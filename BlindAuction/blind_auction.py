from blind_auction_utils import blindBid,logo

bidders = True
maxBid = 0
winner = ""

print(logo)
while bidders:
    name = input("What is your name: ")
    bidAmount = int(input("Enter your bidding amount: $"))
    anyBidders = input("Are there anyother bidders??\n Type \"Yes\" or \"No\": ")
    maxBid, winner = blindBid(name,bidAmount)
    if anyBidders.lower() == "yes":
        bidders = True
    elif anyBidders.lower() == "no":
        bidders = False
    else:
        print("Invalid Choice")
    
print(f"The winner of the bid is {winner} of amount ${maxBid} ")
