# Writing spam

s = input("What should I print?\n")
print(s, s, s, s)
print(s, s, s, s)
print(s, s, s, s)

# Put repeated code into functions
def spam():
    s = input("What should I print?\n")
    print(s)
    print(s)
    # More succinct
    print((s + ", ") * 4)
    # Code that handles the last comma correctly
    print((s + ", ") * 3 + s)

# You have to call functions to run them
spam()
spam()

# Divide repeated code by function
def spam(i): # bad idea to give it the same name
    print((i + ", ") * 3 + i)

s = input("What should I print?\n")
spam(s)

def add(a, b):
    print(f"the sum is {a + b}") # Another nice thing about f strings

add(1, 2) 
c = add(1, 2) # return values: next week
print(c) # unexpected

# Common bugs: calling functions syntax
spam_input # Missing parentheses
take_input() # Doesn't store return value
spam() # Missing parameter
print(i) # No longer accessible - more on that later

# Common bugs: writing functions syntax 
def spam_long(i) # Missing colon
    print((i + ", ") * 10)

def spam_long(i):
print((i + ", ") * 10) # Missing indentation

def spam_long(i): # References wrong variable
    print((s + ", ") * 10)
