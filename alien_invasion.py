import sys
import pygame

class AlienInvasion:

    def __init__(self):
        """inizializza il gioco e ne crea le risorse"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800)) # impostazioni dello sfondo: assegna una finestra all'attributo self.screen, così è disponibile in tutti i metodi della classe. L'oggetto assegnato a self.screen è detto SURFACE ed è la parte di schermo in cui l'oggetto stesso è visualizzabile. La surface restituita da display.set_mode() è l'intera superficie di gioco
        pygame.display.set_caption("Alien Invasion")

    def run_game (self):
        """ciclo principale del gioco"""
        while True:
            # attende eventi di mouse e tastiera
            for event in pygame.event.get(): # la funzione pygame.event.get() la usiamo per accedere agli eventi rilevati da pygame, che restituisce in forma di lista. Qualsiasi evento di tastiera o mouse attiva il ciclo for, detto "ciclo eventi".
                if event.type == pygame.QUIT:
                    sys.exit()

            # rende visibile la schermata disegnata più recentemente: flip aggiorna la visualizzuazione per mostrare le nuove posizioni
            pygame.display.flip()

if __name__ == '__main__':
    # crea un'istanza del gioco e la esegue
    ai = AlienInvasion()
    ai.run_game()