n = input('Enter number: ')
n = int(n)

c = n % 10
n = n // 10

b = n % 10
n = n // 10

a = n % 10
n = n // 10

print('reverced number is: ' + str(c) + str(b) + str(a))