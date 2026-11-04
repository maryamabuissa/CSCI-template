import random

class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Deck:

    def __init__(self, fill):
        if not fill:
            self.deck = []
        else:
            ranks = range(1, 14)
            suits = ["spades", "clubs", "hearts", "diamonds"]
            self.deck = [Card(rank, suit) for rank in ranks for suit in suits]
    
    def __str__(self):
        return self.deck

    def sum(self):
        return sum([card.rank for card in self.deck])

    def draw(self, player_to_display=False):
        index = random.randint(0, len(self.deck) - 1)
        c = self.deck.pop(index)
        if player_to_display:
            print(f"{player_to_display} drew {c}")
        return c

    def drew(self, card):
        self.deck.append(card)



 def round():
     deck = Deck(True)
     your_cards = Deck(False)
     my_cards = Deck(False)
     your_cards.drew(deck.draw("You"))
     my_cards.drew(deck.draw("I"))
     your_cards.drew(deck.draw("You"))
     my_cards.drew(deck.draw())
     while input("hit? Type y/n\n") == "y":
         your_cards.drew(deck.draw("You"))
         if your_cards.sum() > 21:
             print("You lose!")
             return
     while my_cards.sum() < 17:
         my_cards.drew(deck.draw("I"))
         if my_cards.sum() > 21:
             print(f"Well it's not much fair that I busted, I don't even get to choose what I do! It was only {my_cards.sum()} anyways...")
             return
     your_sum = your_cards.sum()
     my_sum = my_cards.sum()
     if your_sum > my_sum:
         print(f"Dang you! You dirty cheater. No way you scored {your_sum} when I only got {my_sum}")
     elif my_sum > your_sum:
         print(f"Obviously *rolls eyes* I win again. My {my_sum} easily bests your measly {your_sum}")
     else:
         print("A tie...?!")

 def main():
     print("Welcome to blackjack! I am the dealer.")
     rounds = 1
     for _ in range(rounds):
         round()

 if __name__ == "__main__":
     main()
