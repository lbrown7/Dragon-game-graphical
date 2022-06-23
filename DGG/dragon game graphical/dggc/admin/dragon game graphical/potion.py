import pygame

from Gideon import Gideon
from settings import Settings
from monster import Monster
from orc import orc


class Potion:
    """a simple class to controll the potions"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("E:/dragon game graphical/images/bmp/potion-1.bmp")
        self.rect = self.image

        self.gideon = Gideon(self)
        self.orc1 = orc(self, 'mt')
        self.m1 = Monster(self, 'br')
        
        self.rect.topleft = self.screen_rect.topleft

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def col(self, sprite):
        if pygame.sprite.collide_rect(self, sprite):
           return True
        else:
            return False

    def healgideon(self):
        if self.col(self.gideon):
            self.settings.man_health += 10

    def healmonster(self):
        if self.col(self.m1):
            self.settings.monster_health += 5
        elif self.col(self.orc1):
            self.settings.orc_health += 5
        else: 
            pass
    
    def heal(self):
        self.healgideon()
        self.healmonster()

    def poruntime(self):
        self.heal()