'''
Created on 2012-8-4

@author: Haohuanw
'''
import os, sys, pygame, random
from pygame.locals import *
from GameObject import *
from math import *
import random
import doubleGame
import singleGame
import battleMode
import battleMode_WE
pygame.init()
global screen
global background
pygame.display.set_caption("Geometric War")
icon = pygame.image.load("images/icon.png")
icon = pygame.display.set_icon(icon)    
background_image_filename = 'images/background.jpg'
screen = pygame.display.set_mode((960, 640), 0, 32)
background = pygame.image.load(background_image_filename).convert()
music = pygame.mixer.music.load ("music/blassic.ogg") 
pygame.mixer.music.play(-1)

class SpaceMenu:
    def __init__(self, *options):

        self.options = options
        self.x = 0
        self.y = 0
        self.font = pygame.font.Font(None, 32)
        self.option = 0
        self.width = 1
        self.color = [0, 0, 0]
        self.hcolor = [0, 0, 0]
        self.height = len(self.options)*self.font.get_height()
        for o in self.options:
            text = o[0]
            ren = self.font.render(text, 1, (0, 0, 0))
            if ren.get_width() > self.width:
                self.width = ren.get_width()

    def draw(self, surface):
        i=0
        for o in self.options:
            if i==self.option:
                clr = self.hcolor
            else:
                clr = self.color
            text = o[0]
            ren = self.font.render(text, 1, clr)
            if ren.get_width() > self.width:
                self.width = ren.get_width()
            surface.blit(ren, (self.x, self.y + i*self.font.get_height()))
            i+=1
     
    def update(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_DOWN:
                    self.option += 1
                if e.key == pygame.K_UP:
                    self.option -= 1
                if e.key == pygame.K_RETURN:
                    self.options[self.option][1]()
        if self.option > len(self.options)-1:
            self.option = 0
        if self.option < 0:
            self.option = len(self.options)-1

    def set_pos(self, x, y):
        self.x = x
        self.y = y
 
    def set_font(self, font):
        self.font = font
      
    def set_highlight_color(self, color):
        self.hcolor = color
      
    def set_normal_color(self, color):
        self.color = color
 
    def center_at(self, x, y):
        self.x = x-(self.width/2)
        self.y = y-(self.height/2)

def missionMenu():
    arena = Arena()
    menuTitle = SpaceMenu(
        ["Geometric War"])

    instructions = SpaceMenu(
        [""], 
        ["In the Kingdom of Geometry, a war is started"],
        [""],
        ["Select Different Game Mode and try your best"],
        [""],
        ["Navigate your soilder with Arrow Keys or WASD"],
        [""],
        ["the period button or C to fire the proton laser."],
        [""],
        ["Use the Slash or V  to shoot a torpedo. "],
        [""],
        ["Be careful, you have a limited supply."],
        [""],
        ["You Can Escape the Game by pressing ESC"],
        [""],
        ["            PRESS ESC TO RETURN             "])
 
    menuTitle.center_at(220, 130)
    menuTitle.set_font(pygame.font.Font("fonts/planet5.ttf", 48))
    menuTitle.set_highlight_color((0, 255, 0))
    
    instructions.center_at(520, 350)
    instructions.set_font(pygame.font.Font("fonts/arial.ttf", 22))
    instructions.set_normal_color((0, 255, 0))
    clock = pygame.time.Clock()
    flag = True
    while flag:
        timePassed = clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    flag = False
        screen.blit(background, (0,0))    
        arena.update(timePassed)
        arena.draw(screen)
        menuTitle.draw(screen)
        instructions.draw(screen)
        pygame.display.flip()

def aboutMenu():
    arena = Arena()
    menuTitle = SpaceMenu(
        ["Geometric War"])
    info = SpaceMenu(
        [""], 
        ["Geometric War Beta"],
        [""],
        ["Designed by the Haohuan Wang."],
        [""],
        ["For CMU APEA Program 15-112 course"],
        [""],
        [""],
        ["      PRESS ESC TO RETURN         "])
        
    menuTitle.center_at(220, 130)
    menuTitle.set_font(pygame.font.Font("fonts/planet5.ttf", 48))
    menuTitle.set_highlight_color((0, 255, 0))

    info.center_at(450, 300)
    info.set_font(pygame.font.Font("fonts/arial.ttf", 28))
    info.set_normal_color((0, 255, 0))
    clock = pygame.time.Clock()
    flag = True
    while flag:
        timePassed = clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    flag = False
        screen.blit(background, (0,0))    
        arena.update(timePassed)
        arena.draw(screen)
        menuTitle.draw(screen)
        info.draw(screen)
        pygame.display.flip()

def startMenu():
    arena = Arena()
    menuTitle = SpaceMenu(
        ["Geometric War"])
        
    menu = SpaceMenu(
        ["Single Player", option5],
        ["Double Players", option6],
        ["Survival Mode[Extremely Hard]", option7],
        ["Battle Mode", option8],
        ["Return",option9])

    menuTitle.center_at(220, 130)
    menuTitle.set_font(pygame.font.Font("fonts/planet5.ttf", 48))
    menuTitle.set_highlight_color((0, 255, 0))
    
    menu.center_at(450, 300)
    menu.set_font(pygame.font.Font("fonts/arial.ttf", 32))
    menu.set_highlight_color((0, 255, 0))
    menu.set_normal_color((0, 85, 0))
    
    clock = pygame.time.Clock()
    while 1:
        timePassed = clock.tick(30)
        events = pygame.event.get()
        menu.update(events)
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                return
        screen.blit(background, (0,0))
        arena.update(timePassed)
        arena.draw(screen)
        menu.draw(screen)
        menuTitle.draw(screen)
        pygame.display.flip()

def survivalMenu():
    arena = Arena()
    menuTitle = SpaceMenu(
        ["Geometric War"])
        
    menu = SpaceMenu(
        ["Single Player", option10],
        ["Double Players", option11],
        ["Return",option1]
        )

    menuTitle.center_at(220, 130)
    menuTitle.set_font(pygame.font.Font("fonts/planet5.ttf", 48))
    menuTitle.set_highlight_color((0, 255, 0))
    
    menu.center_at(450, 300)
    menu.set_font(pygame.font.Font("fonts/arial.ttf", 32))
    menu.set_highlight_color((0, 255, 0))
    menu.set_normal_color((0, 85, 0))
    
    clock = pygame.time.Clock()
    while 1:
        timePassed = clock.tick(30)
        events = pygame.event.get()
        menu.update(events)
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                return
        screen.blit(background, (0,0))
        arena.update(timePassed)
        arena.draw(screen)
        menu.draw(screen)
        menuTitle.draw(screen)
        pygame.display.flip()

def battleMenu():
    arena = Arena()
    menuTitle = SpaceMenu(
        ["Geometric War"])
        
    menu = SpaceMenu(
        ["Without Enemy", option12],
        ["With Enemy", option13],
        ["Return",option1]
        )

    menuTitle.center_at(220, 130)
    menuTitle.set_font(pygame.font.Font("fonts/planet5.ttf", 48))
    menuTitle.set_highlight_color((0, 255, 0))
    
    menu.center_at(450, 300)
    menu.set_font(pygame.font.Font("fonts/arial.ttf", 32))
    menu.set_highlight_color((0, 255, 0))
    menu.set_normal_color((0, 85, 0))
    
    clock = pygame.time.Clock()
    while 1:
        timePassed = clock.tick(30)
        events = pygame.event.get()
        menu.update(events)
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                return
        screen.blit(background, (0,0))
        arena.update(timePassed)
        arena.draw(screen)
        menu.draw(screen)
        menuTitle.draw(screen)
        pygame.display.flip()

def option1():
    startMenu()
def option2():
    missionMenu()
def option3():
    aboutMenu()   
def option4():
    pygame.quit()
    sys.exit()
def option5():
    singleGame.singleGame()
def option6():
    doubleGame.doubleGame()
def option7():
    survivalMenu()
def option8():
    battleMenu()
def option9():
    main()
def option10():
    singleGame.singleGame_survival()
def option11():
    doubleGame.doubleGame_survival()
def option12():
    battleMode_WE.battleGame_WE()
def option13():
    battleMode.battleGame()

def main():

    arena = Arena()
    menuTitle = SpaceMenu(
        ["Geometric War"])
        
    menu = SpaceMenu(
        ["Start", option1],
        ["Misson", option2],
        ["About", option3],
        ["Quit", option4])

    menuTitle.center_at(220, 130)
    menuTitle.set_font(pygame.font.Font("fonts/planet5.ttf", 48))
    menuTitle.set_highlight_color((0, 255, 0))
    
    menu.center_at(450, 300)
    menu.set_font(pygame.font.Font("fonts/arial.ttf", 32))
    menu.set_highlight_color((0, 255, 0))
    menu.set_normal_color((0, 85, 0))
    
    clock = pygame.time.Clock()
    while 1:
        timePassed = clock.tick(30)
        events = pygame.event.get()
        menu.update(events)
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                return
        screen.blit(background, (0,0))
        arena.update(timePassed)
        arena.draw(screen)
        menu.draw(screen)
        menuTitle.draw(screen)
        pygame.display.flip()

main()