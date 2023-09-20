# Import
import random

# User question
input("Question: ")

# Random answer generator
num = random.randint(1, 9)

if num == 1:
    print("Magic 8 Ball: Yes - definitely.")
elif num == 2:
    print("Magic 8 Ball: It is decidedly so.")
elif num == 3:
    print("Magic 8 Ball: Without a doubt.")
elif num == 4:
    print("Magic 8 Ball: Reply hazy, try again.")
elif num == 5:
    print("Magic 8 Ball: Ask again later.")
elif num == 6:
    print("Magic 8 Ball: Better not tell you now.")
elif num == 7:
    print("Magic 8 Ball: My sources say no.")
elif num == 8:
    print("Magic 8 Ball: Outlook not so good.")
elif num == 9:
    print("Magic 8 Ball: Very doubtful.")

#---------------------------------------------------------------------------------------------
# Codedex answer
# Magic 8 Ball 🎱
# Codédex

import random

question = input()

random_number = random.randint(1, 9)

if random_number == 1:
  answer = 'Yes - definitely'
elif random_number == 2:
  answer = 'It is decidedly so'
elif random_number == 3:
  answer = 'Without a doubt'
elif random_number == 4:
  answer = 'Reply hazy, try again'
elif random_number == 5:
  answer = 'Ask again later'
elif random_number == 6:
  answer = 'Better not tell you now'
elif random_number == 7:
  answer = 'My sources say no'
elif random_number == 8:
  answer = 'Outlook not so good'
elif random_number == 9:
  answer = 'Very doubtful'
else:
  answer = 'Error'
  
print('Question:      ' + question) 
print('Magic 8 Ball:  ' + answer)