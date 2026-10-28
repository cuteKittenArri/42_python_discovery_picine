#!/usr/bin/env python3
import sys
import re
length = len(sys.argv) - 1
if length != 2:
	print("none")
else:
	findings = re.findall(sys.argv[1], sys.argv[2])
	if not findings:
		print("none")
	else:
		print(len(findings))
