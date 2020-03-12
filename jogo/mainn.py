import pygame, random, sys, os
from pygame import *

pygame.init()

class MainWindow:
    def __init__(self, width, height):
        self.width=width
        self.height=height
        self.display=pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("run")
    def background(self):
        img = pygame.image.load("fundo.png")
        self.display.blit(img, (0,0))            
mainWindow = MainWindow(800,600)

class square:
    def __init__(self, width, height):
        self.width=40
        self.height=60
        self.x=40
        self.y=34
        self.tela=(800,600)
        self.sq=pygame.draw.rect(self.tela, (255, 0, 0), (self.x, self.y, self.width, self.height))
    def back_square(self):
        self.display.blit(self.sq)
#x = 50
#y = 50
#width = 40
#height = 60
#vel = 5
#win = ((800,600))
#def quadradro():
#    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.exit()
            sys.exit()
        mainWindow.background()
        square.back_square()

    pygame.display.update()
