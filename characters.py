import random

class wolf:
    def __init__(self):
        self._hp = 10 # wolf's hit points.

    def attack(self):
        crit_chance = random.randint(1,10) # Probability: out of 10
        atk_dmg = random.randint(3,5)

        if crit_chance >= 9: # 20% probability
            atk_dmg = atk_dmg + ((atk_dmg * 40)//100) # 40% crit dmg

        return atk_dmg
    
    def dodge_n_attack(self):
        dodge_chances = random.choice([True,False]) # 50% probability
        dodge_n_attack_chances = random.randint(1,10) # Probability: out of 10
        dodge_attack_dmg = 0

        if dodge_chances == False: # didn't dodge
            dodge_attack_dmg = 0
        
        else: # dodged
            if dodge_n_attack_chances >= 7: # 40% probability
                dodge_attack_dmg = random.randint(1,3)
            else:
                dodge_attack_dmg = 0

        return dodge_chances, dodge_attack_dmg

class adventurer:

    def __init__(self):
        pass