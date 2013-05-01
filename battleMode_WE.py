'''
Created on 2012-8-9

@author: Thinkpad
'''
import os, sys, pygame, random
from pygame.locals import *
from GameObject import *
from math import *
import random
pygame.init()
global screen
global background
background_image_filename = 'images/background.jpg'
screen = pygame.display.set_mode((960, 640), 0, 32)
background = pygame.image.load(background_image_filename).convert()
music = pygame.mixer.music.load ("music/blassic.ogg") 
pygame.mixer.music.play(-1)
class Player(GameObject):
    '''
    player
    '''
    def __init__(self,pos,ds,theta,dtheta,imagePass,imageDeath):
        GameObject.__init__(self, pos, ds, theta, dtheta, imagePass)
        self. lasertimer = 0
        self.lasermax = 50.
        self.bombamount = 1
        self.bombtimer = 0
        self.bombmax = 200
        self.deathflag = False
        self.shield = 100
    def update_1(self,timePassed):
        GameObject.update(self, timePassed)
        key = pygame.key.get_pressed()
        if key[pygame.K_PERIOD]:
            self.lasertimer += 1
            if self.lasertimer == self.lasermax:
                laserSprites.append(Laser(Vector2(self.pos.x,self.pos.y),400,self.theta,360,"images/laser.png"))
                fire.play()
                self.lasertimer = 0
            
        if key[pygame.K_SLASH]:
            self.bombtimer = self.bombtimer + 1
            if  self.bombtimer == self.bombmax:
                self.bombtimer = 0
                if self.bombamount > 0:
                    self.bombamount = self.bombamount -1
                    #score.bomb += -1
                    bombSprites.append(Bomb(Vector2(self.pos.x,self.pos.y),200,self.theta,360,"images/bomb.png"))
                    torpedo.play(0,0)
        AposX = self.pos.x
        AposY = self.pos.y
        AsizeX,AsizeY = self.image.get_size()
        for i in xrange(len(shieldPowerUpSprites)-1,-1,-1):
            BposX = shieldPowerUpSprites[i].pos.x
            BposY = shieldPowerUpSprites[i].pos.y
            BsizeX,BsizeY = shieldPowerUpSprites[i].image.get_size()
            if(isCollision(AposX,AposY,AsizeX,AsizeY,BposX,BposY,BsizeX,BsizeY)):
                del shieldPowerUpSprites[i]
                self.shield += 10
                powerup.play()
        for i in xrange(len(bombPowerUpSprites)-1,-1,-1):
            CposX = bombPowerUpSprites[i].pos.x
            CposY = bombPowerUpSprites[i].pos.y
            CsizeX,CsizeY = bombPowerUpSprites[i].image.get_size()
            if(isCollision(AposX,AposY,AsizeX,AsizeY,CposX,CposY,CsizeX,CsizeY)):
                del bombPowerUpSprites[i]
                self.bombamount += 1
                powerup.play()
    
    def draw(self,screen):
        if(self.deathflag == False):
            GameObject.draw(self,screen)

class Player_2(GameObject):
    '''
    player
    '''
    def __init__(self,pos,ds,theta,dtheta,imagePass,imageDeath):
        GameObject.__init__(self, pos, ds, theta, dtheta, imagePass)
        self. lasertimer = 0
        self.lasermax = 50.
        self.bombamount = 1
        self.bombtimer = 0
        self.bombmax = 200
        self.deathflag = False
        self.shield = 100
    def update_2(self,timePassed):
        GameObject.update(self, timePassed)
        key = pygame.key.get_pressed()
        if key[pygame.K_c]:
            self.lasertimer += 1
            if self.lasertimer == self.lasermax:
                laserSprites.append(Laser_2(Vector2(self.pos.x,self.pos.y),400,self.theta,360,"images/laser_2.png"))
                fire.play()
                self.lasertimer = 0
            
        if key[pygame.K_v]:
            self.bombtimer = self.bombtimer + 1
            if  self.bombtimer == self.bombmax:
                self.bombtimer = 0
                if self.bombamount > 0:
                    self.bombamount = self.bombamount -1
                #score.bomb += -1
                    bombSprites.append(Bomb_2(Vector2(self.pos.x,self.pos.y),200,self.theta,360,"images/bomb_2.png"))
                torpedo.play()
        AposX = self.pos.x
        AposY = self.pos.y
        AsizeX,AsizeY = self.image.get_size()
        for i in xrange(len(shieldPowerUpSprites)-1,-1,-1):
            BposX = shieldPowerUpSprites[i].pos.x
            BposY = shieldPowerUpSprites[i].pos.y
            BsizeX,BsizeY = shieldPowerUpSprites[i].image.get_size()
            if(isCollision(AposX,AposY,AsizeX,AsizeY,BposX,BposY,BsizeX,BsizeY)):
                del shieldPowerUpSprites[i]
                self.shield += 10
                powerup.play()
        for i in xrange(len(bombPowerUpSprites)-1,-1,-1):
            CposX = bombPowerUpSprites[i].pos.x
            CposY = bombPowerUpSprites[i].pos.y
            CsizeX,CsizeY = bombPowerUpSprites[i].image.get_size()
            if(isCollision(AposX,AposY,AsizeX,AsizeY,CposX,CposY,CsizeX,CsizeY)):
                del bombPowerUpSprites[i]
                self.bombamount += 1
                powerup.play()
    
    def draw(self,screen):
        if(self.deathflag == False):
            GameObject.draw(self,screen)
    
