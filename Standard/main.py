import pygame
from pygame.locals import *

pygame.init()

import sys


# screen variables
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# screen title
pygame.display.set_caption('Standard Base')


# frames per second
FPS = 60
clock = pygame.time.Clock()


# application loop
while True:
	# rendering
	# background
	screen.fill('#101010')


	# handle keyboard events
	for event in pygame.event.get():
		# quit
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()


	# display update
	pygame.display.flip()
	clock.tick(FPS)