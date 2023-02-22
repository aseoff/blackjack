#WORKING VERSION --> not formatted
from statistics import mean
#STRATGIES - METHODS
#--------
#Split strategy
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
#Basic Strategy
def strategy(dealer_show_card, player_hand):
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
        elif sum(player_hand) >= 17:
            return 'S'
        else:
            print("A case was missed for dealer showing 7-11 with no ace in player hand")
            print(player_hand)
            print(dealer_hand)

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
        elif sum(player_hand) >= 19:
            return 'S'
        else:
            print("A case was missed for dealer showing 7-11 with ACE in player hand")
            print(player_hand)
            print(dealer_hand)

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
        elif sum(player_hand) >= 12:
            return 'S'
        else:
            print("A case was missed for dealer showing 5 or 6 with NO ace in player hand")
            print(player_hand)
            print(dealer_hand)

    #ACE
    elif dealer_show_card in [5,6] and 11 in player_hand:
        #DD
        if sum(player_hand) in [13,14,15,16,17,18]:
            return 'DD'
        #SPLIT

        ##HIT

        #STAY
        elif sum(player_hand) >= 19:
            return 'S'
        else:
            print("A case was missed for dealer showing 5 or 6 with ACE in player hand")
            print(player_hand)
            print(dealer_hand)
    #----------------------------
    #3) 2,3,4 dealer cards
    #NO ACE
    elif dealer_show_card in [2,3,4] and 11 not in player_hand:
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
        elif sum(player_hand) >= 13:
            return 'S'
        else:
            print("Missing a case when dealer showing 2,3,4 and player has NO ace")
            print(player_hand)
            print(dealer_hand)
    #ACE
    elif dealer_show_card in [2,3,4] and 11 in player_hand:
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
        elif sum(player_hand) >= 19:
            return 'S'
        else:
            print("Missing a case when dealer showing 2,3,4 and player has ACE")
            print(player_hand)
            print(dealer_hand)

    else:
        print("YOU MISSED SOMETHING...")
#--------
#Check pair
def pair(hand):
    if len(hand) >= 2:
        if hand[0] == hand[1]:
            return True
    else:
        return False

#player moves
def player_moves(dealer_hand, player_hand):
    dealer_show_card = dealer_hand[0]
    continue_player_hand = True
    can_double_down = True
    did_double_down = False
    while continue_player_hand:
        print("PLAYER HAND IS NOW: ", player_hand)
        if sum(player_hand) > 21 and 11 in player_hand:
            print("CHANGING ACE FROM 11 TO 1 TO SAVE THE BUST!")
            player_hand[player_hand.index(11)] = 1
        move = strategy(dealer_show_card, player_hand)
        if move == 'DD' and can_double_down == True:
            print("DOUBLE DOWN")
            print("PLAYER HAND IS NOW: ", player_hand)
            #Give the player 1 card
            player_hand.append(shuffled_deck.pop())
            did_double_down = True
            #End of player hand
            continue_player_hand = False
            #set can double down to false
            can_double_down = False
        elif move == 'DD' and can_double_down == False:
            #Simply Hit
            player_hand.append(shuffled_deck.pop())
            #continue the hand
            continue_player_hand = True
        elif move == 'H':
            #Give the player 1 card
            player_hand.append(shuffled_deck.pop())
            #continue the hand
            continue_player_hand = True
            #no longer can double down
            can_double_down = False
        elif move == 'S':
            #end the hand
            continue_player_hand = False
        else:
            print("You missed a move! Check all cases")
            print("PLAYER HAS: ", player_hand)
            print("DEALER HAS: ", dealer_hand)
    
    return [player_hand, did_double_down]

#dealer moves
def dealer_moves(dealer_hand):
    continue_dealer_hand = True
    while continue_dealer_hand:
        print("DEALER HAND IS NOW: ", dealer_hand)
        if sum(dealer_hand) > 21 and 11 not in dealer_hand:
            #dealer bust
            continue_dealer_hand = False

        elif sum(dealer_hand) > 21 and 11 in dealer_hand:
            dealer_hand[dealer_hand.index(11)] = 1
            print("DEALER ACE SAVING THE DEALER BUST")
            continue_dealer_hand = True
        
        elif sum(dealer_hand) < 17:
            dealer_hand.append(shuffled_deck.pop())

        elif sum(dealer_hand) >= 17 and sum(dealer_hand) <= 21:
            #No nore cards
            continue_dealer_hand = False
        else:
            print("You missed a case for the dealer")
    
    return dealer_hand

