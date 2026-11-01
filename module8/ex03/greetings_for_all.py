#!/usr/bin/env python3
def greetings(name="noble stranger"):
	if isinstance(name, str):
		print(f"Hello, {name}.")
	else:
		print("ERROR! It was not a name.")

greetings("CS looser")
greetings("42 King")
greetings(420)
greetings()
