import pygame
import time
import zaigraj_skladbo

pygame.mixer.pre_init(44100,-16,2, 2048)
pygame.init()


platno_x = 1000
platno_y = 200

FPS = 20

platno = pygame.display.set_mode((platno_x,platno_y))
ura = pygame.time.Clock()

v_bele_tipke = platno_x/36
v_crne_tipke = v_bele_tipke/1.7
v_tipke = 140
font = pygame.font.SysFont(None,40)

bela = (255,255,255)
crna = (0,0,0)
siva = (200,200,200)
rdeca = (255,0,0)
modra = (0,0,255)


note = "cdefgab"

niz = ""
hitrost = "0"

def tekst(msg,barva):
    besedilo = font.render(msg, True, barva)
    return besedilo, besedilo.get_rect()

def sporocilo(msg,barva):   #funkcija za izpis besedila
    besedilo, kvadrat = tekst(msg, barva)
    kvadrat.center = platno_x/2,platno_y - 20
    platno.blit(besedilo,kvadrat)

def gumb(msg,barva,x,y,sirina,visina):
    besedilo, kvadrat = tekst(msg, barva)
    kvadrat.center = x+(sirina/2),y+(visina/2)
    platno.blit(besedilo,kvadrat)



def narisi(x,y,pritisk,pisi):
    pygame.mixer.set_num_channels(200)
    slovar_not = {}
    for i in "abcdefg":
        for j in range(1,7):
            if (j == 6 and i == "f") or (j == 6 and i == "g"):
                pass
            else:
                slovar_not[i+str(j)] = pygame.mixer.Sound("ZVOKI\\"+i+str(j)+".wav")
            if i in "acdfg":
                if (j == 6 and i == "f") or (j == 6 and i == "g"):
                    pass
                else:
                    slovar_not["v"+i+str(j)] = pygame.mixer.Sound("ZVOKI\\v"+i+str(j)+".wav")
    global niz
    global hitrost
    sezBelih = []
    if (2/3)*v_tipke<y<v_tipke and pritisk: # ko pritisnemo belo tipko spodaj
        izbrana = int(x/v_bele_tipke)
        pygame.draw.rect(platno, siva,((izbrana)*v_bele_tipke,0,v_bele_tipke,v_tipke))
        if pisi:
            niz +=(note[izbrana%7]+str(1+(izbrana+2)//7))
            niz += hitrost+","
            pygame.mixer.find_channel().play(slovar_not[note[izbrana%7]+str(1+(izbrana+2)//7)])
            pisi = False
        
    for i in range(1,36):
        pygame.draw.line(platno, crna, (i*v_bele_tipke,0), (i*v_bele_tipke,v_tipke), 1) 
        if  (i+4) % 7 == 0 or i % 7 == 0: #nekatere črne tipke moramo izpustiti
            sezBelih.append([i*v_bele_tipke,(i+1)*v_bele_tipke - (1/2)*v_crne_tipke])
        else:
            if (i+5) % 7 == 0 or (i+1) % 7 == 0: 
                sezBelih.append([i*v_bele_tipke + (1/2)*v_crne_tipke,(i+1)*v_bele_tipke])
            else:
                sezBelih.append([i*v_bele_tipke + (1/2)*v_crne_tipke,(i+1)*v_bele_tipke - (1/2)*v_crne_tipke])
            pygame.draw.rect(platno, crna,(i*v_bele_tipke-(1/2)*v_crne_tipke,0,v_crne_tipke,(2/3)*v_tipke))
            if i*v_bele_tipke-(1/2)*v_crne_tipke<x<i*v_bele_tipke+(1/2)*v_crne_tipke:
                if 0 < y < (2/3)*v_tipke and pritisk:
                    for j in range(1,36):
                        if  j*v_bele_tipke-(1/2)*v_crne_tipke<x<j*v_bele_tipke+(1/2)*v_crne_tipke:
                            izbrana = j
                    pygame.draw.rect(platno, siva,(i*v_bele_tipke-(1/2)*v_crne_tipke,0,v_crne_tipke,(2/3)*v_tipke))
                    if pisi:
                        niz +="v"
                        if (izbrana-1)%7 == 4:
                            niz +=(note[(izbrana-1)%7]+str((izbrana+2)//7))
                            pygame.mixer.find_channel().play(slovar_not["v"+note[(izbrana-1)%7]+str((izbrana+2)//7)])
                        else:
                            niz +=(note[(izbrana-1)%7]+str(1+(izbrana+2)//7))
                            pygame.mixer.find_channel().play(slovar_not["v"+note[(izbrana-1)%7]+str(1+(izbrana+2)//7)])
                        niz += hitrost+","
                        pisi = False
                
    pygame.draw.line(platno, crna,(0,v_tipke),(platno_x,v_tipke),1)
    for sez in sezBelih:
        if 0 < y < (2/3)*v_tipke and pritisk:
            if sez[0] < x < sez[1]:
                izbrana = int(x/v_bele_tipke)
                pygame.draw.rect(platno,siva,(int(sez[0]),0,int(sez[1]-sez[0]),v_tipke))
                pygame.draw.rect(platno, siva,((izbrana)*v_bele_tipke+1,(2/3)*v_tipke,v_bele_tipke+1,(1/3)*v_tipke+1))
                if pisi:
                    niz +=(note[izbrana%7]+str(1+(izbrana+2)//7))
                    niz += hitrost+","
                    pygame.mixer.find_channel().play(slovar_not[note[izbrana%7]+str(1+(izbrana+2)//7)])
                    pisi = False
    

def klaviatura():
    global niz
    global hitrost
    loop = True
    pritisk = False
    pisi = False
    miska = (-100,-100)
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    hitrost = "0"
                if event.key == pygame.K_1:
                    hitrost = "1"
                if event.key == pygame.K_2:
                    hitrost = "2"
                if event.key == pygame.K_4:
                    hitrost = "4"
                if event.key == pygame.K_8:
                    hitrost = "8"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    miska = pygame.mouse.get_pos()
                    pritisk = True
                    pisi = True
                    if 470 < miska[0] < 630 and 160 < miska[1] < 195:
                        loop = False
            if event.type == pygame.MOUSEBUTTONUP:
                pritisk = False
                miska = (-100,-100)
        
        platno.fill(bela)
        narisi(miska[0],miska[1],pritisk,pisi)
        pisi = False
        pygame.draw.rect(platno,modra,(platno_x/2-30,platno_y-40,160,35))
        gumb("KONČAJ", rdeca, platno_x/2,platno_y - 30,100,20)

        pygame.display.update()  
        ura.tick(FPS)
    
    zaigraj_skladbo.zaigraj(niz)
    pygame.quit()
    quit()

klaviatura()

    
    
