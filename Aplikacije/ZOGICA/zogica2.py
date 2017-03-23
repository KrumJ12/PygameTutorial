import pygame

pygame.init()

platno_x = 800
platno_y = 600

platnoDim = (platno_x,platno_y)
bela = (255,255,255)
crna = (0,0,0)

FPS = 60
ura = pygame.time.Clock()

platno = pygame.display.set_mode((platno_x,platno_y))



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


def zogica():
    g0 = 25/FPS                     
    pozicija = (200,200)
    radij = 25                     
    
    krogec = krog(pozicija,radij,g=g0)  
    
    izhod = False
    while not izhod:
        krogec.pospesi()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #ko pritisnemo križec
                izhod = True
        krogec.pozicija = (krogec.pozicija[0] ,krogec.pozicija[1] + krogec.hitrost)
        ura.tick(FPS)
        platno.fill(bela)
        pygame.draw.circle(platno,crna,[int(krogec.pozicija[0]),int(krogec.pozicija[1])],krogec.radij,0) #krogec narišemo
        pygame.display.update()
            
    pygame.quit()
    quit()

zogica()        
