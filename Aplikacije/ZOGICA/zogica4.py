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
    def __init__(self,poz,r,v=(0,0),g=10,pritisnjen = False,prijem = (0,0)):
        self.pozicija = poz
        self.radij = r
        self.gravitacija = g
        self.hitrost = v
        self.pritisnjen = pritisnjen
        self.prijem = prijem

    def pospesi(self):
        """Zaradi gravitacije krogec pospešuje"""
        vx = 0
        vy = self.hitrost[1] + self.gravitacija
        self.hitrost = (vx,vy)

    def na_tleh(self,tla):
        """Preverimo ali se krog dotika tal."""
        if self.pozicija[1] + self.radij >= tla:
            return True
        return False

        
    def klik_z_misko(self,miska_poz):
        """Preverimo ali je krog kliknjen z misko."""
        if (self.pozicija[0]-miska_poz[0])**2 + (self.pozicija[1]-miska_poz[1])**2 <= self.radij**2:
            return True
        return False
    
    def primi_z_misko(self,miska_poz):
        """Krog primemo z misko, in si zapomnimo kje smo ga prijeli."""
        self.hitrost = (0,0)
        self.gravitacija = 0
        self.pritisnjen = True
        self.prijem = (miska_poz[0]-self.pozicija[0],miska_poz[1]-self.pozicija[1])



def zogica():
    g0 = 25/FPS                     #nastavimo željeno gravitacijo
    pozicija = (200,200)
    radij = 25                     #podatki o žogici
    
    krogec = krog(pozicija,radij,g=g0)  #naredimo objekt s podatki
    
    izhod = False
    while not izhod:
        miska = pygame.mouse.get_pos()
        krogec.pospesi()
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
                    krogec.hitrost = (0,0)
        krogec.pozicija = (krogec.pozicija[0] ,krogec.pozicija[1] + krogec.hitrost[1])
        if krogec.pritisnjen:
            krogec.pozicija = (miska[0] - krogec.prijem[0],miska[1] - krogec.prijem[1])
        if krogec.na_tleh(platnoDim[1]-100):
            krogec.hitrost = (0,0)
            krogec.pozicija = (krogec.pozicija[0],-krogec.radij + platnoDim[1]-100)
        
        ura.tick(FPS)
        platno.fill(bela)
        pygame.draw.rect(platno,zelena,[0,platnoDim[1]-100,platnoDim[0],platnoDim[1]])                   #narišemo tla
        pygame.draw.circle(platno,crna,[int(krogec.pozicija[0]),int(krogec.pozicija[1])],krogec.radij,0) #krogec narišemo
        pygame.display.update()
            
    pygame.quit()
    quit()

zogica()        
