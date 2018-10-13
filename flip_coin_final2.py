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
while count < 100:                                                   
    coin = random.randint(0, 1)
    if coin == 0:
        headsCount += 1
    else:
        tailsCount += 1
    count += 1


print("The number of heads is", headsCount)
print("The number of tails is", tailsCount)

input("\n\nPress the enter key to exit.")


