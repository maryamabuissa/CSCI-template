# This program decides if you win a cash prize based on your ticket number
# How much money does ticket number 1 win? 
# What about ticket number 402?
# What about ticket number 1000?

import sys

def prize(ticket_num):
    prize = 0
    if 200 <= ticket_num <= 500:
        return prize
    if "0" in str(ticket_num) and "2" in str(ticket_num):
        prize += 200
    elif ticket_num % 33 == 0 or ticket_num % 23 == 0:
        prize += 323
    else:
        for i in str(ticket_num):
            prize += 10
    return prize


def main():
    ticket_num = int(sys.argv[1])
    if ticket_num < 0:
        print(f"ticket number cannot be negative")
        exit(1)
    print(f"You prize is {prize(ticket_num)}")

if __name__== "__main__":
    main()
