n = input('Enter number: ')
n = int(n)
start_number = 1
sum = 0

while start_number <= n:
    if start_number % 2 != 0:
        sum = sum + start_number
    start_number += 1
print(sum)