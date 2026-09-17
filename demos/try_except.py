
# Take input between 0 and 125
input = input("How old are you?\n")

try: # run this line of code if it doesn't give an error
    age = int(input)
except ValueError: # if it gives a ValueError, exit
    print("You must enter an integer between 0 and 125.")
    exit(1)
if age < 0 or age > 125: # if they entered an invalid age, exit
    print("You must enter an integer between 0 and 125.")
    exit(1)

# Check if the user is of voting age or not
if age >= 18: # if statement
    print("You can vote!")
else: # else statement
    print("You cannot vote :(")

