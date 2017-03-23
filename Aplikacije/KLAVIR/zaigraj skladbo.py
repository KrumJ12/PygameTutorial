import pygame
import time

pygame.mixer.pre_init(44100,-16,2, 2048)
pygame.init()


platno_x = 1
platno_y = 1
FPS = 60
ura = pygame.time.Clock()

the_entertainer = ("d54,e54,c60,c54,a60,a52,b60,b54,g50,g42,d50,d44,"
        "e50,e44,c50,c44,a50,a42,b50,b44,g40,g32,d40,d34,e40,"
        "e34,c40,c34,a40,a32,b40,b34,a40,a34,vg30,vg24,g30,g21,"
        "g10,g20,g40,b40,d40,g52,g30,b30,d34,vd34,c20,e34,c44,e20,"
        "g20,c34,e34,g20,g30,c42,g30,va30,c30,e34,c44,f20,f32,a30,"
        "c32,e20,e34,e50,c54,g30,c40,f50,d54,vf50,vd54,g20,g50,e54,"
        "e50,c54,f50,e30,g30,c40,d54,g50,e52,g20,d50,b54,f30,g30,b40,"
        "f50,d52,c30,e50,c52,e30,g30,c42,e30,g30,c42,g30,b30,d34,vd34,"
        "c20,e34,c43,e20,g20,c34,e34,g20,g30,c42,g30,va30,c30,e34,c44,"
        "f20,f32,a40,c42,e20,e32,vd20,vd30,a50,a60,c54,g40,g50,d20,c54,"
        "d30,vf40,vf50,c54,a50,a64,d30,vf30,a40,c40,c54,e54,d34,"
        "d54,vf30,a40,c40,c54,a54,g30,b40,d50,f52,g20,g32,"
        "a30,a42,b30,b40,d34,vd34,c20,e34,c44,e20,"
        "g20,c34,e34,g20,g30,c42,g30,va30,c30,e34,c44,f20,f32,a30,"
        "c32,e20,e34,e50,c54,g30,c40,f50,d54,vf50,vd54,g20,g50,e54,"
        "e50,c54,f50,e30,g30,c40,d54,g50,e52,g20,d50,b54,f30,g30,b40,"
        "f50,d52,c30,e50,c52,e30,g30,c42,e30,g30,c42,c54,d54,"
        "c30,c40,e54,c54,g30,c40,e40,d54,e54,va30,va44,"
        "c54,g30,c40,e40,d54,c50,c64,a30,a40,e54,c54,"
        "a40,c40,f40,d54,e54,vg20,vg34,c54,vg30,c40,f40,d54,c54,g20,g30,"
        "e50,g54,c50,e54,g30,c40,e40,d50,f54,e50,g54,g24,b50,d54,"
        "g30,b40,d50,f52,c30,g30,c40,c50,e52,g20,g32,"
        "a30,a42,b30,b40,d34,vd34,c20,e34,c44,e20,"
        "g20,c34,e34,g20,g30,c42,g30,va30,c30,e34,c44,f20,f32,a30,"
        "c32,e20,e34,e50,c54,g30,c40,f50,d54,vf50,vd54,g20,g50,e54,"
        "e50,c54,f50,e30,g30,c40,d54,g50,e52,g20,d50,b54,f30,g30,b40,"
        "f50,d52,c30,e50,c52,e30,g30,c42,e30,g30,c42,c54,d54,"
        "c30,c40,e54,c54,g30,c40,e40,d54,e54,va30,va44,"
        "c54,g30,c40,e40,d54,c50,c64,a30,a40,e54,c54,"
        "a40,c40,f40,d54,e54,vg20,vg34,c54,vg30,c40,f40,d54,c54,g20,g30,"
        "e50,g54,c50,e54,g30,c40,e40,d50,f54,e50,g54,g24,b50,d54,"
        "g30,b40,d50,f52,c30,g30,c40,c50,e52,")

