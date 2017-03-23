import pygame

pygame.init()

platno = pygame.display.set_mode((800,600))
crna = (0,0,0)
bela = (255,255,255)

def igra():
    risi = True
    platno.fill(bela)
    while risi:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                miska = pygame.mouse.get_pos()
                x = miska[0]
                y = miska[1]
                pygame.draw.circle(platno,crna,[x,y],int((x+y)**(1/2)),0)
        pygame.display.update()
    pygame.quit()
    quit()
    
igra()
