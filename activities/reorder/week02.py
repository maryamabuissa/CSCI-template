import sys


# Rearrange these lines of code to swap variables a and b

a = sys.argv[1] # (c) - takes first input
b = sys.argv[2] # (e) - takes second input

tmp = a         # (a)
a = b           # (b)
b = tmp         # (d)

print(a, b)
