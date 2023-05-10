# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x1= 0
y = 30
x2 = 0
velocity = 1
velocity2 = 2
clock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	window.fill((0, 0, 0))
	window.blit(robot, (x1, y))
	window.blit(robot, (x2, y + 100))
	pygame.display.flip()

	x1 += velocity
	if velocity > 0 and x1+robot.get_width() >= 640:
		velocity = -velocity
	if velocity < 0 and x1 <= 0:
		velocity = -velocity
	x2 += velocity2
	if velocity2 > 0 and x2+robot.get_width() >= 640:
		velocity2 = -velocity2
	if velocity2 < 0 and x2 <= 0:
		velocity2 = -velocity2

	clock.tick(60)