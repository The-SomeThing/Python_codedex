# pH level input
ph = int(input("Enter the pH number: "))

# pH level check
if ph < 0:
    print("Error")
elif ph > 14:
    print("Error")
elif ph <= 6:
    print("Acidic")
elif ph == 7:
    print("Neutral")
elif ph >= 8:
    print("Basic")

