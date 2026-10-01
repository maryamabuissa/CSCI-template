# string indexing/slicing

# A string is a list of characters
string = "banana!"
first_char = string[0] # 0-indexing??
last_char = string[len(string)] # error
last_char = string[len(string) - 1] 
last_char = string[-1] 

# indices must be integers
error = string[1.5]

# you can slice with string[start:end] where start is inclusive and end is exclusive
first_half = string[0:len(string)//2]
first_half = string[:len(string)//2]
last_half = string[len(string)//2:]
first_char = string[:1]
empty = string[1:1]

# strings are immutable
string[-1] = "?" # error
new_string = string[:-1] + "?" # You have to make a new one


# string comparison and methods

# you can compare strings
string2 = "banana?"
string3 = "orange"
print(string == string2)
print(string[:-1] == string2[:-1])
print(string < string3) # compares alphabetically
print(string > string3)
print(string > string2) # non letters may be unexpected

# there are many string methods
print(string.upper()) # we've used
camel = "CamelCase"
print(camel.swapcase())
hello = "Hello,world,camel"
split_list = hello.split(",") # we've use, but now it makes more sense
print(split_list)
