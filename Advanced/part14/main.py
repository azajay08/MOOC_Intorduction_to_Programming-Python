# Complete your game here
import pygame
from random import randint

pygame.init()
height = 600
width = 900
window = pygame.display.set_mode((width, height))
robot = pygame.image.load("robot.png")
monster = pygame.image.load("monster.png")
coin = pygame.image.load("coin.png")
coin = pygame.transform.scale(coin, (30, 30))
monster = pygame.transform.scale(monster, (40, 50))
r_width = robot.get_width()
r_height = robot.get_height()
m_width = monster.get_width()
m_height = monster.get_height()
clock = pygame.time.Clock()
game_font = pygame.font.SysFont("Ebrima", 32)
big_text = pygame.font.SysFont("Ebrima", 150)
instructions = pygame.font.SysFont("Ebrima", 75)
start = pygame.font.SysFont("Ebrima", 60)
start_k = pygame.font.SysFont("Ebrima", 40)
NOT_STARTED = 0
RUNNING = 1
GAME_OVER = 2

class Robot():
	def __init__(self, width, height):
		self.x = width
		self.y = height
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		self.multi = 1.0

	def move_bot(self, bot):
		if self.moving_right and self.x < width - bot.r_width:
			self.x += 3 * self.multi
		if self.moving_left and self.x > 0:
			self.x -= 3 * self.multi
		if self.moving_up and self.y > 0:
			self.y -= 3 * self.multi
		if self.moving_down and self.y < height - bot.r_height:
			self.y += 3 * self.multi

class Monster():
	def __init__(self):
		self.x = randint(0, width - monster.get_width())
		self.y = randint(-500, -100)
		self.finished = False

	def move_monsters(self, p1: 'Robot'):
		if self.y < height:
			self.y += 2 * p1.multi
		else:
			self.finished = True

class Coin():
	def __init__(self):
		self.x = randint(0, width - coin.get_width())
		self.y = randint(0, height - coin.get_height())
		self.finished = False