platno = pygame.display.set_mode((platno_x,platno_y))
def zaigraj(niz=""):
    hitrost = input("Vnesi hitrost( > 1: hitreje, < 1:počasnjeje): ")
    hitrost = float(hitrost)
    pygame.mixer.set_num_channels(50)
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
    seznam_not = []
    
    
    for i in range(1,7):
        for znak in "abcdefg":
            for dolzina in "1248":
                nota = znak+str(i)+dolzina
                seznam_not.append(nota)
    nadaljuj = True
    print("Ko si končal, napiši konec. Primer note (a34, zadnja števka pomeni četrtinko)")
    while nadaljuj:
        zapisi = input("zapiši noto: ")
        if zapisi == "konec":
            break
        if zapisi[:-1] in slovar_not:
            niz += zapisi +","
        else:
            print("NISI ZAPISAL VELJAVNE NOTE")
    sez = niz.split(",")
    for par in sez[:-1]:
        if len(par)==3:
            if par[-1] == "0":
                #pygame.mixer.Sound.play(slovar_not[par[:2]])
                pygame.mixer.find_channel().play(slovar_not[par[:2]])
            else:
                #pygame.mixer.Sound.play(slovar_not[par[:2]])
                pygame.mixer.find_channel().play(slovar_not[par[:2]])
                time.sleep(0.8/(hitrost*int(par[2])))
        else:
            if par[-1] == "0":
                #pygame.mixer.Sound.play(slovar_not[par[:3]])
                pygame.mixer.find_channel().play(slovar_not[par[:3]])
            else:
                #pygame.mixer.Sound.play(slovar_not[par[:3]])
                pygame.mixer.find_channel().play(slovar_not[par[:3]])
                time.sleep(0.8/(hitrost*int(par[3])))
        #time.sleep(0.1)


zaigraj("d54,e54,c60,c54,a60,a52,b60,b54,g50,g42,d50,d44,"
        "e50,e44,c50,c44,a50,a42,b50,b44,g40,g32,d40,d34,e40,"
        "e34,c40,c34,a40,a32,b40,b34,a40,a34,vg30,vg24,g30,g21,"
        "g10,g20,g40,b40,d40,g52,g30,b30,d34,vd34,c20,e34,c44,e20,"
        "g20,c34,e34,g20,g30,c42,g30,va30,c30,e34,c44,f20,f32,a30,"
        "c32,e20,e34,e50,c54,g30,c40,f50,d54,vf50,vd54,g20,g50,e54,"
        "e50,c54,f50,e30,g30,c40,d54,g50,e52,g20,d50,b54,f30,g30,b40,"
        "f50,d52,c30,e50,c52,e30,g30,c42,e30,g30,c42,g30,b30,d34,vd34,"
        "c20,e34,c43,e20,g20,c34,e34,g20,g30,c42,g30,va30,c30,e34,c44,"
        "f20,f32,a40,c42,e20,e32,vd20,vd30,a50,a60,c54,g40,g50,d20,c54,"
        "d30,vf40,vf50,c54,a50,a64,d30,vf30,a40,c40,c54,e54,d34,"
        "d54,vf30,a40,c40,c54,a54,g30,b40,d50,f52,g20,g32,"
        "a30,a42,b30,b40,d34,vd34,c20,e34,c44,e20,"
        "g20,c34,e34,g20,g30,c42,g30,va30,c30,e34,c44,f20,f32,a30,"
        "c32,e20,e34,e50,c54,g30,c40,f50,d54,vf50,vd54,g20,g50,e54,"
        "e50,c54,f50,e30,g30,c40,d54,g50,e52,g20,d50,b54,f30,g30,b40,"
        "f50,d52,c30,e50,c52,e30,g30,c42,e30,g30,c42,c54,d54,"
        "c30,c40,e54,c54,g30,c40,e40,d54,e54,va30,va44,"
        "c54,g30,c40,e40,d54,c50,c64,a30,a40,e54,c54,"
        "a40,c40,f40,d54,e54,vg20,vg34,c54,vg30,c40,f40,d54,c54,g20,g30,"
        "e50,g54,c50,e54,g30,c40,e40,d50,f54,e50,g54,g24,b50,d54,"
        "g30,b40,d50,f52,c30,g30,c40,c50,e52,g20,g32,"
        "a30,a42,b30,b40,d34,vd34,c20,e34,c44,e20,"
        "g20,c34,e34,g20,g30,c42,g30,va30,c30,e34,c44,f20,f32,a30,"
        "c32,e20,e34,e50,c54,g30,c40,f50,d54,vf50,vd54,g20,g50,e54,"
        "e50,c54,f50,e30,g30,c40,d54,g50,e52,g20,d50,b54,f30,g30,b40,"
        "f50,d52,c30,e50,c52,e30,g30,c42,e30,g30,c42,c54,d54,"
        "c30,c40,e54,c54,g30,c40,e40,d54,e54,va30,va44,"
        "c54,g30,c40,e40,d54,c50,c64,a30,a40,e54,c54,"
        "a40,c40,f40,d54,e54,vg20,vg34,c54,vg30,c40,f40,d54,c54,g20,g30,"
        "e50,g54,c50,e54,g30,c40,e40,d50,f54,e50,g54,g24,b50,d54,"
        "g30,b40,d50,f52,c30,g30,c40,c50,e52,")
