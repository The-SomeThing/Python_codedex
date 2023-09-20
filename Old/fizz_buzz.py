# FizzBuzz!

f = "Fizz"
b = "Buzz"

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print(f+b)
    elif n % 3 == 0:
        print(f)
    elif n % 5 == 0:
        print(b)
    else:
        print(n)