class Laser(Object):
    '''
    Laser
    '''
    def update(self,timePassed):
        Object.update(self, timePassed)
        AposX = self.pos.x
        AposY = self.pos.y
        AsizeX,AsizeY = self.image.get_size()
        CposX = player2.pos.x
        CposY = player2.pos.y
        CsizeX,CsizeY = player2.image.get_size()
        if(isCollision(AposX,AposY,AsizeX,AsizeY,CposX,CposY,CsizeX,CsizeY)):
            shieldSprites.append(Shield_2(Vector2(CposX-32,CposY-32)))                    
            player2.shield -=30
            self.dflag = True
            if(player2.shield <=0):
                player2.deathflag = True
                player2.shield = 0
                player2.pos = Vector2(10000,10000)
                playerExplosionSprites.append(playerExplosion_2(Vector2(CposX-32,CposY-32)))
                explode.play()

class Laser_2(Object):
    '''
    Laser
    '''
    def update(self,timePassed):
        Object.update(self, timePassed)
        AposX = self.pos.x
        AposY = self.pos.y
        AsizeX,AsizeY = self.image.get_size()
        CposX = player1.pos.x
        CposY = player1.pos.y
        CsizeX,CsizeY = player1.image.get_size()
        if(isCollision(AposX,AposY,AsizeX,AsizeY,CposX,CposY,CsizeX,CsizeY)):
            shieldSprites.append(Shield(Vector2(CposX-32,CposY-32)))                    
            player1.shield -=30
            self.dflag = True
            if(player1.shield <=0):
                player1.deathflag = True
                player1.shield = 0
                player1.pos = Vector2(10000,10000)
                playerExplosionSprites.append(playerExplosion(Vector2(CposX-32,CposY-32)))
                explode.play()

            
class Bomb (Object):
    '''
    Bomb
    '''
    def update(self,timePassed):
        Object.update(self, timePassed)
        AposX = self.pos.x
        AposY = self.pos.y
        AsizeX,AsizeY = self.image.get_size()
        CposX = player2.pos.x
        CposY = player2.pos.y
        CsizeX,CsizeY = player2.image.get_size()
        if(isCollision(AposX,AposY,AsizeX,AsizeY,CposX,CposY,CsizeX,CsizeY)):
            shieldSprites.append(Shield_2(Vector2(CposX-32,CposY-32)))                    
            player2.shield -=89
            self.dflag = True
            if(player2.shield <=0):
                player2.deathflag = True
                player2.shield = 0
                player2.pos = Vector2(10000,10000)
                playerExplosionSprites.append(playerExplosion_2(Vector2(CposX-32,CposY-32)))
                bombExplosionSprites.append(BombExplosion(Vector2(CposX-128,CposY-128),"images/bombexplosion.png"))
                explode.play()
                
class Bomb_2 (Object):
    '''
    Bomb
    '''
    def update(self,timePassed):
        Object.update(self, timePassed)
        AposX = self.pos.x
        AposY = self.pos.y
        AsizeX,AsizeY = self.image.get_size()
        CposX = player1.pos.x
        CposY = player1.pos.y
        CsizeX,CsizeY = player1.image.get_size()
        if(isCollision(AposX,AposY,AsizeX,AsizeY,CposX,CposY,CsizeX,CsizeY)):
            shieldSprites.append(Shield(Vector2(CposX-32,CposY-32)))                    
            player1.shield -=89
            self.dflag = True
            if(player1.shield <=0):
                player1.deathflag = True
                player1.shield = 0
                player1.pos = Vector2(10000,10000)
                bombExplosionSprites.append(BombExplosion(Vector2(CposX-128,CposY-128),"images/bombexplosion_2.png"))
                playerExplosionSprites.append(playerExplosion(Vector2(CposX-32,CposY-32)))
                explode.play()
                   


