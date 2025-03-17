import pygame
pygame.init()
WIDHT=600
HEIGHT=600
screen=pygame.display.set_mode((WIDHT,HEIGHT))
pygame.display.set_caption("shapes")

class Circle:
    def __init__(self,colour,size,pos,wid=0):
        self.pos=pos
        self.colour=colour
        self.size=size
        self.wid=wid
    def draw(self):
        self.draw_circle=pygame.draw.circle(screen,self.colour,self.pos,self.size,self.wid)

    def grow(self,r):
        self.size=self.size+r
        self.draw_circle=pygame.draw.circle(screen,self.colour,self.pos,self.size,self.wid)
circle=Circle("purple",50,(300,300),2)

circle2=Circle("black",60,(300,300),2)

circle3=Circle("blue",70,(300,300),2)



running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            screen.fill("white")
            circle.draw() 
            circle2.draw()  
            circle3.draw()     
            pygame.display.update()
        if event.type==pygame.MOUSEBUTTONUP:
            screen.fill("white")
            circle.grow(18)
            circle2.grow(18)
            circle3.grow(18)
            pygame.display.update()
        if event.type==pygame.MOUSEMOTION:
            pos=pygame.mouse.get_pos()
            circle4=Circle("black",5,pos)
            circle4.draw()
            pygame.display.update()



pygame.quit()