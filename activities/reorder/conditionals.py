import random

# Broken: move or add code
age = int(input("Age?\n"))
if age > 18:
    print("You can vote!")
print("You cannot vote")

# Broken: move, remove, or change indentation of code
age = int(input("Age?\n"))
citizen = input("Citizenship?\n") == "True"
if age > 18 and citizen:
    print("You can vote!")

# Broken: modify conditionals
income = int(input("Income?\n"))
work = input("Did you work here?\n") == "True"
resident = input("Are you a resident?\n") == "True"
if income > 6000 and (work or resident):
    print("You have to pay taxes.")

# Broken: add missing lines of code (hint: what is x = 4 and y = 4?)
x = 4
y = 4
if x > y:
    print('x is greater than y')
elif x == y:
    print("x equals y")
elif x < y:
    print('x is less than y')

# Broken: modify if/else structure
if x < y:
    print('x is less than y')
if x > y:
    print('x is greater than y')
else:
    print('x and y are equal')

