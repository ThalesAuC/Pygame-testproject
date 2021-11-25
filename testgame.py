import sys, pygame
from pygame import display
pygame.init()
pygame.display.set_caption('Mortadelaboy vs Coxinhaman')
programIcon = pygame.image.load('mortadelaboy.png')
pygame.display.set_icon(programIcon)

size = width, height = 1280, 720
speed = [2,2]
black = 0,0,0

screen = pygame.display.set_mode(size)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
