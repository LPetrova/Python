a = int(input('Enter a:  '))
b = int(input('Enter b: '))
operation = input('Enter operation: ')

result = False

if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/':
    result = a / b

if result != False:
    print('Result is: ')
    print(result)
else:
    print('We do not support that operation.')