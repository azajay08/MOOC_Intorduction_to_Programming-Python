# WRITE YOUR SOLUTION HERE:
from random import randint
import pygame

pygame.init()
height = 480
width = 640
window = pygame.display.set_mode((width, height))
robot = pygame.image.load("robot.png")

class Robot():
	def __init__(self):
		self.x = randint(0, width - robot.get_width())
		self.y = randint(0, height - robot.get_height())
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		
	def move_bot(self):
		if self.moving_right and self.x < width - robot.get_width():
			self.x += 3
		if self.moving_left and self.x > 0:
			self.x -= 3
		if self.moving_up and self.y > 0:
			self.y -= 3
		if self.moving_down and self.y < height - robot.get_height():
			self.y += 3
clock = pygame.time.Clock()
robot_amount = 10
p1 = Robot()
p2 = Robot()
	
while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				p2.moving_left = True
			if event.key == pygame.K_RIGHT:
				p2.moving_right = True
			if event.key == pygame.K_UP:
				p2.moving_up = True
			if event.key == pygame.K_DOWN:
				p2.moving_down = True
			if event.key == pygame.K_a:
				p1.moving_left = True
			if event.key == pygame.K_d:
				p1.moving_right = True
			if event.key == pygame.K_w:
				p1.moving_up = True
			if event.key == pygame.K_s:
				p1.moving_down = True
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				p2.moving_left = False
			if event.key == pygame.K_RIGHT:
				p2.moving_right = False
			if event.key == pygame.K_UP:
				p2.moving_up = False
			if event.key == pygame.K_DOWN:
				p2.moving_down = False
			if event.key == pygame.K_a:
				p1.moving_left = False
			if event.key == pygame.K_d:
				p1.moving_right = False
			if event.key == pygame.K_w:
				p1.moving_up = False
			if event.key == pygame.K_s:
				p1.moving_down = False
		if event.type == pygame.QUIT:
			exit()
	p1.move_bot()
	p2.move_bot()
	window.fill((0, 0, 0))
	window.blit(robot, (p1.x, p1.y))
	window.blit(robot, (p2.x, p2.y))
	pygame.display.flip()
	clock.tick(60)