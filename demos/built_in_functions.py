import sys
import random

# Recap: input

# Interactive input
name = input("What is your name?\n")
print(f"Hello, {name}!")

# Command line input
filename = sys.argv[0]
name = sys.argv[1]
print(f"Hello, {name}, from {filename}!")

# Common bugs
a = sys.argv[2] # index out of bounds
name = sys.argv(1) # Syntax
name = input
name = sys.argv[0]
input("what is your name?") # doesn't store

# Built in functions are written as a func_name(arg1, arg2, ...)

# Casting
print("the function 'int()' takes one argument, a string or a float, and tries to return the corresponding number")
a_string = str(a)
a_float = float(a)
b_int = int(b)
e_int = int(e)
invalid = int(d)
c_string = str(c)
c_int = int(c)
a_bool = bool(a)
b_bool = bool(b)
filename = sys.argv[0]
input = int(sys.argv[1])

# arguments
print("This string is the argument to 'print()' \n")
args = 3
print("print() can take", args, "(or more) arguments!")
# random.randint() is a function from the random module
# it takes specifically two arguments
ran = random.randint(1, 5)
# random.random() takes no arguments
ran = random.random()

# there are a lot of built in functions that deal with numbers
a = -3.3
a_abs = abs(a)
a_round = round(a)
print(f"we can take the absolute value of {a} to get {a_abs}")
print(f"or round it to get {a_round}")
hello = "Hello, world!"
print(f'"{hello}" has length {len(hello)}")

# Library: random numbers
ran = random.randint(1, 5)
print(f"group {ran} will present first")
ran = random.random() * 100
print(f"There is a {ran}% probability it will rain today")

# Common bugs: syntax errors
ran = random.random

# Common bugs: missing import
a = sys.argv[1]
a = random.random()

# Common bugs: wrong number of inputs
ran = random.random(1, 6)
ran = random.randint(6)
a = abs()
a = round(4.109, 2) # Wait - it works!
a = "1"
b = "2"
c = max(int(a, b))

# Common bugs: wrong type of input
a = int('hello')
a = "1"
b = abs(a)
b = bool("False") # Runs but at what cost
a = 1
print(len(a))
