import time
import random
import pygame
import os

# Initialize fonts
pygame.font.init()

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

BG = pygame.transform.scale(pygame.image.load(os.path.join("assets","Background","Background-black.png")),
 (WINDOW_WIDTH, WINDOW_HEIGHT))


def main():
	run = True
	Frames_per_seconds = 60
	level = 1
	lives = 5

	main_font = pygame.font.SysFont("comicsans", 50)

	clock = pygame.time.Clock()

	def redraw_window():
		# blit - take BG a draw it at (0,0) locations
		WIN.blit(BG, (0,0))
		# Create text labels and  attach them to te screen
		lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
		level_label = main_font.render(f"Level: {level}", 1, (255,255,255))
		WIN.blit(lives_label, (10,10))
		WIN.blit(level_label, (WINDOW_WIDTH - level_label.get_width() -10, 10))

		pygame.display.update()


	while run:
		clock.tick(Frames_per_seconds)
		redraw_window()

		# Events - player interaction
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False


main()