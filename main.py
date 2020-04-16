import time
import random
import pygame
import os

WINDOW_WIDTH, WINDOW_HEIGHT = 750, 750
RESOLUTION = (WINDOW_WIDTH, WINDOW_HEIGHT)
WIN = pygame.display.set_mode((RESOLUTION))
pygame.display.set_caption("Galaxy Invaders")


RED_SHIP = pygame.image.load(os.path.join("assets/Ships","small_red_ship.png"))
BLUE_SHIP = pygame.image.load(os.path.join("assets/Ships","small_blue_ship.png"))
GREEN_SHIP = pygame.image.load(os.path.join("assets/Ships","small_green_ship.png"))

PLAYER_SHIP = pygame.image.load(os.path.join("assets","Ships","player_yellow_ship.png"))

RED_LASER = pygame.image.load(os.path.join("assets", "Lasers","laser_red.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "Lasers","laser_blue.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "Lasers","laser_green.png"))

PLAYER_LASER = pygame.image.load(os.path.join("assets", "Lasers","laser_yellow.png"))

BG = pygame.image.load(os.path.join("assets","Background","Background-black.png"))


def main():
	run = True
	Frames_per_seconds = 60
	clock = pygame.time.Clock()

	while run:
		clock.tick(Frames_per_seconds)
		# Events - player interaction
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False


main()