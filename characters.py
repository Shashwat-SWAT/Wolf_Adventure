import random

class wolf:

    def __init__(self):
        self._hp = 35 # wolf's hit points.

    def _wolf_fang_passive_damage(self):
        # I am thinking of adding some buff for the attack
        pass

    def attack(self):
        crit_chance = random.randint(1,10) # Probability: out of 10
        atk_dmg = random.randint(4,6)
        crit_dmg = 0

        if crit_chance >= 7: # 40% probability
            crit_dmg = ((atk_dmg * 40)//100) # 40% crit dmg
        
        atk_dmg = atk_dmg + crit_dmg

        return atk_dmg
    
    def dodge_n_attack(self): # This is for when user tries to shiled attack.
        dodge_chances = random.choice([True,False]) # 50% probability of getting True
        dodge_n_attack_chances = random.randint(1,10) # Probability: out of 10
        dodge_attack_dmg = 0

        if dodge_chances == False: # didn't dodge
            dodge_attack_dmg = 0
        
        else: # dodged
            if dodge_n_attack_chances >= 5: # 60% probability
                dodge_attack_dmg = random.randint(3,5)
            else:
                dodge_attack_dmg = 0

        return dodge_chances, dodge_attack_dmg
    
    def reduce_hp_by(self, dmg_taken):
        self._hp = self._hp - dmg_taken

    def get_hp(self):
        return self._hp

class adventurer:

    def __init__(self):
        self._hp = 50 # Player's hit points
    '''
        # This is something i will integra
        self._shield_hp = 10
        self._sword_hp = 10

    '''

    def _good_sword_dmg_buff(self):
        pass

    def attack(self):
        crit_chance = random.randint(1,40) # Probability: out of 40
        atk_dmg = random.randint(2,4)
        crit_dmg = 0

        if crit_chance >= 39: # 5% probability
            crit_dmg = ((atk_dmg * 60)//100) # 60% crit dmg
        
        atk_dmg = atk_dmg + crit_dmg

        return atk_dmg
    
    def shield(self):
        shielded_atk = random.choice([True,False]) # 50% probability
        dmg_shielded = 0

        if shielded_atk == False: # didn't dodge
            dmg_shielded = 0
        
        else: # dodged
            dmg_shielded = random.randint(3,6)
            # The dmg caused by wolf would be reduced by the number we get from this variable

        return shielded_atk, dmg_shielded
    
    def knife_throw(self):
        probability_of_throw = random.choice([True, False, False]) # 33.33% probability of getting True
        knife_dmg = 0
        if probability_of_throw:
            knife_dmg = random.randint(1,3)
        return knife_dmg

    
    def reduce_hp_by(self, dmg_taken):
        self._hp = self._hp - dmg_taken

    def get_hp(self):
        return self._hp