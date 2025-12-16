from characters import wolf, adventurer
from game import GAME
import random

def main():
    a_wolf = wolf()
    did_it_dodge, dodge_dmg = a_wolf.dodge_n_attack()
    atk_dmg_wolf = a_wolf.attack()
    print(did_it_dodge, dodge_dmg, atk_dmg_wolf)
    #GAME.run()

if __name__ == "__main__":
    main()