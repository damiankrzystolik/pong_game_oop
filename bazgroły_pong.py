# wg ksiązki na podstawie gry alien invasion
import sys
import pygame
from settings import Settings
from paletka import Paddle
from pilka import Ball
from score import Score
from button import Button


class PongGame:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Pong - Gra by DK')

        self.p_points = 0
        self.c_points = 0
        self.score_board = Score(self)

        self.l_paddle = Paddle(self, 0, 300, 20, 100, 'red')
        self.r_paddle = Paddle(self, 1180, 300, 20, 150, 'blue')
        self.ball = Ball(self)
        self.game_active = False
        self.pley_button = Button(self, 'Gra')
    def run_game(self):
        while True:
            self._check_events()
            if self.game_active:
                self.ball.color = 'black'

                self.r_paddle.update()

                score_point = self.ball.update2(self.r_paddle, self.l_paddle)
                self.score(score_point)

                self.l_paddle.update_left_paddle(self.ball.posy)

            self._update_screen()
            self.clock.tick(90)


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        self.score_board.prep_score(self.p_points, self.c_points)
        self.score_board.show_score()

        for i in range(self.settings.screen_height // 20):
            pygame.draw.line(self.screen,
                             'white',
                             (self.settings.screen_width // 2, i * 20),
                             (self.settings.screen_width // 2, i * 20 + 10))
            pygame.draw.line(self.screen,
                             'white',
                             (self.settings.screen_width - self.r_paddle.width, i * 20),
                             (self.settings.screen_width - self.r_paddle.width, i * 20 + 10))
            pygame.draw.line(self.screen,
                             'white',
                             (-1 + self.l_paddle.width, i * 20),
                             (-1 + self.l_paddle.width, i * 20 + 10))



        self.l_paddle.draw()
        self.r_paddle.draw()
        self.ball.draw()

        if not self.game_active:
            self.pley_button.draw_button()

        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if self.game_active:
                if event.type == pygame.KEYDOWN:  # event dla naciskania strzałek up i down
                    if event.key == pygame.K_UP:
                        self.r_paddle.moving_up = True
                    elif event.key == pygame.K_DOWN:
                        self.r_paddle.moving_down = True
                    elif event.key == pygame.K_ESCAPE:
                        sys.exit()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.r_paddle.moving_up = False
                    elif event.key == pygame.K_DOWN:
                        self.r_paddle.moving_down = False

                elif event.type == pygame.MOUSEMOTION:
                    self.r_paddle.posy = event.pos[1]
                    if self.r_paddle.posy >= self.settings.screen_height - self.r_paddle.height:
                        self.r_paddle.posy = self.settings.screen_height - self.r_paddle.height
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        if self.pley_button.rect.collidepoint(mouse_pos):
            self.game_active = True


    def score(self, score_point):
        if score_point == False:
            self.p_points += 1
            self.ball.reset_ball()


        elif score_point == True:
            self.c_points += 1
            self.ball.reset_ball()



if __name__ == '__main__':
    game = PongGame()
    game.run_game()
