from random import randint

random_number = randint(1, 99999999999999999999999999999999999999999999)

def numberwang(random_number):

	guesses_left = 99999999999999999999999999999999999999999998

	while guesses_left > 0:
		guess = int(raw_input("Lets play Numberwang! Numberwang? "))
		guesses_left = guesses_left - 1

		if guess == random_number:
			print "Thats Numberwang!"
			break

		elif guess != random_number:
			print "Thats no Numberwang."
			print "You have %s chances left to Numberwang." %(guesses_left)
	
		else:
			print "Awww, bad luck, you've been Wangernumbed."

numberwang(random_number)
