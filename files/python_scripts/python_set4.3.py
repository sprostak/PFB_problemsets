#!/usr/bin/env python3

## SMP 10-12-2022

import sys

start = int(sys.argv[1])
end = int(sys.argv[2])

for i in range(start, end+1):
	if i % 2 != 0:
		print(i)





