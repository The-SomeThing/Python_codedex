# Heigh Check
height = int(input("What is your height in cm? "))

# Credits check
credits = int(input("How many credits do you have? "))

if height >= 137 and credits >= 10:
    print("Enjoy the ride!")
elif height < 137 and credits < 10:
    print("You are not tall enough and you do not have enough credits to ride.")
elif not height >= 137:
    print("You are not tall enough to ride.")
elif not credits >= 10:
    print("You do not have enough credits.")

#---------------------------------------------------------------------------------------------------
# Codedex answer
ride_is_open = True

height = int(input('What is your height (cm)? '))
credits = int(input('How many credits do you have? '))

tall_enough = height >= 137
enough_credits = credits >= 10

if ride_is_open and tall_enough and enough_credits:
  print("Enjoy the ride!")
elif not tall_enough or not enough_credits:
  print("You are either not tall enough to ride or you don't have enough credits.")
else:
  print("Sorry! The ride is currently closed!")