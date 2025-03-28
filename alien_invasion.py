import sys
from time import sleep
import pygame
from settings import Settings 
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from mode_buttons import Mode_buttons
from scoreboard import Scoreboard

class AlienInvasion:

    def __init__(self):
        """inizializza il gioco e ne crea le risorse"""
        pygame.init() # la funzione pygame.init() inizializza le impostazioni dello sfondo necessarie a Pygame per funzionare
        
        self.clock = pygame.time.Clock() # istanza della classe Clock dal modulo pygame.time: creiamo un clock per accertarci che la frequenza dei fotogrammi coincida con le iterazioni del ciclo principale

        self.settings = Settings() 

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) # impostazioni dello sfondo: assegna una finestra all'attributo self.screen, così è disponibile in tutti i metodi della classe. L'oggetto assegnato a self.screen è detto SURFACE ed è la parte di schermo in cui l'oggetto stesso è visualizzabile. La surface restituita da display.set_mode() è l'intera superficie di gioco
        self.screen_rect = self.screen.get_rect()
        # self.screen = pygame.display.set_mode ((0,0), pygame.FULLSCREEN) -- se lo vogliamo a tutto schermo

        pygame.display.set_caption("Alien Invasion")

        self.stats = GameStats (self) # istanza per le statistiche di gioco. Richiede AI_game come argomento

        self.sb = Scoreboard (self)

        self.ship = Ship (self) # dopo averla importata, creo un'istanza di Ship. La chiamata a Ship richiede un argomento: un'istanza di Alien Invasion
        
        self.bullets = pygame.sprite.Group() # il gruppo di proiettili sarà un'istanza della classe pygame.sprite.Group, che si comporta +- come una lista

        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.bg_color = (self.settings.bg_color) # imposto il colore di sfondo

        self.game_active = False # flag: quando parte il gioco è inattivo

        self.play_button = Button (self, "Play")    # crea un'istanza del Button, ma lo disegniamo in update_screen chiamando il suo metodo draW_button()

        self.easy_button = Mode_buttons (self, 'Hard', (450, 560))
        self.medium_button = Mode_buttons (self, 'Very Hard', (650, 560))
        self.hard_button = Mode_buttons (self, 'Asperger', (850, 560))


    def run_game (self):
        """ciclo principale del gioco"""
        while True:
            
            self._check_events()

            if self.game_active:
                self.ship.update()          # chiamata per aggiornare la posizione della nave
                self._update_bullets()      # dei proiettili
                self._update_aliens()       # degli alieni
           
            self._update_screen()
            
            self.clock.tick(60) #  facciamo scattare il clock alla fine del ciclo while; il metodo tick accetta un solo argomento: la frequenza dei fotogrammi di gioco

    def _check_events(self): # metodo helper, con _ all'inizio, refactoring per alleggerire il ciclo principale
        # risponde a eventi di mouse e tastiera
        for event in pygame.event.get(): # la funzione pygame.event.get() la usiamo per accedere agli eventi rilevati da pygame, che restituisce in forma di lista. Qualsiasi evento di tastiera o mouse attiva il ciclo for, detto "ciclo eventi".
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN: # tipo di evento: tasto (premuto)
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos() # restituisce una tupla con le coord x e y del puntatore
                self._check_play_button(mouse_pos)




    def _check_difficulty_button(self, mouse_pos):
        easy_clicked = self.easy_button.rect.collidepoint(mouse_pos)
        medium_clicked = self.medium_button.rect.collidepoint(mouse_pos)
        hard_clicked = self.hard_button.rect.collidepoint(mouse_pos)
        
        if easy_clicked and not self.game_active:
            self.settings.initialize_dynamic_settings(1.4, 2.4, 0.9)
        if medium_clicked and not self.game_active:
            self.settings.initialize_dynamic_settings(1.5, 2.5, 1)
        if hard_clicked and not self.game_active:
            self.settings.initialize_dynamic_settings(2, 3, 2)


    def _check_play_button(self, mouse_pos):
        """inizia una partita quando si preme play"""
        
        self._check_difficulty_button(mouse_pos)
        self.easy_button.hide_button()
        self.medium_button.hide_button()
        self.hard_button.hide_button()

        button_clicked = self.play_button.rect.collidepoint(mouse_pos) # un flag, True o False
        if button_clicked and not self.game_active:     # disattivo il pulsante play per evitare che la sua area resti attiva anche in sua assenza (nn ho capito) Ora forse sì, la partita si riavvia solo se clicchi play e il gioco è non attivo (prima anche se era attivo)
           #self.settings.initialize_dynamic_settings()
           self._play_game()

    def _play_game(self):           # refactoring fatto da me, es. 14.1
        self.stats.reset_stats()    # reimposta le statistiche del gioco
        self.sb.prep_score()        # nuova immagine del punteggio aggiornato; successiva al reset quindi a 0
        self.sb.prep_level()        # nuova immagine del livello
        self.sb.prep_ships()        # numero navi
        self.game_active = True
        self.bullets.empty()        # svuota 
        self.aliens.empty()         # svuota
        self._create_fleet()        # crea flotta
        self.ship.center_ship()     # centra la nave
        pygame.mouse.set_visible(False) # nasconde il puntatore del mouse


    def _check_keydown_events(self, event): # refactoring di check_events da cui trasferisco gli eventi legati a tasto premuto
        if event.key == pygame.K_RIGHT: # tipo di tasto: destra
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit() # abbiamo aggiunto un tasto di uscita rapida
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self._play_game()


    def _check_keyup_events(self, event): # idem per tasto su
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False        

    def _fire_bullet(self):
        """crea un nuovo proiettile e lo aggiunge al gruppo"""
        if len(self.bullets) < self.settings.bullets_allowed:   
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet) # metodo add è l'append di pygame

    def _update_bullets(self):
        self.bullets.update() # chiama automaticamente bullet.update() per tutti i proiettili del gruppo
        for bullet in self.bullets.copy(): # il metodo copy ci permette di modificare la lista originale nel ciclo for   
            if bullet.rect.bottom <= 0: # quando il bottom del rect del proiettile è 0 vuol dire che sta al limite superiore dello schermo
                self.bullets.remove(bullet) # ... quindi deve sparire
            # print (len(self.bullets)) qui solo per controllare che il remove funzionasse

            self._check_bullet_alien_collisions()


    def _check_bullet_alien_collisions(self):      
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, False, True) # controlla se i proiettili colpiscono gli alieni, e nel caso elimina gli uni e gli altri:
        """ogni volta che i rect di un alieno e di un proiettile si sovrappongono groupcollide() aggiunge una coppia chiave (proiettile) - valore (lista degli alieni colpiti) al dizionario collisions che restituisce; il primo True elimina proiettile, il secondo l'alieno"""
        if collisions:
            for aliens in collisions.values():                                  # collision.values = lista di alieni
                self.stats.score += self.settings.alien_points * len(aliens)    # aggiunge il punteggio dell'alieno abbattuto
            self.sb.prep_score()                                                # crea immagine per il nuovo punteggio
            self.sb.prep_level()
            self.sb.check_high_score()
            
        if not self.aliens: # se non ce ne sono più (flotta distrutta), devo ripopolare
            self.bullets.empty() # .empty() elimina da un gruppo tutti gli sprite rimasti
            self._create_fleet() # creo nuova flotta
            self.settings.increase_speed() # aumento difficoltà
            self.stats.level += 1 # incremento il livello nelle stats
            self.sb.prep_level() # lo disegno in cima

    def _update_aliens(self):
        """controlla se la flotta è al bordo, poi aggiorna la posizione"""
        self._check_fleet_edges()
        self.aliens.update()

        # cerca collisioni alieni-nave
        if pygame.sprite.spritecollideany (self.ship, self.aliens): # la funzione spritecollideany accetta due argomenti: uno sprite e un gruppo; se uno solo dei componenti del gruppo tocca lo sprite l'if è soddisfatto
            self._ship_hit()
        self._check_aliens_bottom()


    def _create_fleet(self):
        alien = Alien(self)  # creo istanza di Alien
        alien_width, alien_height = alien.rect.size # all'inizio c'era solo x e width, ora che nidifico aggiungo la y -- e per la misura uso l'attributo size di rect, cioè una tupla che contiene larghezza e altezza
        current_x, current_y = alien_width, alien_height # current_x e current_y sono le posizioni orizzontale e verticale del primo alieno della flotta, e inizialmente la impostiamo alla larghezza e altezza dell'alieno stesso per farlo staccare dai bordi sx e superiore della schermata

        while current_y < (self.settings.screen_height - 3 * alien_height): # racchiudo il while dell'asse x in questo dell'y, che controlla il numero di righe nella schermata
            while current_x < (self.settings.screen_width - 2 * alien_width): # finché current_x (che è pari alla larghezza dell'alieno) è inferiore alla larghezza dello schermo cui sottraggo 2 larghezze aliene -- finché c'è spazio + 2 alieni di margine
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width # aggiungi a current_x 2 larghezze aliene
            # Riempita una riga: reimposta il valore x e incrementa y
            current_x = alien_width # fa ripartire il while x?
            current_y += 2 * alien_height


    def _create_alien(self, x_position, y_position): # helper per fleet, vuole come parametri la posizione
            new_alien = Alien(self) # crea istanza
            new_alien.x = x_position # distanza
            new_alien.y = y_position 
            new_alien.rect.x = x_position # rect
            new_alien.rect.y = y_position
            self.aliens.add(new_alien) # aggiungila al gruppo

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()  # se uno è sul bordo cambiamo direzione a tutta la flotta
                break                           # e usciamo dal ciclo
            
    def _change_fleet_direction(self):
        """fa scendere e cambiare direzione a tutta la flotta"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed  # li facciamo scendere tutti
        self.settings.fleet_direction *= -1                 # poi cambiamo il valore di fleet_direction moltiplicandolo per -1 (da dx a sx e viceversa)

    def _ship_hit(self):
        """risponde alla collisione di un alieno con la nave"""
        # decrementa il numero di navi rimaste
        if self.stats.ships_left >0:    # se ce n'è ancora qualcuna
            self.stats.ships_left -=1   # togline una
            self.sb.prep_ships()

            # fa sparire proiettili e alieni rimasti
            self.bullets.empty()
            self.aliens.empty()

            # crea una nuova flotta e centra la nave
            self._create_fleet()
            self.ship.center_ship()

            # pausa
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)  # ricompare il puntatore


    def _check_aliens_bottom(self):
        """controlla se un alieno ha toccato il fondo della schermata"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # come quando la nave viene colpita
                self._ship_hit()
                break


    def _update_screen(self): # metodo helper come check_events
        # aggiorna le immagini sulla schermata e passa a quella nuova    
        self.screen.fill(self.bg_color) # ridisegna lo sfondo alla fine di ogni ciclo; il metodo fill accetta un solo argomento: un colore.
        for bullet in self.bullets.sprites(): # il metodo bullets.sprites() restituisce una lista di tutti gli sprite del gruppo bullets
            bullet.draw_bullet()
        self.ship.blitme() # disegna la nave sullo sfondo
        self.aliens.draw(self.screen) # il metodo draw vuole un argomento: la superficie su cui disegnare nella posizione definita dal suo attributo rect.
        self.sb.show_score()
        if not self.game_active:
            self.easy_button.draw_button()
            self.medium_button.draw_button()
            self.hard_button.draw_button()
            self.play_button.draw_button() # dopo tutti gli altri così appare in primo piano
        pygame.display.flip() # rende visibile la schermata disegnata più recentemente: flip aggiorna la visualizzuazione per mostrare le nuove posizioni



if __name__ == '__main__':
    # crea un'istanza del gioco e la esegue
    ai = AlienInvasion()
    ai.run_game()