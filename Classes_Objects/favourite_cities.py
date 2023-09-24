#### Favourite cities classes

class City():
    def __init__(self, name, country, population, landmarks, nickname, founded, mayor):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks
        self.nickname = nickname
        self.founded = founded
        self.mayor = mayor

maidstone = City("Maidstone", "England", 177000, ["Mote Park ","Leeds Castle"], "MTown", 1549, "Gordon Newton")

print(vars(maidstone))
