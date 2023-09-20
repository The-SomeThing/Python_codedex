#### Stock Prices

stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68,
                35.82, 43.41, 44.29, 44.65, 53.56,
                49.85, 48.71, 48.71, 49.94, 48.53,
                47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(x):
    return stock_prices[x-1]

def max_prices(a, b):
    return stock_prices[a - 1 : b]

def min_prices(a, b):
    return stock_prices[a - 1: b]


req = int(input('''
Would you like:
1. Price from single day
2. Highest price between two days
3. Lowest price between two days
> '''))

if req == 1:
    val1 = int(input("From which day would you like to see the price?\n> "))
    print(price_at(val1))

if req == 2:
    val1 = int(input("From which day would you like to start the search?\n> "))
    val2 = int(input("From which day would you like to start the search?\n> "))
    print(max(max_prices(val1, val2)))

if req == 3:
    val1 = int(input("From which day would you like to start the search?\n> "))
    val2 = int(input("From which day would you like to start the search?\n> "))
    print(min(min_prices(val1, val2)))
#test