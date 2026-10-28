#!/usr/bin/env python3
import sys
length = len(sys.argv)
if length == 1:
	print("none")
else:
	print(f"parameters: {length - 1}")
	for x in range(1, length):
		print(f"{sys.argv[x]}: {len(sys.argv[x])}")
