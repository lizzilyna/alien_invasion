import pygame.font

class Mode_buttons:
    def __init__(self, game, msg):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 100, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont (None, 38)

        self.rect = pygame.Rect (0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.topleft

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button (self):
        self.screen.fill(self.button_color) # --> Disegna la figura creata da noi
        self.screen.blit(self.msg_image, self.msg_image.rect)  # --> Disegna un'immagine