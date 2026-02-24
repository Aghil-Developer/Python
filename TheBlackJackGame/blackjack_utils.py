import random

#Art
art = '''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/           '''
# Random Number Generator
def randomNumber():
    return random.randint(1, 10)


# BlackJack Game Logic
def blackJack(player,dealer):
    condition = True
    while condition:
        choice = input("Do you want to hit or stand(h/s): ") 
        if choice == "h":
            player.append(randomNumber())
            print("Player's hand:", player)
            if sum(player) > 21:
                print("Computer Final hand:", dealer)
                print("Player Final hand:", player)
                print("Player busts! Dealer wins.")
                condition = False
        elif choice == "s":
                print("Player stands.")
                dealer.append(randomNumber())
                print("Dealer's hand:", dealer)
                if sum(dealer) > 21:
                    print("Computer Final hand:", dealer)
                    print("Player Final hand:", player)
                    print("Dealer busts! Player wins.")
                    condition = False
                elif sum(dealer) > sum(player):
                    print("Computer Final hand:", dealer)
                    print("Player Final hand:", player)
                    print("Dealer wins.")
                    condition = False
                elif sum(dealer) < sum(player):
                    print("Computer Final hand:", dealer)
                    print("Player Final hand:", player)
                    print("Player wins.")
                    condition = False