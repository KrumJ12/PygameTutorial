import pygame
import krog_objekt as kr

pygame.mixer.pre_init(44100,-16,2, 2048)
pygame.init()

FPS = 60

platno_x = 800
platno_y = 600

platnoDim = (platno_x,platno_y)
bela = (255,255,255)
zelena = (0,180,0)
crna = (0,0,0)

boing = pygame.mixer.Sound("boing.wav")
platno = pygame.display.set_mode((platno_x,platno_y))
ura = pygame.time.Clock()

g0 = 40/FPS

def animacija():
    ## pozicja miške, čene je "is not defined"
    miska = (0,0)
    miska1 = (0,0) # hittrost miške
    hitrost_miska_x = 0
    hitrost_miska_y = 0
    slovar_krogcev = {}
    n=1
    slovar_krogcev[str(1)] = kr.krog((200,200),20,(0,0),g0,ro=0.7)
    #slovar_krogcev[str(2)] = kr.krog((400,400),20,(0,0),g0,ro=0.7)

    izhod = False
    while not izhod:
        for krogec in slovar_krogcev.values():
            if krogec.pozicija[1]+krogec.radij != platnoDim[1]-100:
                krogec.pospesi()

            if krogec.proznost == 1:
                magicniFaktor = 0
            else:
                magicniFaktor = 2
            
            miska = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #ko pritisnemo križec
                        izhod = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and krogec.klik_z_misko(miska):

                        krogec.primi_z_misko(miska)
                if event.type == pygame.MOUSEBUTTONUP and krogec.pritisnjen == True:
                    if event.button == 1:
                        krogec.pritisnjen = False
                        krogec.gravitacija = g0
                        krogec.hitrost = (hitrost_miska_x,hitrost_miska_y)
            if krogec.pritisnjen:
                krogec.pozicija = (miska[0] - krogec.prijem[0],miska[1] - krogec.prijem[1])
            platno.fill(bela)
            boing.set_volume((1/200)*((krogec.hitrost[0]**2+krogec.hitrost[1]**2)**(1/2)))
            if krogec.na_tleh(platnoDim[1]-100):
                pygame.mixer.Sound.play(boing)
                krogec.hitrost = (krogec.hitrost[0]*0.95,-(krogec.hitrost[1]-magicniFaktor*krogec.gravitacija)*krogec.proznost) 
                krogec.pozicija = (krogec.pozicija[0],-krogec.radij + platnoDim[1]-100)

            if krogec.igraj:
                pygame.mixer.Sound.play(boing)
                krogec.igraj = False
              
            krogec.zaleti_v_rob(platnoDim)
            krogec.pozicija = (krogec.pozicija[0] + krogec.hitrost[0],krogec.pozicija[1] + krogec.hitrost[1]) 
            ura.tick(FPS)
            miska1 = pygame.mouse.get_pos()
            hitrost_miska_x = (miska1[0]-miska[0])
            hitrost_miska_y = (miska1[1]-miska[1])
            
        for krogec in slovar_krogcev.values():
            pygame.draw.rect(platno,zelena,[0,platnoDim[1]-100,platnoDim[0],platnoDim[1]])
            pygame.draw.circle(platno,crna,[int(krogec.pozicija[0]),int(krogec.pozicija[1])],krogec.radij,0)
        pygame.display.update()
            
    pygame.quit()
    quit()

animacija()
