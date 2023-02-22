#STRATEGY
# #----------------------------
def strategy(dealer_show_card, player_hand):
    if sum(player_hand) > 21 and 11 in player_hand:
        player_hand[player_hand.index(11)] = 1
    #1) High dealer cards
    #NO ACE
    if dealer_show_card in [7,8,9,10,11] and 11 not in player_hand:
        #DD
        if sum(player_hand)in [10,11] and dealer_show_card in [7,8,9]:
            return 'DD'
        elif sum(player_hand) == 11 and dealer_show_card == 10:
            return 'DD'
        
        #Split

        #Hit
        elif sum(player_hand) in [4,5,6,7,8,9,12,13,14,15,16]:
            return 'H'
        elif sum(player_hand) in [10,11] and dealer_show_card == 11:
            return 'H'
        elif sum(player_hand) == 10 and dealer_show_card == 10:
            return 'H'
        #Stay
        elif sum(player_hand) in [17,18,19,20,21]:
            return 'S'
        else:
            print("A case was missed for dealer showing 7-11 with no ace in player hand")

    #ACE
    elif dealer_show_card in [7,8,9,10,11] and 11 in player_hand:
        #HIT
        if sum(player_hand) in [13,14,15,16,17]:
            return 'H'
        elif sum(player_hand) == 18 and dealer_show_card in [9,10,11]:
            return 'H'
        #STAND
        elif sum(player_hand) == 18 and dealer_show_card in [7,8]:
            return 'S'
        elif sum(player_hand) in [19,20]:
            return 'S'
        else:
            print("A case was missed for dealer showing 7-11 with ACE in player hand")
    #----------------------------
    #2) 5 and 6 dealer card
    #NO ACE
    elif dealer_show_card in [5,6] and 11 not in player_hand:
        #DD
        if sum(player_hand) in [9,10,11]:
            return 'DD'
        #SPLIT

        ##HIT
        elif sum(player_hand) in [4,5,6,7,8]:
            return 'H'
        #STAY
        elif sum(player_hand) in [12,13,14,15,16,17,18,19,20]:
            return 'S'
        else:
            print("A case was missed for dealer showing 5 or 6 with NO ace in player hand")

    #ACE
    elif dealer_show_card in [5,6] and 11 in player_hand:
        #DD
        if sum(player_hand) in [13,14,15,16,17,18]:
            return 'DD'
        #SPLIT

        ##HIT

        #STAY
        elif sum(player_hand) in [19,20]:
            return 'S'
        else:
            print("A case was missed for dealer showing 5 or 6 with ACE in player hand")
    #----------------------------
    #3) 2,3,4 dealer cards
    #NO ACE
    if dealer_show_card in [2,3,4] and 11 not in player_hand:
        #DD
        if sum(player_hand) in [10,11]:
            return 'DD'
        elif sum(player_hand) == 9 and dealer_show_card in [3,4]:
            return 'DD'
        #Split

        #Hit
        elif sum(player_hand) in [4,5,6,7,8]:
            return 'H'
        elif sum(player_hand) == 9 and dealer_show_card == 2:
            return 'H'
        elif sum(player_hand) == 12 and dealer_show_card in [2,3]:
            return 'H'
        #Stay
        elif sum(player_hand) == 12 and dealer_show_card == 4:
            return 'S'
        elif sum(player_hand) in [13,14,15,16,17,18,19,20]:
            return 'S'
        else:
            print("Missing a case when dealer showing 2,3,4 and player has NO ace")

    #ACE
    if dealer_show_card in [2,3,4] and 11 in player_hand:
        #DD
        if sum(player_hand) in [15,16,17,18] and dealer_show_card == 4:
            return 'DD'
        elif sum(player_hand) in [17,18] and dealer_show_card == 3:
            return 'DD'
        #Split

        #Hit
        elif sum(player_hand) in [13,14]:
            return 'H'
        elif sum(player_hand) in [15,16] and dealer_show_card in [2,3]:
            return 'H'
        elif sum(player_hand) == 17 and dealer_show_card == 2:
            return 'H'
        #Stay
        elif sum(player_hand) == 18 and dealer_show_card == 2:
            return 'S'
        elif sum(player_hand) in [19,20]:
            return 'H'
        else:
            print("Missing a case when dealer showing 2,3,4 and player has ACE")


#MAIN------------------------
#Create player and dealer hands
player_hand = []
dealer_hand = []

#Simulate all hands
dealer_cards = [2,3,4,5,6,7,8,9,10,11]
player_cards = [2,3,4,5,6,7,8,9,10,11]
for dealer_card in dealer_cards:
    for player_card1 in player_cards:
        for player_card2 in player_cards:
            player_hand = [player_card1, player_card2]
            print("\nDealer card is: ", dealer_card)
            print("\nPlayer has: ", player_hand)
            print("\nStrategy says: ", strategy(dealer_card, player_hand))

