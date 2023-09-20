# Guessing game

attempts = 0
guess = 0

while guess != 6 and attempts < 3:
  guess = int(input("Guess the number:  "))
  attempts +=1

if guess != 6:
   print("Too many failed attempts.")
elif guess == 6:
   print("You're in!")


# Codedex answer

# Guess Number 🔢
# Codédex

#guess = 0
#tries = 0

#while guess != 6 and tries < 5:
  #guess = int(input('Guess the number:  '))
  #tries = tries + 1

#if guess != 6:
  #print('You ran out of tries.')
#else:
  #print('You got it!')