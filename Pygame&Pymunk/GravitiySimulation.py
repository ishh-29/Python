import pygame,sys,pymunk
def apple(s,p):
    body=pymunk.Body(1,100,body_type=pymunk.Body.DYNAMIC)
    body.position=p
    shape=pymunk.Circle(body,50)
    s.add(body,shape)
    return shape
def draw(apples):
    for apple in apples:
        x=int(apple.body.position.x)
        y=int(apple.body.position.y)
        r=img.get_rect(center=(x,y))
        scn.blit(img,r)
def statball(s,p):
    body=pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position=p
    shape=pymunk.Circle(body,40)
    s.add(body,shape)
    return shape
def draw_stat(balls):
    for ball in balls :
        x=int(ball.body.position.x)
        y=int(ball.body.position.y)
        pygame.draw.circle(scn,(0,0,0),(x,y),40)
#Display
pygame.init()
scn=pygame.display.set_mode((800,800))
#Time
t=pygame.time.Clock()
#Space
s=pymunk.Space()
s.gravity=(0,100) #Gravity From x & y axis
a=pygame.image.load('apple.png')
#Resize the image
size = (100, 100)  #Desired width and height
img = pygame.transform.scale(a,size)
apples=[]
balls=[]
balls.append(statball(s,(500,500)))
balls.append(statball(s,(650,500)))
#Game Loop
while True:
    for event in pygame.event.get(): #User Input
        if event.type==pygame.QUIT: #Closing
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN :
            apples.append(apple(s,event.pos))
    scn.fill((217,217,217)) #Background Color
    draw(apples)
    draw_stat(balls)
    s.step(1/50)
    pygame.display.update() #Rendering Frames
    t.tick(120)             #Limiting Fps To 120