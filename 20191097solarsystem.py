import pygame
import numpy as np
import os

pygame.init()

WINDOW_WIDTH = 1450
WINDOW_HEIGHT = 820

BLACK = (0,0,0)
WHITE = (255,255,255)


current_path = os.getcwd()
asset_image_path = os.path.join(current_path, "assets")

sun_image = pygame.image.load(os.path.join(asset_image_path, "sun.png"))
venus_image = pygame.image.load(os.path.join(asset_image_path, "venus.png"))
earth_image = pygame.image.load(os.path.join(asset_image_path, "earth.png"))
moon_image = pygame.image.load(os.path.join(asset_image_path, "moon.png"))
saturn_image = pygame.image.load(os.path.join(asset_image_path, "saturn.png"))
titan_image = pygame.image.load(os.path.join(asset_image_path, "titan.png"))
enterprise_image = pygame.image.load(os.path.join(asset_image_path, "enterprise.png"))

pygame.display.set_caption('20191097 Project2 - Solar system')

screen=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

clock=pygame.time.Clock()

class Planet():
    def __init__(self, centerxy, distance, cycle, image):
        self.centercoord = centerxy
        self.dist=distance
        self.rot=0
        self.rotspeed = 360 / cycle / 40
        self.image = image
        self.centerx=centerxy[0]
        self.centery=centerxy[1]
        self.x=self.centerx + self.dist
        self.y=self.centery

    def update(self, centerplanet):
        self.centerx=centerplanet.x
        self.centery=centerplanet.y
        self.x=self.dist * np.sin(self.rot) + self.centerx
        self.y=self.dist * np.cos(self.rot) + self.centery

        self.rot += self.rotspeed

    def show(self,):
        self.width=self.image.get_width()
        self.height=self.image.get_height()
        pos=[self.x-self.width/2, self.y-self.height/2]
        pygame.draw.circle(screen,WHITE, [self.centerx,self.centery],self.dist, 1)
        screen.blit(self.image, pos)

class Saturn():
    def __init__(self,centerxy, xdist, ydist, cycle, image):
        self.centercoord=centerxy
        self.centerx=centerxy[0]
        self.centery=centerxy[1]
        self.xradius=xdist
        self.yradius=ydist
        self.rot=0
        self.rotspeed = 360 / cycle / 40
        self.image=image
        self.x=xdist+self.centerx
        self.y=ydist+self.centery

    def update(self, centerplanet):
        self.centerx=centerplanet.x
        self.centery=centerplanet.y
        self.x=self.xradius * np.sin(self.rot) + self.centerx
        self.y=self.yradius * np.cos(self.rot) + self.centery

        self.rot += self.rotspeed

    def show(self,):
        self.width=self.image.get_width()
        self.height=self.image.get_height()
        pos=[self.x-self.width/2, self.y-self.height/2]
        pygame.draw.ellipse(screen,WHITE, [self.centerx-self.xradius,self.centery-self.yradius,
            self.xradius*2,self.yradius*2], 1)
        screen.blit(self.image, pos)

class starship():
    def __init__(self, image):
        self.image=image
        self.width=self.image.get_width()
        self.height=self.image.get_height()
        self.x=np.random.randint(1+self.width, WINDOW_WIDTH-self.width)
        self.y=np.random.randint(1+self.height, WINDOW_HEIGHT-self.height)
        self.last_update = 0
        self.dx=np.random.randint(-5,5)
        self.dy=np.random.randint(-5,5)

    def update(self):
        if pygame.time.get_ticks() > self.last_update +1800:
            self.dx=np.random.randint(-5,5)
            self.dy=np.random.randint(-5,5)
            self.last_update = pygame.time.get_ticks()
        self.x += self.dx
        self.y += self.dy
        if self.x > WINDOW_WIDTH or self.x < 0:
            self.dx *= -1
        if self. y > WINDOW_HEIGHT or self.y < 0:
            self.dy *= -1    

    def show(self,):
            pos=[self.x-self.width/2, self.y-self.height/2]
            screen.blit(self.image, pos)
        
sun=Planet([WINDOW_WIDTH/2, WINDOW_HEIGHT/2],0,1,sun_image)
earth=Planet([sun.x, sun.y], 280, 365, earth_image)
venus=Planet([sun.x, sun.y], 150, 225, venus_image)
moon=Planet([earth.x, earth.y],70,27,moon_image)
saturn=Saturn([sun.x,sun.y],650,400,10749,saturn_image)
titan=Planet([saturn.x,saturn.y],170,15.9,titan_image)

planets=[sun,earth,venus,saturn]
satelites=[moon,titan]
enterprise=starship(enterprise_image)

last_update=-900

done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    
    screen.fill(BLACK)
    if last_update + 800 < pygame.time.get_ticks():
        stars=[]
        for i in range(80):
            stars.append([np.random.randint(0,WINDOW_WIDTH), np.random.randint(0,WINDOW_HEIGHT)])
            last_update=pygame.time.get_ticks()

    for i in stars:
        pygame.draw.circle(screen,WHITE, i, 2, 0)

    for i in planets:
        i.update(sun)
        i.show()

    moon.update(earth)
    titan.update(saturn)
    moon.show()
    titan.show()

    enterprise.update()
    enterprise.show()

    pygame.display.flip()
    clock.tick(100)
    
pygame.quit()