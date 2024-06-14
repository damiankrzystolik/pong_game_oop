# wg ksiązki na podstawie gry alien invasion
import sys
import pygame
from settings import Settings
from paletka import Paddle
from pilka import Ball
from score import Score
from button111 import Button


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

        self.l_paddle = Paddle(self, 0, 300, 20, 150, 'red')
        self.r_paddle = Paddle(self, 1180, 300, 20, 150, 'blue')
        self.ball = Ball(self)

        self.game_active = False
        self.paused = False
        self.menu_state = 'main'
        self._load_images()
        self._create_buttons()
        self.font = pygame.font.SysFont('Arial', 30)


        self.start_time = pygame.time.get_ticks()
        self.paddle_speed = 4  # Zmień tę wartość, aby utrudnić lub ułatwić grę




    def _load_images(self):
        self.resume_img = pygame.image.load('images/button_resume.png').convert_alpha()
        self.option_img = pygame.image.load('images/button_options.png').convert_alpha()
        self.quit_img = pygame.image.load('images/button_quit.png').convert_alpha()
        self.back_img = pygame.image.load('images/button_back.png').convert_alpha()
        self.settings_img = pygame.image.load('images/settings_btn.png').convert_alpha()
        self.easy_img = pygame.image.load('images/button_easy.png').convert_alpha()
        self.medium_img = pygame.image.load('images/button_medium.png').convert_alpha()
        self.hard_img = pygame.image.load('images/button_hard.png').convert_alpha()
        self.start_img = pygame.image.load('images/start_game.png').convert_alpha()
        self.gameover_img = pygame.image.load('images/game_over.png').convert_alpha()
        self.win_img = pygame.image.load('images/win.png').convert_alpha()

    def _create_buttons(self):
        self.resume_btn = Button((self.settings.screen_width / 2) - self.resume_img.get_width() / 2, 200,
                                 self.resume_img, 1)
        self.option_btn = Button((self.settings.screen_width / 2) - self.option_img.get_width() / 2, 350,
                                 self.option_img, 1)
        self.quit_btn = Button((self.settings.screen_width / 2) - self.quit_img.get_width() / 2, 445,
                               self.quit_img, 1)
        self.back_btn = Button((self.settings.screen_width / 2) - self.back_img.get_width() / 2, 350,
                               self.back_img, 1)
        self.settings_btn = Button((self.settings.screen_width / 2) - self.settings_img.get_width() / 2, 250,
                                   self.settings_img, 1)
        self.easy_btn = Button((self.settings.screen_width * 0.25) - self.easy_img.get_width() / 2, 350,
                               self.easy_img, 1)
        self.medium_btn = Button((self.settings.screen_width * 0.5) - self.medium_img.get_width() / 2, 350,
                                 self.medium_img, 1)
        self.hard_btn = Button((self.settings.screen_width * 0.75) - self.hard_img.get_width() / 2, 350,
                               self.hard_img, 1)
        self.start_btn = Button((self.settings.screen_width / 2) - self.start_img.get_width() / 2, 250,
                               self.start_img, 1)
        self.gameover_btn = Button((self.settings.screen_width / 2) - self.gameover_img.get_width() / 2, 200,
                                self.gameover_img, 1)
        self.win_btn = Button((self.settings.screen_width / 2) - self.win_img.get_width() / 2, 200,
                                self.win_img, 1)

    def run_game(self):
        while True:
            self._check_events()

            if self.game_active:
                self.r_paddle.update()
                score_point = self.ball.update2(self.r_paddle, self.l_paddle)
                self.score(score_point)
                self.l_paddle.update_left_paddle(self.ball.posy, self.paddle_speed)

            self._update_screen()
            self.clock.tick(60)

    def _draw_table(self):
            # Narysuj linie środkową
        for i in range(self.settings.screen_height // 20):
            pygame.draw.line(self.screen, self.settings.color_white,
                             (self.settings.screen_width // 2, i * 20),
                             (self.settings.screen_width // 2, i * 20 + 10))

        # Narysuj linie boczne
        pygame.draw.rect(self.screen, self.settings.color_white,
                         (self.settings.screen_width - self.r_paddle.width, 0, self.settings.screen_width, self.settings.screen_height))
        pygame.draw.rect(self.screen, self.settings.color_white,
                         (0, 0, self.l_paddle.width, self.settings.screen_height))

        # Narysuj linie strefy serwisu
        for i in range(2):
            top_offset = self.settings.screen_height * (i + 1) / 2
            pygame.draw.line(self.screen, self.settings.color_white,
                             (0, top_offset),
                             (self.settings.screen_width / 4, top_offset), 5)
            pygame.draw.line(self.screen, self.settings.color_white,
                             (self.settings.screen_width * 0.75, top_offset),
                             (self.settings.screen_width , top_offset), 5)

        # Narysuj linie końcowe
        pygame.draw.rect(self.screen, self.settings.color_white,
                         (0, 0, self.settings.screen_width, 5))
        pygame.draw.rect(self.screen, self.settings.color_white,
                         (0, self.settings.screen_height - 5, self.settings.screen_width, 5))

        elapsed_time = pygame.time.get_ticks() - self.start_time
        if elapsed_time < 10000:  # Wyświetl tekst przez 10 sekund (10000 ms)
            self._draw_text('Press SPACE to PAUSE', self.settings.screen_width / 2, 20)


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.score_board.prep_score(self.p_points, self.c_points)
        self.score_board.show_score()

        self._draw_table()

        self.l_paddle.draw()
        self.r_paddle.draw()
        self.ball.draw()

        # self._draw_pause_menu()
        self.menu()
        self.win_lose_condition()

        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.game_active:
                        self.paused = True
                        self.game_active = False
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


    def score(self, score_point):
        if score_point == False:
            self.p_points += 1
            self.ball.reset_ball()
        elif score_point == True:
            self.c_points += 1
            self.ball.reset_ball()

    def win_lose_condition(self):
        if self.p_points >= 2:
            self.game_active = False
            if self.win_btn.draw(self.screen):
                self.p_points = 0
                self.c_points = 0
                self.ball.reset_ball()

        if self.c_points >= 1:
            self.game_active = False
            if self.gameover_btn.draw(self.screen):
                self.p_points = 0
                self.c_points = 0
                self.ball.reset_ball()





    # def _draw_pause_menu(self):
    #     if self.paused:
    #         if self.menu_state == 'main':
    #             if self.resume_btn.draw(self.screen):
    #                 self.paused = False
    #                 self.game_active = True
    #             if self.option_btn.draw(self.screen):
    #                 pygame.time.wait(200)
    #                 self.menu_state = 'options'
    #             if self.quit_btn.draw(self.screen):
    #                 exit()
    #         if self.menu_state == 'options':
    #             if self.back_btn.draw(self.screen):
    #                 pygame.time.wait(200)
    #                 self.menu_state = 'main'
    #             if self.settings_btn.draw(self.screen):
    #                 pygame.time.wait(200)
    #                 self.menu_state = 'settings'
    #         if self.menu_state == 'settings':
    #             if self.easy_btn.draw(self.screen):
    #                 self.paddle_speed = 7
    #                 print(self.paddle_speed)
    #                 self.menu_state = 'options'
    #             if self.medium_btn.draw(self.screen):
    #                 pygame.time.wait(200)
    #                 self.paddle_speed = 10
    #                 print(self.paddle_speed)
    #                 self.menu_state = 'options'
    #             if self.hard_btn.draw(self.screen):
    #                 self.paddle_speed = 13
    #                 self.menu_state = 'options'
    #                 print(self.paddle_speed)


    def menu(self):
        if self.game_active == False and self.menu_state == 'main':
            if pygame.mouse.get_pressed()[0] is False:
                self.quit_btn.clicked = False
                if self.option_btn.draw(self.screen):
                    pygame.time.wait(200)
                    self.menu_state = 'options'
                if self.quit_btn.draw(self.screen):
                    exit()

            if self.paused == False:
                if self.start_btn.draw(self.screen):
                    self.game_active = True
            else:
                if self.resume_btn.draw(self.screen):
                    self.game_active = True

        if self.game_active == False and self.menu_state == 'options':
            if self.back_btn.draw(self.screen):
                pygame.time.wait(200)
                self.menu_state = 'main'
            if self.settings_btn.draw(self.screen):
                pygame.time.wait(200)
                self.menu_state = 'settings'

        if self.game_active == False and self.menu_state == 'settings':
            if self.easy_btn.draw(self.screen):
                self.paddle_speed = 7
                print(self.paddle_speed)
                self.menu_state = 'options'
            if self.medium_btn.draw(self.screen):
                pygame.time.wait(200)
                self.paddle_speed = 10
                print(self.paddle_speed)
                self.menu_state = 'options'
            if self.hard_btn.draw(self.screen):
                self.paddle_speed = 13
                self.menu_state = 'options'
                print(self.paddle_speed)


    def _draw_text(self, text, x, y):
        text_surface = self.font.render(text, True, self.settings.color_white)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)



if __name__ == '__main__':
    game = PongGame()
    game.run_game()
