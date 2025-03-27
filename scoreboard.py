import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    """Comunica info sul punteggio"""

    def __init__(self, game):
        """Inizializza gli attributi dei segnapunti"""
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        # impostazioni dei font per il segnapunti
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont (None, 48) # istanza di un oggetto font

        # prepara l'immagine iniziale al punteggio
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Trasforma il punteggio (testo) in un'immagine renderizzata"""
        rounded_score = round(self.stats.score, -1) # nato per arrotondare i decimali, col valore negativo round arrotonda alle più vicine decine, centinaia, migliaia
        score_str = f"{rounded_score:,}"    # trasformiamo il valore numerico di statsscore in una stringa; ":," = specificatore di formato [1,000]
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)   # la passiamo a render

        #visualizza il punteggio in alto a dx
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20 #così è sempre allineato a 20 px dal lato dx
        self.score_rect.top = 20

    def prep_high_score(self):
        """Trasforma il record in immagine"""
        high_score = round (self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render (high_score_str, True, self.text_color, self.settings.bg_color)

        # Centra il record in cima alla schermata
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Trasforma il livello in immagine"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right -20
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """mostra la navi rimaste"""
        self.ships = Group()                                    # creo un gruppo vuoto che conterrà le istanze della nave
        for ship_number in range(self.stats.ships_left):        # il ciclo itera una volta per ogni nave rimasta (inizialmente 3)
            ship = Ship (self.game)                             # per ognuna crea una nuova nave
            ship.rect.x = 10 + ship_number * ship.rect.width    # impostiamo il valore della coordinata x in modo che le navi sianp vicine
            ship.rect.y = 10
            self.ships.add(ship)

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:              # chiamato ogni volta che un alieno viene colpito
            self.stats.high_score = self.stats.score
            self.prep_high_score()


    def show_score(self):
        """Disegna sullo schermo punti, livelli e navi"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)


