#### Fortune Cookie

import random

# Fortune gen
no0 = random.randint(0, 7)
no1 = random.randint(0, 7)
no2 = random.randint(0, 7)

# Possible Fortunes
fortunes = ["Don't pursue happiness - create it.",                                  # 0
            "All things are difficult before they are easy.",                       # 1
            "The early bird gets the worm, but the second mouse gets the cheese.",  # 2
            "Someone in your life needs a letter from you.",                        # 3
            "Don't just think. Act!",                                               # 4
            "Your heart will skip a beat.",                                         # 5
            "The fortune you search for is in another cookie.",                     # 6
            "Help! I'm being held prisoner in a Chinese bakery!"]                   # 7


# Fortune function
def fortune():
    print(fortunes[no0])
    print(fortunes[no1])
    print(fortunes[no2])
fortune()
