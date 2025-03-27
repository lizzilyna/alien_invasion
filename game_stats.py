class GameStats:
    """tiene traccia delle statistiche del gioco"""
    
    def __init__ (self, ai_game):
        """inizializza le statistiche"""
        self.settings = ai_game.settings
        self.high_score = 0 # non va mai reimpostato perciò lo inizializziamo qua anziché in reset_stats
        self.reset_stats()

    def reset_stats(self):
        """inizializza le statistiche che possono cambiare durante il gioco"""
        self.ships_left = self.settings.ship_limit # all'inizio del gioco il numero di navi è quello stabilito nei settings
        self.score = 0
        self.level = 1