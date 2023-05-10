# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
screen_width = 640
screen_height = 480
window = pygame.display.set_mode((screen_width, screen_height))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))
width = robot.get_width()
height = robot.get_height()
x = 50
for i in range(10):
	window.blit(robot, (x, 100))
	x += width
pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()