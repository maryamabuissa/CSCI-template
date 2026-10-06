# list indexing/slicing

# a list is a list of elements of a any type (different from other languages)
cheeses = ['Cheddar', 'Feta', 'Gouda']
first_cheese = cheeses[0] # 0-indexing
last_cheese = cheeses[len(cheeses) - 1] # error
last_char = cheeses[-1]

# lists can have any type
weird = [first_cheese, 1, 2]
# nested list
weird2 = [[1, 2], "hello", True]
print(len(weird2))
print(2 in weird2)
print(1 in weird2) # Unexpected - but "True == 1" is technically true

# slicing is the same as with strings 
first_half = cheeses[:len(cheeses)//2]
last_half = cheeses[len(cheeses)//2:]

# lists are mutable
cheeses[-1] = "Mozzarella" 
print(cheeses)
new_cheeses = cheeses[:-1] + ["Compte"] # does the same thing into a new list
print(new_cheeses)

# you can compare lists for equality
# Common bugs: equal vs identical
a = [4, 5]
b = [4, 5]
print("is a equal to b?", a == b)
print("is a identical to b?", a is b)
b = a
print("is a identical to b?", a is b)

# many list methods
# Some change the list "in place"
a.append(4)
print(a)
# Some return something
c = a.copy()
print("is a identical to c?", a is c)
print(a.count(4))
first = a.pop(0)
print(f"Removed {first} from {a} at index 0")
d = a.reverse()
print(d)
print(a)
