#### Birthday Messages

import datetime as dt, bday_messages as bdm

today = dt.date.today()

next_bday = dt.date(2024, 2, 3)
star_wars = dt.date(1977, 5, 25)

days_away = next_bday - today

if today == next_bday:
    print(bdm.random_message)

else:
    print(f"My next birthday is {days_away.days} days away!")

print(today - star_wars)
