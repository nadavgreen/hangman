class Game:
	@staticmethod
	def check(guess, guesses, random_word):
		pass
		Game._check_random_word(random_word)
		Game._check_guess(guess, random_word)
		Game._check_guesses(guesses, random_word)

		guesses.extend(letter for letter in guess if letter not in guesses)
		lives, solved = Game._remaining_lives(guesses, random_word)

		

		return {
			'lives': lives,
			'guesses': guesses,
			'random_word': Game._format(random_word, guesses),
			'solved': solved
		}

	@staticmethod
	def _check_guess(guess, random_word):
		pass
		if type(guess) != str:
			raise TypeError('type of guess or guess in guesses must be a str')
		if not len(guess):
			raise ValueError('length of guess or guess in guesses must be at least 1')
		if len(guess) > len(random_word):
			raise ValueError('length of guess or guess in guesses must be less than or equal to length of word')
		if not str.isalpha(guess):
			raise ValueError('value of guess or guess in guesses must be alpha')

	@staticmethod
	def _check_guesses(guesses, random_word):
		pass
		if type(guesses) != list:
			raise TypeError('type of guesses must be a list')
		for guess in guesses:
			Game._check_guess(guess, random_word)

	@staticmethod
	def _check_random_word(random_word):
		pass
		if type(random_word) != str:
			raise TypeError('type of random_word must be a str')
		if not len(random_word):
			raise ValueError('length of random_word must be at least 1')
		if not str.isalpha(random_word):
			raise ValueError('value of random_word must be alpha')

	@staticmethod
	def _remaining_lives(guesses, random_word):
		lives = 6
		solved = True
		
		for guess in guesses:
			if guess not in random_word:
				lives -= 1
			if not lives:
				break

		for letter in random_word:
			if letter not in guesses:
				solved = False
				break

		return lives, solved

	@staticmethod
	def _format(random_word, guesses):
		word = ''
		for letter in random_word:
			if letter in guesses:
				word += letter
			else:
				word += '*'

		return word
