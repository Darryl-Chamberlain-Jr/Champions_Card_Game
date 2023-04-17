from enum import Enum
import pygame
from models import *

class GameState(Enum):
    THINKING = 0
    FACEDOWN = 1
    REVEAL = 2
    ENDED = 3

class ChampionEngine:
    deck = None
    player1 = None
    player2 = None
    pile = None
    state = None
    currentPlayer = None
    result = None

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        self.pile = Pile()
        self.deal()
        self.currentPlayer = self.player1
        self.state = GameState.FACEDOWN

    def deal(self):
        for i in range(0, 3):
            self.player1.draw(self.deck)
            self.player2.draw(self.deck)

    def switchPlayer(self):
        if self.currentPlayer == self.player1:
            self.currentPlayer = self.player2
        else:
            self.currentPlayer = self.player1

    def winBattle(self, player):
        self.state = GameState.REVEAL
        # Win - Loss - Draw values?

    def play(self, key):
        if key == None:
            return 
        
        if self.state == GameState.ENDED:
            return
        
        # Player 1 chooses a card to place face down

        # Player 1 draws a card

        # Player 2 chooses a card to place face down

        # Player 2 draws a card

        # Reveal both cards. Assign each player a Win, Loss, or Draw

        