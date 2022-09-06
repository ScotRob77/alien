import random
from countries import country_list
import alien
import string

game_finished = False
remaining_attempts = len(alien.ALIENS)
display = []
alphabet = string.ascii_uppercase


print(alien.LOGO)

def intro():
    """
    Welcome message introducing the name of the game.
    Welcome text and instructions for gameplay.
    Enter name input to start game.
    """
    print("        WELCOME TO ALIEN INVASION...!\n")
    print("Hello Earthling, I am from the planet Aldaran...\n")
    print("We have been watching Earth for many years...\n")
    print("You have not been doing a good job of keeping it safe...\n")
    print("So we are here to take over...\n")
    print("If you want to stop us from invading...\n")
    print("You need to guess which country we intend to invade first.\n")
    print("But beware. you can only guess wrong 6 times...\n")
    print("Before you start you need to tell us your name.\n")
    
    user = input("What is your name Earthling?\n")

    print(f"Greetings {user}...\n")

    return user


intro()    

def select_random_country(country_list):
    """
    Will randomly select a country from the list of countries
    """
    return random.choice(country_list)


random_country = select_random_country(country_list)
country_length = len(random_country)

for _ in range(country_length):
    display += "_"

while not game_finished:
    guess = input("Guess a letter: ").upper()
    if len(guess) != 1:
        print("Whoa there Earthling. One letter at a time..!\n")

    if guess in display:
        print(f"You've already guessed {guess}, Choose again...")

    if guess not in alphabet:
        print("Please enter a LETTER.")


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
