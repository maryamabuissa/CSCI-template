import sys

# Variables
# format: {variable} = {value}
a = 1 # type: int
b = -3.1 # type: float
c = True # type: boolean
d = "Hello" # type: string
e = '8' # type: string
f = input() # type: string

# Best printing practice: fstrings

print(f"c is {c} and b is {b}")

# Operators

sum = a + b
prod1 = a * b
prod2 = a * e # error
power = a ** e_int
div = b / a
floor_div = a // b
mod = a % 2
# do tracing
concat1 = d + e
concat_invalid = d + a # error
concat2 = d + a_string
bool1 = c or a >= 2
bool2 = c and b == 1
bool3 = not c

# Operator precedence: 
# ()
# **
# *, /, //, %
# +, -
# ==, <=, >=, !=, <, >, is, in
# not
# and
# or
#
# left to right within a level


# Truth tables:
#
# true and true => true
# true and false => false
# false and false => false
#
# true or true => true
# true or false => true
# false or false => false
