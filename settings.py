# wg ksiązki na podstawie gry alien invasion
import pygame


class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 100, 0)
        self.color_white = 'white'
        self.color_black = 'black'
        self.ball_sound_1 = pygame.mixer.Sound('images/serw.mp3')
        self.ball_sound_2 = pygame.mixer.Sound('images/boop.mp3')
        self.win_sound = pygame.mixer.Sound('images/8-bit-win.mp3')
        self.win_sound_2 = pygame.mixer.Sound('images/success-fanfare-trumpets-6185.mp3')
        self.lose_sound = pygame.mixer.Sound('images/8-bit-lose.mp3')
