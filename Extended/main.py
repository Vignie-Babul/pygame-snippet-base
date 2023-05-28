import pygame
from pygame.locals import *

pygame.init()

import sys


# screen variables
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# screen title
pygame.display.set_caption('Extended Base')
# screen icon
screen_icon = pygame.image.load('assets/graphic/icon/icon.png')
pygame.display.set_icon(screen_icon)


# frames per second
FPS = 60
clock = pygame.time.Clock()


# font
font_size = 32
general_font = pygame.font.Font('assets/fonts/consola.ttf', font_size)


# basic colors
WHITE = '#ffffff'
LIGHT_GRAY = '#808080'
GREY = '#505050'
DARK_GREY = '#101010'
BLACK = '#000000'
RED = '#e83131'
ORANGE = '#e86e31'
YELLLOW = '#e8bd31'
GREEN = '#68e831'
CYAN = '#31e8d6'
BLUE = '#3168e8'
PURPLE = '#9331e8'
PINK = '#e831c0'
# background color
BG = BLACK


# application loop
while True:
	# keyboard events
	keys = pygame.key.get_pressed()
	# mouse events
	mouse_pressed = pygame.mouse.get_pressed()
	mouse_position = pygame.mouse.get_pos()


	# rendering
	# background
	screen.fill(BG)


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