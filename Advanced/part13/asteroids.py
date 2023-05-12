# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()
height = 480
width = 640
window = pygame.display.set_mode((width, height))
robot = pygame.image.load("robot.png")
rock = pygame.image.load("rock.png")
r_width = robot.get_width()
r_height = robot.get_height()
game_font = pygame.font.SysFont("Ebrima", 32)
pygame.display.set_caption("Asteroids")
score = 0

class Robot():
	def __init__(self):
		self.x = width / 2
		self.y = height - r_height
		self.moving_right = False
		self.moving_left = False
		
	def move_bot(self):
		if self.moving_right and self.x < width - r_width:
			self.x += 3
		if self.moving_left and self.x > 0:
			self.x -= 3

class Asteroid():
	def __init__(self):
		self.x = randint(0, width - rock.get_width())
		self.y = randint(-500, -100)
		self.finished = False
	

	def move_rock(self):
		if self.y < height:
			self.y += 1
	
clock = pygame.time.Clock()
p1 = Robot()
rock_amount = 4
rocks = []
for i in range(rock_amount):
	i = Asteroid()
	rocks.append(i)

while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				exit()
			if event.key == pygame.K_q:
				exit()
			if event.key == pygame.K_LEFT:
				p1.moving_left = True
			if event.key == pygame.K_RIGHT:
				p1.moving_right = True
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				p1.moving_left = False
			if event.key == pygame.K_RIGHT:
				p1.moving_right = False
		if event.type == pygame.QUIT:
			exit()
	window.fill((0, 0, 0))
	p1.move_bot()
	window.blit(robot, (p1.x, p1.y))
	for i in rocks:
		i.move_rock()
		window.blit(rock, (i.x, i.y))
		if i.y == height:
			exit()
		if p1.x + r_width > i.x and p1.x < i.x + rock.get_width() and\
		p1.y + r_height > i.y and p1.y < i.y + rock.get_height():
			score += 1
			i.finished = True
		if i.finished:
			rocks.remove(i)
			i = Asteroid()
			rocks.append(i)
	rounded_score = round(score)
	score_str = "Score:{:,}".format(rounded_score)
	text = game_font.render(score_str, True, (255, 0, 0))
	window.blit(text, (10, 10))
	pygame.display.flip()
	clock.tick(60)