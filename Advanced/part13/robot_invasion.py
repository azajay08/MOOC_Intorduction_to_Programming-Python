# WRITE YOUR SOLUTION HERE:

import pygame
from random import randint

pygame.init()
height = 480
width = 640
window = pygame.display.set_mode((width, height))
robot = pygame.image.load("robot.png")

class Robot():
	def __init__(self):
		self.x = randint(0, width)
		self.y = randint(-500, -100)
		self.finished = False
		
	
	def move_bot(self):
		if self.y < height - robot.get_height():
			self.y += 2
		else:
			if self.x < width / 2:
				self.x -= 2
			else:
				self.x += 2
		if self.x < (0 - robot.get_width()) or self.x > width:
			self.finished = True

clock = pygame.time.Clock()
robot_amount = 10
robots = []
for i in range(robot_amount):
	i = Robot()
	robots.append(i)
	
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
	window.fill((0, 0, 0))
	for i in robots:
		i.move_bot()
		window.blit(robot, (i.x, i.y))
		if i.finished:
			robots.remove(i)
			i = Robot()
			robots.append(i)
	pygame.display.flip()
	clock.tick(60)

