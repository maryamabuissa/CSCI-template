import random

class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def rank(self):
        return self.rank

    def suit(self):
        return self.suit

    def to_string(self):
        return f"{self.rank} of {self.suit}"

class Deck:

    def __init__(self, fill):
        if not fill:
            self.deck = []
        else:
            ranks = range(1, 13)
            suits = ["spades", "clubs", "hearts", "diamonds"]
            self.deck = [Card(rank, suit) for rank in ranks for suit in suits]
    
    def sum(self):
        return sum([card.rank for card in self.deck])

    def draw(self, player_to_display=False):
        index = random.randint(0, len(self.deck) - 1)
        c = self.deck.pop(index)
        if player_to_display:
            print(f"{player_to_display} drew {c.to_string()}")
        return c

    def drew(self, card):
        self.deck.append(card)
