class Settings:
    """contiene tutte le impostazioni del gioco"""

    def __init__(self):
        # Screen settings -->
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 255)