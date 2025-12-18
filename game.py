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
        
        print(f'''\nThe game has started, Enter A/a for attack and S/s for shielding the attack.
Adventurer you must not attack more than 3 times in a row, if you do you will not be able to attack for 2 turns.''')
        choice = input(f'\nAdventurer {self.get_name()}, your is choice: ')
        choice.lower()

        a_wolf = wolf() # character instances!
        a_adventurer = adventurer()

        attack_cool_down_lis = [] # Checks cool down for attack! 3 attack in a row.
        cool_down_initiate = False
        cool_down_time = 2
        ''' for now I just want the cool down to be for the user to
        not be able to attack for two turns'''

        while a_wolf.get_hp() >= 0 and a_adventurer.get_hp() >= 0:
            # The game runs until one of them prerishes.

            CLS()
            wolf_choice = random.choice(['a','d'])

            if choice == 'a' and cool_down_initiate == False:
                cool_down_time = 2 # redefining the cool down as it again enters attack section of code.
                attack_cool_down_lis.append(choice)

                dmg_delt_by_atk = a_adventurer.attack() # attack damage
                did_it_dodge, counter_dmg = a_wolf.dodge_n_attack()
                throables_dmg = a_adventurer.knife_throw()

                if did_it_dodge == True:
                    if counter_dmg > 0:
                        print(f"The wolf dodged and counter attacked! inflicting {counter_dmg} damage.")
                        a_adventurer.reduce_hp_by(counter_dmg)
                    else:
                        if throables_dmg > 0:
                            print(f'The wolf dodged your attack, but you managed to inflict {throables_dmg} damage using a throable knife')
                            a_wolf.reduce_hp_by(throables_dmg)
                        else:
                            print('The wolf dodged both of your attack, and didn\'t counter attack.')

                else:
                    print(f"The wolf couldn't dodge your attack. It caused {dmg_delt_by_atk} damage")
                    a_wolf.reduce_hp_by(dmg_delt_by_atk) # registering damage, reducing health
                
            else:
                attack_cool_down_lis.clear()

                if cool_down_initiate == True and cool_down_time != 0: # The attack cool down.
                    luck_attack = random.randint(1,100)

                    if luck_attack == 7 or luck_attack == 5 or luck_attack == 2: 
                        # Probability: 3 out of 100 of hitting this damage
                        minor_dmg = random.randint(1,2)
                        print(f'lucky! you managed to inflict {minor_dmg} while it was about to attack you!')
                        a_wolf.reduce_hp_by(minor_dmg)
                    
                    else:
                        opening_heavy_dmg = a_wolf.attack() * 2
                        print(f'Wolf saw an opening and attacked, causing {opening_heavy_dmg} damage.')
                        a_adventurer.reduce_hp_by(opening_heavy_dmg)

                    print(f'Attack cool down (turns left): {cool_down_time}')
                    cool_down_time -= 1 

                    if cool_down_time == 0: # Clearing cool down.
                        cool_down_initiate = False

                else:

                    if wolf_choice == 'a':
                        shieled_the_attack, shielded_dmg = a_adventurer.shield()
                        wolf_atk_dmg = a_wolf.attack()

                        if shieled_the_attack:
                            if wolf_atk_dmg > shielded_dmg:
                                dmg_taken_by_adventurer = wolf_atk_dmg - shielded_dmg
                                print(f'The managed to inflict {dmg_delt_by_atk} damage.')
                                a_adventurer.reduce_hp_by(dmg_taken_by_adventurer)
                            else:
                                print('The adventurer managed to shield the attack completely.')

                        else:
                            print("you couldn't shield the attack at all")
                            print(f"Wolf caused {wolf_atk_dmg} damage to your hp.")
                            a_adventurer.reduce_hp_by(wolf_atk_dmg)
                    
                    else:
                        print("you both decided to not attack.")

            if len(attack_cool_down_lis) == 3:
                cool_down_initiate = True
                ''' This means user entered "a" for 3 times in a row, because each time he enteres "s" 
                the list is cleared but because the len of the list is 3 i would imply that the user kept entering
                "a" for 3 times.'''
            
            if a_wolf.get_hp() >= 0 and a_adventurer.get_hp() >= 0:   
                print(f'Attack Streak: {len(attack_cool_down_lis)}')             
                print(f'wolf hp: {a_wolf.get_hp()} adventurer hp: {a_adventurer.get_hp()}')
                print('What will be your decision, A/a for attack and S/s for shielding the attack: ')
                choice = input(f'Adventurer {self.get_name()}, your is choice: ')
                choice.lower()