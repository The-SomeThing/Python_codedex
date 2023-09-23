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

def select_w_menu():
    item1 = input("\nWhat would you like?\n> ")
    if item1 in w_menu:
        basket.append(item1)
        select_w_menu()
    elif item1 in ["Done", "Finish", "Quit"]:
        return
    else:
        print("Invalid Input")
        select_w_menu()


def welcome_menu():
    print()
    for i in w_menu:
        print(i)
    accepted_answers = ["y", "yes", "n", "no"]
    welc_y_n = input("\nWould you like something from the Welcome Menu? (y/n)\n> ")
    while welc_y_n.lower() not in accepted_answers:
        print("Inavlid input\n")
        welc_y_n = input("\nWould you like something from the Welcome Menu? (y/n)\n> ")
    if welc_y_n in ["y", "yes"]:
        select_w_menu()
    elif welc_y_n in ["n", "no"]:
        main_menu()

def select_m_menu():
    item1 = input("\nWhat would you like from the menu?\n> ")
    if item1 in m_menu:
        basket.append(item1)
        select_m_menu()
    elif item1 in ["Done", "Finish", "Quit"]:
        return
    else:
        select_m_menu()


def main_menu():
    print()
    for i in m_menu:
        print(i)
    accepted_answers = ["y", "yes", "n", "no"]
    welc_y_n = input("\nWould you like something from the Main Menu? (y/n)\n> ")
    while welc_y_n.lower() not in accepted_answers:
        print("Inavlid input\n")
        welc_y_n = input("\nWould you like something from the Main Menu? (y/n)\n> ")
    if welc_y_n in ["y", "yes"]:
        select_m_menu()
    elif welc_y_n in ["n", "no"]:
        main_menu()


welcome_menu()
main_menu()


print("\nYour order: ", basket)
