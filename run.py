import random
from countries import country_list
import alien

game_finished = False
remaining_attempts = len(alien.ALIENS) - 1
display = []