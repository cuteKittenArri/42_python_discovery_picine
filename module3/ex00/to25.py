#!/usr/bin/env python3
i = int(input("Enter a number less than 25:"))
if i > 25:
	print("ERROR")
while i <= 25:
	print("Inside the loop, my variable is", i)
	i += 1
