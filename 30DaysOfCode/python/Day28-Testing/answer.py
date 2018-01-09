#!/usr/bin/python
from __future__ import print_function

import sys
import random

T = random.randrange(5,20,1)
print (T)
for i in range(T):
	n = 3 + i
	k = 3
	if (i % 2) == 0:
		a = [-1] + [0] + [1] * (n - 2)
	else:
		a = [-1] + [0] * 2 + [1] * (n - 3)
	print(n, k)
	print (*a,sep=' ')