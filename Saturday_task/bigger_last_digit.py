n = input('Eneter n: ')
m = input('Eneter m: ')
n = int(n)
m = int(m)

last_digit_n = n % 10
last_digit_m = m % 10

if last_digit_n != last_digit_m:
    if last_digit_n > last_digit_m:
        print(last_digit_n)
    else:
        print(last_digit_m)

else:
    if n > m:
        print(n)
    else:
        print(m)