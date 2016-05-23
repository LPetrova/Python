n = input('Enter 3-digit number: ')
n = int(n)

a = n % 10
n = n // 10

b = n % 10
n = n // 10

c = n % 10
n = n // 10

print(a, b, c)

if a >= b and b >= c:
    print('The smallest number is: ' + str(c) + str(b) + str(a))
    print('The biggest number is: ' + str(a) + str(b) + str(c))
elif a >= c and c >= b:
     print('The smallest number is: ' + str(b) + str(c) + str(a))
     print('The biggest number is: ' + str(a) + str(c) + str(b))
elif a <= b and b <= c:
      print('+The smallest number is: ' + str(a) + str(b) + str(c))
      print('+The biggest number is: ' + str(c) + str(b) + str(a))
elif a <= c and c <= b:
      print('The smallest number is: ' + str(a) + str(c) + str(b))
      print('The biggest number is: ' + str(b) + str(c) + str(a))
elif c >= a and a >= b:
      print('The smallest number is: ' + str(b) + str(a) + str(c))
      print('The biggest number is: ' + str(c) + str(a) + str(b))
else:
      print('The smallest number is: ' + str(c) + str(a) + str(b))
      print('The biggest number is: ' + str(b) + str(a) + str(c))