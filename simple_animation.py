# Simple Animation with PyGame, Lorenzo Saliard, 12/08/21, 12;11, v0.3

import pygame, sys, time
from pygame.locals import *

from myFirstPygame import GREEN, RED

# Setup PyGame
pygame.init()

# Setup the Window 
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation Example!')

# Setupid the direction variables.
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4

# Setupd color values.
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0 , 255)