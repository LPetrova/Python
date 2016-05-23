from random import randint

n = input('Enter dice side: ')
n = int(n)
player_1 = input('Enter player1 name: ')
player_2 = input('Enter player2 name: ')

dice_1 = randint(1, n)
print(player_1 + ' rolls ' + str(dice_1))

dice_2 = randint(1, n)
print(player_2 + ' rolls ' + str(dice_2))

if dice_1 > dice_2:
    print(player_1 + ' is winner!')
elif dice_1 == dice_2:
    print('It is equality!')
else:
    print(player_2 + ' is winner!')
