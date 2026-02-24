logo = """
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-'''---------'' '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
"""
def intro():
    return "Welcome to Blind Bidd!!\nTry to bid higher to keep ahead in the auction , also be careful about your money in your pocket!!S"

def highestbid(biddingDetails):
    winner = ""
    maxbid=0
    for bidder in biddingDetails:
        bid_amount = biddingDetails[bidder]
        if bid_amount > maxbid:
            winner = bidder
            maxbid = bid_amount
    print("The winner of this auction is "+winner+" with a bid amount of $ "+str(maxbid))