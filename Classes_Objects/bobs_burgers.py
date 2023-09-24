#### Bob's Burgers Restaruant

class Restaurant:
    name        = ""
    category    = ""
    rating      = 0.0
    delivery    = True

bobs_burgers = Restaurant()
bobs_burgers.name = "Bob's Burgers"
bobs_burgers.category = "American Diner"
bobs_burgers.rating = 3.81
bobs_burgers.delivery = False

print()
print(vars(bobs_burgers))
print()

thaise_tafel = Restaurant()
thaise_tafel.name = "Thaise Tafel"
thaise_tafel.category = "Indonesian"
thaise_tafel.rating = 4.3
thaise_tafel.delivery = True

print()
print(vars(thaise_tafel))
print()

new_york_pizza = Restaurant()
new_york_pizza.name = "New York Pizza"
new_york_pizza.category = "Pizza"
new_york_pizza.rating = 3.5
new_york_pizza.delivery = True

print()
print(vars(new_york_pizza))
print()

mcdonalds = Restaurant()
mcdonalds.name = "McDonalds"
mcdonalds.category = "Fast Food"
mcdonalds.rating = 3.92
mcdonalds.delivery = False

print()
print(vars(mcdonalds))
print()
