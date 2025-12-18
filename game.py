from characters import wolf,adventurer

class GAME:

    def __init__(self, p_n):
        self._PlayerName = p_n
    
    def get_name(self):
        return self._PlayerName
    
    def run(self):
        
        print('The game has started, Enter A/a for attack and B/b for shielding the attack: ')
        choice = input('Enter your choice: ')
        choice.lower()

        wolf0 = wolf() # character instances!
        adventurer0 = adventurer()

        attack_cool_down_lis = []
        check_three_atk_row = False


        while wolf0.get_hp() != 0 and adventurer0.get_hp() != 0:

            attack_cool_down_lis.append(choice)

            if choice == 'a':
                pass
            else:
                pass

            if len(attack_cool_down_lis) == 3:
                
                check_three_atk_row = False

                for choice_made in attack_cool_down_lis:
                    if choice_made == 'a':
                        a_counts += 1
                        check_three_atk_row = True
                    else:
                        check_three_atk_row = False
                        break