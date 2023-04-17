# main.py

import pygame
from models import *
from engine import *
  
pygame.init()

gameEngine=ChampionEngine()

bounds = (1024, 768)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("Champions")

cardBack = pygame.image.load('images/BACK.png')

def scale_card_image(card_image):
    scaled_image=pygame.transform.scale(card_image, (int(238*0.6), int(332*0.6)))
    return scaled_image

def renderIntro(window):
    window.fill((15,0,169))
    font = pygame.font.SysFont('comicsans',60, True)
    window.blit(scale_card_image(cardBack), (650, 200))
    win_loss_tie_text=font.render(f'W-L-T', True, (255,255,255))
    window.blit(win_loss_tie_text, (700, 10))

def renderGame(window):
    window.fill((15,0,169))
    font = pygame.font.SysFont('comicsans',60, True)

    # Player 1 Hand
    window.blit(scale_card_image(gameEngine.player1.hand[0].image), (50, 200))
    window.blit(scale_card_image(gameEngine.player1.hand[1].image), (150, 200))
    window.blit(scale_card_image(gameEngine.player1.hand[2].image), (250, 200))
    
    # Player 2 Hand
    window.blit(scale_card_image(cardBack), (650, 200))
    window.blit(scale_card_image(cardBack), (750, 200))
    window.blit(scale_card_image(cardBack), (850, 200))

    # Win - Loss - Tie
    win_loss_tie_text=font.render(f'W-L-T', True, (255,255,255))
    # Win - Loss - Tie Player 1
    w_l_t_p1 = font.render(f'{gameEngine.player1.wins}-{gameEngine.player1.losses}-{gameEngine.player1.ties}', True, (255,255,255))
    window.blit(win_loss_tie_text, (100, 10))
    window.blit(w_l_t_p1, (120, 70))

    # Win - Loss - Tie Player 2
    w_l_t_p2 = font.render(f'{gameEngine.player2.wins}-{gameEngine.player2.losses}-{gameEngine.player2.ties}', True, (255,255,255))
    window.blit(win_loss_tie_text, (700, 10))
    window.blit(w_l_t_p2, (720, 70))

    topCard = gameEngine.pile.peek()
    if (topCard != None):
        window.blit(topCard.image, (400, 200))

# Intro window
renderIntro(window)
pygame.display.update()
pygame.time.delay(3000)

run = True
while run:
    key = None;
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            key = event.key

    gameEngine.play(key)

    renderGame(window)
    pygame.display.update()

    if gameEngine.state == GameState.REVEAL:
        pygame.time.delay(3000)
        gameEngine.state = GameState.FACEDOWN