import pygame

class Settings:
    def __init__(self):
        self.screen_width = 700
        self.screen_height = 600
        self.bg_color = (215, 215, 140)
        self.bg2c = (0, 0, 0)
        self.bg3c = (43, 89, 132)
        
        # gideon's settings
        self.man_speed = 0.5
        self.man_running_speed = 1
        self.man_health = 20

        # orc1's speed settings
        self.orc1_speed = 0.3

        # Monster's speed (not yet used)
        self.monster_speed = 1
        
        # dragon settings
        self.dragon_speed = 1
        self.dragon_flying_speed = 2

    def animate(self, paths=[]):
        for image in paths:
            self.image = pygame.image.load(image)
            self.rect = self.image.get_rect()

            #self.screen = ai_game.screen
            #self.screen.blit(self.image, self.rect)