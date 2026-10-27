#!/usr/bin/env python3
print("Enter the first number:")
x = int(input())
print("Enter the second number:")
y = int(input())
result = x * y
print(x, 'x', y, '=', result)
if result < 0:
	print("This number is negative.")
if result > 0:
	print("This number is positive.")
if result == 0:
	print("This number is both positive and negative.")
