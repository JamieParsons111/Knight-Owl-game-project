import pygame

pygame.init()

#defining size of game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

'''Defining the variable player as a rectangle (Rect), taking in variables:
# X & Y coordinates, and height and width of rectangle
''' 
player = pygame.Rect((300, 250, 50, 50))


# Just for quitting out the game
run = True
''' 
pygame.draw.rect(screen,(100, 200,100))
Draws out the rectangle on the screen, 
Next Parenthesis is the RBG Colours of the rectangle itself
'''
while run:

    #Screen background colour
    screen.fill((0,0,0))

    #This is the player 
    pygame.draw.rect(screen,(100, 200,100),player)

    key = pygame.key.get_pressed()
    #Movement
    # Move left key
    if key[pygame.K_a] == True:
        # move_ip = Move in place
        player.move_ip(-1, 0)
    # Move Right key
    elif key[pygame.K_d] == True:
        player.move_ip(1,0)

    # Move Up key
    elif key[pygame.K_w] == True:
        player.move_ip(0,-1)

    # Move down key
    elif key[pygame.K_s] == True:
        player.move_ip(0,1)

    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()