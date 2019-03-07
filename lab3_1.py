import sys
import math

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

c_c = c * c
aa_bb = (a*a) + (b*b)

if c_c == aa_bb :
	print('triangle')
elif a == b == c:
	print('triangle')
else :
	print('not triangle')
