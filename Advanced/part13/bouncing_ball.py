# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
s_height = 480
s_width = 640
window = pygame.display.set_mode((s_width, s_height))

ball = pygame.image.load("ball.png")

x = 0
y = 0
xvelocity = 3
yvelocity = 3
clock = pygame.time.Clock()
x_move = True
y_move = False

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	window.fill((0, 0, 0))
	window.blit(ball, (x, y))
	pygame.display.flip()
	y += yvelocity
	x += xvelocity
	if yvelocity > 0 and y + ball.get_height() >= s_height:
		yvelocity = -yvelocity
	if yvelocity < 0 and y <= 0:
		yvelocity = -yvelocity

	if xvelocity > 0 and x + ball.get_width() >= s_width:
		xvelocity = -xvelocity
	if xvelocity < 0 and x <= 0:
		xvelocity = -xvelocity
	clock.tick(60)