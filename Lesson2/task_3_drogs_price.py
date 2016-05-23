all_prices =[]
while True:
    price = input("Please enter a price: ")
    if price == 'stop':
        break

    all_prices.append(float(price))

print('All prices: ')
print(all_prices)

sum_prices = sum(all_prices)
min_price = min(all_prices)
max_price = max(all_prices)

all_prices.sort()
lower_price = all_prices[0]

if len(all_prices) > 0:
    while len(all_prices) > 0 and all_prices[0] == lower_price:
        price.pop(0)

if len(all_prices) > 0:
    highest_price = all_prices[-1]
    while len(all_prices) > 0 and all_prices[-1] == highest_price:
        price.pop(-1)

print('Print after lowest and highest price')
print(all_prices)


