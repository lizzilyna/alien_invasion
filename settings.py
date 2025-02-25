class Settings:
    """contiene tutte le impostazioni del gioco"""

    def __init__(self):
        # Screen settings -->
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.bullet_width = 3000 #3000 sw voglio testare facendo veloce
        self.bullet_height = 15
        self.bullet_color = (255, 0, 255)
        self.bullets_allowed = 30 # limitare il numero di proiettili sulla schermata
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10 # velocità alla quale la flotta scende quando un alieno tocca il bordo dx o sx

        # fleet_direction 1 rappresenta destra, -1 sinistra
        self.fleet_direction = 1