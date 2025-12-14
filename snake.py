import pygame
import random

# Initialize Pygame
pygame.init()

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
purple = (160, 32, 240)

# Display dimensions
dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('BlackMamba Basic Game')

clock = pygame.time.Clock()

snake_block = 20

# Fonts
score_font = pygame.font.SysFont("comicsansms", 35)
message_font = pygame.font.SysFont("comicsansms", 25)


def your_score(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = message_font.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    # Initial snake position
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Initialize snake speed inside the function
    snake_speed = 15

    # Initial food position
    foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0

    # Power-up
    powerup_active = False
    powerupx = 0
    powerupy = 0

    score = 0

    while not game_over:

        while game_close:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            your_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        # Check wall collisions
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)

        # Draw food
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        # Randomly activate power-up
        if not powerup_active and random.randint(1, 50) == 25:
            powerup_active = True
            powerupx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
            powerupy = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0

        if powerup_active:
            pygame.draw.rect(dis, purple, [powerupx, powerupy, snake_block, snake_block])

        # Snake mechanics
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        your_score(score)

        pygame.display.update()

        # Check food collision
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
            length_of_snake += 1
            score += 10
            snake_speed += 0.5

        # Check power-up collision
        if powerup_active and x1 == powerupx and y1 == powerupy:
            length_of_snake += 2
            score += 30
            powerup_active = False

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
