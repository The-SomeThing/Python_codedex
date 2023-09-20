# The Sorting Hat

# Houses

Gryffindor  = 0
Ravenclaw   = 0
Hufflepuff  = 0
Slytherin   = 0

# Question 1

print("Q1) Do you prefer Dawn or Dusk?\n1) Dawn\n2) Dusk")
question_1 = int(input())

if      question_1 == 1:
    Gryffindor  =   Ravenclaw   = Ravenclaw + 1
elif    question_1 == 2:
    Hufflepuff  =   Slytherin   = Slytherin + 1
else:
    print()
    print("Wrong input.")
    print()

# Question 2
print("Q2) Whem I'm dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold")
question_2 = int(input())

if      question_2 == 1:
    Hufflepuff  =   Hufflepuff  + 2
elif    question_2 == 2:
    Slytherin   =   Slytherin   + 2
elif    question_2 == 3:
    Ravenclaw   =   Ravenclaw   + 2
elif    question_2 == 4:
    Gryffindor  =   Gryffindor  + 2
else:
    print()
    print("Wrong input.")
    print()

# Question 3
print("Q3) Which kind of instrument most pleases your ear?\n1) The Violin\n2) The Trumpet\n3) The Piano\n4) The Drums")
question_3 = int(input())

if      question_3 == 1:
    Slytherin   =   Slytherin   + 4
elif    question_3 == 2:
    Hufflepuff  =   Hufflepuff  + 4
elif    question_3 == 3:
    Ravenclaw   =   Ravenclaw   + 4
elif    question_3 == 4:
    Gryffindor  =   Gryffindor  + 4
else:
    print()
    print("Wrong input.")
    print()

# House count
print()
print("Total:")
print("Gryffindor: ", Gryffindor)
print("Ravenclaw: ", Ravenclaw)
print("Hufflepuff:", Hufflepuff)
print("Slytherin", Slytherin)
print()

# House message

print()
if      Gryffindor > Ravenclaw and Gryffindor > Hufflepuff and Gryffindor > Slytherin:
    print("GRYFFINDORRRR!")
elif    Ravenclaw > Hufflepuff and Ravenclaw > Slytherin:
    print("RAVENCLAWW!")
elif    Hufflepuff > Slytherin:
    print("HUFFLEPUFF!")
elif    Slytherin > Gryffindor:
    print("SLYTHERIN!")
else:
    print("I'm sorry but you have performed underage magic in the presense of a muggle.")
    print()

#-----------------------------------------------------------------------------------------------------------------
# Codedex answer

# Sorting Hat 🧙‍♂️
# Codédex

#gryffindor = 0
#hufflepuff = 0
#ravenclaw = 0
#slytherin = 0

#print('===============')
#print('The Sorting Hat')
#print('===============')

# ~~~~~~~~~~~~~~~ Question 1 ~~~~~~~~~~~~~~~

#print('Q1) Do you like Dawn or Dusk?')

#print('  1) Dawn')
#print('  2) Dusk')

#answer = int(input('Enter answer (1-2): '))

#if answer == 1:
  #gryffindor += 1
  #ravenclaw += 1
#elif answer == 2:
  #hufflepuff += 1
  #slytherin +=1
#else:
  #print('Wrong input.')

# ~~~~~~~~~~~~~~~ Question 2 ~~~~~~~~~~~~~~~

#print("\nQ2) When I'm dead, I want people to remember me as:")

#print('  1) The Good')
#print('  2) The Great')
#print('  3) The Wise')
#print('  4) The Bold')

#answer = int(input('Enter your answer (1-4): '))

#if answer == 1:
  #hufflepuff += 2
#elif answer == 2:
  #slytherin += 2
#elif answer == 3:
  #ravenclaw += 2
#elif answer == 4:
  #gryffindor += 2
#else:
  #print('Wrong input.')

# ~~~~~~~~~~~~~~~ Question 3 ~~~~~~~~~~~~~~~

#print('\nQ3) Which kind of instrument most pleases your ear?')

#print('  1) The violin')
#print('  2) The trumpet')
#print('  3) The piano')
#print('  4) The drum')

#answer = int(input('Enter your answer (1-4): '))

#if answer == 1:
  #slytherin += 4
#elif answer == 2:
  #hufflepuff += 4
#elif answer == 3:
  #ravenclaw +=4
#elif answer == 4:
  #gryffindor += 4
#else:
  #print('Wrong input.')
  
#print("Gryffindor: ", gryffindor)
#print("Ravenclaw: ", ravenclaw)
#print("Hufflepuff: ", hufflepuff)
#print("Slytherin: ", slytherin)

#most_points = max(gryffindor, ravenclaw, hufflepuff, slytherin) # We'll learn about max() in the Functions chapter

#if gryffindor == most_points:
  #print('🦁 Gryffindor!')
#elif ravenclaw == most_points:
  #print('🦅 Ravenclaw!')
#elif hufflepuff == most_points:
  #print('🦡 Hufflepuff!')
#else:
  #print('🐍 Slytherin!')