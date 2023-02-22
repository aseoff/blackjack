import pandas as pd
import ast
from statistics import mean

num_samples = 10
all_results = []
for sample in range(0,num_samples):
    result = []
    df = pd.read_csv(f'sample_format{sample+1}.csv')
    #df.head()

    #Create $5 bet size consistent per hand --> no pressing
    min_bet = 10
    bet_size = 5
    df['min_consistent'] = df['result(s)'] * min_bet

    consec_wins = 0
    
    for index, row in df.iterrows():
        total_bet = min_bet + (bet_size * consec_wins)
        pressed_result = total_bet * int(row['result(s)'])
        # Assign the new value to the new column
        df.loc[index, 'pressed_result'] = pressed_result
        if row['result(s)'] >= 0:
            consec_wins = consec_wins + 1
        elif row['result(s)'] == 0:
            consec_wins = consec_wins
        else:
            consec_wins = 0

    for index, row in df.iterrows():
        true_count = float(row['true_count'])
        print("TRUE COUNT: ", true_count)
        spread_result = 0
        if true_count < 1.5:
            spread_result = min_bet * float(row['result(s)'])
            df.loc[index, 'spread_result'] = spread_result
        elif true_count >= 1.5 and true_count < 2.5:
            spread_result = (min_bet*2) * float(row['result(s)'])
            df.loc[index, 'spread_result'] = spread_result
        elif true_count >= 2.5 and true_count < 3.5:
            spread_result = (min_bet*4) * float(row['result(s)'])
            df.loc[index, 'spread_result'] = spread_result
        elif true_count >= 3.5:
            spread_result = (min_bet*8) * float(row['result(s)'])
            df.loc[index, 'spread_result'] = spread_result
        
    print("Total profit with consistent betting: ", sum(df['min_consistent']))
    print("Total profit with pressed betting: ", sum(df['pressed_result']))
    print("Total profit with spread betting: ", sum(df['spread_result']))

    df.to_csv("check.csv", index = False)

    result = [sample+1, sum(df['min_consistent']), sum(df['pressed_result']), sum(df['spread_result'])]
    
    all_results.append(result)
    # Assign the new value to the new column

data = all_results
df = pd.DataFrame(data, columns = ['sample_num', 'min_every_time', 'pressed_bets', 'count_1_8'])
df.to_csv(f'final_results.csv', index = False)