#record hand result
def record_hand_result(player_hand, dealer_hand, did_double_down):
    #SHOW FINAL COUNTS
    print("Final player sum: ", sum(player_hand))
    print("Final dealer hand:", sum(dealer_hand))

    if sum(player_hand) > sum(dealer_hand) and sum(player_hand) <= 21 and did_double_down == False:
        print("PLAYER WINS")
        return 'p'
    elif sum(player_hand) > sum(dealer_hand) and sum(player_hand) <= 21 and did_double_down == True:
        print("PLAYER WINS ON DOUBLE DOWN")
        return 'pdd'
    elif sum(dealer_hand) > sum(player_hand) and sum(dealer_hand) <= 21 and did_double_down == False:
        print("DEALER WINS")
        return 'd'
    elif sum(dealer_hand) > sum(player_hand) and sum(dealer_hand) <= 21 and did_double_down == True:
        print("DEALER WINS ON PLAYER DOUBLE DOWN")
        return 'ddd'
    elif sum(dealer_hand) > 21 and sum(player_hand) <= 21 and did_double_down == False:
        print("PLAYER WINS ON DEALER BUST")
        return 'p'
    elif sum(dealer_hand) > 21 and sum(player_hand) <= 21 and did_double_down == True:
        print("PLAYER WINS ON DEALER BUST WITH DOUBLE DOWN")
        return 'pdd'
    elif sum(player_hand) > 21:
        print("DEALER WINS ON PLAYER BUST")
        return 'd'
    else:
        print("PUSH")
        return 'pu'

#Splitting
def split(original_hand):
    #Create list to hold split hands
    split_hands = []
    dd_status = []
    two_cards_per_hand = False
    
    #split og hand into two new hands
    hand1 = [original_hand[0]]
    hand2 = [original_hand[1]]

    #Add new hands to list of split hands
    split_hands.append(hand1)
    split_hands.append(hand2)

    #check if pair is aces
    if hand1[0] == 11:
        print("SPLITTING ACES")
        for hand in split_hands:
            if len(hand) == 1:
                hand.append(shuffled_deck.pop()) #ALL HANDS NOW HAVE 2 CARDS
        
        #CHECK DOUBLE ACE CASE ON THE SPLIT
        for hand in split_hands:
            if hand[0] == hand[1]:
                print("ANOTHER ACE AFTER INITIAL ACE SPLIT --> CHANGING ACE to 1")
                hand[1] = 1

        dd_status = [False, False]         
            
    #Add a card and check if new pair (non aces)
    else:
        while two_cards_per_hand == False:
            for hand in split_hands:
                if len(hand) == 1:
                    hand.append(shuffled_deck.pop()) #ALL HANDS NOW HAVE 2 CARDS
                    if hand[0] == hand[1] and len(split_hands) < 4 and hand[0] != 11:
                        #Split the hand again
                        new_hand1 = [hand[0]]
                        new_hand2 = [hand[1]]
                        split_hands.remove(hand)
                        split_hands.insert(0, new_hand1)
                        split_hands.insert(1, new_hand2)
                    else:
                        #Play strategy once hands all have 2 cards and no pairs/pairs maxed out
                        hand_info = player_moves(dealer_hand, hand)
                        hand = hand_info[0]
                        dd_status.insert(split_hands.index(hand), hand_info[1])
            for hand in split_hands:
                if len(hand) == 1:
                    two_cards_per_hand = False
                    break
                else:
                    two_cards_per_hand = True
    
    print(split_hands)
    print(dd_status)
    return [split_hands, dd_status]

