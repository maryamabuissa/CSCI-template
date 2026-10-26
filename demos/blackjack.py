import random

my_cards = []
your_cards = []

def create_sorted_deck():
    ranks = range(1, 13)
    suits = ["spades", "clubs", "hearts", "diamonds"]
    deck = []
    for rank in ranks:
        for suit in suits:
            deck.append({"suit": suit, "rank": rank})
    return deck

def get_random_card(deck):
    index = random.randint(0, len(deck) - 1)
    return deck.pop(index)

def sum_hand(hand):
    sum = 0
    for card in hand:
        sum += card["rank"]
    return sum

def deal_one_to_all(deck, hole):
    draw = get_random_card(deck)
    your_cards.append(draw)
    print(f"You drew the {draw["rank"]} of {draw["suit"]}")
    draw = get_random_card(deck)
    my_cards.append(draw)
    if not hole:
        print(f"I drew the {draw["rank"]} of {draw["suit"]}")
    else:
        print("My card is face down.")

def round():
    deck = create_sorted_deck()
    deal_one_to_all(deck, False)
    deal_one_to_all(deck, True)
    while input("hit? Type y/n\n") == "y":
        draw = get_random_card(deck)
        your_cards.append(draw)
        print(f"You drew the {draw["rank"]} of {draw["suit"]}")
        if sum_hand(your_cards) > 21:
            print("You lose!")
            exit()
    while sum_hand(my_cards) < 17:
        draw = get_random_card(deck)
        my_cards.append(draw)
        if sum_hand(my_cards) > 21:
            print(f"Well it's not much fair that I busted, I don't even get to choose what I do! It was only {sum_hand(my_cards)} anyways...")
            exit()
    your_sum = sum_hand(your_cards)
    my_sum = sum_hand(my_cards)
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


# What if I wanted to use a list of dictionaries to implement the following functionalities?
# Check if there are any duplicate cards in play
# Combine multiple hands
# Compare winning hands in a game like poker
# Compare two cards
# Print cards often
# Validate user input
