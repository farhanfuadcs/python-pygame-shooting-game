import pygame


import os 

from tkinter import messagebox


pygame.font.init()

pygame.mixer.init()

WIDTH,HEIGHT=800,600
w,h=50,80
velocity=6
yellowcolor=(255,255,0)
redcolor=(255,0,0)
white=(255,255,255)


window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Shooting Game by FUAD")

space_bg=pygame.transform.scale(pygame.image.load(os.path.join("Assets","space.png")),(WIDTH,HEIGHT))
ys=pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("Assets","Yellow spaceship.png")),(w,h)),270)
rs=pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("Assets","Red spaceship.png")),(w,h)),90)

bulletsound=pygame.mixer.Sound(os.path.join("Assets","shootingsound.mp3"))
impactsound=pygame.mixer.Sound(os.path.join("Assets","bulletimpact.mp3"))



bullet_vel=7


yellowhit=pygame.USEREVENT+1
redhit=pygame.USEREVENT+2


healthtext=pygame.font.SysFont("Arial",35)
winnertext=pygame.font.SysFont("Cosmic",50)



FPS=60


def draw(yellow,red,yellowbullets,redbullets,redhealth,yellowhealth):
    window.blit(space_bg,(0,0))


    for bullet in yellowbullets:
        pygame.draw.rect(window,yellowcolor,bullet)

    for bullet in redbullets:
        pygame.draw.rect(window,redcolor,bullet)

    window.blit(ys,(yellow.x,yellow.y))
    window.blit(rs,(red.x,red.y))

    redhealthtext=healthtext.render(f"Helath: {str(redhealth)}",1,white)
    yellowhealthtext=healthtext.render(f"Health: {str(yellowhealth)}",1,white)

    window.blit(yellowhealthtext,(10,10))
    window.blit(redhealthtext,(WIDTH-redhealthtext.get_width()-10,10))

    pygame.display.update()



def playermovement(key,yellow):
    if key[pygame.K_w] and yellow.y>10:
        yellow.y-=velocity
    if key[pygame.K_s] and yellow.y<HEIGHT-60:
        yellow.y+=velocity
    if key[pygame.K_a] and yellow.x>0:
        yellow.x-=velocity
    if key[pygame.K_d] and yellow.x<WIDTH/2-120:
        yellow.x+=velocity





def ai_movement(red,yellow,yellowbullets):
    danger=False

    for bullet in yellowbullets:
        if bullet.x<red.x and bullet.x>red.x-150:
            if abs(bullet.centery-red.centery)<60:
                danger=True
                if red.centery>bullet.centery:
                    red.y+=velocity*2

                else:
                    red.y-=velocity*2
                
            
                break

    if not danger:
        if red.centery<yellow.centery:
            red.y+=velocity
        if red.centery>yellow.centery:
            red.y-=velocity
    

    red.y=max(0,min(red.y,HEIGHT-red.height))






def bullet_movement(yellowbullets,redbullets,yellow,red):
    yellow_hitarea=pygame.Rect(
        yellow.x+15,
        yellow.y,
        yellow.width-30,
        yellow.height-25,
    )


    red_hitarea=pygame.Rect(
        red.x+15,
        red.y,
        red.width-30,
        red.height-25,
    )


    for bullet in yellowbullets:
        bullet.x+=bullet_vel
        if red_hitarea.colliderect(bullet):
            pygame.event.post(pygame.event.Event(redhit))
            yellowbullets.remove(bullet)
        elif bullet.x>WIDTH:
            yellowbullets.remove(bullet)

    for bullet in redbullets:
        bullet.x-=bullet_vel
        if yellow_hitarea.colliderect(bullet):
            pygame.event.post(pygame.event.Event(yellowhit))
            redbullets.remove(bullet)
        elif bullet.x<0:
            redbullets.remove(bullet)


def ai_bullet_movement(red,redbullets):
    if len(redbullets)<4:
        bullet=pygame.Rect(red.x,red.y+red.height//2-18,10,6)
        redbullets.append(bullet)
        bulletsound.play()



def draw_winner(winner):
    winnerdisplay=winnertext.render(winner,1,white)
    window.blit(winnerdisplay,(WIDTH//2-winnerdisplay.get_width()//2,HEIGHT//2-winnerdisplay.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)




def main():
    run=True
    clock=pygame.time.Clock()
    aishoottimer=0

    yellow=pygame.Rect(90,250,w,h)
    red=pygame.Rect(600,250,w,h)

    yellowbullets=[]
    redbullets=[]

    yellowhealth=10
    redhealth=10

    messagebox.showinfo(title="Control Guide",message="WASD: Move | Left Click: Shoot")
    pygame.time.delay(2000)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False

            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1 and len(yellowbullets)<4:
                    bullet=pygame.Rect(yellow.x+yellow.width,yellow.y+yellow.height//2-18,10,6)
                    yellowbullets.append(bullet)
                    bulletsound.play()


            if event.type==redhit:
                redhealth-=1
                impactsound.play()

            if event.type==yellowhit:
                yellowhealth-=1
                impactsound.play()


        winner=""

        if redhealth<=0:
            winner="You Win"

        if yellowhealth<=0:
            winner="AI Wins"

        if winner!="":
            draw_winner(winner)
            break





        key=pygame.key.get_pressed()
        draw(yellow,red,yellowbullets,redbullets,redhealth,yellowhealth)
        playermovement(key,yellow)
        ai_movement(red,yellow,yellowbullets)
        bullet_movement(yellowbullets,redbullets,yellow,red)
        aishoottimer+=clock.get_time()
        if aishoottimer>=100:
            ai_bullet_movement(red,redbullets)
            aishoottimer=0



if __name__=="__main__":
    while True:
        main()

        restart=messagebox.askyesno(title="Game Over",message="Do you want to restart the game?")

        if not restart:
            break

    pygame.quit()