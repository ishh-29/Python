import pygame,sys,random
def animate():
    global bspeedx,bspeedy,p1sc,p2sc,time
    ball.x+=bspeedx
    ball.y+=bspeedy
    if ball.top<=0 or ball.bottom >=h:
        bspeedy*=-1
    if ball.left<=0 :
        p1sc+=1
        time=pygame.time.get_ticks()
    if ball.right>=w:
        p2sc+=1
        time=pygame.time.get_ticks()
    if ball.colliderect(p1) and bspeedx>0 :
        if abs(ball.right-p1.left)<10 :
            bspeedx*=-1
        elif abs(ball.bottom-p1.top)<10 and bspeedy>0:
            bspeedy*=-1
        elif abs(ball.top-p1.bottom)<10 and bspeedy<0:
            bspeedy*=-1
    if ball.colliderect(p2) and bspeedx<0 :
        if abs(ball.left-p2.right)<10:
            bspeedx*=-1
        elif abs(ball.bottom-p2.top)<10 and bspeedy>0:
            bspeedy*=-1
        elif abs(ball.top-p2.bottom)<10 and bspeedy<0:
            bspeedy*=-1
def p_animate():
    p1.y+=pspeed
    if p1.top<=0 :
        p1.top=0
    if p1.bottom>=h:
        p1.bottom=h
def o_animate():
    if p2.top<ball.y :
        p2.top+=ospeed
    if p2.bottom>ball.y :
        p2.bottom-=ospeed
    if p2.top<=0 :
        p2.top=0
    if p2.bottom>=h:
        p2.bottom=h
def breset():
    global bspeedx , bspeedy,time
    curtime=pygame.time.get_ticks()
    ball.center=(w/2,h/2)
    if curtime-time<700:
        n3=f.render("3",False,c1)
        scn.blit(n3,((w/2-10),(h/2+20)))
    if 700<curtime-time<1400:
        n2=f.render("2",False,c1)
        scn.blit(n2,((w/2-10),(h/2+20)))
    if 1400<curtime-time<2100:
        n1=f.render("1",False,c1)
        scn.blit(n1,((w/2-10),(h/2+20)))
    if curtime-time<2100:
        bspeedx,bspeedy=0,0
    else:
        bspeedy=4*random.choice((-1,1))
        bspeedx=4*random.choice((-1,1))
        time=None
#Initializing Setup
pygame.init()
t=pygame.time.Clock()
w,h=1280,960
scn=pygame.display.set_mode((w,h))
pygame.display.set_caption("Ping Pong")
#Game Variables
ball=pygame.Rect(w/2-15,h/2-15,30,30)
p1=pygame.Rect(w-20,h/2-70,10,140)
p2=pygame.Rect(10,h/2-70,10,140)
c=pygame.Color('black')
c1=pygame.Color('gray')
c2=pygame.Color('gray')
bspeedx=7 *random.choice((-1,1))
bspeedy=7 *random.choice((-1,1))
pspeed=0
ospeed=7
#Text Variables
p1sc=0
p2sc=0
f=pygame.font.Font("freesansbold.ttf",32)
#Timer
time=True
#Handling Input 
while True :
    for event in pygame.event.get(): #User Input
        if event.type==pygame.QUIT : #Closing
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN :
                pspeed+=7
            if event.key==pygame.K_UP :
                pspeed-=7
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_DOWN :
                pspeed-=7
            if event.key==pygame.K_UP :
                pspeed+=7
    animate()
    p_animate()
    o_animate()
    #Visuals
    scn.fill(c)
    pygame.draw.rect(scn,c1,p1)
    pygame.draw.rect(scn,c1,p2)
    pygame.draw.ellipse(scn,c2,ball)
    pygame.draw.aaline(scn,c2,(w/2,0),(w/2,h))
    if time :
        breset()
    p1text=f.render(f"{p1sc}",False,c1) 
    scn.blit(p1text,(660,470))
    p2text=f.render(f"{p2sc}",False,c1) 
    scn.blit(p2text,(600,470))
    #Updating Window
    pygame.display.flip() #Draws The Picture
    t.tick(60) #Fps Control