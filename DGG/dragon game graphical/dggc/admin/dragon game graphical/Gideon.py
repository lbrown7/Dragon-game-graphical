import pygame

from settings import Settings
from Tree import tree


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

        pygame.image = pygame.image.load("E:/dragon game graphical/images/bmp/gideon-U-1.bmp")
        self.rect = self.image.get_rect()
        
        self.rect.midbottom = self.screen_rect.midbottom

        self.tree7 = tree(self, 'ml')

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
                       
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.runningRight = False
        self.runningLeft = False
        self.runningUp = False
        self.runningDown = False
        self.attack = False
    
    def update(self):
        paralized = False
        arrows = 0
        swords = 0
        
        if self.moving_right and paralized == False and self.rect.right < self.screen_rect.right:
            self.x += self.settings.man_speed
            self.image = pygame.image.load("E:/dragon game graphical/images/bmp/gideon-R-1.bmp")
            self.rect = self.image.get_rect()
        elif self.moving_left and paralized == False and self.rect.left > 0:
            self.x -= self.settings.man_speed
            self.image = pygame.image.load("E:/dragon game graphical/images/bmp/gideon-L-1.bmp")
            self.rect = self.image.get_rect()
        elif self.moving_up and paralized == False:
            self.y -= self.settings.man_speed
            self.image = pygame.image.load("E:/dragon game graphical/images/bmp/gideon-U-1.bmp")
            self.rect = self.image.get_rect()
        elif self.moving_down and paralized == False:
            self.y += self.settings.man_speed
            self.image = pygame.image.load("E:/dragon game graphical/images/bmp/gideon-D-1.bmp")
            self.rect = self.image.get_rect()
        elif self.runningRight and self.rect.right < self.screen_rect.right:
            if paralized:
                self.x += self.settings.man_speed
                self.image = pygame.image.load("E:/dragon game graphical/images/bmp/gideon-R-1.bmp")
                self.rect = self.image.get_rect()
            else:
                self.x += self.settings.man_running_speed
                self.image = pygame.image.load("E:/dragon game graphical/images/bmp/gideon-R-1.bmp")
                self.rect = self.image.get_rect()
        elif self.runningLeft and self.rect.left > 0:
            if paralized:
                self.x -= self.settings.man_speed
                self.image = pygame.image.load("E:/dragon game graphical/images/bmp/gideon-L-1.bmp")
                self.rect = self.image.get_rect()
            else:
                self.x -= self.settings.man_running_speed
                self.image = pygame.image.load("E:/dragon game graphical/images/bmp/gideon-L-1.bmp")
                self.rect = self.image.get_rect()
        elif self.runningUp:
            if paralized:
                self.y += self.settings.man_speed
                self.image = pygame.image.load("E:/dragon game graphical/images/bmp/gideon-U-1.bmp")
                self.rect = self.image.get_rect()
            else:
                self.y += self.settings.man_running_speed
                self.image = pygame.image.load("E:/dragon game graphical/images/bmp/gideon-U-1.bmp")
                self.rect = self.image.get_rect()
        elif self.runningDown:
            if paralized:
                self.y += self.settings.man_speed
                self.image = pygame.image.load("E:/dragon game graphical/images/bmp/gideon-D-1.bmp")
                self.rect = self.image.get_rect()
            else:
                self.y += self.settings.man_running_speed
                self.image = pygame.image.load("E:/dragon game graphical/images/bmp/gideon-D-1.bmp")
                self.rect = self.image.get_rect()
        elif self.attack:
            pass
        
        self.rect.x = self.x
        self.rect.y = self.y
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    '''def potion_collide(self, p):
        col = pygame.sprite.collide_rect(self, self.potion1)
        if col == True:
            self.settings.man_health += p'''