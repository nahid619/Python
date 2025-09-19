import random

user_wins=0
com_wins=0
options = ['rock','paper','scissors']

while True:
    user_input=input('Type Rock/Paper/Scissor or Q to quit: ').lower()
    if user_input == 'q':
        break

    if user_input not in options:
        print('INVALID')
        continue
    
    random_number = random.randint(0,2)
    #0=rock #1=paper #2=scissor
    com_pick = options[random_number]
    print('Computer picks',com_pick+'.')
    
    if user_input == 'rock' and com_pick=='scissors':
        print('Hurray You Won!')
        user_wins+=1
    elif user_input == 'paper' and com_pick=='rock':
        print('Hurray You Won!')
        user_wins+=1
    elif user_input == 'scissors' and com_pick=='paper':
        print('Hurray You Won!')
        user_wins+=1
    elif user_input == com_pick:
        print("It's a draw")
    else:
        print('Upps you Lost!')
        com_wins+=1


if com_wins > user_wins:
    print('Computer won',com_wins,'times')
    print('you won',user_wins,'times')
else: 
    print('you won',user_wins,'times')
    print('Computer won',com_wins,'times')

print('Good Bye')

