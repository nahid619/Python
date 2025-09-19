print('Welcome to my computer Quize!')

playing=input("do you want to play? ")
#print(playing)

if playing.lower() !="yes":
    quit()

print("OK. Let's Gooooooo......")
score = 0

answer=input('1. what does cpu stand for? ')
if answer.lower() =="central processing unit":
    print('Correct!')
    score+=1
else:
    print('Wrong Answer')

answer=input('2. what does Gpu stand for? ')
if answer.lower() =="graphics processing unit":
    print('Correct!')
    score+=1
else:
    print('Wrong Answer')

answer=input('3. what does RAM stand for? ')
if answer.lower() =="random access memory":
    print('Correct!')
    score+=1
else:
    print('Wrong Answer')

answer=input('4. what is google? ')
if answer.lower() =="search engine":
    print('Correct!')
    score+=1
else:
    print('Wrong Answer')


print('you got ' + str(score) + ' quetions correct')
print(f'You got {(score/4)*100}% correct.')