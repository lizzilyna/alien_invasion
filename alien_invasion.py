import sys
import pygame
from settings import Settings # dal modulo creato importiamo le impostazioni 
from ship import Ship

class AlienInvasion:

    def __init__(self):
        """inizializza il gioco e ne crea le risorse"""
        pygame.init() # la funzione pygame.init() inizializza le impostazioni dello sfondo necessarie a Pygame per funzionare
        
        self.clock = pygame.time.Clock() # istanza della classe Clock dal modulo pygame.time: creiamo un clock per accertarci che la frequenza dei fotogrammi coincida con le iterazioni del ciclo principale

        self.settings = Settings() 

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) # impostazioni dello sfondo: assegna una finestra all'attributo self.screen, così è disponibile in tutti i metodi della classe. L'oggetto assegnato a self.screen è detto SURFACE ed è la parte di schermo in cui l'oggetto stesso è visualizzabile. La surface restituita da display.set_mode() è l'intera superficie di gioco

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship (self) # dopo averla importata, creo un'istanza di Ship. La chiamata a Ship richiede un argomento: un'istanza di Alien Invasion

        self.bg_color = (self.settings.bg_color) # imposto il colore di sfondo

    def run_game (self):
        """ciclo principale del gioco"""
        while True:
            
            self._check_events()
            self.ship.update()
            self._update_screen()

            self.clock.tick(60) #  facciamo scattare il clock alla fine del ciclo while; il metodo tick accetta un solo argomento: la frequenza dei fotogrammi di gioco

    def _check_events(self): # metodo helper, con _ all'inizio, refactoring per alleggerire il ciclo principale
        # risponde a eventi di mouse e tastiera
        for event in pygame.event.get(): # la funzione pygame.event.get() la usiamo per accedere agli eventi rilevati da pygame, che restituisce in forma di lista. Qualsiasi evento di tastiera o mouse attiva il ciclo for, detto "ciclo eventi".
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN: # tipo di evento: tasto
                if event.key == pygame.K_RIGHT: # tipo di tasto: destra
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False

    def _update_screen(self): # metodo helper come check_events
        # aggiorna le immagini sulla schermata e passa a quella nuova    
        self.screen.fill(self.bg_color) # ridisegna lo sfondo alla fine di ogni ciclo; il metodo fill accetta un solo argomento: un colore.
        self.ship.blitme() # disegna la nave sullo sfondo 
        pygame.display.flip() # rende visibile la schermata disegnata più recentemente: flip aggiorna la visualizzuazione per mostrare le nuove posizioni



if __name__ == '__main__':
    # crea un'istanza del gioco e la esegue
    ai = AlienInvasion()
    ai.run_game()