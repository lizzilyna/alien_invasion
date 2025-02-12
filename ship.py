import pygame

class Ship:
    def __init__(self, ai_game):
       
        """inizializza la nave e imposta la posizione iniziale"""
        self.screen = ai_game.screen # assegno ship alla schermata del gioco
        self.settings = ai_game.settings 
        self.screen_rect = ai_game.screen.get_rect() # col metodo get_rect accedo all'attributo rect della schermata, poi lo assegno a ship (per posizionarla nel punto giusto della schermata)

        """carica la nave e ne ottiene il rettangolo"""
        self.image = pygame.image.load('images/space_inv_ship2.bmp') # assegno a self.image il risultato di questa funzione, che è una superficie che rappresenta la nave
        self.rect = self.image.get_rect() # qui assegno l'attributo rect grazie al quale posso posizionare la ship

        self.rect.midbottom = self.screen_rect.midbottom # faccio coincidere la posizione iniziale di ship (che voglio in basso al centro) col midbottom del rect della schermata di ai

        self.x = float(self.rect.x) # funzione float per convertire self.rect.x in valore a virgola mobile

        self.moving_right = False # flag movimento: all'inizio non si muove
        self.moving_left = False

    def update (self):
        if self.moving_right and self.rect.right < self.screen_rect.right: # e se la mia posizione a dx è < della posizione a dx della schermata?? (sì: libro: self.rect.right == coordinata x del bordo dx della nave; self.screen_rect.right == bordo dx della schermata)
            self.x += self.settings.ship_speed # è a self.x, che non è un rect, che assegno la ship_speed che è un float
        if self.moving_left and self.rect.left > 0: # perché la sx massima della schermata è 0????? (sì: libro: se il lato sinistro della nave è > 0 la nave non ha raggiunto il bordo sinistro della schermata)
            self.x -= self.settings.ship_speed
        
        self.rect.x = self.x # la posizione finale della nave coincide con self.x

    def blitme (self):
        """disegna la nave nella posizione corrente"""
        self.screen.blit(self.image, self.rect) # cosa, dove


# Ora importo la classe in alien_invasion e ne creo un'istanza.