n = int(input('Enter a number: '))
start = 1
end = n

print('Counting from 1 to n')
while start <= end:
    print(start)
    start += 1

start = n
end = 1
print('Counting from n to 1')
while start >= end:
    print(start)
    start -= 1
