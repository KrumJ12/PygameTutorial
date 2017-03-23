import pygame

pygame.init()

platno_x = 800
platno_y = 600


bela = (255,255,255)
crna = (0,0,0)

platno = pygame.display.set_mode((platno_x,platno_y))


class krog():
    def __init__(self,poz,r):
        self.pozicija = poz
        self.radij = r
        


def zogica():
    pozicija = (200,200)
    radij = 25                     
    
    krogec = krog(pozicija,radij)  
    
    izhod = False
    while not izhod:
        
        for dogodek in pygame.event.get():
            if dogodek.type == pygame.QUIT: 
                izhod = True
                
        platno.fill(bela)
        pygame.draw.circle(platno,crna,[int(krogec.pozicija[0]),int(krogec.pozicija[1])],krogec.radij,0) #krogec narišemo
        pygame.display.update()
            
    pygame.quit()
    quit()
    

zogica()        
