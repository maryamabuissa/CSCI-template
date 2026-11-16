# file I/O

import os


with open('example.txt', 'w') as file:
    file.write("Hello, CSCI110!")

with open('example.txt', 'a') as file:
    file.write("\nKeep on learning!")

with open('example.txt', 'r') as file:
    print(file.read())

with open('example.txt', 'r') as file:
    for line in file:
        print(f"Professor A says {line}")

with open('example.txt', 'r') as file:
    print(file.readline())


# Good practice: check if file exists

print(os.path.isfile('example.txt'))
os.rename('example.txt', 'new_example.txt') # you can check size, rename, remove files


# terminal type stuff
print(os.getcwd())
os.mkdir('newDirectory')
os.chdir('newDirectory')
with open('example.txt', 'w') as file:
    file.write(input("What do you want to write?"))
print(os.listdir())

