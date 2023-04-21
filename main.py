# main.py

import pygame
from models import *
from engine import *
  
pygame.init()

gameEngine=ChampionEngine()

bounds = (1200, 800)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("Champions")

cardBack = pygame.image.load('images/BACK.jpeg')

def scale_card_image(card_image):
    scaled_image=pygame.transform.scale(card_image, (int(238*0.6), int(332*0.6)))
    return scaled_image

def renderIntro(window):
    window.fill((178, 144, 130))
    font = pygame.font.SysFont('Times', 60, True)
    window.blit(scale_card_image(cardBack), (650, 200))
    win_loss_tie_text=font.render(f'W-L-T', True, (255,255,255))
    window.blit(win_loss_tie_text, (700, 10))

def renderGame(window):
    window.fill((178, 144, 130))
    font = pygame.font.SysFont('arial',60, True)
    card_font = pygame.font.SysFont('arial', 30, True)

    # Player 1 Hand
    window.blit(scale_card_image(gameEngine.player1.hand[0].image), (50, 200))
    window.blit(card_font.render(f'{gameEngine.player1.hand[0].suit.name}', True, (255,255,255)), (50, 400))
    window.blit(card_font.render(f'{gameEngine.player1.hand[0].value}', True, (255,255,255)), (50, 435))

    window.blit(scale_card_image(gameEngine.player1.hand[1].image), (200, 200))
    window.blit(card_font.render(f'{gameEngine.player1.hand[1].suit.name}', True, (255,255,255)), (200, 400))
    window.blit(card_font.render(f'{gameEngine.player1.hand[1].value}', True, (255,255,255)), (200, 435))

    window.blit(scale_card_image(gameEngine.player1.hand[2].image), (350, 200))
    window.blit(card_font.render(f'{gameEngine.player1.hand[2].suit.name}', True, (255,255,255)), (350, 400))
    window.blit(card_font.render(f'{gameEngine.player1.hand[2].value}', True, (255,255,255)), (350, 435))
    
    # Player 2 Hand
    window.blit(scale_card_image(cardBack), (650, 200))
    window.blit(scale_card_image(cardBack), (800, 200))
    window.blit(scale_card_image(cardBack), (950, 200))

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

    # Strengths Legend
    suit_strengths_statement=font.render('Copper < Silver < Electrum < Jewel', True, (255,255,255))
    value_strengths_statement=font.render('Croc < Pharoah < Sphinx < Dragon', True, (255,255,255))
    window.blit(suit_strengths_statement, (100, 675))
    window.blit(value_strengths_statement, (100, 600))


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