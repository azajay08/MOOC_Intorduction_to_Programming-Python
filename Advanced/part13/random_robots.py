# WRITE YOUR SOLUTION HERE:

import pygame
from random import randint

pygame.init()
screen_width = 640
screen_height = 480
window = pygame.display.set_mode((screen_width, screen_height))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))
width = robot.get_width()
height = robot.get_height()
i = 0
while i < 1000:
	x = randint(0, (screen_width - width))
	y = randint(0, (screen_height - height))
	window.blit(robot, (x, y))
	i += 1
pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()