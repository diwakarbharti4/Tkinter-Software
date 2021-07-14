import pygame

#intializing the pygame
#pygame.init()

#creating screen
screen=pygame.display.set_mode((800,600))

#Game LOOP
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False