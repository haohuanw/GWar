'''
Created on 2012-8-4

@author: Haohuanw
'''

import os, sys, pygame, random
from pygame.locals import *
#Load Image
def load_image(name, colorkey=None):
    try:
        image = pygame.image.load(name)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image

#Load Sounds
def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    try:
        sound = pygame.mixer.Sound(name)
    except pygame.error, message:
        print 'Cannot load sound:', name
        raise SystemExit, message
    return sound

def isCollision(AposX, AposY, AsizeX, AsizeY, BposX, BposY, BsizeX, BsizeY):
    if ((AposX+AsizeX <= BposX +BsizeX \
         and AposX +AsizeX >= BposX )\
        or(AposX <= BposX + BsizeX\
           and AposX +AsizeX >= BposX ))\
           \
           and ((AposY+AsizeY <= BposY +BsizeY \
                 and AposY +AsizeY> BposY) \
                or(AposY <= BposY +BsizeY \
                   and AposY > BposY)):
        return True
    else:   
        return False
    