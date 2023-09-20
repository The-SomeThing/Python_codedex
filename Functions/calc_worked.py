#### Simple Calc

# Operators
def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

def exponent(x, y):
    return x ** y

operator = (int(input("> What operator would you like to use?\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponent\n> ")))

x = int(input("x = "))
y = int(input("y = "))

if operator == 1:
    print(addition(x, y))

elif operator == 2:
    print(subtraction(x, y))

elif operator == 3:
    print(multiplication(x, y))

elif operator == 4:
    print(division(x, y))

elif operator == 5:
    print(exponent(x, y))

else:
    print("Error")
