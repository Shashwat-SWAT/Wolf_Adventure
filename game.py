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
        
        CLS()
        print(f'''\nThe game has started, Enter A/a for attack and S/s for shielding the attack.
Adventurer you must not attack more than 3 times in a row, if you do you will not be able to attack for 2 turns.''')
        choice = input(f'\nAdventurer {self.get_name()}, your is choice: ')
        choice = choice.lower()

        while choice != 'a' and choice != 's':
            choice = input(f'\nPlease either enter \'A/a\' or \'S/s\': ')
            choice = choice.lower()


        a_wolf = wolf() # character instances!
        a_adventurer = adventurer()

        attack_cool_down_lis = [] # Checks cool down for attack! 3 attack in a row.
        cool_down_initiate = False
        cool_down_time = 2
        cool_down_choice = 0
        ''' for now I just want the cool down to be for the user to
        not be able to attack for two turns'''

        while a_wolf.get_hp() > 0 and a_adventurer.get_hp() > 0:
            # The game runs until one of them prerishes.

            CLS()
            wolf_choice = random.choice(['d','a']) # wolf dodge % = 50%

            if choice == 'a' and cool_down_initiate == False: # Enters when it is not in cool down mode, and user chose 'a'

                cool_down_time = 2 # redefining the cool down as it again enters attack section of code.
                attack_cool_down_lis.append(choice)

                dmg_delt_by_atk = a_adventurer.attack() # attack damage
                did_it_dodge, counter_dmg = a_wolf.dodge_n_attack()
                throables_dmg = a_adventurer.knife_throw()

                if wolf_choice == 'a':
                    
                    print('You both decided to attack, with a lot opening!')
                    wolfs_atk = a_wolf.attack()

                    a_adventurer.reduce_hp_by(wolfs_atk * 2)
                    a_wolf.reduce_hp_by(dmg_delt_by_atk * 3)

                    if (dmg_delt_by_atk * 3) > (wolfs_atk * 2):
                        print(f'You managed to deal {dmg_delt_by_atk * 3}, while wolf only inflicted {wolfs_atk * 2} damage.')
                    elif (dmg_delt_by_atk * 3) == (wolfs_atk * 2):
                        print(f'You both caused {dmg_delt_by_atk * 3} damage to each other.')
                    else:
                        print(f'The wolf caused {wolfs_atk * 2} damage, but you only caused {dmg_delt_by_atk * 3} damage to the wolf.')

                else:

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
                
            else: # Enter user chose 'b'

                attack_cool_down_lis.clear()

                # Program primarily looks at attack cool down, if it is initiated then goes in this loop

                if cool_down_initiate == True and cool_down_time != 0: 
                    luck_attack = random.choices([x for x in range(1,101)], k=3)

                    if cool_down_choice in luck_attack: 
                        # Probability: 3 out of 100 of hitting this damage (maximum)
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

                # Enters only if there is no attack cool down initiation.

                else:

                    if wolf_choice == 'a':
                        shieled_the_attack, shielded_dmg = a_adventurer.shield()
                        wolf_atk_dmg = a_wolf.attack()

                        if shieled_the_attack:
                            if wolf_atk_dmg > shielded_dmg:
                                dmg_taken_by_adventurer = wolf_atk_dmg - shielded_dmg
                                print(f'The wolf managed to inflict {dmg_taken_by_adventurer} damage.')
                                a_adventurer.reduce_hp_by(dmg_taken_by_adventurer)
                            else:
                                print('The adventurer managed to shield the attack completely', end='')
                                
                                chances_damaging_shield = random.choice([True, False])
                                if not(chances_damaging_shield):
                                    caused_shielded_dmg = random.randint(1,3)
                                    print(f', but wolf caused {caused_shielded_dmg} damage to the shield')
                                    a_adventurer.reduce_shield_hp_by(caused_shielded_dmg)
                                else:
                                    pre_shield_hp = a_adventurer.get_shield_hp()
                                    if a_adventurer.get_shield_hp() < 15:
                                        a_adventurer.recover_shield()
                                    post_shield_hp = a_adventurer.get_shield_hp()
                                    if post_shield_hp>pre_shield_hp:
                                        print(', and also managed to repair the shield')
                                    else:
                                        print('.')

                        else:
                            print("you couldn't shield the attack at all")
                            print(f"Wolf caused {wolf_atk_dmg} damage to your hp.")
                            a_adventurer.reduce_hp_by(wolf_atk_dmg)
                    
                    else:
                        knife_throw = a_adventurer.knife_throw()
                        if knife_throw > 0: # 50% chance of throwing the knife at wolf.    
                            print(f'You saw the oppertuinity and attacked teh wolf with a throable knife. It did {knife_throw} damage.')
                            a_wolf.reduce_hp_by(knife_throw)
                        else:
                            print('You both decided to do nothing.')

            if len(attack_cool_down_lis) == 3:
                cool_down_initiate = True
                ''' This means user entered "a" for 3 times in a row, because each time he enteres "s" 
                the list is cleared but because the len of the list is 3 i would imply that the user kept entering
                "a" for 3 times.'''
            
            # ---------- Printing menu ---------- #

            if a_wolf.get_hp() > 0 and a_adventurer.get_hp() > 0:   
                print(f'\nAttack Streak: {len(attack_cool_down_lis)}')             
                print(f'wolf hp: {a_wolf.get_hp()} adventurer hp: {a_adventurer.get_hp()} shield hp: {a_adventurer.get_shield_hp()}')

                if cool_down_initiate == False:    # Enters when it is not in cool down mode
                    print('\nWhat will be your decision, A/a for attack and S/s for shielding the attack: ')
                    choice = input(f'Adventurer {self.get_name()}, your is choice: ')
                    choice = choice.lower()

                    while choice != 'a' and choice != 's':
                        choice = input(f'\nPlease either enter \'A/a\' or \'S/s\': ')
                        choice = choice.lower()

                else:
                    print('\nEnter a number within 1-100, if you are lucky you might attack the wolf even though you are in attack cool down.')
                    cool_down_choice = input('Enter your choice of number: ')

                    while not(cool_down_choice in [str(x) for x in range(1,101)]):
                        print('\nPlease enter a number within 1-100.')
                        cool_down_choice = input('Enter your choice of number: ')

                    cool_down_choice = int(cool_down_choice) # changing the input to int after making sure.

        # ---------- Winning Condition ---------- #

        if (a_wolf.get_hp() <= 0 and a_adventurer.get_hp() <= 0):
            print('You both have died in this battle, would you like to play again?')
            play_again = input("Enter 'Y/y' if you wish to play again: ")
            play_again = play_again.lower()

            if play_again == 'y':
                CLS()
                self.run()

        elif (a_wolf.get_hp() <= 0 and a_adventurer.get_hp() > 0):
            print('You have succesfully slain the wolf, would you like to play again?')
            print(f'Your remaining hp: {a_adventurer.get_hp()}')
            play_again = input("Enter 'Y/y' if you wish to play again: ")
            play_again = play_again.lower()

            if play_again == 'y':
                CLS()
                self.run()

        else:
            print('You got killed, would you like to play again?')
            print(f'Wolf\'s remaining hp: {a_wolf.get_hp()}')
            play_again = input("Enter 'Y/y' if you wish to play again: ")
            play_again = play_again.lower()

            if play_again == 'y':
                CLS()
                self.run()