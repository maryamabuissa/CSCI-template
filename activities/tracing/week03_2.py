# What does the following program print?
# a) I believe... b is 7
# I believe... b is 7
#
# b) I believe.. b is 10
# I believe.. b is 10
#
# c) I believe.. b is 10
# I believe... b is 7
#
# d) I believe.. b is 7
# I believe.. b is 10

def useless(b, a): # Must define first so it can be called
    print(f"I believe... b is {a}")

def useful(a, b):
    a = b
    useless(a, b)

# Note: code starts running HERE!
b = 10
a = 7
useful(10, 7)
print(f"I believe... b is {b}")
