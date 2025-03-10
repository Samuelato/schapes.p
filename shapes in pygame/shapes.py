import pygame
pygame.init()
WIDHT=600
HEIGHT=600
screen=pygame.display.set_mode((WIDHT,HEIGHT))
pygame.display.set_caption("shapes")

class Circle:
    def __init__(self,colour,size,x,y):
        self.x=x
        self.y=y
        self.colour=colour
        self.size=size
    def draw(self):
        self.draw_circle=pygame.draw.circle(screen,self.colour,(self.x,self.y),self.size)




running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            




pygame.quit()