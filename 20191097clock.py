# -*- coding: utf-8 -*- 

import pygame
import numpy as np 
import datetime
import os

# 게임 윈도우 크기
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 800

# 색 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255,0,0)

current_path=os.getcwd()
asset_path=os.path.join(current_path,'assets')
clockbackground = pygame.image.load(os.path.join(asset_path,'clock.png'))

# Pygame 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("20191097 Project2 - Clock")

# 윈도우 생성
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 게임 화면 업데이트 속도
clock = pygame.time.Clock()

# 폰트 선택(폰트, 크기, 두껍게, 이탤릭)
font = pygame.font.SysFont('FixedSys', 40, True, False)

def Rmat(deg):
    radian = np.deg2rad(deg)
    c=np.cos(radian)
    s=np.sin(radian)
    R=np.array([[c, -s, 0], [s,c,0], [0,0,1]])
    return R

def Tmat(a,b):
    H=np.eye(3)
    H[0,2]=a
    H[1,2]=b
    return H

hourpoly=np.array([ [0,0,1],[210,0,1],[210,20,1],[0,20,1] ])
hourpoly1=hourpoly.T
minutepoly=np.array([ [0,0,1],[300,0,1],[300,20,1],[0,20,1] ])
minutepoly1=minutepoly.T
secondpoly=np.array([ [0,0,1],[320,0,1],[320,10,1],[0,10,1] ])
secondpoly1=secondpoly.T

cor1=np.array([30,10,1])
cor2=np.array([30,5,1])


# 게임 반복 구간
done=False
while not done:
    screen.fill(WHITE)
    screen.blit(clockbackground,[0,0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    timenow=datetime.datetime.now()
    degree1 = timenow.hour*30 -90 + timenow.minute/2 + timenow.second/120
    degree2 = timenow.minute*6 + timenow.second/10 -90
    degree3 = timenow.second*6 -90

    hourH=Tmat(320,340) @ Tmat(30,10) @ Rmat(degree1) @ Tmat(-30,-10)
    hourpp = hourH @ hourpoly1
    hourcor = hourH @ cor1
    hour=hourpp[0:2,:].T

    cor= hourH @ cor1
    minuteH=Tmat(320,340) @ Tmat(30,10) @ Rmat(degree2) @ Tmat(-30,-10)
    minutepp = minuteH @ minutepoly1
    minute=minutepp[0:2,:].T

    secondH=Tmat(320,345) @ Tmat(30,5) @ Rmat(degree3) @ Tmat(-30,-5)
    secondcor= secondH @ cor2
    secondpp = secondH @ secondpoly1
    second=secondpp[0:2,:].T

    pygame.draw.polygon(screen, BLACK, hour, 0)
    pygame.draw.polygon(screen, BLACK, minute, 0)
    pygame.draw.polygon(screen, RED, second, 0)
    time=font.render(str(datetime.datetime.now()),True,BLACK)
    screen.blit(time,[100,710])

    # 화면 업데이트
    pygame.display.flip()
    clock.tick(60)

# 게임 종료
pygame.quit()