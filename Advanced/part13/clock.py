# WRITE YOUR SOLUTION HERE:

import pygame
import math
from datetime import datetime
 
pygame.init()
width, height = 640, 480
center_x = width / 2
center_y = height / 2
window = pygame.display.set_mode((width, height))
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
center = (center_x, center_y)

def hand_calculation(time, length, width):
	angle = 2 * math.pi * time - math.pi / 2
	hand_x = center_x + math.cos(angle) * length
	hand_y = center_y + math.sin(angle) * length
	pygame.draw.line(window, blue, center, (hand_x, hand_y), width)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				exit()
			if event.key == pygame.K_q:
				exit()
	hours = datetime.now().hour%12
	minutes = datetime.now().minute
	seconds = datetime.now().second
	pygame.display.set_caption(str(datetime.now().time())[:8])
	window.fill((0, 0, 0))

	pygame.draw.circle(window, red, center, 200)
	pygame.draw.circle(window, black, center, 195)
	pygame.draw.circle(window, red, center, 10)

	hand_calculation((seconds / 60), 185, 1)
	hand_calculation((((minutes + seconds) / 60) / 60), 180, 2)
	hand_calculation((((((hours + minutes) / 60) + seconds) / 3600) / 12), 150, 5)
	
	pygame.display.flip()