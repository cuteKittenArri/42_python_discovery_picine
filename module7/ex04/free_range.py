#!/usr/bin/env python3
import sys
if len(sys.argv) != 3:
	print("none")
else:
	num1 = int(sys.argv[1])
	num2 = int(sys.argv[2])
	array = []
	for i in range(num1, num2 + 1):
		array.append(i)
	print(array)
