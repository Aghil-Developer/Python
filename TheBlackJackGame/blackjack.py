from blackjack_utils import blackJack, randomNumber,art

print(art)


# Track Player&Dealer Score
player = []
dealer = []


startGame = input("Do you want to play BlackJack? (y/n): ")
if startGame == "y":

    # Player Intialization
    player.append(randomNumber())
    player.append(randomNumber())
    
    # Dealer Intialization
    dealer.append(randomNumber())
    dealer.append(randomNumber())
    print("Player's hand:", player)
    print("Dealer's hand:",dealer[0])

    # Game Logic
    blackJack(player,dealer)
        