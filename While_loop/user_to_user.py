a = input('Enter a: ')
b = input('Enter b: ')

if a > b:
    a = int(a)
    b = int(b)

    while a <= b:
        print(a)
        a += 1

else:
    a = int(a)
    b = int(b)

    while b <= a:
        print(b)
        b += 1