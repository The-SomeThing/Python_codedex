#Currency calculator

# Columbian Pesos (1 CO = 0.00023 EUR)
CO = float(input("What do you have left over in Pesos? "))
print(CO)
print()

# CO to EUR
CO = CO * 0.00023
print(CO)


# Peruvian Soles (1 SOL = 0.25 EUR)
PE = float(input("What do you have left in Soles? "))
print(PE)
print()

# PE to EUR
PE = PE * 0.25
print(PE)
print()

# Brazilian Reais (1 BR = 0.19 EUR)
BR = float(input("What do you have left in Reais? "))
print(BR)
print()

# BR to EUR
BR = BR * 0.19
print(BR)
print()

# Total EUR
total = CO + PE + BR
print("€",total)