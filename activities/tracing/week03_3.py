# What does the following print?
# a) the sum is 4
# b) the sum is 4
# the sum is 3
# c) the sum is 3 
# d) the sum is 3
# the sum is 3
# the sum is 3
# e) none of the above


def add(a, b):
    print(f"the sum is {a + b}") # Another nice thing about f strings

a = 2
b = 2

add(1, b) 
c = add(a, 3)
print(c) 
