from characters import wolf, adventurer
from game import GAME
import random

def main():
    a_wolf = wolf()
    did_it_dodge, dodge_dmg = a_wolf.dodge_n_attack()
    atk_dmg_wolf, critw = a_wolf.attack()
    print(did_it_dodge, dodge_dmg, atk_dmg_wolf, critw)

    a_player = adventurer()
    did_it_shield, dmg_shielded = a_player.shield()
    atk_dmg_player, critp = a_player.attack()
    print(did_it_shield, dmg_shielded, atk_dmg_player, critp)
    #GAME.run()

if __name__ == "__main__":
    main()