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
y = 100
i = 0
xoffset = 0
while i < 10:
	x = 50 + xoffset
	j = 0
	while j < 10:
		window.blit(robot, (x, y))
		x += width - 10
		j += 1
	xoffset += 10
	y += 20
	i += 1
pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()