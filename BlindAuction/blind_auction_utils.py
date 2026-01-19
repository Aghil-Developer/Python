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

bidding_details = {}
def blindBid(name,amount):
    
    maxBiddAmount = 0
    maxBidderName = ""

    bidding_details[name] = amount

    for i in bidding_details:
        if bidding_details[name] > bidding_details[i]:
            maxBiddAmount = amount
            maxBidderName = name
            
    return [maxBiddAmount,maxBidderName]