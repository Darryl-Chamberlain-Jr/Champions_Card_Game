from enum import Enum
import pygame
import random

class Suits(Enum):
    Jewel = 4
    Electrum = 3
    Silver = 2
    Copper = 1

class Card:
    suit = None
    value = None
    image = None
    rank = 0

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.image = pygame.image.load('images/' + str(self.value) + '_of_' + self.suit.name + '.jpeg')

    def convert_to_rank(self):
        # value is the 10s place
        if str(self.value) == "Dragon":
            self.rank = 40
        elif str(self.value) == "Sphinx":
            self.rank = 30
        elif str(self.value) == "Pharoah":
            self.rank = 20
        else:
            self.rank = 10

        if self.suit.name == "Jewel":
            self.rank += self.suit.Jewel.value
        elif self.suit.name == "Electrum":
            self.rank += self.suit.Electrum.value
        elif self.suit.name == "Silver":
            self.rank += self.suit.Silver.value
        else:
            self.rank += self.suit.Copper.value

class Deck:
    cards = None

    def __init__(self):
        self.cards=[]
        for suit in Suits:
            for value in ["Croc", "Pharoah", "Sphinx", "Dragon"]:
                new_card=Card(suit, value)
                new_card.convert_to_rank()
                self.cards.append(new_card)

    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        return self.cards.pop()
        
    def length(self):
        return len(self.cards)

class Player:
    hand = None
    name = None
    deck = None
    played_card = None
    wins = 0
    losses = 0
    ties = 0
    card_1_key = None
    card_2_key = None
    card_3_key = None

    def __init__(self, name, deck, card_1_key, card_2_key, card_3_key):
        self.hand = []
        self.name = name
        self.deck = deck
        self.card_1_key = card_1_key
        self.card_2_key = card_2_key
        self.card_3_key = card_3_key

    def draw(self):
        self.hand.append(self.deck.cards.pop(0))

#    def play(self, played_card):
#        return self.hand.pop(played_card)