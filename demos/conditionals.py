
age = int(input("How old are you?\n"))

# Conditionals create control flow
if age >= 18: # if statement
    print("You can vote!")
    print("and you have full legal rights")
elif age < 0: # else if statement
    print("Your age seems off...")
else: # else statement
    print("You cannot vote :(")

if age >= 18 and random.random() == 0: # and returns true if both sides are true
    print("It's your lucky day, you can vote!")
else:
    if age == 100: # Nested if statement
        print("congrats on the centennial! Still can't vote though.")
    print("Sorry bud, no luck.")

# Truth tables: 
# true and true -> true
# true and false -> false
# true or true -> true
# true or false -> true
# not true -> false
# not false -> true

# Common bugs: syntax and indentation 
if age >= 18
    print("oops")

if age >= 18:
    print("You can vote")
    else: 
        print("You cannot vote")

if age >= 18:
print("You can vote")

if age = 18:
    print("You must register to vote")
