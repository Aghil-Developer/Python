from blind_auction_utils import logo,highestbid,intro

bids={}
contineBid = True


print(logo)
print(intro())


while contineBid:

    name = input("Enter your name: ")
    amount = int(input("Enter the amount:$ "))

    bids[name] = amount

    shouldContinue = input("Are there anymore bidders? Type 'yes' or 'no': ")

    if shouldContinue.lower() == "no":
        highestbid(bids)
        contineBid = False

