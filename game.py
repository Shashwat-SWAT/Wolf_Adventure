from characters import wolf,adventurer

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

        while wolf0.get_hp() != 0 and adventurer0.get_hp() != 0:

            if choice == 'a' and cool_down_initiate == False:
                attack_cool_down_lis.append(choice)

                dmg_delt_by_atk = adventurer0.attack()
                wolf0.reduce_hp_by(dmg_delt_by_atk)
                
            else:
                attack_cool_down_lis.clear()
                
                if cool_down_initiate == True and cool_down_time != 0:
                    cool_down_time -= 1
                    if cool_down_time == 0:
                        cool_down_initiate = False
                
                if choice == 'a':
                    print('sorry!')

            if len(attack_cool_down_lis) == 3:
                cool_down_initiate = True
            
            print('The game has started, Enter A/a for attack and S/s for shielding the attack: ')
            choice = input(f'Adventurer {self.get_name()}, your is choice: ')
            choice.lower()
