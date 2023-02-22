import pandas as pd
import ast
from statistics import mean

def calculate_count(card):
    if card in [2,3,4,5,6]:
        count = 1
    elif card in [1,10,11]:
        count = -1
    else:
        count = 0
    
    return count

num_samples = 10

for sample in range(0,num_samples):
    df = pd.read_csv(f'sample{sample+1}.csv')
    #df.head()
# Loop through the rows of the DataFrame
    flists = []
    running_count = 0
    prev_remaining_cards = 0
    
    for index, row in df.iterrows():
        if row['num_remaining_cards'] > prev_remaining_cards:
            running_count = 0
        prev_remaining_cards = row['num_remaining_cards']
        player_starting_hand = ast.literal_eval(row['player_starting_hand'])
        if 11 in player_starting_hand:
            soft_status = 'soft'
        else:
            soft_status = 'hard'
        
        hand_id = int(row['hand_id'])
        dealer_show_card = int(row['dealer_show_card'])
        player_starting_sum = sum(player_starting_hand) #--> in df
        dealer_starting_hand = ast.literal_eval(row['dealer_starting_hand'])
        dealer_starting_sum = sum(dealer_starting_hand) #--> in df
        player_final_hands = ast.literal_eval(row['player_final_hand(s)'])
        dealer_final_hand = ast.literal_eval(row['dealer_final_hand'])
        dealer_final_sum = sum(dealer_final_hand)
        hand_result = row['result(s)']
        split_status  = 'no split'
        split_hand_sums = []
        remaining_cards = int(row['num_remaining_cards'])
        remaining_decks = remaining_cards // 52
        true_count = 0
        
        print(player_final_hands)
        for card_or_hand in player_final_hands:
            if isinstance(card_or_hand, int):
                #print(card_or_hand)
                #print("NO SPLIT")
                player_final_sum = sum(player_final_hands) #--> in df
                split_status = 'no split'
                num_hands = 1
                running_count = running_count + calculate_count(card_or_hand)
                print('running count: ', running_count)
                #break
            else:
                #print("SPLIT")
                split_status = 'split'
                split_hand_sums.append(sum(card_or_hand)) #[18,16]
                
                print(card_or_hand)
                for card in card_or_hand:
                    running_count = running_count + calculate_count(card)
                    print("running count: ", running_count)
                #print(isinstance(card_or_hand, list))

        print(dealer_final_hand)
        for card in dealer_final_hand:
            running_count = running_count + calculate_count(card)
            print("running count: ", running_count)

        if split_status == 'split':
            player_final_sum = mean(split_hand_sums)
            num_hands = len(split_hand_sums)

        #Numeric results
        numeric_result = 0
        if hand_result not in ['p','d','pu','pdd','ddd','pbj']:
            #SPLIT HAND
            hand_result = ast.literal_eval(hand_result)
            #print(hand_result)
            for result in hand_result:
                #print(result)
                if result == 'p':
                    numeric_result = numeric_result + 1
                elif result == 'd':
                    numeric_result = numeric_result - 1
                elif result == 'pu':
                    numeric_result = numeric_result
                elif result == 'pdd':
                    numeric_result = numeric_result + 2
                elif result == 'ddd':
                    numeric_result = numeric_result -2
                elif result == 'pbj':
                    numeric_result = numeric_result + 1.5
                #print(numeric_result)
        
        else:
            #ONE RESULT
            if hand_result == 'p':
                numeric_result = 1
            elif hand_result == 'd':
                numeric_result = -1
            elif hand_result == 'pu':
                numeric_result = 0
            elif hand_result == 'pdd':
                numeric_result = 2
            elif hand_result == 'ddd':
                numeric_result = -2
            elif hand_result == 'pbj':
                numeric_result = 1.5

        if remaining_decks == 0:
            true_count = running_count // 1
        else:
            true_count = float(running_count) / float(remaining_decks)
        
        frow = [hand_id, player_starting_sum, soft_status, split_status, num_hands, dealer_show_card, player_final_sum, dealer_final_sum, numeric_result, remaining_cards, remaining_decks, player_final_hands, dealer_final_hand, running_count, true_count]
        flists.append(frow)

    #Create dataframe with hand info
    data = flists
    df = pd.DataFrame(data, columns = ['hand_id', 'player_starting_sum','soft_status','split_status','num_hands','dealer_show_card', 'player_final_sum','dealer_final_sum','result(s)', 'num_remaining_cards', 'remaining_decks', 'player_final_hands', 'dealer_final_hand', 'running_count','true_count'])
    #df.head(10)
    
    df.to_csv(f'sample_format{sample+1}.csv', index = False)