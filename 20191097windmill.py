# -*- coding: utf-8 -*- 

import pygame
import numpy as np 
import os

# 게임 윈도우 크기
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 800

# 색 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0,255,0)

current_path=os.getcwd()
asset_path=os.path.join(current_path,'assets')
clockbackground = pygame.image.load(os.path.join(asset_path,'windmill.png'))

# Pygame 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("20191097 Project2 - Windmill")

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

wingpoly=np.array([ [0,0,1],[215,0,1],[215,30,1],[60,30,1],[60,5,1],[0,5,1] ])
wing=wingpoly.T
degree = 0
# 게임 반복 구간
done=False
while not done:
    screen.fill(GREEN)
    screen.blit(clockbackground,[255,270])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    degree-=1

    wing1H=Tmat(350,340) @ Rmat(degree)
    wing1pp = wing1H @ wing
    wing1=wing1pp[0:2,:].T

    wing2H=Tmat(350,340) @ Rmat(degree+90)
    wing2pp = wing2H @ wing
    wing2=wing2pp[0:2,:].T

    wing3H=Tmat(350,340) @ Rmat(degree+180)
    wing3pp = wing3H @ wing
    wing3=wing3pp[0:2,:].T

    wing4H=Tmat(350,340) @ Rmat(degree+270)
    wing4pp = wing4H @ wing
    wing4=wing4pp[0:2,:].T

    pygame.draw.polygon(screen, WHITE, wing1, 0)
    pygame.draw.polygon(screen, WHITE, wing2, 0)
    pygame.draw.polygon(screen, WHITE, wing3, 0)
    pygame.draw.polygon(screen, WHITE, wing4, 0)

    # 화면 업데이트
    pygame.display.flip()
    clock.tick(60)

# 게임 종료
pygame.quit()