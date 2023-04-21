from enum import Enum
import pygame
import random

class Suits(Enum):
    Electrum = 4
    Jewel = 3
    Silver = 2
    Copper = 1

class Card:
    suit = None
    value = None
    image = None

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.image = pygame.image.load('images/' + str(self.value) + '_of_' + self.suit.name + '.jpeg')

class Deck:
    cards = None

    def __init__(self):
        self.cards=[]
        for suit in Suits:
            for value in ["Croc", "Pharoah", "Sphinx", "Dragon"]:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        return self.cards.pop()
        
    def length(self):
        return len(self.cards)
    
class Pile:
    cards = None
    
    def __init__(self):
        self.cards = []
    
    def add(self, card):
        self.cards.append(card)

    def peek(self):
        if len(self.cards) > 0:
            return self.cards[-1]
        else:
            return None
    
    def popAll(self):
        return self.cards
    
    def clear(self):
        self.cards = []

class Player:
    hand = None
    name = None
    wins = 0
    losses = 0
    ties = 0

    def __init__(self, name):
        self.hand = []
        self.name = name

    def draw(self, deck):
        self.hand.append(deck.deal())

    def play(self):
        return self.hand.pop(0)