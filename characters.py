import random

class wolf:
    def __init__(self):
        self._hp = 10

    def attack(self):
        crit_chance = random.randint(1,10) # Probability of out of 10
        atk_dmg = random.randint(3,5)

        if crit_chance >= 9: # 20% probability
            atk_dmg = atk_dmg + ((atk_dmg * 40)//100) # 40% crit dmg
    
    def dou


class adventurer:

    def __init__(self):
        pass