extends Control

signal text_box_closed # A signal with name "text_box_closed"

@export var Enemy_wolf: Resource = null

var current_player_health = 0
var current_enemy_health = 0

func _ready(): # dunder operator to tell that the game has started
	
	set_health($"Wolf's box/HP bar", Enemy_wolf.health, Enemy_wolf.health)
	set_health($"Adventurer panal/Adventurer's box/HP bar", AdventurerState.C_Health, AdventurerState.M_Health)
	$"Wolf's box/Wolf".texture = Enemy_wolf.texture
	
	current_player_health = AdventurerState.C_Health
	current_enemy_health = Enemy_wolf.health
	
	$Display_Text.hide()
	# '$' is for the elements in the scene, using that is like mentioning the element in the scene
	# '.' something that comes after that is a function that element is capable of doing.
	$"Adventurer's actions".hide()
	# .hide() is like clicking the eye icon to hide that element from the scene.
	display("A wild %s has appeared!" % Enemy_wolf.name.to_upper() )
	# the display function helps us edit what is to appear in the lable of the panal.
	await (self.text_box_closed)
	# await is works like a buffer that waits for a signal to move onto other lines of code.
	$"Adventurer's actions".show()

func set_health(progress_bar, current_hp, max_hp):
	progress_bar.value = current_hp
	progress_bar.max_value = max_hp
	progress_bar.get_node("HP").text = "HP: %d/%d" % [current_hp, max_hp]

@warning_ignore("unused_parameter")
func _input(event): # dunder for dealing with inputs
	
	if (Input.is_action_just_pressed('ui_accept') or Input.is_mouse_button_pressed(MOUSE_BUTTON_LEFT)) and $Display_Text.visible:
		
		""" Input.is_action_just_pressed('ui_accept') - refers to is_action_just_pressed()
{is the action that was just done pressing} 'ui_accept' means {enter or space key} and that's
what it checks for """

		$Display_Text.hide()
		$"Adventurer's actions".show()
		emit_signal("text_box_closed") # Sends the "text_box_closed" signal off

func display(text):
	
	$"Adventurer's actions".hide()
	$Display_Text.show()
	$Display_Text/"Pop up message".text = text

func _on_exit_pressed():
	
	# Node specific dunder
	
	display("Press Enter/Space key to exit.")
	await (self.text_box_closed)
	@warning_ignore("redundant_await")
	await(get_tree().create_timer(0.25))
	
	# get_tree().create_timer(0.25) creats a timer for 0.25 sec,
	# which is inside the await that makes it wait for 0.25 sec
	
	get_tree().quit()
	# then the program ends

# ------------- Enemy's functions ------------- #

func enemy_decides_attack():
	return [true, false].pick_random()

func enemy_dodge_n_counter():
	var dodge = [true,true,false].pick_random()
	var counter_chance = randi_range(1,10)
	var counter_dmg = 0
	
	if dodge:
		if counter_chance >= 4:
			counter_dmg = randi_range(Enemy_wolf.min_counter_dmg, Enemy_wolf.max_counter_dmg)
		else:
			counter_dmg = 0
	else:
		counter_dmg = 0
		
	return [dodge, counter_dmg]
	
func enemy_atk_dmg():
	var base_dmg = randi_range(Enemy_wolf.min_base_atk_dmg, Enemy_wolf.max_base_atk_dmg)
	var crit_chances = randi_range(1,10)
	var ene_atk_dmg = 0
	
	if crit_chances >= 7:
		@warning_ignore("integer_division")
		ene_atk_dmg = base_dmg + floori((base_dmg * 60)/100)
	else:
		ene_atk_dmg = base_dmg
		
	return ene_atk_dmg

func enemy_dmg_ani():
	$AnimationPlayer.play("Enemy_damaged")
	await (get_tree().create_timer(0.6).timeout)
	
func screen_shake():
	$Camera2D.enabled = true
	$AnimationPlayer.play("shake")
	await (get_tree().create_timer(0.6).timeout)
	$Camera2D.enabled = false

func Enemy_turn_to_attack():
	
	win_or_lose_cond()
	
	display("Now it's %s turn!!" % Enemy_wolf.name)
	await (self.text_box_closed)
	
	var knife_atk_dmg = AdventurerState.knife_throw()
	var player_atk: bool = [true,false,false,false].pick_random()
	var player_atk_for_ene_turn = randi_range(1,4)
	var enemy_attack_dmg = enemy_atk_dmg()
	
	if player_atk:
		$"Adventurer's actions".hide()
		display('You got a chance to hit the %s with your sword while it\nwas attacking you, causing %d damage.' % [Enemy_wolf.name, player_atk_for_ene_turn])
		await (self.text_box_closed)
		current_enemy_health = max(0, current_enemy_health - player_atk_for_ene_turn)
		enemy_dmg_ani()
		
		display('While the %s caused %d damage to your health.' % [Enemy_wolf.name, enemy_attack_dmg])
		await (self.text_box_closed)
		current_player_health = max(0, current_player_health - enemy_attack_dmg)
		screen_shake()
		
	else:
		
		if knife_atk_dmg > 0:
			display('The %s missed it\'s chance to attack.' %Enemy_wolf.name)
			await (self.text_box_closed)
			display('You got really lucky and hit the %s with\nyour throable knife causing %d damage.' % [Enemy_wolf.name, knife_atk_dmg])
			await (self.text_box_closed)
			current_enemy_health = max(0, current_enemy_health - knife_atk_dmg)
			enemy_dmg_ani()
		else:
			$"Adventurer's actions".hide()
			display("The %s attacked at you feircely, which caused %d damage\nto your health." % [Enemy_wolf.name,max (0, enemy_attack_dmg - 2)])
			await (self.text_box_closed)
			current_player_health = max(0, (current_player_health) - max (0, enemy_attack_dmg - 2))
			screen_shake()
	
	set_health($"Wolf's box/HP bar", current_enemy_health, Enemy_wolf.health)
	set_health($"Adventurer panal/Adventurer's box/HP bar", current_player_health, AdventurerState.M_Health)

	# ------------- Enemy's functions ------------- #

