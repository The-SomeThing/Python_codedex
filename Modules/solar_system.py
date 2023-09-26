#### Solar system

from math import pi
from random import choice as ch
import datetime

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

random_planet = ch(planets)

def area_calc(r):
    area = round(4 * pi * r ** 2)
    return area

if random_planet == "Mercury":
    print(random_planet, "is", area_calc(2440), "Km2")

elif random_planet == "Venus":
    print(random_planet, "is", area_calc(6052), "Km2")

elif random_planet == "Earth":
    print(random_planet, "is", area_calc(6371), "Km2")

elif random_planet == "Mars":
    print(random_planet, "is", area_calc(3390), "Km2")

elif random_planet == "Saturn":
    print(random_planet, "is", area_calc(58232), "Km2")

