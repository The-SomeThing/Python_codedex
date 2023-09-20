#### Basic Calculator

func    = 0

# Which operation is going to be used
def operator(z):
    global func
    func = z

# Value of x and y
def values(x, y):
    x = int(input("x = "))
    y = int(input("y = "))

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

operator(z = int(input("> What operator would you like to use?\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponent\n> ")))

print(func)

# > What calculation would you like to perform?\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Divide\n5. Exponent\n> "