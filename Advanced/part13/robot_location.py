# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()
height = 480
width = 640
window = pygame.display.set_mode((width, height))
robot = pygame.image.load("robot.png")
r_width = robot.get_width()
r_height = robot.get_height()
class Robot():
	def __init__(self):
		self.x = randint(0, width - r_width)
		self.y = randint(0, height - r_height)

clock = pygame.time.Clock()
i = Robot()
target_x = 0
target_y = 0
while True:
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			target_x = event.pos[0]
			target_y = event.pos[1]
		if target_x > i.x and target_x < i.x + r_width and target_y > i.y and target_y < i.y +r_height:
			i.x = randint(0, width - r_width)
			i.y = randint(0, height - r_height)
		if event.type == pygame.QUIT:
			exit()
	window.fill((0, 0, 0))
	window.blit(robot, (i.x, i.y))
	pygame.display.flip()
	clock.tick(60)