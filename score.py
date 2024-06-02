import pygame.font
import pygame
from settings import Settings

class Score:
    def __init__(self, screen):
        self.screen = screen.screen
        self.settings = Settings()
        self.text_color = ('white')
        self.font = pygame.font.Font('ChakraPetch-Regular.ttf', 250)


    def prep_score(self, p_points, c_points):
        ply_score = f'{str(p_points)}'
        self.p_score_img = self.font.render(ply_score, True, self.text_color, self.settings.bg_color)
        self.p_score_rect = self.p_score_img.get_rect(center=((self.settings.screen_width / 2) - 150,
                                                              self.settings.screen_height / 2))

        podzielnik = ':'
        self.podzielnik = self.font.render(podzielnik, True, self.text_color, self.settings.bg_color)
        self.podzielnik_rect = self.podzielnik.get_rect(center=(self.settings.screen_width / 2,
                                                                (self.settings.screen_height / 2) - 30))

        c_score = f'{str(c_points)}'
        self.score_img = self.font.render(c_score, True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_img.get_rect(center=((self.settings.screen_width / 2) + 150,
                                                          self.settings.screen_height / 2))

    def show_score(self):
        self.screen.blit(self.p_score_img, self.p_score_rect)
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.podzielnik, self.podzielnik_rect)

