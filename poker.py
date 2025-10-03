import math
import random
import threading
import os
import keyboard

class Card:
    SUITS = ["Hearts", "Clubs", "Diamonds", "Spades"]
    RANKS = [("2", 1), ("3", 2), ("4", 3), ("5", 4), ("6", 5), ("7", 6),
             ("8", 7), ("9", 8), ("10", 9), ("J", 10), ("Q", 11), ("K", 12), ("A", 13)]

    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f"{self.rank} of {self.suit}"

def esc_listener():
    keyboard.wait('esc')
    print("ESC pressed! Exiting...")
    os._exit(0)

my_deck = []
for suit in Card.SUITS:
    for rank, value in Card.RANKS:
         my_deck.append(Card(suit, rank, value))
    random.shuffle(my_deck)

player_hand = []
for i in range(5):
    player_hand.append(my_deck.pop())
player_hand.sort(key=lambda card: card.value, reverse=False) #key=lambda - for each card in the list sort by card.value
print(f"You have: {[str(card) for card in player_hand]}")
i = 0
for card in player_hand:
    threading.Thread(target=esc_listener, daemon=True).start()
    print(f"Do you want to redraw {card}? (y/n)")
    response = input().lower()
    if response != 'y' and response != 'n':
        print("Invalid input, please enter 'y' or 'n'.")
        response = input().lower()
    if response == 'y':
        player_hand[i] = my_deck.pop()
    else:
        pass
    i += 1
player_hand.sort(key=lambda card: card.value, reverse=False)
print(f"Your final hand: {[str(card) for card in player_hand]}")

def evaluate_hand(hand):
    # Check for flush / poker
    # Check for straight
    # Check for pairs, three of a kind, four of a kind, full house