import random

print("Choose your highest number: ")
top_num = input()

if top_num.isdigit():
    top_num = int(top_num)

    if top_num<=0:
        print('Please type a number greater than zero. Thank you!')
        exit()
else:
    exit()


correct=random.randint(0,top_num)
gues = 0

while True:
    gues +=1
    user_input = input("Guess a number: ")
    if user_input.isdigit():
        user_input = int(user_input)
    else:
        print('Please type a number next time.')
        continue
    
    if user_input == correct:
        print('Hurray you are correct.')
        break
    elif user_input < correct:
        print('you were below the number')
    else:
        print('You were above the number')


if gues==1:
    print('Your Are the GOAT. Answer in',gues,'try')
else:
    print(f'you got it in {gues} times')
