import pygame

pygame.init()

platno_x = 800
platno_y = 600

platnoDim = (platno_x,platno_y)
bela = (255,255,255)
zelena = (0,160,0)
crna = (0,0,0)

FPS = 60

platno = pygame.display.set_mode((platno_x,platno_y))
ura = pygame.time.Clock()

class krog():
    def __init__(self,poz,r,v=0,g=10):
        self.pozicija = poz
        self.radij = r
        self.gravitacija = g
        self.hitrost = v

    def pospesi(self):
        """Zaradi gravitacije krogec pospešuje"""
        v = self.hitrost + self.gravitacija
        self.hitrost = v

    def na_tleh(self,tla):
        """Preverimo ali se krog dotika tal."""
        if self.pozicija[1] + self.radij >= tla:
            return True
        return False



def zogica():
    g0 = 25/FPS                     #nastavimo željeno gravitacijo
    pozicija = (200,200)
    radij = 25                     #podatki o žogici
    
    krogec = krog(pozicija,radij,g=g0)  #naredimo objekt s podatki
    
    izhod = False
    while not izhod:
        krogec.pospesi()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #ko pritisnemo križec
                izhod = True
        krogec.pozicija = (krogec.pozicija[0] ,krogec.pozicija[1] + krogec.hitrost)

        if krogec.na_tleh(platnoDim[1]-100):
            krogec.hitrost = 0
            krogec.pozicija = (krogec.pozicija[0],-krogec.radij + platnoDim[1]-100)
        
        ura.tick(FPS)
        platno.fill(bela)
        pygame.draw.rect(platno,zelena,[0,platnoDim[1]-100,platnoDim[0],platnoDim[1]])                   #narišemo tla
        pygame.draw.circle(platno,crna,[int(krogec.pozicija[0]),int(krogec.pozicija[1])],krogec.radij,0) #krogec narišemo
        pygame.display.update()
            
    pygame.quit()
    quit()

zogica()        
