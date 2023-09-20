welc_menu = {
    "Fries"                 : 2.00,
    "Cheese Sticks"         : 3.50,
    "McFlurry"              : 2.50,
    "McWrap"                : 5.00,
}

main_menu = {
    "3 Chicken McNuggets"   : 4.00,
    "6 Chicken McNuggets"   : 6.50,
    "9 Chicken McNuggets"   : 8.00,
    "Big Mac"               : 4.50,
    "The McRib"             : 5.00,
    "The McPlant"           : 4.50,
}

basket = []

def select_item(menu):
    item = input(f"Which item would you like from the {menu}?\n> ")
    if item in menu:
        basket.append((item, menu[item]))
    else:
        print("Item not found in the menu.")

def checkout():
    total = sum(item[1] for item in basket)
    print("\nItems in your basket:")
    for item, price in basket:
        print(f"{item}: ${price:.2f}")
    print(f"Total: ${total:.2f}")

    tip_percentage = float(input("Enter a tip percentage (e.g., 10 for 10%): "))
    tip_amount = (tip_percentage / 100) * total
    total_with_tip = total + tip_amount
    print(f"Tip: ${tip_amount:.2f}")
    print(f"Total with Tip: ${total_with_tip:.2f}")

while True:
    print("\nWelcome to the Drive-Thru!")
    print("1. Welcome Menu")
    print("2. Main Menu")
    print("3. Review Basket")
    print("4. Checkout")
    print("5. Exit")

    choice = input("Please select an option (1/2/3/4/5): ")

    if choice == "1":
        select_item(welc_menu)
    elif choice == "2":
        select_item(main_menu)
    elif choice == "3":
        checkout()
    elif choice == "4":
        checkout()
        basket = []  # Clear the basket after checkout
    elif choice == "5":
        print("Thank you for visiting! Goodbye.")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4/5).")