def simulate_hand():
    #Check for player BJ
    if sum(player_hand) == 21:
        if dealer_show_card == 11 and sum(dealer_hand) == 21:
            #Dealer also has blackjack with ace showing --> even money
            print("PLAYER AND DEALER HAVE BLACKJACK")
            results.append('p')
            return 'p'
        elif dealer_show_card == 10 and sum(dealer_hand) == 21:
            #Dealer also has blackjack with 10 showing --> push
            print("PLAYER AND DEALER HAVE BLACKJACK")
            results.append('pu')
            return 'pu'
        else:
            #Dealer does not have blackjack --> player gets 3:2 money
            print("PLAYER HAS BLACKJACK")
            results.append('pbj')
            return 'pbj'

    elif sum(dealer_hand) == 21:
        #Dealer has blackjack and player does not --> player loses
        print("DEALER HAS BLACKJACK")
        results.append('d')
        return 'd'

    else:
        #NO BLACKJACKS TO START PLAY THE HAND HERE
        #1) Check pair
        if pair(player_hand):
            #Create split card
            split_card = player_hand[0]
            #Check split (max 4 splits minus aces)
            if split_strategy(dealer_show_card, split_card) == 'split':
                print("SPLIT CASE!")
                split_details = split(player_hand)
                final_split_hands = split_details[0]
                split_hands_dds = split_details[1]

                all_splits_bust = False
                for hand in final_split_hands:
                    if sum(hand) <= 21:
                        all_splits_bust = False
                        break
                    else:
                        all_splits_bust = True
                if all_splits_bust == True:
                    print("ALL SPLITS BUSTED VERY RARE CASE")
                    dealer_final_hand = dealer_hand
                else:
                    dealer_final_hand = dealer_moves(dealer_hand)
                
                for hand in final_split_hands:
                    results.append(record_hand_result(hand, dealer_final_hand, split_hands_dds[final_split_hands.index(hand)]))
                
                
                # print("FINAL SPLIT HANDS: ", final_split_hands)
                # print("FINAL SPLIT DD STATUSES: ", split_hands_dds)

            else:
                #Don't split
                #play strategy (plug it in!)
                hand_info = player_moves(dealer_hand, player_hand)
                player_final_hand = hand_info[0]
                dd = hand_info[1]
                if sum(player_final_hand) > 21:
                    print("No need to draw dealer cards after player bust (pair case)")
                    dealer_final_hand = dealer_hand
                else:
                    dealer_final_hand = dealer_moves(dealer_hand)
                
                results.append(record_hand_result(player_final_hand, dealer_final_hand, dd))

            
            
        else:
            #Don't split
            #play strategy (plug it in!)
            hand_info = player_moves(dealer_hand, player_hand)
            player_final_hand = hand_info[0]
            dd = hand_info[1]
            if sum(player_final_hand) > 21:
                print("No need to draw dealer cards after player bust (non split case)")
                dealer_final_hand = dealer_hand
            else:
                dealer_final_hand = dealer_moves(dealer_hand)
            
            results.append(record_hand_result(player_final_hand, dealer_final_hand, dd))

#MAIN-------------------------
#GAME FLOW OUTLINE
import random as rand

#Create deck(s)
cards_in_deck = [2,3,4,5,6,7,8,9,10,10,10,10,11]
deck = cards_in_deck * 24 #6 decks
# print(deck)
# print(len(deck))

#Shuffle deck(s)
rand.shuffle(deck)
shuffled_deck = deck
print(shuffled_deck)

#check cards in deck

#number of hands counter
results = []
overall_results = []

num_simulations = int(input("How many simulations: "))
num_hands = int(input("How many hands per simulation: "))
for x in range (0,num_simulations):
    results = []
    for i in range(0,num_hands):
        if len(shuffled_deck) < 25:
            print("resetting deck")
            print(shuffled_deck)
            #reset deck
            cards_in_deck = [2,3,4,5,6,7,8,9,10,10,10,10,11]
            deck = cards_in_deck * 24 #6 decks
            rand.shuffle(deck)
            shuffled_deck = deck

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

        #cards visible to player
        print("Player has: ", player_hand)
        print("Dealer showing: ", dealer_hand[0])

        #create variable called dealer_show_card
        dealer_show_card = dealer_hand[0]
        
        simulate_hand()
    
    regular_wins = results.count('p')
    dd_wins = results.count('pdd')
    player_bj = results.count('pbj')
    regular_losses = results.count('d')
    dd_losses = results.count('ddd')
    pushes = results.count('pu')
    round_results = [regular_wins,dd_wins,player_bj,regular_losses,dd_losses,pushes]
    
    overall_results.append(round_results)
    

print(overall_results)

profits = []
winning_percent = []
house_edges = []
for result in overall_results:
    house_edge = 0
    wins = result[0] + (result[1]*2) + (result[2]*1.5)
    losses = (result[3]*1) + (result[4]*2)
    print("LOSSES: ", losses)
    amount_wagered = result[0] + (result[1]*2) + result[2] + (result[3]*1) + (result[4]*2) + result[5]
    print("AMOUNT WAGERED: ", amount_wagered)
    house_edge = (losses) / (amount_wagered)
    house_edges.append(house_edge)
    
print(house_edges)
print("Average house edge: ", mean(house_edges), "%")
