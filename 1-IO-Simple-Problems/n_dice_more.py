from random import randint

n = int(input('Enter side: '))

dice_1 = randint(1, n)
print('First roll: ')
print(dice_1)

dice_2 = randint(1, n)
print('Second roll: ')
print(dice_2)

dice_3 = randint(1, n)
print('Third roll: ')
print(dice_3)

sum = dice_1 + dice_2 + dice_3
print('The sum is: ')
print(sum)