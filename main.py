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


# abstract class - we are not going to use it, we will inherit from 
class Ship:
	def __init__(self, x, y, health=100):
		self.x = x
		self.y = y
		self.health = health
		self.ship_img = None
		self.laser_img = None
		self.lasers = []
		self.cool_down_counter = 0


	def draw(self, window):
		window.blit(self.ship_img, (self.x, self.y))


	def get_width(self):
		return self.ship_img.get_width()

	def get_height(self):
		return self.ship_img.get_height()


class Player(Ship):
	def __init__(self, x, y, health=100):
		# Use Ship Class initlaization method
		super().__init__(x, y, health)
		self.ship_img = PLAYER_SHIP
		self.laser_img = PLAYER_LASER
		# Detect perfect pixel colision using mask
		self.mask = pygame.mask.from_surface(self.ship_img)
		self.max_health = health


class Enemy(Ship):
	COLOR_DICT = {
		"red" : (RED_SHIP, RED_LASER),
		"green" : (GREEN_SHIP, GREEN_LASER),
		"blue" :  (BLUE_SHIP, BLUE_LASER)
	}

	def __init__(self, x, y, color, health=100):
		super().__init__(x,y,health)
		self.ship_img, self.laser_img = self.COLOR_DICT[color]
		self.mask = pygame.mask.from_surface(self.ship_img)

	def move(self, vel):
		self.y += vel




def main():
	run = True
	Frames_per_seconds = 60
	main_font = pygame.font.SysFont("comicsans", 50)
	lost_font = pygame.font.SysFont("comicsans", 60)
	level = 0
	lives = 5
	lost = False
	lost_count = 0

	player_velocity = 5

	
	# Enemies 
	enemies = []
	wave_length = 5
	enemy_velocity = 1

	player = Player(300, 650)

	clock = pygame.time.Clock()

	def redraw_window():
		# blit - take BG a draw it at (0,0) locations
		WIN.blit(BG, (0,0))
		# Create text labels and  attach them to te screen
		lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
		level_label = main_font.render(f"Level: {level}", 1, (255,255,255))
		WIN.blit(lives_label, (10,10))
		WIN.blit(level_label, (WINDOW_WIDTH - level_label.get_width() -10, 10))

		# Draw all enemies
		for enemy in enemies:
			enemy.draw(WIN)

		player.draw(WIN)


		if lost:
			lost_label = lost_font.render("You Lost!!", 1, (255,255,255))
			WIN.blit(lost_label, (WINDOW_WIDTH/2 - lost_label.get_width()/2, 350))



		# Update after drawing
		pygame.display.update()


	while run:
		clock.tick(Frames_per_seconds)
		redraw_window()

		if lives <= 0 or player.health <= 0:
			lost = True
			lost_count += 1

		if lost:
			# Set the time for showing lost message
			if lost_count > Frames_per_seconds * 3:
				run = False
			else:
				# Go to next iteration ignoring rest of code
				continue

		# All enemies has been killed
		if len(enemies) == 0:
			level += 1
			wave_length += 5
			for i in range(wave_length):
				enemy = Enemy(random.randrange(50, WINDOW_WIDTH-100),
					random.randrange(-1500, -100),
					random.choice(["red","blue","green"]))
				enemies.append(enemy)

		

		

		keys = pygame.key.get_pressed()
		# returns dict of keys and values - weather are they pressed or not
		# accessing keys, moving and restrictions 
		if keys[pygame.K_a] and player.x - player_velocity > 0:
			player.x -= player_velocity
		if keys[pygame.K_d] and player.x + player_velocity + player.get_width() < WINDOW_WIDTH: 
			player.x += player_velocity
		if keys[pygame.K_w] and player.y - player_velocity > 0:
			player.y -= player_velocity
		if keys[pygame.K_s] and player.y + player_velocity + player.get_height() < WINDOW_HEIGHT:
			player.y += player_velocity

		# QUIT Player Interaction
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False


		# Moving enemies
		for enemy in enemies:
			enemy.move(enemy_velocity)
			# If enemy has crossed bottom of the window:
			if enemy.y + enemy.get_height() > WINDOW_HEIGHT:
				lives -= 1
				enemies.remove(enemy)

		


main()


