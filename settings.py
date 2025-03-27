class Settings:
    """inizializza le impostazioni statiche del gioco"""

    def __init__(self):
        # Screen settings -->
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (230, 230, 230)

        # Ship settings -->
        self.ship_limit = 3

        # Bullet settings -->
        self.bullet_width = 400 #3000 se voglio testare facendo veloce
        self.bullet_height = 15
        self.bullet_color = (255, 0, 255)
        self.bullets_allowed = 30 # limitare il numero di proiettili sulla schermata

        # Alien settings -->
        self.fleet_drop_speed = 10 # velocità alla quale la flotta scende quando un alieno tocca il bordo dx o sx

        # Quanto accelera il gioco -->
        self.speedup_scale = 1.1
        
        # Aumenta il valore degli alieni -->
        self.score_scale = 1.5

        # Chiamiamo il metodo che inizializza le impostazioni che cambiano con l'aumentare della difficoltà
        self.initialize_dynamic_settings(0, 0, 0) 


    def initialize_dynamic_settings(self, ship_speed, bullet_speed, alien_speed):
        """lo usiamo all'avvio di partita"""
        self.ship_speed = ship_speed
        self.bullet_speed = bullet_speed
        self.alien_speed = alien_speed
        
        self.alien_points = 50

        # fleet_direction 1 rappresenta destra, -1 sinistra
        self.fleet_direction = 1

    def increase_speed(self):
        """"aumenta le impostazioni di velocità - lo usiamo all'abbattimento dell'ultimo alieno della flotta"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        