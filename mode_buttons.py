import pygame.font
from settings import Settings

class Mode_buttons:
    def __init__(self, game, msg, rect_center):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = Settings()

        self.width, self.height = 150, 50
        self.button_color = (253, 6, 185)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont (None, 34)

        self.rect = pygame.Rect (0, 0, self.width, self.height)
        self.rect.center = rect_center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button (self):
        self.screen.fill(self.button_color, self.rect) # --> Disegna la figura creata da noi
        self.screen.blit(self.msg_image, self.msg_image_rect)  # --> Disegna un'immagine

    def hide_button (self):
        self.rect = pygame.Rect (0, 0, 0, 0)
        self.msg_image = pygame.Surface ((0,0))
        self.msg_image_rect = pygame.Rect(0, 0, 0, 0) 

