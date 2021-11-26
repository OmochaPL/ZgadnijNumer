	import random

	def guess(x) :
		random_number = random.randint(1,x)
		guess = 0
		while guess != random_number:
		guess = int(input(f'Zgadnij o której liczbie  w zakresie od 1 do {x} własnie myślę?')
		if guess < random_number:
			print ('Za mało!')
		elif guess > random_number:
			print ('Za dużo!')
	print(f'Wygrałeś! Właśnie myślałem o liczbie {random_number}!')
		
guess(20)
