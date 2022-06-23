import pygame

class tree:
    """a simple class to controll the tree"""

    def __init__(self, ai_game, a='', x=0, y=0):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("E:/dragon game graphical/images/bmp/bush.bmp")
        self.rect = self.image.get_rect()
        
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

    def blitme(self):
        self.screen.blit(self.image, self.rect)       