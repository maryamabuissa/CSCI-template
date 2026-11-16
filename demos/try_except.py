
i = input("What is your age?\n")

try:
    age = int(i)
except ValueError:
    print("You must enter a number between 0 and 125")
    exit(1)

if age < 0 or age > 125:
    print("You must enter a number between 0 and 125")
    exit(1)

if age >= 18:
    print("You can vote")
else:
    print("You can't vote yet")