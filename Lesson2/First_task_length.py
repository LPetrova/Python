n = input('Enter string: ')
length_word = len(n)

if length_word < 10:
    print(n)
else:
    print(n[0:10] + '...')#slacing
'''
 for i in range(10):
        print(n[i], end='')
    print('...')
'''


