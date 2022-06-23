import time

print('loading backup files...')
time.sleep(0.2)

print('ready!')
time.sleep(1)

print('backing up...')

file1 = "E:/dragon game graphical/dggc/admin/dragon game graphical/dragon game graphical test.py"
file2 = "E:/dragon game graphical/dggc/admin/dragon game graphical/Gideon.py"
file3 = "E:/dragon game graphical/dggc/admin/dragon game graphical/settings.py"
file4 = "E:/dragon game graphical/dggc/admin/dragon game graphical/Tree.py"
file5 = "E:/dragon game graphical/dggc/admin/dragon game graphical/orc.py"
with open(file1, 'w+') as f:
    f.write('''import sys
import pygame
import pdb
from settings import Settings
from Gideon import Gideon
from orc import Orc

class Game:
    """a genaral class to controll the whole game
    reterns: self.x, self.y
    attributes: none
    """

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("The Adventures of Gideon")
        
        self.gideon = Gideon(self)
        self.orc = Orc(self)

        orc = self.orc
        gideon = self.gideon

    def run_game(self):
        while True:
            self._check_gideon_events()
            self.gideon.update()
            self._update_screen()
        
    def _check_gideon_events(self):
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.gideon.moving_right = True
                    if event.key == pygame.K_LEFT:
                        self.gideon.moving_left = True
                    if event.key == pygame.K_UP:
                        self.gideon.moving_up = True
                    if event.key == pygame.K_DOWN:
                        self.gideon.moving_down = True
                elif event.type == pygame.KEYUP:
                    if event.type == pygame.K_RIGHT:
                        self.gideon.moving_right = False
                    if event.type == pygame.K_LEFT:
                        self.gideon.moving_left = False
                    if event.key == pygame.K_UP:
                        self.gideon.moving_up = False
                    if event.key == pygame.K_DOWN:
                        self.gideon.moving_down = False

    def _check_orc_events(self):
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.orc.moving_right = True
                    if event.key == pygame.K_LEFT:
                        self.orc.moving_left = True
                    if event.key == pygame.K_UP:
                        self.orc.moving_up = True
                    if event.key == pygame.K_DOWN:
                        self.orc.moving_down = True
                elif event.type == pygame.KEYUP:
                    if event.type == pygame.K_RIGHT:
                        self.orc.moving_right = False
                    if event.type == pygame.K_LEFT:
                        self.orc.moving_left = False
                    if event.key == pygame.K_UP:
                        self.orc.moving_up = False
                    if event.key == pygame.K_DOWN:
                        self.orc.moving_down = False
                        
    def _update_screen(self):
            self.screen.fill(self.settings.bg_color)
            self.gideon.blitme()
            self.orc.blitme()

            pygame.display.flip()
    
    def _check_collisions(self):
        if pygame.sprite.spritecollideany(self.gideon, self.orc):
            print('gideon hit orc')
        if pygame.sprite.spritecollideany(self.orc, self.gideon):
            print('orc hit gideon')

    def collide(self, spriteGroup1, spriteGroup2):
        if pygame.sprite.spritecollide(spriteGroup1, spriteGroup2, False):
           return True

    
if __name__ == "__main__":
    ai = Game()
    ai.run_game()
''')
    f.close()


with open(file2, 'w+') as f2:
    f2.write('''import pygame
from settings import DGGsettings

class Gideon:
    """a class to controll gideon
    returns: none
    attributes: self, gideon
    functions: __init__, update, blitme
    """

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("E:/dragon game graphical/images/bmp/gideon-U-1.bmp")
        self.rect = self.image.get_rect()
        
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
                       
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        paralized = False
        arrows = False
        swords = 0
        if self.moving_right and paralized == False:
            self.x += self.settings.man_speed
            self.image = pygame.image.load("E:/dragon game graphical/images/bmp/gideon-U-1.bmp")
            self.rect = self.image.get_rect()
        if self.moving_left and paralized == False:
            self.x -= self.settings.man_speed
            self.image = pygame.image.load("E:/dragon game graphical/images/bmp/gideon-U-1.bmp")
            self.rect = self.image.get_rect()
        if self.moving_up and paralized == False:
            self.y -= self.settings.man_speed
            self.image = pygame.image.load("E:/dragon game graphical/images/bmp/gideon-U-1.bmp")
            self.rect = self.image.get_rect()
        if self.moving_down and paralized == False:
            self.y += self.settings.man_speed
            self.image = pygame.image.load("E:/dragon game graphical/images/bmp/gideon-U-1.bmp")
            self.rect = self.image.get_rect()
        
        self.rect.x = self.x
        self.rect.y = self.y
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
''')
    f2.close()

with open(file3, 'w+') as f3:
    f3.write('''class Settings:
    def __init__(self):
        self.screen_width = 700
        self.screen_height = 600
        self.bg_color = (215, 215, 140)
        
        paralized = False
        arrows = False
        swords = 0

        self.man_speed = 0.1
''')
    f3.close()

with open(file4, 'w+') as f4:
    f4.write('''import pygame

class tree:
    """a simple class to controll the tree"""

    def __init__(self, x, y, ai_game):
        self.x = x
        self.y = y
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("E:/dragon game graphical/images/bmp/bush.bmp")
        self.rect = self.image.get_rect()
        
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect) 
''')
    f4.close()

time.sleep(1)
print('almost done!!!')

with open(file5, 'w+') as f5:
    f5.write('''import pygame
import random
from settings import DGGsettings
from Gideon import Gideon

class Orc:
    """a class to controll the orcs
    returns: none
    attributes: self, gideon
    functions: __init__, update, blitme
    """
    
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("E:/dragon game graphical/images/bmp/orc-R.bmp")
        self.rect = self.image.get_rect()

        self.rect.midtop = self.screen_rect.midtop

        self.gideon = Gideon(self)
        
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)
                       
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        paralized = False
        arrows = False
        swords = 0
        dead = False
        if self.moving_right and paralized == False:
            self.x += self.settings.man_speed
            self.image = pygame.image.load("E:/dragon game graphical/images/bmp/orc-R.bmp")
            self.rect = self.image.get_rect()
        if self.moving_left and paralized == False:
            self.x -= self.settings.man_speed
            self.image = pygame.image.load("E:/dragon game graphical/images/bmp/orc-L.bmp")
            self.rect = self.image.get_rect()
        if self.moving_up and paralized == False:
            self.y -= self.settings.man_speed
            self.image = pygame.image.load("E:/dragon game graphical/images/bmp/orc-R.bmp")
            self.rect = self.image.get_rect()
        if self.moving_down and paralized == False:
            self.y += self.settings.man_speed
            self.image = pygame.image.load("E:/dragon game graphical/images/bmp/orc-L.bmp")
            self.rect = self.image.get_rect()
        
        self.rect.x = self.x
        self.rect.y = self.y
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
''')
    f5.close()

time.sleep(2)

print('done!!!')
