import random
import time

import pygame

from Gideon import Gideon
from settings import Settings


class orc:
    """a class to controll the orc1s
    returns: none
    attributes: self, gideon
    functions: __init__, update, blitme
    """
    
    def __init__(self, ai_game, a='', x=int, y=int):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.gideon = Gideon(self)

        self.image = pygame.image.load("E:/dragon game graphical/images/bmp/orc-R.bmp")
        self.rect = self.image.get_rect()
        
        # this defines self.x and self.y by just randomizeing it
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        if a == 'mr':
            self.rect.midright = self.screen_rect.midright
        elif a == 'ml':
            self.rect.midleft = self.screen_rect.midleft
        elif a == 'mb':
            self.rect.midbottom = self.screen_rect.midbottom
        elif a == 'mt':
            self.rect.midtop = self.screen_rect.midtop
        elif a == 'tl':
            self.rect.topleft = self.screen_rect.topleft
        elif a == 'tr':
            self.rect.topright = self.screen_rect.topright
        elif a == 'bl':
            self.rect.bottomleft = self.screen_rect.bottomleft
        elif a == 'br':
            self.rect.bottomright = self.screen_rect.bottomright
        else:
            self.x = x
            self.y = y

        # movement flags                        
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self, a='', x=0, y=0):
        #self.dead2()
        pass
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def spawn(self, t):
        self.image = pygame.image.load("E:/dragon game graphical/images/bmp/nys.bmp")
        self.rect = self.image.get_rect()

        time.sleep(t)

        self.image = pygame.image.load("E:/dragon game graphical/images/bmp/orc1-R.bmp")
        self.rect = self.image.get_rect()

    def dead2(self):
        col = pygame.sprite.collide_rect(self.gideon, self)
        if col and self.gideon.attack:
            self.dead = True