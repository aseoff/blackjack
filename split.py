deck = [5,6,7,6,8,10]
hand = [8,8]

def split(original_hand):
    #Create list to hold split hands
    split_hands = []
    two_cards_per_hand = False
    
    #split og hand into two new hands
    hand1 = [original_hand[0]]
    hand2 = [original_hand[1]]

    #Add new hands to list of split hands
    split_hands.append(hand1)
    split_hands.append(hand2)

    #Add a card and check if pair
    while two_cards_per_hand == False:
        for hand in split_hands:
            if len(hand) == 1:
                hand.append(deck.pop())
                if hand[0] == hand[1] and len(split_hands) < 4:
                    #Split the hand again
                    new_hand1 = [hand[0]]
                    new_hand2 = [hand[1]]
                    split_hands.remove(hand)
                    split_hands.insert(0, new_hand1)
                    split_hands.insert(1, new_hand2)
                else:
                    #play strategy on that hand
                    print("PLAY STRAT")
        for hand in split_hands:
            if len(hand) == 1:
                two_cards_per_hand = False
                break
            else:
                two_cards_per_hand = True


    print(split_hands)


split(hand)

