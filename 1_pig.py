import random

def roll():
    min_value=1
    max_value=6
    roll = random.randint(min_value,max_value)
    return roll

while True:
    player = input('Enter the number of players (2-4): ')
    if player.isdigit():
        player = int(player)
        if 2<=player<=4:
            break  
        else:
            print("must be between 2-4 players.")      
    else:
        print('invalid! try again:- ')

max_score = 50
player_scores = [ 0 for _ in range(player)]

while max(player_scores)<max_score:
    for i in range(player):
        print("\nPlayer",i+1,"turn has started")
        print("your total score is: ", player_scores[i],'\n')
        current_score=0

        while True:
            should_roll = input("would you like to roll(y): ").lower()
            if should_roll != 'y':
                break
            
            value = roll()
            if value==1:
                print("you rolled 1! turn done")
                current_score = 0 
                break
            else: 
                current_score += value
                print("you rolled a:",value)

            print("your score is: ",current_score)

        player_scores[i]+=current_score
        print("your total score is: ", player_scores[i])


max_score=max(player_scores)
winning_index=player_scores.index(max_score)
print("player number",winning_index+1,"won with",max_score)
