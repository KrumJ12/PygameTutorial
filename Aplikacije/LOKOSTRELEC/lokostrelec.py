import pygame
import random

pygame.init()

zelena= (0,255,0)
crna= (0,0,0)
modra= (0,0,255)
temnoZ = (24,124,37)
bela=(255,255,255)
platnox=1100
platnoy=800
platno=pygame.display.set_mode((platnox,platnoy))
pygame.display.set_caption("Lokostrelec")
lok = pygame.image.load('lok.png')

ura = pygame.time.Clock()  #ura
fps=30
font = pygame.font.SysFont(None,40)

def tekst(msg,barva,x,y):   #funkcija za izpis besedila
    besedilo = font.render(msg, True, barva)
    platno.blit(besedilo, [x,y])

def igra():
    konec=False
    stZadetkov=0 #kolikokrat smo zadeli tarčo
    stStrelov = 0

       
    #dolzina palice, hitrost tarce v smeri y in smer (1 dol, 2 gor)
    d=150
    dv=4
    smer=1
    #pozicija tarce x in y
    tx=platnox-20 
    ty=0
    
    #pozicija x in y puščice, hitrost v smeri x
    px=120
    py=365
    dx=20

    lahkoStreljam=True
    ustreljeno=False
    zadeto= False
    
    while not konec:

        if stStrelov==6: #v resnici bo eden manj
            platno.fill(bela)
            tekst("Od "+str(stStrelov-1)+ " strelov si zadel: "+str(stZadetkov), temnoZ,400,80)
            tekst("Pritisni N za novo igro ali K za konec", modra,500,500)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #ko pritisnemo križec
                    konec = True
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_n:
                    igra()
                if event.key ==pygame.K_k:
                    konec = True
        else: 

            for event in pygame.event.get():
                if event.type == pygame.QUIT: #ko pritisnemo križec
                    konec = True
                if event.type == pygame.KEYDOWN: #streljamo s SPACE
                    if lahkoStreljam and not zadeto and event.key == pygame.K_SPACE:
                        lahkoStreljam=False
                        ustreljeno=True
                        stStrelov +=1
                        
            platno.fill(zelena)
            platno.blit(lok,(100,300))
            pygame.draw.line(platno,crna,(tx,ty),(tx,ty+d),5)
            ty = ty+ (-1)**smer*dv
            
            if ty > platnoy : #pridemo na vrh
                if zadeto:
                    dv=min (dv+0.2, 6.5) #vsakemu novemu povečamo hitrost
                    #vendar nikoli čez 6,5
                    d=max(40,0.9*d)
                px=120 #puščico postavimo v začetni položaj, spet lahko streljamo
                py=365
                ustreljeno=False
                lahkoStreljam=True
                zadeto=False
                dilema=random.randint(1,2) #dve moznosti
                if dilema ==1: #gremo gor
                    smer= 1
                else: #pojavimo se na vrhu
                    ty=0
                    smer=2
            elif ty < -d: #pridemo na dno
                if zadeto:
                    dv=min (dv+0.2, 6.5) #vsakemu novemu povečamo hitrost
                    #vendar nikoli čez 6,5
                    d=max(40,0.9*d)
                px=120
                py=365
                ustreljeno=False
                lahkoStreljam=True
                zadeto=False
                dilema=random.randint(1,2)
                if dilema ==1: #gremo dol
                    smer=2
                else:
                    ty=platnoy
                    smer=1
                    
            if zadeto:
                ustreljeno = False
                pygame.draw.line(platno,crna,(tx-30,py ),(tx,py ),2)
                py=py+(-1)**smer*dv
                
                
            if ustreljeno:
                pygame.draw.line(platno,crna,(px,py),(px+30,py),2)
                px= px+ dx
                if abs((px +30) - tx) < 15:
                    #gledamo konico puščice, zaradi nezveznosti modela
                    #enakost ne bo nujno izpolnjena,
                    #želimo pa imeti majhno razliko
                    if py > ty and py < (ty+d): #zadeli smo tarčo
                        stZadetkov +=1
                        zadeto = True

                        
            tekst("Tvoj rezultat:"+str(stZadetkov)+"/"+str(stStrelov), temnoZ,400,80)
            pygame.display.update()
            ura.tick(fps)
                

    pygame.quit()
    quit()

igra()
