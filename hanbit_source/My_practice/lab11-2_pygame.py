import pygame
import random
import sys

moniter = None
colorList = ["red","green","blue","black","magenta","orange","gray"]

pygame.init()
moniter = pygame.display.set_mode((500, 700))
color = random.choice(colorList)
turtle = pygame.image.load("C:/Users/jw/Desktop/git/MyStudy/hanbit_source/FirstPython/Chapter11/turtle.png")
tx, ty = 200, 300


while True:
    moniter.fill(color)
    moniter.blit(turtle, (tx,ty))
    pygame.display.update()

    for e in pygame.event.get():
        if e.type in [pygame.QUIT]:
            pygame.quit()
            sys.exit()

        # if e.type in [pygame.KEYDOWN] :
        #     if e.key == pygame.K_LEFT : tx -= 10
        #     elif e.key == pygame.K_RIGHT : tx += 10
        #     elif e.key == pygame.K_UP : ty -= 10
        #     elif e.key == pygame.K_DOWN : ty += 10 방향키 누르면 움직이는 거북이 표현
        
        if e.type in [pygame.KEYDOWN] :
            if e.key == pygame.K_SPACE :
                tx = random.randint(0,500) # 랜덤한 위치에 거북이 출현, 화면 밖으로도 나감
                ty = random.randint(0,700) # x축,y축 이미지 픽셀만큼 빼면 밖으로 안나감.