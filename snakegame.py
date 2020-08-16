import pygame
import random
import os
pygame.mixer.init()
pygame.init()
screen_width=1100
screen_height=700
# Colours*(rgb)
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
blue=(51,255,255)
dark_blue=(0,76,153)
gray=(128,128,128)
gameWindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.update()
pygame.display.set_caption("Snake Game")
pygame.display.update()
# Background Image
bk_img=pygame.image.load("download.jfif")
bk_img=pygame.transform.scale(bk_img,(screen_width,550)).convert_alpha()
gameoverimg=pygame.image.load("goimg.jpg")
gameoverimg=pygame.transform.scale(gameoverimg,(screen_width,550)).convert_alpha()
box_size = 25
font = pygame.font.SysFont(None, 65)
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])
def plot_snake(gameWindow,color,snake_lst,snake_size,):
    for x,y in snake_lst:
        pygame.draw.rect(gameWindow,red,[x,y,box_size,box_size])

def Welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill(blue)
        gameWindow.blit(bk_img, (0, 0))
        text_screen("Welcome to Snake Game",black,260,580)
        text_screen("Press Space bar to play the game",black,200,630)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
                exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.load("bksound.mp3")
                    pygame.mixer.music.play(-1)
                    gameloop()

        pygame.display.update()
        pygame.time.Clock().tick(60)


def gameloop():
    # Game specific varibles
    game_over = False
    exit_game = False
    fps = 60
    x_pos = 50
    y_pos = 35
    x_velocity = 0
    y_velocity = 0
    x_speed=0
    y_speed=0
    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    food_size = 25

    snake_lst = []
    snk_length = 1
    if(not os.path.exists("Hiscore.txt")):
        with open("Hiscore.txt","w") as f:
            f.write("0")
    with open("Hiscore.txt","r") as f:
        Hiscore=f.read()
    score = 0
    while not exit_game:
        if game_over:
            with open("Hiscore.txt", "w") as f:
                f.write(str(Hiscore))
            gameWindow.fill(blue)
            gameWindow.blit(gameoverimg,(0,0))
            text_screen("Score: "+str(score),black,435,570)
            text_screen("Press Enter to Continue",black,300,620)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                    exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        Welcome()
        else:


            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_RIGHT:
                            x_velocity+=8
                            y_velocity=0

                        if event.key==pygame.K_DOWN:
                            y_velocity+=8
                            x_velocity=0

                        if event.key==pygame.K_LEFT:
                            x_velocity+=-8
                            y_velocity=0

                        if event.key==pygame.K_UP:
                            y_velocity+=-8
                            x_velocity=0

            x_pos=x_pos+x_velocity
            y_pos=y_pos+y_velocity
            if abs(x_pos-food_x)<6 and abs(y_pos-food_y)<6:
                score+=10

                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20, screen_height/2)
                snk_length+=5
                if score>int(Hiscore):
                    Hiscore=score



            gameWindow.fill(blue)
            text_screen("Score: " + str(score)+"     Highest Score: "+str(Hiscore), gray, 5, 5)
            pygame.draw.rect(gameWindow, black,[food_x, food_y, food_size, food_size])
            head=[]
            head.append(x_pos)
            head.append(y_pos)
            snake_lst.append(head)
            if len(snake_lst)>snk_length:
                del snake_lst[0]

            #     for collision
            if x_pos<0 or x_pos>screen_width or y_pos<0 or y_pos>screen_height:
                game_over=True
                pygame.mixer.init()
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()
            if head in snake_lst[:-1]:
                game_over=True
                pygame.mixer.init()
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()

            plot_snake(gameWindow,red,snake_lst,box_size)
        pygame.display.update()
        pygame.time.Clock().tick(fps)


    pygame.quit()
    quit()
if __name__ == '__main__':
    Welcome()
