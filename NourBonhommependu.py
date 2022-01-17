#!/usr/bin/env python3

import random

with open('randomwordlist.py', 'r') as f:
	words = f.readlines()

mot = random.choice(words)[:-1]

allowed_errors = 6
guesses = []
done = False

while not done:
	for letter in mot:
		if letter.lower() in guesses: 
			print(letter, end =" ")
	else:
		print("_", end=" ")
	print(" ")
	guess = input(f'nombre erreurs restante {allowed_errors}, Prochaine lettre:')
	guesses.append(guess.lower())
	if guess.lower() not in mot.lower():
		allowed_errors -= 1
		if allowed_errors == 0:
			break
		
	done = True 
	for letter in mot:
		if letter.lower() not in guesses:
			done = False 
			
if done:
	print(f'Ta trouver le mot {mot} salope!')
else:
	print(f't fkg nul lol')
