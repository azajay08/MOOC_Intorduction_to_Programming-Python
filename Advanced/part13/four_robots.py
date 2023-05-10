
# The exercises in this part of the course have no automated tests, as the results as visually verified.
# The tests grant points automatically as you submit your solution to the server, no matter what your implementation.
# Only submit your solution when you are ready, and your solution matches the exercise description.
# The exercises may not have automatic tests, but the course staff will still see your solution.
# If your solution clearly does not match the exercise description, you may lose the points granted for the exercises in this part.

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
window.blit(robot, (0, 0))
window.blit(robot, (0, (screen_height - height)))
window.blit(robot, ((screen_width - width), (screen_height - height)))
window.blit(robot, ((screen_width - width), 0))
pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()