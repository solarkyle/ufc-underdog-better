# got the data from https://www.kaggle.com/mdabbert/ufc-fights-2010-2020-with-betting-odds


import pandas as pd

file = pd.read_csv('Documents/ufc.csv')
file = file.dropna()

number = 200
total_profit = 0
dog_winner = 0
for index, row in file.iterrows():
    R_fighter = row['R_fighter']
    B_fighter = row['B_fighter']
    R_odds = row['R_odds']
    B_odds = row['B_odds']
    Winner = row['Winner']
    
    if R_odds < B_odds:
        dog = 'Blue'
        dog_odds = B_odds
    else:
        dog = 'Red'
        dog_odds = R_odds

    if dog_odds > number:


        if Winner == dog:
            dog_winner += 1
            total_profit += dog_odds
            #print(f'you won ${dog_odds} on {R_fighter} vs {B_fighter}')
        else:
            total_profit-=100
            #print(f'you lost $100 on {R_fighter} vs {B_fighter}')


print(dog_winner)
print(f'You would have won ${int(total_profit)}')