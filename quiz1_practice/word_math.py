'''
What does this program print?

a) 
Happy birthday to you Happy birthday to you
Happy birthday dear Nunu Happy birthday to you

b)
Happy birthday to youHappy birthday to you
Happy birthday dear NunuHappy birthday to you

c)
Happy birthday to youHappy birthday to you
Happy birthday dear Nunu Happy birthday to you
'''
b = "Nunu"
name = b
a = "Happy birthday "
c = "dear " + name
b = "to you"

print((a + b) * 2)
print(a + c, a + b)
