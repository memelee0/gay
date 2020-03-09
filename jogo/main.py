
import pygame, sys,os

from pygame.locals import *

# initializing pygame

pygame.init()

# setting up the screen

pygame.display.set_caption('Cenario')

size = width, height = 600, 400

screen = pygame.display.set_mode(size)

black = 0, 0, 0

window = pygame.display.set_mode(max(pygame.display.list_modes()))

# fliping the display

pygame.display.flip()

# ############################################################################

# def load_image #

# 02/09/2008 #

# #

# function that loads the images into memory #

# ############################################################################

def load_image(name):

    fullname = os.path.join('imagens', name)

    try:

    image = pygame.image.load(fullname)

    except pygame.error, message:

    print 'Cannot load image:', fullname

    raise SystemExit, message

    return image, image.get_rect()

# end load_image

# ############################################################################

# class Avatar #

# 02/09/2008 #

# #

# class responsible for designing and move the sprite of avatar #

# ############################################################################

class Avatar(pygame.sprite.Sprite):

    def __init__(self, startpos):

    pygame.sprite.Sprite.__init__(self)

    self.direction = 1

    self.image, self.rect = load_image('firts.bmp')

    self.rect.centerx = startpos[0]

    self.rect.centery = startpos[1]

# move the sprite

def move(self,x,y):

    self.rect.move_ip(x,y)

# detection of edges - não esta funcionando

    if self.rect.left < 0:

    self.direction = 1

    elif self.rect.right > width:

    self.direction = -1

# end Avatar

# ############################################################################

# class Maps #

# 02/10/2008 #

# #

# class responsible for designing the map #

# ############################################################################

class Maps(pygame.sprite.Sprite):

    def __init__(self, startpos):

    pygame.sprite.Sprite.__init__(self)

    self.image, self.rect = load_image('maps.bmp')

    self.rect.centerx = startpos[0]

    self.rect.centery = startpos[1]

# end Maps

# ############################################################################

# class Game #

# 02/09/2008 #

# #

# class main #

# ############################################################################

class Game():

    avatar = Avatar([500,500])

    maps = Maps([300,300])

    clock = pygame.time.Clock()

while 1:

# ensures that the program will not run more than 120fps

    clock.tick(120)

# events of keyboard

    for event in pygame.event.get():

    if event.type == QUIT:

    sys.exit(0)

    elif event.type == pygame.KEYDOWN:

    if event.key == pygame.K_LEFT:

    avatar.move(-10,0)

    if event.key == pygame.K_RIGHT:

    avatar.move(10,0)

    if event.key == pygame.K_UP:

    avatar.move(0,-10)

    if event.key == pygame.K_DOWN:

    avatar.move(0,10)

# detection between objects

#if avatar.rect.colliderect(maps.rect):

screen.fill(black)

screen.blit(avatar.image, avatar.rect)

screen.blit(maps.image, maps.rect)

pygame.display.flip()

# end Game