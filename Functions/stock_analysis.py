#### Stock time analysis

# Stock Prices Jan 1 - 20
stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68,
                35.82, 43.41, 44.29, 44.65, 53.56,
                49.85, 48.71, 48.71, 49.94, 48.53,
                47.03, 46.59, 48.62, 44.21, 47.21] # t=20 0b=19

# Possible results
def single_day(x):
    return stock_prices[x - 1]

def max_prices(a, b):
    return stock_prices[a - 1 : b]

def min_prices(a, b):
    return stock_prices[a - 1 : b]

# Request
req = int(input('''
Would you like:
1. Price from one day
2. Maximum price between two days
3. Minimum price between two days
> '''))

if req == 1:
    val1 = int(input("From which day of January would you like the stock price of?\n> "))
    print(single_day(val1))

elif req == 2:
    val1 = int(input("Which day would you like to begin your search?\n> "))
    val2 = int(input("Which day would you like to end your search?\n> "))
    print(max(max_prices(val1, val2)))

elif req == 3:
    val1 = int(input("Which day would you like to begin your search?\n> "))
    val2 = int(input("Which day would you like to end your search?\n> "))
    print(min(min_prices(val1, val2)))

else:
    print("Error")
