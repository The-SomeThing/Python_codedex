#### Drive thru

w_menu = ["Fries",
          "Cheese Sticks",
          "McFlurry",
          "McWrap"]


m_menu = ["3 Chicken McNuggets",
             "6 Chicken McNuggets",
             "9 Chicken McNuggets",
             "Big Mac",
             "The McRib",
             "The McPlant"]

basket = []

def welcome_menu(x):
    item = w_menu[x - 1]
    basket.append(item)
    print("Your Order: ", basket)

def main_menu(x):
    item = m_menu[x - 1]
    basket.append(item)
    print("Your Order: ", basket)


print("\nWelcome to McDonalds!\n")
print(*w_menu, sep = ", ")


welcome_menu(x = int(input("\nWhat d'ya want?\n> ")))

print("\nHere's our main menu!\n")
print(*m_menu, sep = ", ")

main_menu(x = int(input("\nWhat d'ya want?\n> ")))


print("\nYour Order: ", *basket)
