import random

#Title and Intro
print("\n\t\t\tFlip a Coin\n\n")

#Let the user 'flip' the coin
input("\nPress the enter key to 'flip' the coin a hundred times \
and find out the number of heads and tails you've flipped.\n\n")

# set the coin

headsCount = 0
tailsCount = 0
count = 0

# the loop
#If you declar The while loop condition should be less than 100.
#Otherwise you will get 101 counts.
while count < 100:                                                   
    coin = random.randint(0, 1)
    if coin == 0:
        headsCount += 1
    else:
#Because We already declared randint(1, 2).
#So the coin value is 0 or 1.So we can use else condition.
        tailsCount += 1
    count += 1


print("The number of heads was", headsCount)
print("The number of tails was", tailsCount)

input("\n\nPress the enter key to exit.")

#http://python.6.x6.nabble.com/Tutor-While-Loops-Coin-Flip-Game-
#td1687001.html
