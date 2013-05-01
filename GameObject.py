'''
Created on 2012-8-4

@author: Haohuanw
'''
import pygame.sprite
from loader import *
from math import *
from vector2 import *
import random

class GameObject(pygame.sprite.Sprite):
    '''
    object that can move and rotate in the game including: enemy, player
    '''
    def __init__(self,pos,ds,theta,dtheta,imagePass):
        '''
        Constructor
        '''
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(imagePass,-1) #set center at other position
        self.pos = pos#right-left top
        self.ds = ds#movement speed
        self.theta = theta#angle at this pos
        self.dtheta = dtheta#rotation spped
        self.rotation_direction = 0.
        self.movement_direction = 0.
        self.rotated_image = self.image
        self.rotated_pos = self.pos
        self.deathflag = False
        
    def update(self,timePassed):#when rotate, update theta each time
        self.rotated_image = pygame.transform.rotate(self.image, self.theta)
        w,h = self.rotated_image.get_size()
        self.rotated_pos = Vector2(self.pos.x-w/2, self.pos.y-h/2)
        timePassedSeconds = timePassed / 1000.0
        self.theta += self.rotation_direction * self.dtheta * timePassedSeconds
        heading_x = sin(self.theta*pi/180.)
        heading_y = cos(self.theta*pi/180.)
        heading = Vector2(heading_x, heading_y)
        heading *= self.movement_direction
        self.pos+= heading * self.ds*timePassedSeconds
        self.rotation_direction = 0
        self.movement_direction = 0
        if(self.deathflag == False):
            if self.pos.x < 20:
                self.pos.x = 940
            elif self.pos.x > 940:
                self.pos.x = 20
         
            if self.pos.y < 20:
                self.pos.y = 620
            elif self.pos.y > 620:
                self.pos.y = 20
    def getTheta(self):
        return self.theta
    
    def getMovement(self):
        return self.movement_direction
            
    def draw(self,screen):
        screen.blit(self.rotated_image, self.rotated_pos)

class Object(pygame.sprite.Sprite):
    '''
    object that can move and rotate in the game including: enemy, player
    '''
    def __init__(self,pos,ds,theta,dtheta,imagePass):
        '''
        Constructor
        '''
        pygame.sprite.Sprite.__init__(self)
        self.image= load_image(imagePass,-1) #set center at other position
        self.pos = pos#right-left top
        self.ds = ds#movement speed
        self.theta = theta#angle at this pos
        self.dtheta = dtheta#rotation spped
        self.rotation_direction = 0.
        self.movement_direction = -1.
        self.rotated_image = self.image
        self.rotated_pos = self.pos
        self.dflag = False
        
    def update(self,timePassed):#when rotate, update theta each time
        self.rotated_image = pygame.transform.rotate(self.image, self.theta)
        w,h = self.rotated_image.get_size()
        self.rotated_pos = Vector2(self.pos.x-w/2, self.pos.y-h/2)
        timePassedSeconds = timePassed / 1000.0
        self.theta += self.rotation_direction * self.dtheta * timePassedSeconds
        heading_x = sin(self.theta*pi/180.)
        heading_y = cos(self.theta*pi/180.)
        heading = Vector2(heading_x, heading_y)
        heading *= self.movement_direction
        self.pos+= heading * self.ds*timePassedSeconds
        #self.rotation_direction = 0
        #self.movement_direction = 0

        if self.pos.x < 0:
            self.dflag = True
        elif self.pos.x > 960:
            self.dflag = True
         
        if self.pos.y < 0:
            self.dflag = True
        elif self.pos.y > 640:
            self.dflag = True
    def getTheta(self):
        return self.theta
    
    def getMovement(self):
        return self.movement_direction
            
    def draw(self,screen):
        if(self.dflag == False):
            screen.blit(self.rotated_image, self.rotated_pos)

#doesn't use
class EnemyObject(Object):
    def __init__(self,pos,ds,theta,dtheta,imagePass):
        Object.__init__(self,pos,ds,theta,dtheta,imagePass)
    def update(self,timePassed):
        Object.update(self, timePassed)
        x,y = random.randint(1,960),random.randint(1,640)
        print x,y
        if(x == self.pos.x):
            self.theta = 0
        else:
            self.theta = atan2((y-self.pos.y),(x-self.pos.x))
        if(y>self.pos.y and x>self.pos.x):
            self.movement_direction = 1
            self.rotation_direction = 1
        if(y<self.pos.y and x>self.pos.x):
            self.movement_direction = -1
            self.rotation_direction = 1
        if(y>self.pos.y and x<self.pos.x):
            self.movement_direction = 1
            self.rotation_direction = -1
        if(y<self.pos.y and x>self.pos.x):
            self.movement_direction = -1
            self.rotation_direction = -1
     
class Arena(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/arena.jpg", -1)
        self.dy = 0.5
        self.pos = Vector2(0,-1000)
        #self.pos.x = 0
        #self.pos.y = -600
        self.reset()
        
    def update(self,timePassed):
        self.pos.y += self.dy
        if self.pos.y >= 0:
            self.reset() 
    
    def draw(self,screen):
        screen.blit(self.image,self.pos)
    def reset(self):
        self.pos.y = -600

class Score_2(pygame.sprite.Sprite):
    def __init__(self,shield1,bomb1,bomb2,shield2):
        pygame.sprite.Sprite.__init__(self)
        self.score1 = 0
        self.score2 = 0
        self.bomb1= bomb1
        self.bomb2 = bomb2
        self.shield1 = shield1
        self.shield2 = shield2
        self.font = pygame.font.Font("fonts/arial.ttf", 28)
        self.pos = Vector2(0,0)
        self.pos1 = Vector2(0,600)
        self.pos2 = Vector2(840,600)
    def update(self,timePassed):
        self.text = "Player1: Shield: %d     Torpedo: %d            Torpedo: %d     Shield: %d :Player2" \
                    % (self.shield1, self.bomb1,self.bomb2,self.shield2)
        self.text1 = "Score: %d" % self.score1
        self.text2 = "Score: %d" % self.score2
        self.image = self.font.render(self.text, 1, (0, 255, 0))
        self.image1 = self.font.render(self.text1, 1, (0, 255, 0))
        self.image2 = self.font.render(self.text2, 1, (0, 255, 0))
    def draw(self,screen):
        screen.blit(self.image,self.pos) 
        screen.blit(self.image1,self.pos1) 
        screen.blit(self.image2,self.pos2)    
        
class Score_1(pygame.sprite.Sprite):
    def __init__(self,shield1,bomb1):
        pygame.sprite.Sprite.__init__(self)
        self.score1 = 0
        self.score2 = 0
        self.bomb1= bomb1
        self.shield1 = shield1
        self.font = pygame.font.Font("fonts/arial.ttf", 28)
        self.pos = Vector2(0,0)
        self.pos1 = Vector2(0,600)
    def update(self,timePassed):
        self.text = "Player1: Shield: %d     Torpedo: %d   " \
                    % (self.shield1, self.bomb1)
        self.text1 = "Score: %d" % self.score1
        self.image = self.font.render(self.text, 1, (0, 255, 0))
        self.image1 = self.font.render(self.text1, 1, (0, 255, 0))
    def draw(self,screen):
        screen.blit(self.image,self.pos) 
        screen.blit(self.image1,self.pos1)    
        
        
        
