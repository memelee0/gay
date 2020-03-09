import pygame, random, sys
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


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.exit()
            sys.exit()
        mainWindow.background()
    
        
    pygame.display.update()