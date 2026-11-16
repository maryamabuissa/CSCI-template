# Common bugs: equal vs identical
a = [4, 5]
b = [4, 5]
print("is a equal to b?", a == b)
print("is a identical to b?", a is b)
b = a
print("is a identical to b?", a is b)