class playerExplosion(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/playerExplosion.png", -1)
        self.pos = pos
        self.counter = 0
        self.maxcount = 100
        self.flag = True
        
    def update(self):
        self.counter+=1
        if(self.counter == self.maxcount):
            self.flag = False

    def draw(self,screen):
        if(self.flag == True):
            screen.blit(self.image,self.pos)

class playerExplosion_2(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/playerExplosion_2.png", -1)
        self.pos = pos
        self.counter = 0
        self.maxcount = 100
        self.flag = True
        
    def update(self):
        self.counter+=1
        if(self.counter == self.maxcount):
            self.flag = False

    def draw(self,screen):
        if(self.flag == True):
            screen.blit(self.image,self.pos)

class BombExplosion(pygame.sprite.Sprite):
    def __init__(self,pos,imagePass):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(imagePass, -1)
        self.pos = pos
        self.counter = 0
        self.maxcount = 50
        self.flag = True
        
    def update(self):
        self.counter+=1
        if(self.counter == self.maxcount):
            self.flag = False

    def draw(self,screen):
        if(self.flag == True):
            screen.blit(self.image,self.pos)

class Shield(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/shield.png", -1)
        self.pos = pos
        self.counter = 0
        self.maxcount = 10
        self.flag = True
        
    def update(self):
        self.counter+=1
        if(self.counter == self.maxcount):
            self.flag = False

    def draw(self,screen):
        if(self.flag == True):
            screen.blit(self.image,self.pos)

class Shield_2(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/shield_2.png", -1)
        self.pos = pos
        self.counter = 0
        self.maxcount = 10
        self.flag = True
        
    def update(self):
        self.counter+=1
        if(self.counter == self.maxcount):
            self.flag = False

    def draw(self,screen):
        if(self.flag == True):
            screen.blit(self.image,self.pos)
            
class shieldPowerUp(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/shieldpowerup.png", -1)
        self.pos = pos
        self.flag = True
        
    def update(self):
        if self.pos.x < 50:
            self.pos.x = 50
        elif self.pos.x > 850:
            self.pos.x = 850
         
        if self.pos.y < 50:
            self.pos.y = 50
        elif self.pos.y > 550:
            self.pos.y = 550

    def draw(self,screen):
        screen.blit(self.image,self.pos)

class bombPowerUp(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/torpedpowerup.png", -1)
        self.pos = pos
        self.flag = True
        
    def update(self):
        if self.pos.x < 50:
            self.pos.x = 50
        elif self.pos.x > 850:
            self.pos.x = 850
         
        if self.pos.y < 50:
            self.pos.y = 50
        elif self.pos.y > 550:
            self.pos.y = 550

    def draw(self,screen):
        screen.blit(self.image,self.pos)

class GameOver(pygame.sprite.Sprite):
    def __init__(self):
        self.font = pygame.font.Font("fonts/planet5.ttf", 48)
        self.pos = Vector2(250,160)
    def update(self,timePassed):
        self.text = "Game Over"
        self.image = self.font.render(self.text, 1, (0, 255, 0))
    def draw(self,screen):
        if(isGameOver == True):
            screen.blit(self.image,self.pos) 

class GameOverReturn(pygame.sprite.Sprite):
    def __init__(self):
        self.font = pygame.font.Font("fonts/arial.ttf", 38)
        self.pos = Vector2(300,380)
    def update(self,timePassed):
        self.text = "Press ESC to Return"
        self.image = self.font.render(self.text, 1, (0, 255, 0))
    def draw(self,screen):
        if(isGameOver == True):
            screen.blit(self.image,self.pos) 

class Win(pygame.sprite.Sprite):
    def __init__(self):
        self.font = pygame.font.Font("fonts/planet5.ttf", 48)
        self.pos = Vector2(220,160)
    def update(self,timePassed):
        self.text = "Player1 Win"
        self.image = self.font.render(self.text, 1, (0, 255, 0))
        self.text2 = "Player2 Win"
        self.image2 = self.font.render(self.text2, 1, (0, 255, 0))
    def draw(self,screen):
        if(player1.deathflag == True):
            screen.blit(self.image2,self.pos)
        if(player2.deathflag == True):
            screen.blit(self.image,self.pos)

class Win_1(pygame.sprite.Sprite):
    def __init__(self):
        self.font = pygame.font.Font("fonts/arial.ttf", 38)
        self.pos = Vector2(300,380)
    def update(self,timePassed):
        self.text = "Press ESC to Return"
        self.image = self.font.render(self.text, 1, (0, 255, 0))
    def draw(self,screen):
        if(player1.deathflag == True or player2.deathflag == True):
            screen.blit(self.image,self.pos) 

def battleGame_WE():
    global isGameOver 
    isGameOver = False
    enemyCounter = 0
    flag = True
    #######################################################################################
    global fire
    fire = load_sound("music/laser.ogg")
    global explode
    explode = load_sound("music/explode.ogg")
    global torpedo
    torpedo = load_sound("music/torpedo.ogg")
    global powerup
    powerup = load_sound("music/powerup.ogg")
    global player1
    global player2
    a = random.randint(0,960)
    b = random.randint(0,640)
    c = random.randint(0,960)
    d = random.randint(0,640)
    gameover = GameOver()
    gameoverR  = GameOverReturn()
    winwin = Win()
    winR = Win_1()
    player1 = Player(Vector2(a, b) ,300,0,360,"images/player.png","images/playerExplosion.png")
    player2 = Player_2(Vector2(c, d) ,300,0,360,"images/player2.png","images/playerExplosion_2.png")
    arena = Arena()
    global score
    score = []
    score.append(Score_2(player1.shield,player1.bombamount,player2.bombamount,player2.shield))
    global laserSprites
    laserSprites = []
    global bombSprites
    bombSprites = []
    global bombExplosionSprites
    bombExplosionSprites = []
    global shieldSprites
    shieldSprites = []
    global shieldPowerUpSprites
    shieldPowerUpSprites = []
    global bombPowerUpSprites
    bombPowerUpSprites = []
    global playerExplosionSprites
    playerExplosionSprites = []
    #########################################################################################
    
    clock = pygame.time.Clock()
    
    while flag:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_ESCAPE]:
            flag = False
        if pressed_keys[K_LEFT]:
            player1.rotation_direction = +1.
        if pressed_keys[K_RIGHT]:
            player1.rotation_direction = -1.
  
        if pressed_keys[K_UP]:
            player1.movement_direction = -1.
        if pressed_keys[K_DOWN]:
            player1.movement_direction = +1.
    
        if pressed_keys[K_a]:
            player2.rotation_direction = +1.
        if pressed_keys[K_d]:
            player2.rotation_direction = -1.
  
        if pressed_keys[K_w]:
            player2.movement_direction = -1.
        if pressed_keys[K_s]:
            player2.movement_direction = +1
           
        timePassed = clock.tick()
        index = random.randint(0,500)
        if(index == 50 and len(shieldPowerUpSprites) == 0):
            m = random.randint(0,960)
            n = random.randint(0,640)
            shieldPowerUpSprites.append(shieldPowerUp(Vector2(m,n)))
        if(index == 70 and len(bombPowerUpSprites) == 0):
            m = random.randint(0,960)
            n = random.randint(0,640)
            bombPowerUpSprites.append(bombPowerUp(Vector2(m,n)))
        screen.blit(background, (0,0))
        #update
        ################################################################################
        player1.update_1(timePassed)
        player2.update_2(timePassed)
        #enemy.update(timePassed)
        for laser in laserSprites:
            laser.update(timePassed)
        for bomb in bombSprites:
            bomb.update(timePassed)
        for shield in shieldSprites:
            shield.update()
        for bomb in bombExplosionSprites:
            bomb.update()
        for powerUp in shieldPowerUpSprites:
            powerUp.update()
        for powerUp in bombPowerUpSprites:
            powerUp.update()
        for explosion in playerExplosionSprites:
            explosion.update()
        score.append(Score_2(player1.shield,player1.bombamount,player2.bombamount,player2.shield))
        score[1].score1 = score[0].score1
        score[1].score2 = score[0].score2
        del score[0]
        for score2 in score:
            score2.update(timePassed)
        gameover.update(timePassed)
        gameoverR.update(timePassed)
        winwin.update(timePassed)
        winR.update(timePassed)
        arena.update(timePassed)
        #########################################################################################
        #draw
        #########################################################################################
        arena.draw(screen)
        for score2 in score:
            score2.draw(screen)
        for laser in laserSprites:
            laser.draw(screen)
        for bomb in bombSprites:
            bomb.draw(screen)
        for shield in shieldSprites:
            shield.draw(screen)
        for bomb in bombExplosionSprites:
            bomb.draw(screen)
        for powerUp in shieldPowerUpSprites:
            powerUp.draw(screen)
        for powerUp in bombPowerUpSprites:
            powerUp.draw(screen)
        for explosion in playerExplosionSprites:
            explosion.draw(screen)
        player1.draw(screen)
        player2.draw(screen)
        gameover.draw(screen)
        gameoverR.draw(screen)
        winwin.draw(screen)
        winR.draw(screen)
        ############################################################################################
        for i in xrange(len(laserSprites)-1,-1,-1):
            if(laserSprites[i].dflag == True):
                del laserSprites[i]
        for i in xrange(len(bombSprites)-1,-1,-1):
            if(bombSprites[i].dflag == True):
                del bombSprites[i]
        if(player1.deathflag == True and player2.deathflag == True):
            isGameOver = True
        #############################################################################################
        pygame.display.update()
        
