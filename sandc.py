import random

class Sandc:
	def __init__(self):
		self.states = {'Abia':'Umuahia', 'Anambra': 'Awka', 'Akwa Ibom':'Uyo', 'Adamawa':'Yola', 'Bauchi':'Bauchi', 'Bayelsa':'Yenagoa', 'Benue':'Makurdi', 'Borno':'Maiduguri', 'Cross River':'Calabar', 'Delta':'Asaba', 'Ebonyi':'Abakaliki', 'Edo':'Benin', 'Ekiti':'Ado-Ekiti', 'Enugu':'Enugu', 'Gombe':'Gombe', 'Imo':'Owerri', 'Jigawa':'Dutse', 'Kaduna':'Kaduna', 'Kano':'Kano', 'Katsina':'Katsina', 'Kebbi':'Birnin Kebbi', 'Kogi':'Lokoja', 'Kwara':'Ilorin', 'Ogun':'Abeokuta', 'Ondo':'Akure', 'Osun':'Osogbo', 'Oyo':'Ibadan', 'Plateau':'Jos', 'Rivers':'Porthacourt', 'Sokoto':'Sokoto', 'Taraba':'Jalingo', 'Yobe':'Damaturu', 'Zamfara':'Gusau', 'FCT':'Abuja'}
		self.score = 0
		self.used_states = []

	def get_state(self):
		state = random.choice(list(self.states))
		if state in self.used_states:
			return self.get_state()
		else:
			self.used_states.append(state)
			return {'state':state, 'capital':self.states[state]}
		# def question():
		# 	if len(self.states) > len(self.used_states):
		# 		state = self.unique_state()
		# 		answer = input(f'What is the capital of {state}?: ')
		# 		correct_capital = states_and_capitals[state]
		# 		if correct_capital.lower() == answer.lower():
		# 			score+=1
		# 			print('\nAwesome!\n')
		# 			start()
		# 		else:
		# 			print(f'The capital of {state} is {correct_capital}')
		# 			print(f'You scored {score}')
		# 			again = input('Want to go again? ')
		# 			if again.lower() == 'yes':
		# 				start()
		# 			else:
		# 				print('goodbye!')
		# 	else:
		# 		print(f"Hurray! you've answered all the questions\n You  scored {score}")
