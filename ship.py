import pygame

class Ship:
    def __init__(self, ai_game):
       
        """inizializza la nave e imposta la posizione iniziale"""
        self.screen = ai_game.screen # assegno ship alla schermata del gioco 
        self.screen_rect = ai_game.screen.get_rect() # col metodo get_rect accedo all'attributo rect della schermata, poi lo assegno a ship (per posizionarla nel punto giusto della schermata)

        """carica la nave e ne ottiene il rettangolo"""
        self.image = pygame.image.load('images/space_inv_ship2.bmp') # assegno a self.image il risultato di questa funzione, che è una superficie che rappresenta la nave
        self.rect = self.image.get_rect() # qui assegno l'attributo rect grazie al quale posso posizionare la ship

        self.rect.midbottom = self.screen_rect.midbottom # faccio coincidere la posizione iniziale di ship (che voglio in basso al centro) col midbottom del rect della schermata di ai

        self.moving_right = False # flag movimento: all'inizio non si muove

    def update (self):
        if self.moving_right:
            self.rect.x += 1

    def blitme (self):
        """disegna la nave nella posizione corrente"""
        self.screen.blit(self.image, self.rect)


# Ora importo la classe in alien_invasion e ne creo un'istanza.