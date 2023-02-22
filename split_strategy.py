#SPLIT STRATEGY
#---------------------
def split_strategy(dealer_show_card, player_card):
    #1) Dealer showing 8-11
    if dealer_show_card in [8,9,10,11]:
        #No split
        if player_card in [2,3,4,5,6,7,10]:
            return 'NS'
        elif player_card == 9 and dealer_show_card in [10,11]:
            return 'NS'
        #Split:
        elif player_card in [8,11]:
            return 'split'
        elif player_card == 9 and dealer_show_card in [8,9]:
            return 'split'
        else:
            print("You missed a split case with dealer showing 8-11")

    #2) Dealer showing 5-7
    elif dealer_show_card in [5,6,7]:
        #No split
        if player_card in [4,6,9] and dealer_show_card == 7:
            return 'NS'
        elif player_card in [5,10]:
            return 'NS'
        #Split
        elif player_card in [2,3,8,9,11]:
            return 'split'
        elif player_card in [4,6,7] and dealer_show_card != 7:
            return 'split'
        elif player_card == 7 and dealer_show_card == 7:
            return 'split'
        else:
            print("You missed a split case with dealer showing 5-7")

    #3) Dealer showing 2-4
    elif dealer_show_card in [2,3,4]:
        #No split
        if player_card in [4,5,10]:
            return 'NS'
        #Split
        elif player_card in [2,3,6,7,8,9,11]:
            return 'split'
        else:
            print("You missed a split case with dealer showing 2-4")


#MAIN-----------------
#Simulate all pairs
dealer_cards = [2,3,4,5,6,7,8,9,10,11]
player_cards = [2,3,4,5,6,7,8,9,10,11]
for dealer_card in dealer_cards:
    for player_card in player_cards:
        print("\nDealer card is: ", dealer_card)
        print("\nPlayer has a pair of: ", player_card)
        print("\nStrategy says: ", split_strategy(dealer_card, player_card))