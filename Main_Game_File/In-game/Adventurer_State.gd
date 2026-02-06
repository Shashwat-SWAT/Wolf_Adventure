extends Node

var M_Health = 50
var C_Health = 50

func attack_damage():
	
	var base_atk_dmg = randi_range(2,4)
	var crit_chance = randi_range(1,40)
	var Attack_dmg = 0
	
	if crit_chance >= 39:
		@warning_ignore("integer_division")
		Attack_dmg = base_atk_dmg + floori((base_atk_dmg * 60)/100)
	else:
		Attack_dmg = base_atk_dmg
		
	return Attack_dmg

func knife_throw():
	
	var prob_knife_throw = [true, false, false].pick_random()
	var k_throw_dmg = 0
	
	if prob_knife_throw:
		k_throw_dmg = randi_range(2,4)

	return k_throw_dmg

func shield_Aatk():
	var shielded_atk: bool = [true,false].pick_random() # 50% probability
	var dmg_shielded = 0

	if shielded_atk == false: # didn't shield
		dmg_shielded = 0

	else: # shieled
		dmg_shielded = randi_range(3,6)
		# The dmg caused by wolf would be reduced by the number we get from this variable

	return [shielded_atk, dmg_shielded]
