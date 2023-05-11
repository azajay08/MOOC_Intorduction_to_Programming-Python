# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
height = 480
width = 640
window = pygame.display.set_mode((width, height))
robot = pygame.image.load("robot.png")

class Robot():
	def __init__(self):
		self.x = width / 2
		self.y = height / 2
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
i = Robot()
	
while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				i.moving_left = True
			if event.key == pygame.K_RIGHT:
				i.moving_right = True
			if event.key == pygame.K_UP:
				i.moving_up = True
			if event.key == pygame.K_DOWN:
				i.moving_down = True
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				i.moving_left = False
			if event.key == pygame.K_RIGHT:
				i.moving_right = False
			if event.key == pygame.K_UP:
				i.moving_up = False
			if event.key == pygame.K_DOWN:
				i.moving_down = False
		if event.type == pygame.QUIT:
			exit()
	i.move_bot()
	window.fill((0, 0, 0))
	window.blit(robot, (i.x, i.y))
	pygame.display.flip()
	clock.tick(60)