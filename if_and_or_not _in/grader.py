mark = int(input('Enter a mark: '))

min = 0
max = 100

if mark > min and mark <= 50:
    print('Слаб 2')
elif mark > 51 and mark <= 60:
    print('Среден 3')
elif mark > 61 and mark <= 70:
    print('Добър 4')
elif mark > 71 and mark <= 80:
    print('Много Добър 5')
elif mark > 81 and mark < 100:
    print('Отличен 6')
elif mark == max:
    print('Много Отличен 7')