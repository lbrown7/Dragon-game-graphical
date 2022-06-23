import pdb
import random
import sys
import time

import pygame
import pygame.mixer

from Gideon import Gideon
from monster import Monster
from orc import orc
from potion import Potion
from settings import Settings
from Shop import shop
from Tree import tree


class Game:
    """a genaral class to controll the whole game
    reterns: self.x, self.y
    attributes: none
    """
    
    def __init__(self):
        pygame.init()
        self.settings = Settings()
                
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("The Adventures of Gideon")

        self.keys = pygame.key.get_pressed()

        self.gideon = Gideon(self)
        self.orc1 = orc(self, 'mt')
        self.tree1 = tree(self, 'ml')
        self.tree2 = tree(self, 'tr')
        self.tree3 = tree(self, 'bl')
        self.shop1 = shop(self)
        self.potion1 = Potion(self)
        self.m1 = Monster(self, 'br')

        # this is somethihng I am not so sure about yet because I think soething is wrong with the asterisk (this is an asterisk: *)
        #self.trees = pygame.sprite.Group(*'self.tree1' 'self.tree2' 'self.tree3')
        
        self.trees = self.__iter__()

    def run_game(self):
        while True:
            self._check_gideon_events()
            self.gideon.update()
            self._check_collisions()
            self._update_screen()
            self.check_dead()
            self.sound()

    def __iter__(self):
        GameIterator = iter()
        return GameIterator(self)

    def hitTree(self):
        while pygame.sprite.groupcollide(self.trees, self):
            self.gideon.y += 1
            self.gideon.x += 1

    def _check_gideon_events(self):
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.gideon.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.gideon.moving_left = True
                    elif event.key == pygame.K_UP:
                        self.gideon.moving_up = True
                    elif event.key == pygame.K_DOWN:
                        self.gideon.moving_down = True
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        exit()
                        quit()
                        sys.exit()
                    elif self.keys[pygame.K_RIGHT] and self.keys[pygame.K_RSHIFT]:
                        self.gideon.runningRight = True
                    elif self.keys[pygame.K_LEFT] and self.keys[pygame.K_RSHIFT]:
                        self.gideon.runningLeft = True
                    elif event.key == pygame.K_SPACE:
                        self.gideon.attack = True
                elif event.type == pygame.KEYUP:
                    if event.type == pygame.K_RIGHT:
                        self.gideon.moving_right = False
                    elif event.type == pygame.K_LEFT:
                        self.gideon.moving_left = False
                    elif event.key == pygame.K_UP:
                        self.gideon.moving_up = False
                    elif event.key == pygame.K_DOWN:
                        self.gideon.moving_down = False

    def _check_orc1_events(self):
        '''if a player is near the orc1 comes tord it'''
        pass

    def check_dead(self):
        '''make's sure that gideon has not died'''
        if self.settings.man_health == 0:
            exit()
            pygame.quit()
            sys.exit()
            quit()
        
                        
    def _update_screen(self):
            self.screen.fill(self.settings.bg_color)
            self.blitmes()
            self.shopFuncs()
                
            pygame.display.flip()

    def blitmes(self):
        self.gideon.blitme()
        self.orc1.blitme()
        self.tree1.blitme()
        self.tree2.blitme()
        self.tree3.blitme()
        self.shop1.blitme()
        self.potion1.blitme()
        self.m1.blitme()

    def shopFuncs(self):
        pass

    def _check_collisions(self):
        self.checkCollision(self.gideon, self.orc1, self.settings.man_health, 2)
        self.checkCollision(self.gideon, self.tree1, self.gideon.x, 1)
        self.screenChange()

    def changeColor(self, path):
        self.screen.fill(path)
    
    def screenChange(self):
        if pygame.sprite.collide_rect(self.gideon, self.shop1): 
            self.changeColor(self.settings.bg2c)

    def changeWindow(self):
        if self.gideon.rect.right > self.gideon.screen_rect.right + 1:
            self.changeColor(self.settings.bg3c)
    
############################################ put all test below here ##############################################################

    def checkCollision(self, sprite1, sprite2, func, ji):
        col = pygame.sprite.collide_rect(sprite1, sprite2)
        if col == True:
            func -= ji

    def sound(self):
        pygame.mixer.music.load("E:/dragon game graphical/audio/moonlight.wav")
        pygame.mixer.music.play(-1)

    def abbandon(self, a):
        if a == True:
            pygame.quit()
            quit()
            exit()
            sys.exit()
        else:
            pass

    def enter_shop(self, sprite1, sprite):
        self.screenChange()

    def animate(self, paths=[]):
        if paths:
            for image in paths:
                self.image = pygame.image.load(image)
                self.image.blitme()
                time.sleep(0.2)

########################################### put all tests above here ###############################################################
        
    
if __name__ == "__main__":
    g = Game()
    g.run_game()