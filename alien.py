import pygame
from pygame.sprite import Sprite

class Alien (Sprite):
    """la classe che rappresenta un singolo alieno"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        """avvia ogni nuovo alieno in alto a sx della schermata"""
        self.rect.x = self.rect.width # posizione a sinistra: uguale alla larghezza dell'alieno/2
        self.rect.y = self.rect.width/2 # posizione in alto: uguale all'altezza dell'alieno/2

        """memorizza la posizione orizzontale precisa perché rect usa solo int"""
        self.x = float(self.rect.x)
