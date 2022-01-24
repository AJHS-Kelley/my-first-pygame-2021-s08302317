# PyGame Collision Detection Practice, Lorenzo Saliard, January 24, 2022, 11:50am, v0.2

import pygame, sys, random
from pygame.locals import *

# setup PyGame
pygame.init()
mainClock = pygame.time.Clock() 

# Setup the PyGame Window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('collision Detection 2022')