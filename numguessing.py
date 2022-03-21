import time
import random
print("-----    Welcome to Number Guessing Game - Created by Feyzullah Akyüz    ----- \n")
time.sleep(3)
print("I will keep a number between 0 and 100 in my mind and you will try to find the number.  \n")
time.sleep(3)
print("Give me one second , Just I think  \n")
time.sleep(3)
realnumber = random.randrange(1,100)
print("Okey , I kept a number in my mind, let's see if you can find it? ")

while (True):
    num = int(input("What is your guess ? :  "))
    if(num > realnumber):
        print("Under ! ")
        continue
    elif (num < realnumber):
        print("Over ! ")
        continue
    elif (num == realnumber):
        input("You win ! Thanks for playing ....")
        break