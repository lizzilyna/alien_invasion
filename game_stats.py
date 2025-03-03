class GameStats:
    """tiene traccia delle statistiche del gioco"""
    
    def __init__ (self, ai_game):
        """inizializza le statistiche"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """inizializza lw statistiche che possono cambiare durante il gioco"""
        self.ships_left = self.settings.ship_limit