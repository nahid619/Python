name=input('Type your name- ')
print('Welcome',name,'to this adventure')


x=input('yes or no! option? ').lower()
if x != 'yes':
    print('Thanks for visiting.')
    exit()

answer = input("you have come to an end and you can go leftt or right. which way would you like to go? ").lower()

if answer=='left':
    print('you came to a river.')
    print('you can walk around it or swim through it.')
    answer=input("what you want to do? ").lower()
    if answer=='swim':
        print('you swim across and eaten by elegater')
    elif answer=='walk':
        print('you walk many miles and died of being hungry')
    else:
        print('INVALID OPTION!')

elif answer=='right':
    print('you came to a broken bridge.')
    print('you can walk around it or go over it.')
    answer=input("what you want to do? ").lower()
    
    if answer=='over':
        print('the brid broke and you fell into the river.')
    
    elif answer=='walk':
        print('you walk many miles and came to a strange village.')
        answer=input('do you want to stay in the village?(yes or no) ').lower()
        
        if answer=='yes':
            print('welcome to the village')
        elif answer == 'no':
            print('congratualtions you are safe. you take some food and walk away.')
        else:
         print('INVALID OPTION!')   
   
    else:
        print('INVALID OPTION!')

else:
    print('INVALID OPTION!')


