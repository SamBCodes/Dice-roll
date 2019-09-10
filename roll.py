import random
import time

while 1:
    high = int(input("Enter Highest face:"))
    print("Your number is", end=' ')
    for i in range(3):
        time.sleep(0.4)
        print('.', end=' ')
    time.sleep(0.4)
    print(random.randrange(1, high+1, 1))
    true = str(input("Roll Again(y/n)?"))
    if true == 'n':
        break
    elif true == 'y':
        continue
    else:
        print('Wrong Choice! Exiting!')
        exit
