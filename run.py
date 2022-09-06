import random
from countries import country_list
import alien

game_finished = False
remaining_attempts = len(alien.ALIENS)
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
    display += "_"

while not game_finished:
    guess = input("Guess a letter: ").strip()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(country_length):
        letter = random_country[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in random_country:
        print(f"You guessed {guess}, that's not in the country...")
        print("You lose a life...")
        remaining_attempts -= 1
        if remaining_attempts == 0:
            game_finished = True
            print("Game Over.... You lose..!")

        if "_" not in display:
            game_finished = True
            print("You Won")

        print(alien.ALIENS[remaining_attempts])
        