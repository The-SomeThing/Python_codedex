#### Playground to test thing before throwing it into a programme

func = 0 

def func_input(x):
    global func
    func = x

func_input(x = int(input("Enter number > ")))

print(func)

def operation(x):
    x = int(input("> "))

def test1():
    if func == 1:
        operation()
