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

class Laser:
	def __init__(self, x, y, img):
		self.x = x
		self.y = y
		self.img = img
		self.mask = pygame.mask.from_surface(self.img)

	def draw(self, window):
		window.blit(self.img, (self.x, self.y))

	def move(self, vel):
		self.y += vel

	def off_screen(self, height):
		return not(self.y <= height and self.y >= 0)

	def collision(self, obj):
		return collide(self, obj)

class Laser:
	def __init__(self, x,y, img):
		self.x = x
		self.y = y
		self.img = img
		self.mask = pygame.mask.from_surface(self.img)

	def draw(self, window):
		window.blit(self.img, (self.x, self.y))

	def move(self, vel):
		self.y += vel

	def off_screen(self, height):
		return not (self.y <= WINDOW_HEIGHT and self.y >= 0)

	def collision(self, obj):
		return collide(self, obj)



# abstract class - we are not going to use it, we will inherit from 
class Ship:
	COOLDOWN = 30
<<<<<<< HEAD

=======
>>>>>>> b2321442999f0398b8419f701f9801597ede013e
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
		for laser in self.lasers:
			laser.draw(window)

<<<<<<< HEAD
	def move_lasers(self, vel, obj):
		self.cooldown()
		for laser in self.lasers:
			laser.move(vel)
			if laser.off_screen(WINDOW_HEIGHT):
				self.lasers.remove(laser)
			elif laser.collision(obj):
				obj.health -= 10
				self.lasers.remove(laser)

	def cooldown(self):
=======
	def move_lasers(self, velocity, objs):
		self.cooldown()
		for laser in self.lasers:
			laser.move(velocity)
			if laser.off_screen(WINDOW_HEIGHT):
				self.lasers.remove(laser)
			else:
				for obj in objs:
					if laser.collision(obj):
						objs.remove(obj)
						self.laser.remove(laser)


	def cooldown(self):
		# To Not shoot so fast
>>>>>>> b2321442999f0398b8419f701f9801597ede013e
		if self.cool_down_counter >= self.COOLDOWN:
			self.cool_down_counter = 0
		elif self.cool_down_counter > 0:
			self.cool_down_counter += 1

	def shoot(self):
		if self.cool_down_counter == 0:
			laser = Laser(self.x, self.y, self.laser_img)
			self.lasers.append(laser)
<<<<<<< HEAD
			self.cool_down_counter = 1

=======
			self.cool_down_counter = 1	
>>>>>>> b2321442999f0398b8419f701f9801597ede013e

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

	def move_laswe(self, vel, objs):
		self.cooldown()
		for laser in self.lasers:
			laser.move(vel)
			if lasser.off_screen(WINDOW_HEIGHT):
				self.lasers.remove(lase)
			else:
				for obj in objs:
					if laser.collision(obj):
						objs.remove(obj)
						self.lasers.remove(laser)


	def move_lasers(self, vel, objs):
		self.cooldown()
		for laser in self.lasers:
			laser.move(vel)
			if laser.off_screen(WINDOW_HEIGHT):
				self.lasers.remove(laser)
			else:
				for obj in objs:
					if laser.collision(obj):
						objs.remove(obj)
						if laser in self.lasers:
							self.lasers.remove(laser)

	def draw(self, window):
		super().draw(window)
		self.healthbar(window)

	def healthbar(self, window):
		pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
		pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))



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

	def shoot(self):
		if self.cool_down_counter == 0:
			laser = Laser(self.x-20, self.y, self.laser_img)
			self.lasers.append(laser)
			self.cool_down_counter = 1

def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

def collide(obj1, obj2):
	offset_x = obj2.x - obj1.x
	offset_y = obj2.y - obj1.y
	return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None            

def main():
	run = True
	lost = False
	lost_count = 0
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
	laser_velocity = 4

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

<<<<<<< HEAD
=======

>>>>>>> b2321442999f0398b8419f701f9801597ede013e
		if lost:
			lost_label = lost_font.render("You Lost!!", 1, (255,255,255))
			WIN.blit(lost_label, (WINDOW_WIDTH/2 - lost_label.get_width()/2, 350))

<<<<<<< HEAD
=======


>>>>>>> b2321442999f0398b8419f701f9801597ede013e
		# Update after drawing
		pygame.display.update()


	while run:
		clock.tick(Frames_per_seconds)
		redraw_window()

		if lives <= 0 or player.health <= 0:
			lost = True
			lost_count += 1

		if lost:
<<<<<<< HEAD
			if lost_count >Frames_per_seconds * 3:
				run = False
			else:
=======
			# Set the time for showing lost message
			if lost_count > Frames_per_seconds * 3:
				run = False
			else:
				# Go to next iteration ignoring rest of code
>>>>>>> b2321442999f0398b8419f701f9801597ede013e
				continue

		# All enemies has been killed
		if len(enemies) == 0:
			level += 1
			wave_length += 5
			for i in range(wave_length):
				enemy = Enemy(random.randrange(50, WINDOW_WIDTH-100), 
					random.randrange(-1500, -100), 
					random.choice(["red", "blue", "green"]))
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
		if keys[pygame.K_SPACE]:
			player.shoot()

		# QUIT Player Interaction
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False


		for enemy in enemies[:]:
			enemy.move(enemy_velocity)
			enemy.move_lasers(laser_velocity, player)
<<<<<<< HEAD

			if random.randrange(0, 2*60) == 1:
				enemy.shoot()

			if collide(enemy, player):
				player.health -= 10
				enemies.remove(enemy)
			elif enemy.y + enemy.get_height() > WINDOW_HEIGHT:
				lives -= 1
				enemies.remove(enemy)

		player.move_lasers(-laser_velocity, enemies)

		

def main_menu():
	title_font = pygame.font.SysFont("comicsans", 70)
	run = True
	while run:
		WIN.blit(BG, (0,0))
		title_label = title_font.render("Press the mouse to begin...", 1, (255,255,255))
		WIN.blit(title_label, (WINDOW_WIDTH/2 - title_label.get_width()/2, 350))
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				main()
	pygame.quit()


main_menu()
=======
			# If enemy has crossed bottom of the window:
			if enemy.y + enemy.get_height() > WINDOW_HEIGHT:
				lives -= 1
				enemies.remove(enemy)

		player.move_lasers(-laser_velocity, enemies)

		
>>>>>>> b2321442999f0398b8419f701f9801597ede013e


main()