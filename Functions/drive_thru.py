#### Drive thru

import random

welc_men_accept = ["y", "yes"]
welc_men_deny   = ["n", "no"]

basket = []

w_menu = ["Fries",
          "Cheese Sticks",
          "McFlurry",
          "McWrap"]


main_menu = ["3 Chicken McNuggets",
             "6 Chicken McNuggets",
             "9 Chicken McNuggets",
             "Big Mac",
             "The McRib",
             "The McPlant"]

# Select from Welcome menu
def welcome_item_select():
    global basket
    item1 = input("Which item would you like?\n> ").lower
    if item1 in w_menu:
        basket.append(item1)


# Welcome Menu List
def welcome_men():
    for i in w_menu:
        print(i)
    menu_option = input("Would you like something from the Welcome Menu?\n> ")
    if menu_option in welc_men_accept:
        welcome_item_select()
    if menu_option in welc_men_deny:
        get_item()


# Select from main menu
def get_item():
    menu_option = input("Would you like something from the Main Menu?\n> ")




# Show Welcome menu
welcome_men()


print(basket)