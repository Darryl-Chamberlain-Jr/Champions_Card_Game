# main.py

import pygame
from models import *
from engine import *
  
pygame.init()

gameEngine=ChampionEngine()

bounds = (1200, 800)
intro_window = pygame.display.set_mode(bounds)
pygame.display.set_caption("Champions")

cardBack = pygame.image.load('images/BACK.jpeg')

def scale_card_image(card_image):
    scaled_image=pygame.transform.scale(card_image, (int(238*0.6), int(332*0.6)))
    return scaled_image

def renderIntro(window):
    window.fill((178, 144, 130))
    # Player 2 Hand
    window.blit(scale_card_image(cardBack), (650, 200))
    window.blit(scale_card_image(cardBack), (800, 200))
    window.blit(scale_card_image(cardBack), (950, 200))

def renderStart(window):
    window.fill((178, 144, 130))
    font = pygame.font.SysFont('arial',60, True)
    card_font = pygame.font.SysFont('arial', 30, True)
    comparison_font = pygame.font.SysFont('arial', 200, True)



    # Phases of Rendering Game
        # Phase 1 - Player's full hand is shown and none are chosen
        # Phase 2 - Player is highlighting one card in hand with a "Confirm" button
        # Phase 3 - Player draws a new card, other card played.
        # Phase 4 - CPU plays card, draws new card. 
        # Phase 5 - Reveals the two cards. 
        # Phase 6 - Update W-L-T scores, discard played cards

    # Player 1 Hand full hand
    player1_shift=50
    keys_to_play=["Q", "W", "E"]
    for index in range(0, len(gameEngine.player1.hand)):
        window.blit(scale_card_image(gameEngine.player1.hand[index].image), (player1_shift, 200))
        window.blit(card_font.render(f'{gameEngine.player1.hand[index].suit.name}', True, (255,255,255)), (player1_shift, 400))
        window.blit(card_font.render(f'{gameEngine.player1.hand[index].value}', True, (255,255,255)), (player1_shift, 435))
        window.blit(card_font.render(f'TO PLAY CARD PRESS', True, (255,255,255)), (100, 500))
        window.blit(card_font.render(f'{keys_to_play[index]}', True, (255,255,255)), (player1_shift+50, 535))
        player1_shift+=150
    
    # Player 2 Hand
    player2_shift=650
    for index in range(0, len(gameEngine.player2.hand)):
        window.blit(scale_card_image(cardBack), (player2_shift, 200))
        player2_shift+=150

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

    # Player 1 Choice
    if gameEngine.state != GameState.REVEAL:
        # Strengths Legend 
        suit_strengths_statement=font.render('Jewel > Electrum > Silver > Copper', True, (255,255,255))
        value_strengths_statement=font.render('Dragon > Sphinx > Pharoah > Croc', True, (255,255,255))
        window.blit(value_strengths_statement, (100, 600))
        window.blit(suit_strengths_statement, (100, 675))
    elif gameEngine.state == GameState.REVEAL:
        window.blit(scale_card_image(gameEngine.player1.played_card.image), (200, 600))
        window.blit(scale_card_image(gameEngine.player2.played_card.image), (800, 600))
        if gameEngine.player1.played_card.rank > gameEngine.player2.played_card.rank:
            comparison_symbol=">"
        elif gameEngine.player1.played_card.rank < gameEngine.player2.played_card.rank:
            comparison_symbol="<"
        else:
            comparison_symbol="="
        window.blit(comparison_font.render(f'{comparison_symbol}', True, (255,255,255)), (500, 600))

run = True
while run:
    key = None

#    if gameEngine.state == GameState.INTRO:
#        print('Made it here')
#        # Intro window
#        renderIntro(intro_window)
#        pygame.display.update()
#        pygame.time.delay(3000)

    start_window = pygame.display.set_mode(bounds)
    pygame.display.set_caption("Champions")
    renderStart(start_window)
    pygame.display.update()

    gameEngine.cpu_play_card()
    gameEngine.player2.draw()

    pygame.display.update()
    pygame.time.delay(2000)
    gameEngine.state = GameState.THINKING

#    renderCPUFacedown(window)
#    pygame.display.update()
#    pygame.time.delay(3000)

    while key not in [pygame.K_q, pygame.K_w, pygame.K_e]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN:
                key = event.key

    gameEngine.play_card(key)
    gameEngine.player1.draw()
    gameEngine.state = GameState.REVEAL

    renderStart(start_window)
    pygame.display.update()
    pygame.time.delay(3000)

    if gameEngine.player1.played_card.rank > gameEngine.player2.played_card.rank:
        gameEngine.player1.wins += 1
        gameEngine.player2.losses += 1
    elif gameEngine.player1.played_card.rank < gameEngine.player2.played_card.rank:
        gameEngine.player1.losses += 1
        gameEngine.player2.wins += 1
    else: 
        gameEngine.player1.ties += 1
        gameEngine.player2.ties += 1
    gameEngine.state = GameState.TALLYSCORE

    # Clear played cards
    gameEngine.player1.played_card = None
    gameEngine.player2.played_card = None

    if gameEngine.player1.deck.length() == 0:
    #    renderCPUFacedown(window)
    #    pygame.display.update()
        gameEngine.state =GameState.ENDED
        run = False