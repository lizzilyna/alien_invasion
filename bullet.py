import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        """crea un oggetto proiettile nella posizione corrente della nave"""
        super().__init__() # eredita da Sprite
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        """crea il rect del bullet a (0,0) e imposta la posizione corretta"""
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)# il proiettile non si basa su un'immagine, dobbiamo costruirlo da 0 con la classe Rect che chiede le coordinate x e y dell'angolo superiore sx del rect, poi le misure. Lo mettiamo su 0, 0 ma poi la posizione (che dipende da quella della navicella) cambierà alla riga successiva.
        self.rect.midtop = ai_game.ship.rect.midtop # facciamo coincidere il suo attributo midtop con l'attributo midtop della ship

        """memorizza la posizione del bullet come float"""
        self.y = float(self.rect.y)

    def update (self):
        """fa salire il bullet nella schermata"""
        self.y -= self.settings.bullet_speed # aggiorna la posizione del bullet; va verso l'alto quindi il valore di y diminuisce
        self.rect.y = self.y # aggiorna la posizione del rect

    def draw_bullet (self):
        """disegna il bullet sulla schermata"""
        pygame.draw.rect (self.screen, self.color, self.rect) # la funzione draw.rect riempie la parte di schermo definita dal rect del bullet col colore del bullet; parametri: superficie, colore e oggetto pygame Rect.


