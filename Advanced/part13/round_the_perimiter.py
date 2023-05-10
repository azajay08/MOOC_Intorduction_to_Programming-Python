# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
s_height = 480
s_width = 640
window = pygame.display.set_mode((s_width, s_height))

robot = pygame.image.load("robot.png")

x = 0
y = 0
velocity = 1
clock = pygame.time.Clock()
x_move = True
y_move = False

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	window.fill((0, 0, 0))
	window.blit(robot, (x, y))
	pygame.display.flip()
	if y_move:
		y += velocity
		if velocity > 0 and y+robot.get_height() >= s_height:
			x_move = True
			y_move = False
			velocity = -velocity
		if velocity < 0 and y <= 0:
			velocity = -velocity
			x_move = True
			y_move = False

	if x_move:
		x += velocity
		if velocity > 0 and x+robot.get_width() >= s_width:
			y_move = True
			x_move = False
			# velocity = -velocity
		if velocity < 0 and x <= 0:
			# velocity = -velocity
			y_move = True
			x_move = False


	clock.tick(60)