# Simple Animation with PyGame, Lorenzo Saliard, 12/08/21, 11;59, v0.1

import pygame, sys, time
from pygame.locals import *

# Setup PyGame
pygame.init()

# Setup the Window 
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation Example!')