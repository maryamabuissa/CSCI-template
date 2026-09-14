# This program decides the ticket price for someone
# What is the ticket price for a 10 y/o matinee?
import sys

def price(age, is_matinee):
    price = 10
    if age <= 3 and (not is_matinee) or age > 3:
        price += 3
    if age > 3 and age <= 13 and not is_matinee or age > 13:
        price += 4
    if age > 13 and not is_matinee:
        price += 5
    return price


def main():
    age = int(sys.argv[1])
    if age < 0:
        print(f"age cannot be negative")
        exit(1)
    is_matinee = bool(sys.argv[2])
    print(f"You price is {price(age, is_matinee)}")

if __name__== "__main__":
    main()
