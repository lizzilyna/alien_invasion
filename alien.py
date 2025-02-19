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
        self.y = float(self.rect.y)

    def check_edges(self):
        """restituisce True se un alieno è al bordo della finestra"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0) # Questo è un test condizionale messo in forma diversa dal blocco if, e restituisce True se l'alieno è a su uno dei due bordi; l'alieno è al bordo dx se l'attributo right suo rect è >= all'attributo right della schermata, al bordo sx se l'attributo left del suo rect è <= 0.

    def update(self):
        """sposta l'alieno a destra o a sinistra"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

