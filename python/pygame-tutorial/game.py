# python3 -m venv env
# source env/bin/activate
#
# python3 -m pip install pygame

import pygame
from sys import exit
import random

pygame.init()

WIDTH = 1600
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Zelda')

clock = pygame.time.Clock()

sky_surf = pygame.image.load('graphics/sky.jpg').convert()

ground_surf = pygame.image.load('graphics/ground.png').convert()

score_font = pygame.font.Font('font/pixeltype.ttf', 50)
score_surf = score_font.render('my game', False, (225, 225, 255)).convert()
score_rect = score_surf.get_rect(center = (800, 50))

snail_surf = pygame.image.load('graphics/snail/snail_1.png').convert_alpha()
snail_app = [{
	'initial': 2200,
	'speed': 3,
	'rect': None,
}, {
	'initial': 2350,
	'speed': 3,
	'rect': None,
}, {
	'initial': 2600,
	'speed': 2,
	'rect': None,
}, {
	'initial': 3000,
	'speed': 3,
	'rect': None,
}]
for snail in snail_app:
	snail['rect'] = snail_surf.get_rect(bottomright = (snail['initial'], 700))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 700))
player_gravity = 0

while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				player_gravity = -20

			# if event.key == pygame.K_LCTRL:
			# 	print('l ctrl')
			# if event.key == pygame.K_RCTRL:
			# 	print('r ctrl')
			# if event.key == pygame.K_LALT:
			# 	print('l alt')
			# if event.key == pygame.K_RALT:
			# 	print('r alt')
			# if event.key == pygame.K_LMETA:
			# 	print('l meta')
			# if event.key == pygame.K_RMETA:
			# 	print('r meta')
			# if event.key == pygame.K_LSUPER:
			# 	print('l super')
			# if event.key == pygame.K_RSUPER:
			# 	print('r super')
			# if event.mod & pygame.KMOD_LCTRL: # left control
			# 	print('mod l ctrl')
			# if event.mod & pygame.KMOD_RCTRL: # right control
			# 	print('mod r ctrl')
			# if event.mod == pygame.KMOD_NONE:
			# 	print('mod none')
			# else:
			# 	if event.mod & pygame.KMOD_CTRL:  # left control or right control or both
			# 		print('mod l/r ctrl')
			# 	if event.mod & pygame.KMOD_LALT:  # left alt
			# 		print('mod l alt')
			# 	if event.mod & pygame.KMOD_RALT:  # right alt
			# 		print('mod r alt')
			# 	if event.mod & pygame.KMOD_ALT:   # left alt or right alt or both
			# 		print('mod l/r alt')
			# 	if event.mod & pygame.KMOD_LMETA: # left meta
			# 		print('mod l meta')
			# 	if event.mod & pygame.KMOD_RMETA: # right meta
			# 		print('mod r meta')
			# 	if event.mod & pygame.KMOD_META:  # left meta or right meta or both
			# 		print('mod l/r meta')
			# 	if event.mod & pygame.KMOD_MODE:
			# 		print('mod mode')

	screen.blit(sky_surf, (0, 0))

	screen.blit(ground_surf, (0, 700))
	screen.blit(ground_surf, (700, 700))
	screen.blit(ground_surf, (1400, 700))

	screen.blit(score_surf, score_rect)

	for snail in snail_app:
		snail['rect'].x -= snail['speed']
		if snail['rect'].right <= 0:
			snail['rect'].left = 1600
			snail_move = random.randint(0, 9)
			if snail_move == 0 or snail_move == 1:
				snail['speed'] = 2
			elif snail_move == 8 or snail_move == 9:
				snail['speed'] = 4
			else:
				snail['speed'] = 3
		screen.blit(snail_surf, snail['rect'])

	player_gravity += 1
	player_rect.y += player_gravity
	screen.blit(player_surf, player_rect)

	pygame.display.update()
	clock.tick(60)
