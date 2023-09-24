#### The Pokedex class

class Pokedex():
    def __init__(self, entry, name, type, description, caught, level, region, height):
        self.entry          = entry
        self.name           = name
        self.type           = type
        self.description    = description
        self.caught         = caught
        self.level          = level
        self.region         = region
        self.height         = height

    def speak(self):
        print(f"{self.name}, {self.name}!")

bulbasaur = Pokedex(1, "Bulbasaur", ["Grass", "Poison"],
                    "There is a plant seed on its back right from the day this Pokémon is born. The seed slowly grows larger.",
                    True, 9, "Viridian Forest", 2.04)

charmander = Pokedex(4, "Charmander", ["Fire"],
                     "It has a preference for hot things. When it rains, steam is said to spout from the tip of its tail.",
                     True, 7, "Unknown", 2.00)

squirtle = Pokedex(7, "Squirtle", ["Water"],
                   "When it feels threatened, it draws its limbs inside its shell and sprays water from its mouth.",
                   True, 10, "Unknown", 1.08)

print()
print(vars(bulbasaur))
print()
print(vars(charmander))
print()
print(vars(squirtle))
print()

bulbasaur.speak()

charmander.speak()

squirtle.speak()

