#!usr/bin/env python3

import pygame
import random


pygame.init()
#create the screen
screen = pygame.display.set_mode((800,600))
#Tittle and icon
pygame.display.set_caption("Space invaders")
icon = pygame.image.load("rocket.png")
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480
playerX_change = 0;

#Enemy
enemyImg = pygame.image.load("ufo.png")
enemyX = random.randint(0,734)
enemyY = 100
enemyX_change = 0.3
enemyY_change = 50

def player(x,y):
	screen.blit(playerImg,(x,y))

def enemy(x,y):
	screen.blit(enemyImg,(x,y))

#Game loop
running = True
while running:

	screen.fill((100,100,100))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# Check if something pressed
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT:
			playerX_change = -0.1
		if event.key == pygame.K_RIGHT:
			playerX_change = 0.1
	if event.type == pygame.KEYUP:
		if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
			playerX_change = 0

	playerX += playerX_change

	if playerX >= 736:
		playerX = 736
	elif playerX <= 0:
		playerX = 0


	enemyX += enemyX_change

	if enemyX >= 736:
		#playerX = 736
		enemyX_change = -0.3
		enemyY += 50
	elif enemyX <= 0:
		enemyY +=50
		enemyX_change = 0.3
		#playerX = 0


	enemy(enemyX,enemyY)
	player(playerX,playerY)
	pygame.display.update()

