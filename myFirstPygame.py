# My First PyGame, Lorenzo Saliard, 11/30/21, 12:15PM, v0.0

import pygame, sys
from pygame.locals import *

# Initialize pygame
pygame.init()

#setup the Window to draw on.
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('My First PyGame')

# Setup Color Values.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PUKEBROWN = (178, 255, 111)