func win_or_lose_cond():

	if (current_enemy_health == 0):
		display("%s was defeated!" % Enemy_wolf.name)
		await (self.text_box_closed)
		$"AnimationPlayer".play("Enemy_died")
		await($AnimationPlayer.animation_finished)
		get_tree().quit()

		
	elif (current_player_health == 0):
		display("you were defeated!")
		await (self.text_box_closed)
		$"AnimationPlayer".play("Player_died")
		await($AnimationPlayer.animation_finished)
		get_tree().quit()
		
	else:
		pass

func _on_attack_pressed():
	
	win_or_lose_cond()
	
	var knife_throw_atk_dmg = AdventurerState.knife_throw()
	var adven_atk_dmg = AdventurerState.attack_damage()
	var enemy_atk = enemy_atk_dmg()
	
	if enemy_decides_attack():
		
		display("You both decide to attack, leaving you both with a lot openings")
		await (self.text_box_closed)
		
		if (adven_atk_dmg*3) > (enemy_atk*2):
			
			display('You managed to deal %d, while %s only inflicted %d damage.' % [(adven_atk_dmg*3),Enemy_wolf.name,(enemy_atk*2)])
			await (self.text_box_closed)
		elif (adven_atk_dmg*3) == (enemy_atk*2):
			
			display('You both caused %d damage to each other.' % (adven_atk_dmg*3))
			await (self.text_box_closed)
		else:
			
			display('The %s caused %d damage, but you only caused\n%d damage to the %s.' % [Enemy_wolf.name,(enemy_atk*2),(adven_atk_dmg*3),Enemy_wolf.name])
			await (self.text_box_closed)
		
		current_enemy_health = max(0, current_enemy_health - (adven_atk_dmg*3))
		enemy_dmg_ani()
		current_player_health = max(0, current_player_health - (enemy_atk*2))
		screen_shake()
		
	else:
		
		var counter_chance = enemy_dodge_n_counter()
		
		if counter_chance[0] == true: # the array has two values one for it it dodges or not and one for the counter attack damage.
			if counter_chance[1] > 0:
				
				display("The %s dodged and counter attacked! inflicting %d damage" % [Enemy_wolf.name,counter_chance[1]])
				await (self.text_box_closed)
				current_player_health = max(0, current_player_health - counter_chance[1])
				screen_shake()
				
			else:
				if knife_throw_atk_dmg > 0:
					display('The %s dodged your attack, but you managed to inflict %d damage\nusing a throable knife' % [Enemy_wolf.name,knife_throw_atk_dmg])
					await(self.text_box_closed)
					current_enemy_health = max(0, current_enemy_health - knife_throw_atk_dmg)
					enemy_dmg_ani()
				else:
					display("The %s dodged but couldn't counter attack." % Enemy_wolf.name)
					await(self.text_box_closed)
					
		else:
			display("The %s dodged your attack, but couldn't counter attack." % Enemy_wolf.name)
			await (self.text_box_closed)
		
	set_health($"Wolf's box/HP bar", current_enemy_health, Enemy_wolf.health)
	set_health($"Adventurer panal/Adventurer's box/HP bar", current_player_health, AdventurerState.M_Health)
	
	if current_player_health != 0:
		Enemy_turn_to_attack() # calls enemy's turn function

func _on_shield_pressed():
	
	win_or_lose_cond()
	
	var enemy_deci = enemy_decides_attack()
	var knife_throw_adven = AdventurerState.knife_throw()
	var shielded_opt = AdventurerState.shield_Aatk()
	var enemy_atk = enemy_atk_dmg()
	
	var shielded_attack = shielded_opt[1]
	
	if (enemy_deci):
		if (shielded_opt[0]):
			if (enemy_atk > shielded_attack) and (shielded_attack > 0):
				var dmg_taken_by_adventurer = enemy_atk - shielded_attack
				$"Adventurer's actions".hide()
				display("The wolf managed to inflict %d damage." % dmg_taken_by_adventurer)
				await (self.text_box_closed)
				current_player_health = max(0, current_player_health - dmg_taken_by_adventurer)
				screen_shake()
			else:
				$"Adventurer's actions".hide()
				display("The adventurer managed to shield the attack completely!")
				await (self.text_box_closed)
		
	
	else:
		if (knife_throw_adven > 0):
			$"Adventurer's actions".hide()
			display("You saw the opportunity and attacked the %s with a\nthroable knife. It did %d damage." % [Enemy_wolf.name, knife_throw_adven])
			await (self.text_box_closed)
			current_enemy_health = max(0, current_enemy_health - knife_throw_adven)
			enemy_dmg_ani()
		else:
			$"Adventurer's actions".hide()
			display("You both decided not to attack each other.")
			await (self.text_box_closed)

	set_health($"Wolf's box/HP bar", current_enemy_health, Enemy_wolf.health)
	set_health($"Adventurer panal/Adventurer's box/HP bar", current_player_health, AdventurerState.M_Health)
	
	Enemy_turn_to_attack()
