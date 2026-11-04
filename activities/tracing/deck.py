from tmp import Card, Deck

# What would the following code print if I added "print(a)" at the first comment? 
# What about print(b) at the second comment?
# What about print(b.sum())?

def main():
    a = Deck(True)
    b = Deck(False)
    c = Card(20, "banana")
    d = a.draw()
    b.drew(c)
    b.drew(d)
    # ADD CODE HERE

    e = Card("banana", 20)
    b.drew(e)
    # OR ADD CODE HERE

if __name__ == "__main__":
    main()
