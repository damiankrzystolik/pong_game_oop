# wg ksiązki na podstawie gry alien invasion
import pygame
from settings import Settings


class Paddle:
    def __init__(self, pongGame, posx, posy, width, height, color):
        self.screen = pongGame.screen  # nie rozumiem jak to działa -
                                        # odniesienie do aktualnego egzemplarza klasy PongGame
        self.settings = Settings()
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.color = color

        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up:
            self.posy -= 15
            if self.posy <= 0:
                self.posy = 0
        if self.moving_down:
            self.posy += 15
            if self.posy + self.height >= self.settings.screen_height:
                self.posy = self.settings.screen_height - self.height

    def update_left_paddle(self, posy_ball, paddle_speed):
        # pomysł z neta

        if posy_ball > self.posy + self.height / 2:
            self.posy += paddle_speed
        if posy_ball < self.posy + self.height / 2:
            self.posy -= paddle_speed

        if self.posy + self.height > self.settings.screen_height:
            self.posy = self.settings.screen_height - self.height
        if self.posy < 0:
            self.posy = 0


    def draw(self):
        self.paddle = pygame.Rect(self.posx, self.posy, self.width, self.height)
        pygame.draw.rect(self.screen, self.color, self.paddle)


