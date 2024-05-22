import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
SCREEN_SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
run = True

# wymiary i pozycja paletek
PADDLE_HEIGHT = 100
PADDLE_WIDHT = 10
x_right_paddle = WIDTH - PADDLE_WIDHT
y_right_paddle = HEIGHT / 2 - PADDLE_HEIGHT / 2
x_left_paddle = 0
y_left_paddle = HEIGHT / 2 - PADDLE_HEIGHT / 2

# paletki
left_paddle = pygame.Rect(x_left_paddle, y_left_paddle, PADDLE_WIDHT, PADDLE_HEIGHT)
right_paddle = pygame.Rect(x_right_paddle, y_right_paddle, PADDLE_WIDHT, PADDLE_HEIGHT)

# piłka
R_BALL = 10
x_ball = WIDTH / 2
y_ball = random.randint(R_BALL, HEIGHT - R_BALL)
# Prędkość poruszania się piłki
speed = -4
ball_speed_x = speed
ball_speed_y = speed

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN: # event dla naciskania strzałek up i down
            if event.key == pygame.K_UP:
                y_right_paddle = y_right_paddle - 40
            if event.key == pygame.K_DOWN:
                y_right_paddle = y_right_paddle + 40
        elif event.type == pygame.MOUSEMOTION:
            y_right_paddle = event.pos[1]

    screen.fill("black")

    # Aktualizacja pozycji piłki
    x_ball += ball_speed_x
    y_ball += ball_speed_y

    # Odbijanie piłki od krawędzi ekranu
    if y_ball - R_BALL <= 0 or y_ball + R_BALL >= HEIGHT:
        ball_speed_y = -ball_speed_y
    if x_ball + R_BALL >= WIDTH - PADDLE_WIDHT:
        if y_ball >= y_right_paddle and y_ball <= y_right_paddle + PADDLE_HEIGHT:
            ball_speed_x = -ball_speed_x
    if x_ball + R_BALL >= WIDTH:
        ball_speed_x = -ball_speed_x
        print('punkt')
    if x_ball - R_BALL <= PADDLE_WIDHT:
        ball_speed_x = -ball_speed_x


    y_left_paddle = y_ball - PADDLE_HEIGHT / 2

    left_paddle = pygame.Rect(x_left_paddle, y_left_paddle, PADDLE_WIDHT, PADDLE_HEIGHT)
    right_paddle = pygame.Rect(x_right_paddle, y_right_paddle, PADDLE_WIDHT, PADDLE_HEIGHT)

    pygame.draw.rect(screen, (0, 255, 0), left_paddle)
    pygame.draw.rect(screen, (0, 255, 0), right_paddle)
    pygame.draw.circle(screen, (255, 255, 255), (x_ball, y_ball), R_BALL)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()