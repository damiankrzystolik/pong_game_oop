import pygame
import random
from settings import Settings


class Ball:
    def __init__(self, ponggame):
        self.settings = Settings()
        self.screen = ponggame.screen
        self.r = 10
        self.posx = (self.settings.screen_width / 2) - self.r
        self.posy = random.randint(self.r, self.settings.screen_height - self.r)
        self.color = self.settings.color_black
        self.speed = 7
        self.ball_speed_x = self.speed
        self.ball_speed_y = self.speed

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.posx, self.posy), self.r)

    def update(self, right_paddle, left_paddle):
        self.posx += self.ball_speed_x
        self.posy += self.ball_speed_y

        if self.posx - self.r <= 0:
            self.ball_speed_x = 0
            self.ball_speed_y = 0
            return False

        if self.posx + self.r >= self.settings.screen_width:
            self.ball_speed_x = 0
            self.ball_speed_y = 0
            return True

        elif self.posy - self.r <= 0 or self.posy + self.r >= self.settings.screen_height:
            self.ball_speed_y = -self.ball_speed_y
            pygame.mixer.Sound.play(self.settings.ball_sound_2)

        elif self.posx + self.r >= self.settings.screen_width - right_paddle.width:
            if self.posy >= right_paddle.posy and self.posy <= right_paddle.posy + right_paddle.height:
                hit_offset = ((self.posy - right_paddle.posy) / right_paddle.height)
                i = abs((hit_offset - 0.5) * 2) + 1

                if hit_offset >= 0 and hit_offset < 0.1:
                    pygame.mixer.Sound.play(self.settings.ball_sound_1)
                    if self.ball_speed_y < 0:
                        self.ball_speed_y = self.ball_speed_y * i
                        self.ball_speed_x = -self.ball_speed_x * i
                    else:
                        self.ball_speed_y = -self.speed * i
                        self.ball_speed_x = -self.speed * i

                elif hit_offset >= 0.1 and hit_offset < 0.2:
                    pygame.mixer.Sound.play(self.settings.ball_sound_1)
                    self.ball_speed_x = -self.ball_speed_x * i
                    if self.ball_speed_y < 0:
                        self.ball_speed_y = -(self.speed * i)
                    else:
                        self.ball_speed_y = (self.speed * i)

                elif hit_offset >= 0.2 and hit_offset < 0.35:
                    pygame.mixer.Sound.play(self.settings.ball_sound_1)
                    self.ball_speed_x = -self.ball_speed_x * i
                    if self.ball_speed_y < 0:
                        self.ball_speed_y = -(self.speed * i)
                    else:
                        self.ball_speed_y = (self.speed * i)

                elif hit_offset >= 0.35 and hit_offset < 0.65:
                    pygame.mixer.Sound.play(self.settings.ball_sound_1)
                    self.ball_speed_x = self.ball_speed_x * (0.2 - i)
                    if self.ball_speed_y < 0:
                        self.ball_speed_y = (self.speed * (0.1 - i))
                    else:
                        self.ball_speed_y = -(self.speed * (0.1 - i))

                elif hit_offset >= 0.65 and hit_offset < 0.8:
                    pygame.mixer.Sound.play(self.settings.ball_sound_1)
                    self.ball_speed_x = -self.ball_speed_x * i
                    if self.ball_speed_y < 0:
                        self.ball_speed_y = -(self.speed * i)
                    else:
                        self.ball_speed_y = (self.speed * i)

                elif hit_offset >= 0.8 and hit_offset < 0.9:
                    pygame.mixer.Sound.play(self.settings.ball_sound_1)
                    self.ball_speed_x = -self.ball_speed_x * i
                    if self.ball_speed_y < 0:
                        self.ball_speed_y = -(self.speed * i)
                    else:
                        self.ball_speed_y = (self.speed * i)

                elif hit_offset >= 0.9 and hit_offset <= 1:
                    pygame.mixer.Sound.play(self.settings.ball_sound_1)
                    if self.ball_speed_y < 0:
                        self.ball_speed_y = -self.speed * i
                        self.ball_speed_x = -self.speed * i
                    else:
                        self.ball_speed_y = self.ball_speed_y * i
                        self.ball_speed_x = -self.ball_speed_x * i

        elif self.posx - self.r < left_paddle.width:
            if self.posy >= left_paddle.posy and self.posy <= left_paddle.posy + left_paddle.height:
                self.ball_speed_x = -self.ball_speed_x
                pygame.mixer.Sound.play(self.settings.ball_sound_1)

        if abs(self.ball_speed_x) < 5:  # żeby piłeczka anie zwalniała za bardzo
            if self.ball_speed_x < 0:
                self.ball_speed_x = -5
            else:
                self.ball_speed_x = 5
            print(f'111 {self.ball_speed_x}')

    def reset_ball(self):
        self.posx = (self.settings.screen_width / 2) - self.r
        self.posy = random.randint(self.r, self.settings.screen_height - self.r)
        self.ball_speed_y = self.speed
        self.ball_speed_x = self.speed
        pygame.time.delay(500)
