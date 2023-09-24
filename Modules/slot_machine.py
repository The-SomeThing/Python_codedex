#### Slot Machine

import random

symbols = ["🍒", "🍇", "🍉", "7️⃣"]
jackpot = ["7️⃣", "7️⃣", "7️⃣"]


def play():
    result = random.choices(symbols, k = 3)
    print(f"{result[0]} | {result[1]} | {result[2]}")
    if result == jackpot:
        print("JACKPOT!!")
    else:
        print("Thanks for playing")

play()