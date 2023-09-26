#### Slot Machine

import random

symbols = ["🍒", "🍇", "🍉", "7️⃣"]
jackpot = ["7️⃣", "7️⃣", "7️⃣"]

accepted_answer = ["y", "Y", "yes", "Yes"]

run = True

def play():
    result = random.choices(symbols, k = 3)
    print(f"\n{result[0]} | {result[1]} | {result[2]}\n")
    
    if result == jackpot:
        print("JACKPOT!!\n")
    else:
        print("Thanks for playing\n")


while run is True:
    keep_playing = input("\nWould you like to keep playing?\n> ")
    if keep_playing in accepted_answer:
        play()
    else:
        print("\nSee You Next Time.\n")
        run = False
