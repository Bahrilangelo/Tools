import pygame

pygame.init()

# Screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

# Our player object is here
player = pygame.Rect((300,300, 50, 50))

run = True

# Game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

while run:
    # Screen color
    screen.fill((255,0,255))

    # Printing our player object
    pygame.draw.rect(screen, (255,0,0), player)

    # We take the pressed element on keyboard
    key = pygame.key.get_pressed()
    
    # If pressed a on the keyboard we move the player
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)

    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)

    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)

    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)

    # When we press the close button our loop is stop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Refresh screen when we while loop is finished
    pygame.display.update()

# Quiting our code
pygame.quit()