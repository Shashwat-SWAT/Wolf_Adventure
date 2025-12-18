from characters import wolf,adventurer
import random
from os import system

def CLS():
    system('cls')

class GAME:

    def __init__(self, p_n):
        self._PlayerName = p_n
    
    def get_name(self):
        return self._PlayerName
    
    def run(self):
        
        print('The game has started, Enter A/a for attack and S/s for shielding the attack: ')
        choice = input(f'Adventurer {self.get_name()}, your is choice: ')
        choice.lower()

        wolf0 = wolf() # character instances!
        adventurer0 = adventurer()

        attack_cool_down_lis = [] # Checks cool down for attack! 3 attack in a row.
        cool_down_initiate = False
        cool_down_time = 2
        ''' for now I just want the cool down to be for the user to
        not be able to attack for two turns'''

        while wolf0.get_hp() >= 0 and adventurer0.get_hp() >= 0:
            # The game runs until one of them prerishes.

            CLS()
            
            if choice == 'a' and cool_down_initiate == False:
                cool_down_time = 2 # redefining the cool down as it again enters attack section of code.
                attack_cool_down_lis.append(choice)

                dmg_delt_by_atk = adventurer0.attack() # attack damage
                wolf0.reduce_hp_by(dmg_delt_by_atk) # registering damage, reducing health
                
            else:
                attack_cool_down_lis.clear()
                
                if cool_down_initiate == True and cool_down_time != 0: # The attack cool down.

                    luck_attack = random.randint(1,100)

                    if luck_attack == 7 or luck_attack == 5 or luck_attack == 2: 
                        # Probability: 3 out of 100 of hitting this damage
                        print('lucky!')
                        wolf0.reduce_hp_by(random.randint(1,2))

                    cool_down_time -= 1 
                    if cool_down_time == 0: # Clearing cool down.
                        cool_down_initiate = False


            if len(attack_cool_down_lis) == 3:
                cool_down_initiate = True
                ''' This means user entered "a" for 3 times in a row, because each time he enteres "s" 
                the list is cleared but because the len of the list is 3 i would imply that the user kept entering
                "a" for 3 times.'''
            
            if wolf0.get_hp() >= 0 and adventurer0.get_hp() >= 0:                
                print(f'wolf hp: {wolf0.get_hp()} adventurer hp: {adventurer0.get_hp()}')
                print('The game has started, Enter A/a for attack and S/s for shielding the attack: ')
                choice = input(f'Adventurer {self.get_name()}, your is choice: ')
                choice.lower()
