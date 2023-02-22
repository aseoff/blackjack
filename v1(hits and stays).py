import random as rand

#Create deck(s)
cards_in_deck = [2,3,4,5,6,7,8,9,10,10,10,10,11]
deck = cards_in_deck * 4
# print(deck)
# print(len(deck))

#Shuffle deck(s)
rand.shuffle(deck)
shuffled_deck = deck
print(shuffled_deck)

#Play a full hand
def play_hand():
    
    play = True
    
    #Create player and dealer hands
    player_hand = []
    dealer_hand = []

    #Deal initial cards
    player_hand.append(shuffled_deck.pop())
    dealer_hand.append(shuffled_deck.pop())
    player_hand.append(shuffled_deck.pop())
    dealer_hand.append(shuffled_deck.pop())

    #check hands
    print(player_hand)
    print(dealer_hand)

    #check cards in deck
    print(len(shuffled_deck))

    #cards visible to player
    print("Player has: ", player_hand)
    print("Dealer showing: ", dealer_hand[0])

    #create variable called dealer_show_card
    dealer_show_card = dealer_hand[0]

    #check for player blackjack
    if sum(player_hand) == 21:
        print("PLAYER HAS BLACKJACK") #check dealer and then end hand
        play = False
    #check for dealer blackjack (if necessary)
    if sum(dealer_hand) == 21:
        print("DEALER HAS BLACKJACK") #hand is over
        play = False
    while play:
        #IMPLEMENTING THE STRATEGY (REMEMBER ACES)
        #1) Dealer high card up
        if dealer_show_card in [7,8,9,10,11]:
            #Hit case
            if sum(player_hand) < 17:
                print("HIT")
                player_hand.append(shuffled_deck.pop())
                print("New player hand: ", player_hand)
                print("New player sum: ", sum(player_hand))
            
            elif sum(player_hand) > 21 and 11 in player_hand:
                print("PLAYER ACE CASE SAVING THE BUST")
                player_hand[player_hand.index(11)] = 1
            #Stay case
            else:
                print("STAY")
                play = False

        #2) Dealer small/mid card up
        if dealer_show_card in [2,3,4,5,6]:
            #Hit case
            if sum(player_hand) < 12 or (sum(player_hand) < 17 and 11 in player_hand):
                print("HIT")
                player_hand.append(shuffled_deck.pop())
                print("New player hand: ", player_hand)
                print("New player sum: ", sum(player_hand))
            
            elif sum(player_hand) > 21 and 11 in player_hand:
                print("PLAYER ACE CASE SAVING THE BUST")
                player_hand[player_hand.index(11)] = 1
           
            #Stay case
            else:
                print("STAY")
                play = False
    
    #Dealer rules
    dealer_hit = True
    dealer_sum = sum(dealer_hand)
    while dealer_hit:
        if sum(player_hand) > 21:
            break
        if dealer_sum < 17:
            dealer_hand.append(shuffled_deck.pop())
            dealer_sum = sum(dealer_hand)
            print("PLAYER HAS: ", player_hand)
            print("DEALER HAS: ", dealer_hand)
            if 11 in dealer_hand and sum(dealer_hand) > 21:
                print("DEALER ACE SAVING BUST CASE")
                dealer_sum = dealer_sum - 10
                dealer_hand[dealer_hand.index(11)] = 1
        else:
            break

    #SHOW FINAL COUNTS
    print("Final player sum: ", sum(player_hand))
    print("Final dealer hand:", sum(dealer_hand))

    if sum(player_hand) > sum(dealer_hand) and sum(player_hand) <= 21:
        print("PLAYER WINS")
        return 'p'
    elif sum(dealer_hand) > sum(player_hand) and sum(dealer_hand) <= 21:
        print("DEALER WINS")
        return 'd'
    elif sum(dealer_hand) > 21 and sum(player_hand) <= 21:
        print("PLAYER WINS ON DEALER BUST")
        return 'p'
    elif sum(player_hand) > 21:
        print("DEALER WINS ON PLAYER BUST")
        return 'd'
    else:
        print("PUSH")
        return 'pu'


score_list = []
for i in range(0,1000):
    if len(shuffled_deck) < 15:
        #Time to reshuffle
        cards_in_deck = [2,3,4,5,6,7,8,9,10,10,10,10,11]
        deck = cards_in_deck * 4
        rand.shuffle(deck)
        shuffled_deck = deck
    #Play a hand and record the outcome
    score_list.append(play_hand())

print("Player: ", score_list.count('p'))
print("Dealer: ", score_list.count('d'))
print("Pushes: ", score_list.count('pu'))