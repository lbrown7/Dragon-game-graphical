import sys

import pygame

from Gideon import Gideon


class shop:
    """a simple class to controll the tree"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("E:/dragon game graphical/images/bmp/shop entrance.bmp")
        self.rect = self.image.get_rect()
        
        self.rect.midright = self.screen_rect.midright

        self.gideon = Gideon(self)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def buy(self, things, ppt):
        if len(things) != len(ppt):
            print('error')
            quit()
            exit()
            sys.exit()
            pygame.quit()
        elif len(things) == len(ppt):
            for thing in things:
                for p in ppt:
                    pass
