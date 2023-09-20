#### Don't Repeat Yourself / DRY

# A variable which can store multiple homogeneous values e.g. all numbers / all strings
ok_values = [1204, 1862, 2024, 0000]

# A variable input, in this case an integer
code_in = int(input("Please insert your pin: "))

# Variable storing conversion of integer to binary value
code_bin = bin(code_in)

# Print to return successful entry and binary value
if code_in in ok_values:
    print("PIN Successful")
    print(code_bin)

# Print incorrect answer
else:
    print("Incorrect PIN")