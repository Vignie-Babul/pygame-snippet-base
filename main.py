import pygame
from pygame.locals import *

pygame.init()

import sys


# screen configure
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Base')

clock = pygame.time.Clock()


# application loop
while True:
	# rendering
	# background
	screen.fill('#101010')


	# game events
	for event in pygame.event.get():
		# quit
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()


	# display update
	pygame.display.flip()
	clock.tick(60)