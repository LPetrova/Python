N = int(input('Enter N: '))
M = int(input('Enter M: '))

min_number = 0
max_number = 0

if N < M:
    min_number = N
    max_number = M
else:
    min_number = M
    max_number = N

start = min_number

while start <= max_number:
    n = start
    sum = 0

    while n != 0:
        digit = n % 10
        sum = sum + digit
        n = n // 10

    print('Sum of digits of ' + str(start) + ' = ' + str(sum))
    start = start + 1
