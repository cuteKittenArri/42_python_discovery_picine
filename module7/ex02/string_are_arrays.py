#!/usr/bin/env python3
import sys
boo = False
if len(sys.argv) - 1 != 1:
	print("none")
else:
	s = sys.argv[1]
	for c in s:
		if c == 'z':
			print(c, end='')
			boo = True
	if boo != True:
		print("none")
	else:
		print()
