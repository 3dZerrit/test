import random

UserI = input()
BotI = random.randrange(0, 21)
V2 = "shit"

if UserI == V2:
    print("skill issue")
else:
    if UserI != int(BotI):
        print("The number was " + str(BotI))
        print("Stupid Looser")
    else: 
        print("Sucker you beat me")

