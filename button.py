import pygame.font

class Button:
    '''crea pulsanti'''
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # imposta dimensioni e proprietà
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)           # argomento None indica di usare il valore di font predefinito

        # costruisce l'oggetto rect del pulsante e lo centra
        self.rect = pygame.Rect (0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center          # facciamo coincidere il suo valore di centro a quello della schermata

        self._prep_msg(msg)

    def _prep_msg(self, msg):                               # msg è il testo da renderizzare come immagine
        """renderizza msg come immagine e lo centra nel pulsante"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color) # font.render trasforma il testo in immagine; il booleano è per gli anti alias
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """disegna un pulsante vuoto, poi disegna il messaggio"""
        self.screen.fill(self.button_color, self.rect)              # con fill disegno la porzione rettangolare
        self.screen.blit(self.msg_image, self.msg_image_rect)       # con blit l'immagine del testo