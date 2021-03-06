import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
aqua = (0, 255, 255)
                       
dis_width = 1280
dis_height = 720

dis = pygame.display.set_mode((dis_width, dis_height))#Makes the display screen
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_block = 20
food_block = 20
snake_speed = 10

font_style = pygame.font.SysFont("calibri", 35)
score_font = pygame.font.SysFont("calibri", 40)


def Your_score(score):#displays the score
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):#draws the snake
    for x in snake_list:
        pygame.draw.rect(dis, aqua, [x[0], x[1], snake_block, snake_block])


def message(msg, color):#displays game over message
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [370, 350])


def gameLoop():#initializes the game
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0#x and y coordinates of the food
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:#calls the message function when u lose
            dis.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:#if u lost
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:#if u havent lost *yet*
                        gameLoop()

        for event in pygame.event.get():#user input/ key inputs(moving the snake)
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, green, [foodx, foody, food_block, food_block])#draws the food
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
                
        for x in snake_List[0:-1]:#to check for head's collision with the rest of the body
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 <= foodx + 10 and x1 >= foodx - 10 and y1 <= foody + 10 and y1 >= foody :#when the snake eats the food
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1#updating the length of the snake

        clock.tick(snake_speed)

    pygame.quit()
    quit()#quits the program

gameLoop()
