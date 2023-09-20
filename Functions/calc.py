#### Fast calc

# Operators
def addition(x, y):
    return x + y

def subtraction(x,y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def exponent(x, y):
    return x ** y

operation = [addition, subtraction, multiply, divide, exponent] # allows me to call the function from the list

op = int(input("> Which operation would you like to use?\n> 1. Add\n> 2. Subtract\n> 3. Multiply\n> 4. Divide\n> 5. Exponent\n> "))

val1 = int(input("x = "))
val2 = int(input("y = "))

print(operation[op - 1](val1, val2)) # pulls the function based on the users selection, and feeds the variables into it.
