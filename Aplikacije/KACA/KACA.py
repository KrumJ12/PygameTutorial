import pygame
import time
import random

#OGRODJE
pygame.init() #inicializira funkcije iz pygame

bela = (255,255,255)
crna = (0,0,0)
modra = (0,0,255)
rdeca = (255,0,0)
pisano = (150,100,200)
FPS = 15

smer = "desno"

platno_x = 1100
platno_y = 600

platno = pygame.display.set_mode((platno_x,platno_y)) #platno s podanimi dimenzijami
pygame.display.set_caption("MOJA IGRA") #naslov programa
glava = pygame.image.load('snake.png')
telo = pygame.image.load('telo.png')

jabolko = pygame.image.load('jabolko.png')
ura = pygame.time.Clock()  #ura

font = pygame.font.SysFont(None,40)

def sporocilo(msg,barva):   #funkcija za izpis besedila
    besedilo = font.render(msg, True, barva)
    platno.blit(besedilo, [platno_x/7,platno_y/2])

def kaca(nasaVelikost,seznamKace):
    if smer == "gor":
        glavaPoz = pygame.transform.rotate(glava,180)
    if smer == "levo":
        glavaPoz = pygame.transform.rotate(glava,270)
    if smer == "desno":
        glavaPoz = pygame.transform.rotate(glava,90)
    if smer == "dol":
        glavaPoz = glava
        
    platno.blit(glavaPoz, (seznamKace[-1][0],seznamKace[-1][1]))
    
    for XY in seznamKace[:-1]:
        platno.blit(telo, (XY[0],XY[1]))
    

def igra():
    global smer
    igraIzhod = False #ali igra teče
    igraKonec = False

    nasaVelikost = 20
    velikostKocke = 20
    
    koord_x = round((platno_x/2 - 10)/20)*20
    koord_y = round((platno_y/2 - 10)/20)*20
    sprememba_x = nasaVelikost
    sprememba_y = 0

    dolzinaKace = 1
    seznamKace = []
    
    
    
    kockaX = round(random.randrange(0,platno_x - velikostKocke)/20)*20
    kockaY = round(random.randrange(0,platno_y - velikostKocke)/20)*20

    
    while not igraIzhod:

        while igraKonec == True:
            platno.fill(bela)
            sporocilo("ZALETEL SI SE PRITISNI P ZA PONOVNO IGRANJE, I ZA IZHOD",pisano)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        igra()
                    if event.key == pygame.K_i:
                        igraIzhod = True
                        igraKonec = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #ko pritisnemo križec
                igraIzhod = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and smer != "desno":
                    smer = "levo"
                    sprememba_x = -nasaVelikost
                    sprememba_y = 0
                if event.key == pygame.K_RIGHT and smer != "levo":
                    smer = "desno"
                    sprememba_x = nasaVelikost
                    sprememba_y = 0
                if event.key == pygame.K_UP and smer != "dol":
                    smer = "gor"
                    sprememba_y = -nasaVelikost
                    sprememba_x = 0
                if event.key == pygame.K_DOWN and smer != "gor":
                    smer = "dol"
                    sprememba_y = nasaVelikost
                    sprememba_x = 0
##            if event.type == pygame.KEYUP:
##                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
##                    sprememba_x = 0
##                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
##                    sprememba_y = 0
                    

        for kosKace in seznamKace[:-1]:
            if kosKace == glavaKace:
                igraKonec = True
        
        if koord_x + nasaVelikost > platno_x or koord_x < 0 or koord_y + nasaVelikost > platno_y or koord_y < 0:
            igraKonec = True

        if kockaX - nasaVelikost < koord_x < kockaX + velikostKocke and kockaY - nasaVelikost < koord_y < kockaY + velikostKocke:
            kockaX = round(random.randrange(0,platno_x - velikostKocke)/20)*20
            kockaY = round(random.randrange(0,platno_y - velikostKocke)/20)*20
            seznamKace.append(glavaKace)

        koord_x += sprememba_x
        koord_y += sprememba_y

        
        platno.fill(bela)  #zapolni platno
        platno.blit(jabolko,[kockaX,kockaY])
        #pygame.draw.rect(platno,crna,[kockaX,kockaY,velikostKocke,velikostKocke])

        glavaKace = []
        glavaKace.append(koord_x)
        glavaKace.append(koord_y)
        seznamKace.append(glavaKace)

        if len(seznamKace) > dolzinaKace:
            del seznamKace[0]
        

        kaca(nasaVelikost,seznamKace)
        
        pygame.display.update()  #posodobi platno, parameter določa katero mesto
        ura.tick(FPS) #frames per second

    pygame.quit()
    quit()

igra()
