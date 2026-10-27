#!/usr/bin/env python3
x = 0
y = 0
while  x <= 10:
	print("Table of", x, end=": ")
	while y <= 10:
		print(x*y, end=' ')
		y += 1
	print()
	x += 1
	y = 0
