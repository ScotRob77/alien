import random
from countries import country_list
import alien

game_finished = False
remaining_attempts = len(alien.ALIENS) - 1
display = []

print(alien.LOGO)
print("        WELCOME TO ALIEN INVASION..!\n")

def select_random_country(country_list):
    """
    Will randomly select a country from the list of countries
    """
    return random.choice(country_list)
print(select_random_country(country_list))

random_country = select_random_country(country_list)
country_length = len(random_country)

for _ in range(country_length):
    display += " _ "