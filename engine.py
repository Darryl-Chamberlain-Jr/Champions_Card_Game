from enum import Enum
import pygame
import random
from models import *

class GameState(Enum):
    INTRO = -1
    START = 0
    THINKING = 1
    FACEDOWN = 2
    REVEAL = 3
    TALLYSCORE = 4
    ENDED = 5

class ChampionEngine:
    player1 = None
    player2 = None
    state = None
    result = None

    def __init__(self):
        self.state = GameState.INTRO
        self.player1 = Player("Player 1", Deck(), pygame.K_q, pygame.K_w, pygame.K_e)
        self.player1.deck.shuffle()
        
        self.player2 = Player("Player 2", Deck(), pygame.K_q, pygame.K_w, pygame.K_e)
        self.player2.deck.shuffle()
        
        self.deal()

    def deal(self):
        for i in range(0, 3):
            self.player1.draw()
            self.player2.draw()
    
    def cpu_play_card(self):
        self.player2.played_card = self.player2.hand.pop(random.randint(0, 2))

    # Go from THINKING to FACEDOWN
    def play_card(self, key):
        if key == pygame.K_q:
            self.player1.played_card = self.player1.hand.pop(0)
        elif key == pygame.K_w:
            self.player1.played_card = self.player1.hand.pop(1)
        elif key == pygame.K_e:
            self.player1.played_card = self.player1.hand.pop(2)
        else:
            print('Incorrect key')