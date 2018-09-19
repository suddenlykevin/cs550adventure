#in-class guessing game practice
#Kevin Xie 09/17/2018
#Not the final project, but first attempt at a guessing game in class.

import random

def start():
	guess = input("\nGuess how many humans I ate today!\n\n>>> ")
	if int(guess) > answer:
		print("\nDo I really look that fat? Lower.")
		start()
	elif int(guess) < answer:
		print("\nI'll have you know I come from an affluent family. Higher.")
		start()
	elif int(guess) == answer: # could use "else"
		print("\nRight on the money, lil' human. But I've got room for one more!")

answer = random.randint(0,60)
start()