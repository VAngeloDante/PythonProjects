import math
import random
import threading
import os
import keyboard

class Card:
    SUITS = ["Hearts", "Clubs", "Diamonds", "Spades"]
    RANKS = [("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6), ("7", 7),
             ("8", 8), ("9", 9), ("10", 10), ("J", 10), ("Q", 10), ("K", 10), ("A", 11)]

    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f"{self.rank} of {self.suit} with value of {self.value}"
    
def esc_listener():
    keyboard.wait('esc')
    print("ESC pressed! Exiting...")
    os._exit(0)

my_deck = []
for suit in Card.SUITS:
    for rank, value in Card.RANKS:
        my_deck.append(Card(suit, rank, value))
random.shuffle(my_deck)  # Shuffle the deck

isGameOver = False
isTie = False

dealers_hand = []
players_hand = []
dealers_hand.append(my_deck.pop())
players_hand.append(my_deck.pop())
players_hand.append(my_deck.pop())
print(f"Dealer's hand: {dealers_hand[0]} and a hidden card")
print(f"Player's hand: {players_hand[0]} and {players_hand[1]}")
while not isGameOver and not isTie:
    threading.Thread(target=esc_listener, daemon=True).start()

    player_score = sum(card.value for card in players_hand)
    dealer_score = sum(card.value for card in dealers_hand)
    player_choice = input(f"Your current score is {player_score}. Would you like to hit or stand? (h/s): ").lower()
    if player_choice != 'h' and player_choice != 's':
        print("Invalid input, please enter 'h' to hit or 's' to stand.")
        continue
    if player_choice == 'h':
        players_hand.append(my_deck.pop())
        player_score = sum(card.value for card in players_hand)
        if player_score > 21 and any(card.rank == "A" for card in players_hand):
            for card in players_hand:
                if card.rank == "A" and card.value == 11:
                    card.value = 1
                    break
            player_score = sum(card.value for card in players_hand)
        print(f"Player's hand: {[str(card) for card in players_hand]} with score of {player_score}")
        if player_score > 21:
            print("Player busts! Dealer wins.")
            isGameOver = True
            break
    else:
        while dealer_score < 17:
            dealers_hand.append(my_deck.pop())
            print(f"Dealer's hand: {[str(card) for card in dealers_hand]}")
            dealer_score = sum(card.value for card in dealers_hand)
        if dealer_score > 21:
            print(f"Dealer busts with score of {dealer_score}")
            print(f"Player wins!")
            isGameOver = True
            break
        if dealer_score > player_score:
            print(f"Dealer wins with score {dealer_score} agains player's score {player_score}")
            isGameOver = True
            break
        if dealer_score < player_score:
            print(f"Player wins with score {player_score} agains dealer's score {dealer_score}")
            isGameOver = True
            break
        else:
            print(f"It's a tie, both players have a score of {player_score}")
            isGameOver = True
            break