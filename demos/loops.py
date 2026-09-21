import time

# For loops

# syntax to iterate through a list
# for elt in <list>:
for i in range(10):
    print(i)

word = "monument"
for letter in word:
    print(letter, end=" ")

# While loops

# syntax to repeat something until a boolean is false
# while <boolean>:
while (True):
    print("This runs forever")
    time.sleep(1)

i = 0
while i < 10:
    print(f"iteration {i}")
    i = i + 1


# Common bugs: indentation
word = "monument"
for letter in word:
if letter == "x":
    print("Found an x!")

# Common bugs: off by one
n = 10
for i in range(n):
    if i == n:
        print("last iteration")
    else:
        print(f"iteration {i},")
while i <= 10:
    print(i)
    i = i + 1

# Common bugs: scope
i = 3
for i in range(10):
    print(i)
print(f"I sure hope {i} is 3...")

# Common bugs: increment issues
i = 0
while i < 10:   # runs forever
    print(i)

while i < 10:
    if i % 3 == 0:
        print(f"{i} divisible by 3")
        i = i + 1
    elif i % 2 == 0:
        print(f"{i} is even")
    i = i + 1
