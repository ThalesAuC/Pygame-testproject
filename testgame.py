import sys, pygame
from pygame import *
pygame.init()
pygame.display.set_caption('Mortadelaboy')
programIcon = pygame.image.load('mortadelaboy.png')
pygame.display.set_icon(programIcon)
bg = pygame.image.load('bg.png')
screen = pygame.display.set_mode((1280,720))
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    playerImg = pygame.image.load('mortadelaboy.png')
    screen.blit(bg,(0,0))