class RoboGame():
	def __init__(self):
		pygame.display.set_caption("RoboGame!")
		self.state = NOT_STARTED
		self.lives = 5
		self.lives_robot = [Robot(750, 10), Robot(780, 10), Robot(810, 10) , Robot(840, 10), Robot(870, 10)]
		self.p1 = Robot(width / 2, height / 2)
		self.enemies = []
		self.enemy_count = 10
		self.i = 0
		self.coins = []
		self.coin_count = 1
		self.coins_i = 0
		self.collected = 0
		self.score = 0
		self.r = 0
		self.g = 50
		self.b = 50
		self.r_width = robot.get_width()
		self.r_height = robot.get_height()
		self.robot = pygame.transform.scale(robot, (self.r_width, self.r_height))
		self.mini_robot = pygame.transform.scale(robot, (20, 40))

	def check_events(self):
		for event in pygame.event.get():
			if self.state == RUNNING or self.state == NOT_STARTED:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						exit()
					if event.key == pygame.K_q:
						exit()
					if event.key == pygame.K_LEFT:
						self.p1.moving_left = True
					if event.key == pygame.K_RIGHT:
						self.p1.moving_right = True
					if event.key == pygame.K_UP:
						self.p1.moving_up = True
					if event.key == pygame.K_DOWN:
						self.p1.moving_down = True
					if event.key == pygame.K_SPACE:
						self.state = RUNNING
				if event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT:
						self.p1.moving_left = False
					if event.key == pygame.K_RIGHT:
						self.p1.moving_right = False
					if event.key == pygame.K_UP:
						self.p1.moving_up = False
					if event.key == pygame.K_DOWN:
						self.p1.moving_down = False
			else:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						exit()
					if event.key == pygame.K_q:
						exit()
					if event.key == pygame.K_SPACE:
						# self.state == RUNNING
						main()
			if event.type == pygame.QUIT:
				exit()

	def change_colour(self):
		if self.r < 150:
			self.r += 50
			return
		if self.b < 250:
			self.b += 50
			return
		if self.g < 250:
			self.g += 50
		if self.g == 250:
			self.r = 0
			self.g = 100
			self.b = 100

	def check_coin_collisions(self):
		for c in self.coins:
			if self.p1.x + self.r_width > c.x and self.p1.x < c.x + 30 and\
				  self.p1.y + self.r_height > c.y and self.p1.y < c.y + 30:
				self.collected += 1
				self.score += 1
				self.coins.remove(c)
				# still need to add multipliers 
				if self.score % 5 == 0:
					self.p1.multi += 0.1
					self.enemy_count += 2
					self.change_colour()
					if self.r_height > 40:
						self.r_height /= 1.2
						self.r_width /= 1.2
						self.robot = pygame.transform.scale(robot, (self.r_width, self.r_height))

	def update_score(self):
		rounded_score = round(self.score)
		score_str = "Score:{:,}".format(rounded_score)
		text = game_font.render(score_str, True, (255, 0, 0))
		window.blit(text, (10, 10))

	def monster_check(self):
		while self.i < self.enemy_count:
			self.enemies.append(Monster())
			self.i += 1
		for m in self.enemies:
			m.move_monsters(self.p1)
			window.blit(monster, (m.x, m.y))
			if m.finished:	
				self.enemies.remove(m)
				self.enemies.append(Monster())

	def coin_check(self):
		while self.coins_i < self.coin_count:
			self.coins.append(Coin())
			window.blit(coin, (self.coins[self.coins_i].x, self.coins[self.coins_i].y))
			self.coins_i += 1
		for c in self.coins:
			window.blit(coin, (c.x, c.y))
		if self.collected == self.coin_count:
			self.coin_count += 1
			self.coins_i = 0
			self.collected = 0

	def check_lives(self):
		for i in self.lives_robot:
			window.blit(self.mini_robot, (i.x, i.y))
		if self.lives == 0:
			self.state = GAME_OVER

	def check_monster_collisions(self):
		for m in self.enemies:
			if self.p1.x + self.r_width > m.x + (m_width / 5) and self.p1.x < m.x + (m_width) - (m_width / 5) and\
				  self.p1.y + self.r_height > m.y + (m_height / 5) and self.p1.y < m.y + (m_height) - (m_height / 5):
				self.enemies.remove(m)
				if self.lives > 0:
					self.lives -= 1
					# self.state = PAUSED
					self.lives_robot.pop(0)

	def run_end_game(self):
		window.fill((150, 0, 0))
		esc_str = "PRESS 'q' or 'esc' TO ESCAPE"
		esc_text = instructions.render(esc_str, True, (0, 0, 0))
		esc_rect = esc_text.get_rect()
		esc_rect.centerx = window.get_rect().centerx
		esc_rect.y = window.get_rect().centery - 200
		g_str = "GAME OVER"
		g_text = big_text.render(g_str, True, (0, 0, 0))
		g_rect = g_text.get_rect()
		g_rect.center = window.get_rect().center
		space_str = "PRESS 'SPACE' TO RESTART"
		space_text = instructions.render(space_str, True, (0, 0, 0))
		space_rect = space_text.get_rect()
		space_rect.centerx = window.get_rect().centerx
		space_rect.y = window.get_rect().centery + 150
		window.blit(g_text, (g_rect))
		window.blit(space_text, (space_rect))
		window.blit(esc_text, (esc_rect))

	def run_start_screen(self):
		window.fill((100, 200, 100))
		i_str = "COLLECT COINS TO EARN POINTS"
		i_text = start_k.render(i_str, True, (0, 0, 0))
		i_rect = i_text.get_rect()
		i_rect.y = 10
		i_rect.centerx = window.get_rect().centerx
		rule_str = "AVOID THE GHOSTS, HIT ONE AND YOU LOSE A LIFE"
		rule_text = start_k.render(rule_str, True, (0, 0, 0))
		rule_rect = rule_text.get_rect()
		rule_rect.y = 60
		rule_rect.centerx = window.get_rect().centerx
		life_str = "YOU HAVE 5 LIVES"
		life_text = start_k.render(life_str, True, (0, 0, 0))
		life_rect = life_text.get_rect()
		life_rect.y = 110
		life_rect.centerx = window.get_rect().centerx
		inten_str = "INTENSITY INCREASES EVERY 5 COINS"
		inten_text = start_k.render(inten_str, True, (0, 0, 0))
		inten_rect = inten_text.get_rect()
		inten_rect.y = 160
		inten_rect.centerx = window.get_rect().centerx
		g_str = "ROBO GAME!"
		g_text = big_text.render(g_str, True, (255, 255, 0))
		g_rect = g_text.get_rect()
		g_rect.center = window.get_rect().center
		ctrl_str = "USE ARROW KEYS TO MOVE"
		space_str = "PRESS 'SPACE' TO START"
		esc_str = "PRESS 'q' or 'esc' TO ESCAPE"
		ctrl_text = start.render(ctrl_str, True, (0, 0, 0))
		ctrl_rect = ctrl_text.get_rect()
		ctrl_rect.y = window.get_rect().centery + 70
		ctrl_rect.centerx = window.get_rect().centerx
		esc_text = start.render(esc_str, True, (0, 0, 0))
		esc_rect = esc_text.get_rect()
		esc_rect.y = window.get_rect().centery + 150
		esc_rect.centerx = window.get_rect().centerx
		space_text = start.render(space_str, True, (0, 0, 0))
		space_rect = space_text.get_rect()
		space_rect.centerx = window.get_rect().centerx
		space_rect.y = window.get_rect().centery + 230
		window.blit(g_text, (g_rect))
		window.blit(space_text, (space_rect))
		window.blit(esc_text, (esc_rect))
		window.blit(i_text, (i_rect))
		window.blit(rule_text, (rule_rect))
		window.blit(life_text, (life_rect))
		window.blit(inten_text, (inten_rect))
		window.blit(ctrl_text, (ctrl_rect))

	def run_game(self):
		while True:
			self.check_events()
			if self.state == NOT_STARTED:
				self.run_start_screen()
			if self.state == RUNNING:
				window.fill((self.r, self.g, self.b))
				self.p1.move_bot(self)
				self.monster_check()
				self.coin_check()
				self.check_coin_collisions()
				self.check_monster_collisions()
				self.update_score()
				self.check_lives()
				window.blit(self.robot, (self.p1.x, self.p1.y))
			if self.state == GAME_OVER:
				self.run_end_game()
			pygame.display.flip()
			clock.tick(60)
def main():
	robo = RoboGame()
	robo.run_game()

main()
