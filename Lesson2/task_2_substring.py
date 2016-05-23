first_text = input('Enter first string: ')
second_text = input('Enter second string: ')

find_text = first_text.find(second_text)

if find_text == -1:
    print(first_text)
else:
    print(first_text[find_text + len(second_text):])


