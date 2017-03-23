import pygame
import time


pygame.mixer.pre_init(44100,-16,2, 2048)
pygame.init()


platno_x = 100
platno_y = 100
FPS = 60
ura = pygame.time.Clock()

the_entertainer = ("d54,e54,c60,c54,a60,a52,b60,b54,g50,g42,d50,d44,"
        "e50,e44,c50,c44,a50,a42,b50,b44,g40,g32,d40,d34,e40,"
        "e34,c40,c34,a40,a32,b40,b34,a40,a34,vg30,vg24,g30,g21,"
        "g10,g20,g40,b40,d40,g52,g30,b40,d44,vd44,c30,e44,c54,e30,"
        "g30,c44,e44,g20,g30,c52,g30,va40,c40,e44,c54,f20,f32,a40,"
        "c42,e20,e34,e50,c54,g30,c40,f50,d54,vf50,vd54,g20,g50,e54,"
        "e50,c54,f50,e30,g30,c40,d54,g50,e52,g20,d50,b54,f30,g30,b40,"
        "f50,d52,c30,e50,c52,e30,g30,c42,e30,g30,c42,g30,b40,d44,vd44,"
        "c30,e44,c53,e30,g30,c44,e44,g20,g30,c52,g30,va40,c40,e44,c54,"
        "f20,f32,a40,c42,e20,e32,vd20,vd30,a50,a60,c54,g40,g50,c54,"
        "d20,d30,vf40,vf50,c54,a50,a64,d30,vf30,a40,c40,c54,e54,d34,"
        "d54,vf30,a40,c40,c54,a54,g30,b40,d50,f52,g20,g32,"
        "a30,a42,b30,b40,d44,vd44,c30,e44,c54,e30,"
        "g30,c44,e44,g20,g30,c52,g30,va40,c40,e44,c54,f20,f32,a40,"
        "c42,e20,e34,e50,c54,g30,c40,f50,d54,vf50,vd54,g20,g50,e54,"
        "e50,c54,f50,e30,g30,c40,d54,g50,e52,g20,d50,b54,f30,g30,b40,"
        "f50,d52,c30,e50,c52,e30,g30,c42,e30,g30,c42,c54,d54,"
        "c30,c40,e54,c54,g30,c40,e40,d54,e54,va30,va44,"
        "c54,g30,c40,e40,d54,c50,c64,a30,a40,e54,c54,"
        "a40,c40,f40,d54,e54,vg20,vg34,c54,vg30,c40,f40,d54,c54,g20,g30,"
        "e50,g54,c50,e54,g30,c40,e40,d50,f54,e50,g54,g24,b50,d54,"
        "g30,b40,d50,f52,c30,g30,c40,c50,e52,g20,g32,"
        "a30,a42,b30,b40,d44,vd44,c30,e44,c54,e30,"
        "g30,c44,e44,g20,g30,c52,g30,va40,c40,e44,c54,f20,f32,a40,"
        "c42,e20,e34,e50,c54,g30,c40,f50,d54,vf50,vd54,g20,g50,e54,"
        "e50,c54,f50,e30,g30,c40,d54,g50,e52,g20,d50,b54,f30,g30,b40,"
        "f50,d52,c30,e50,c52,e30,g30,c42,e30,g30,c42,g30,b40,d44,vd44,"
        "c30,e44,c53,e30,g30,c44,e44,g20,g30,c52,g30,va40,c40,e44,c54,"
        "f20,f32,a40,c42,e20,e32,vd20,vd30,a50,a60,c54,g40,g50,c54,"
        "d20,d30,vf40,vf50,c54,a50,a64,d30,vf30,a40,c40,c54,e54,d34,"
        "d54,vf30,a40,c40,c54,a54,g30,b40,d50,f52,g20,g32,"
        "a30,a42,b30,b40,d44,vd44,c30,e44,c54,e30,"
        "g30,c44,e44,g20,g30,c52,g30,va40,c40,e44,c54,f20,f32,a40,"
        "c42,e20,e34,e50,c54,g30,c40,f50,d54,vf50,vd54,g20,g50,e54,"
        "e50,c54,f50,e30,g30,c40,d54,g50,e52,g20,d50,b54,f30,g30,b40,"
        "f50,d52,c30,e50,c52,e30,g30,c42,e30,g30,c42,"
        "c54,d54,c30,c40,e54,c54,g30,c40,e40,d54,e54,va30,va44,"
        "c54,g30,c40,e40,d54,c50,c64,a30,a40,e54,c54,"
        "a40,c40,f40,d54,e54,vg20,vg34,c54,vg30,c40,f40,d54,c54,g20,g30,"
        "e50,g54,c50,e54,g30,c40,e40,d50,f54,e50,g54,g24,b50,d54,"
        "g30,b40,d50,f52,c30,g30,c40,c50,e52,"   #KONEC PRVEGA DELA
        "g20,g32,c20,c34,e40,c50,e54,f40,d40,f54,vf40,vd50,vf54,"
        "c20,c30,g40,e50,g52,g30,c40,e40,a50,e50,a64,g40,e50,g54,g24,"
        "e40,c50,e54,g30,c40,e40,f40,d50,f54,vf40,vd50,vf54,c30,"
        "g40,e50,g52,g30,c40,e40,a50,e50,a64,g40,e40,g54,g24,e54,"
        "g30,c40,e40,c54,g44,f20,a54,b54,a40,c40,f40,c54,d54,f30,e54,"
        "d54,vg30,c40,f40,c54,d54,e30,g44,e54,g30,c40,e40,f54,g54,g20,a64,"
        "g54,g30,c40,e40,e54,f54,c20,c30,g40,e50,g52,g30,c40,e40,a50,e50,a64,"
        "g40,e50,g54,g24,e40,c50,e54,g30,c40,e40,f40,d40,f54,vf40,vd50,vf54,"
        "c30,g40,e50,g52,g30,c40,e40,a50,e50,a64,g40,e50,g54,e34,g54,"
        "vd30,a64,va64,d30,d50,g50,b64,d50,g50,b54,g30,b40,d44,c50,vf50,"
        "b64,d34,a64,a40,c40,d40,c50,vf54,d54,g30,b40,d40,b50,g52,"
        "f20,f32,e20,e34,e40,c50,e54,d20,d30,f40,d50,f54,vf40,vd50,vf54,"
        "c20,c30,g40,e50,g52,g30,c40,e40,a50,e50,a64,g40,e50,g54,g24,"
        "e40,c50,e54,g30,c40,e40,f40,d50,f54,vf40,vd50,vf54,c20,c30,g40,"
        "e50,g52,g30,c40,e40,a50,e50,a64,g40,e50,g54,g24,e54,g30,c40,e40,c54,"
        "g44,f20,a54,b54,a40,c40,f40,c54,d54,f30,e54,d54,vg30,c40,f40,c54,d54,"
        "e30,c52,g30,c40,e42,c34,g44,va40,c40,e40,vf44,g44,f30,a40,c40,f40,c52,"
        "f30,a40,c40,f40,a54,c54,vf30,a40,c40,vd44,a54,vf30,a40,c40,vd40,c54,a54,"
        "g30,c40,e40,g44,c54,g30,c40,e40,e54,g54,g30,c40,e44,e54,g30,c40,e40,c54,g44,"
        "d30,a40,vf40,a52,d30,a40,vf40,c52,g30,b40,f40,e54,f40,d54,g30,b44,e40,c54,"
        "c30,c42,g20,g32,e20,e34,e40,c50,e54,f40,d40,f54,vf40,vd50,vf54,"
        "c20,c30,g40,e50,g52,g30,c40,e40,a50,e50,a64,g40,e50,g54,g24,"
        "e40,c50,e54,g30,c40,e40,f40,d50,f54,vf40,vd50,vf54,c30,"
        "g40,e50,g52,g30,c40,e40,a50,e50,a64,g40,e40,g54,g24,e54,"
        "g30,c40,e40,c54,g44,f20,a54,b54,a40,c40,f40,c54,d54,f30,e54,"
        "d54,vg30,c40,f40,c54,d54,e30,g44,e54,g30,c40,e40,f54,g54,g20,a64,"
        "g54,g30,c40,e40,e54,f54,c20,c30,g40,e50,g52,g30,c40,e40,a50,e50,a64,"
        "g40,e50,g54,g24,e40,c50,e54,g30,c40,e40,f40,d40,f54,vf40,vd50,vf54,"
        "c30,g40,e50,g52,g30,c40,e40,a50,e50,a64,g40,e50,g54,e34,g54,"
        "vd30,a64,va64,d30,d50,g50,b64,d50,g50,b54,g30,b40,d44,c50,vf50,"
        "b64,d34,a64,a40,c40,d40,c50,vf54,d54,g30,b40,d40,b50,g52,"
        "f20,f32,e20,e34,e40,c50,e54,d20,d30,f40,d50,f54,vf40,vd50,vf54,"
        "c20,c30,g40,e50,g52,g30,c40,e40,a50,e50,a64,g40,e50,g54,g24,"
        "e40,c50,e54,g30,c40,e40,f40,d50,f54,vf40,vd50,vf54,c20,c30,g40,"
        "e50,g52,g30,c40,e40,a50,e50,a64,g40,e50,g54,g24,e54,"
        "g30,c40,e40,c54,g44,f20,a54,b54,a40,c40,f40,c54,d54,f30,e54,d54,"
        "vg30,c40,f40,c54,d54,e30,c52,g30,c40,e42,c34,g44,va40,c40,e40,"
        "vf44,g44,f30,a40,c40,f40,c52,f30,a40,c40,f40,a54,c54,vf30,a40,"
        "c40,vd44,a54,vf30,a40,c40,vd40,c54,a54,g30,c40,e40,g44,c54,g30,"
        "c40,e40,e54,g54,g30,c40,e44,e54,g30,c40,e40,c54,g44,d30,a40,vf40,"
        "a52,d30,a40,vf40,c52,g30,b40,f40,e54,f40,d54,g30,b44,e40,c54,"
        "c30,c42,g20,g32,c20,c32,d44,vd44,c30,e44,c54,e30,"     #KONEC DRUGEGA DELA
        "g30,c44,e44,g20,g30,c52,g30,va40,c40,e44,c54,f20,f32,a40,"
        "c42,e20,e34,e50,c54,g30,c40,f50,d54,vf50,vd54,g20,g50,e54,"
        "e50,c54,f50,e30,g30,c40,d54,g50,e52,g20,d50,b54,f30,g30,b40,"
        "f50,d52,c30,e50,c52,e30,g30,c42,e30,g30,c42,g30,b40,d44,vd44,"
        "c30,e44,c53,e30,g30,c44,e44,g20,g30,c52,g30,va40,c40,e44,c54,"
        "f20,f32,a40,c42,e20,e32,vd20,vd30,a50,a60,c54,g40,g50,c54,"
        "d20,d30,vf40,vf50,c54,a50,a64,d30,vf30,a40,c40,c54,e54,d34,"
        "d54,vf30,a40,c40,c54,a54,g30,b40,d50,f52,g20,g32,"
        "a30,a42,b30,b40,d44,vd44,c30,e44,c54,e30,"
        "g30,c44,e44,g20,g30,c52,g30,va40,c40,e44,c54,f20,f32,a40,"
        "c42,e20,e34,e50,c54,g30,c40,f50,d54,vf50,vd54,g20,g50,e54,"
        "e50,c54,f50,e30,g30,c40,d54,g50,e52,g20,d50,b54,f30,g30,b40,"
        "f50,d52,c30,e50,c52,e30,g30,c42,e30,g30,c42,c54,d54,"
        "c30,c40,e54,c54,g30,c40,e40,d54,e54,va30,va44,"
        "c54,g30,c40,e40,d54,c50,c64,a30,a40,e54,c54,"
        "a40,c40,f40,d54,e54,vg20,vg34,c54,vg30,c40,f40,d54,c54,g20,g30,"
        "e50,g54,c50,e54,g30,c40,e40,d50,f54,e50,g54,g24,b50,d54,"
        "g30,b40,d50,f52,c30,g30,c40,c50,e52,g20,g32,c20,c30,c50,e51,"   #KONEC PRVEGA DELA DRUGIČ
        "f20,f50,a64,vg54,a40,c40,f40,f50,a62,c32,a40,c40,f40,f50,a60,"
        "c62,va30,f50,va62,va40,d40,f40,va54,a54,f30,va54,c54,va40,"
        "d40,f40,d52,d20,d50,f54,e54,a40,d40,f40,d50,f52,a32,a40,d40,f40,"
        "d50,f50,a62,g20,d50,g50,va62,va40,d40,g44,vf44,d30,g44,a54,"
        "va40,d40,va54,g54,va30,va40,d52,va40,d40,g54,d54,g20,g34,g54,"
        "vg20,vg30,d52,a30,a40,c52,a40,c40,f42,d30,f52,a40,d40,f42,"
        "e30,e54,vg54,b40,d40,e40,b64,e64,vg34,d64,"
        "b40,d40,e40,b64,c64,a40,c40,e40,a61,g30,c40,e40,va52,c32,"
        "f20,f50,a64,vg54,a40,c40,f40,f50,a62,c32,a40,c40,f40,f50,a60,"
        "c62,va30,f50,va62,va40,d40,f40,va54,a54,f30,va54,c54,va40,"
        "d40,f40,d52,d20,d50,f54,e54,a40,d40,f40,d50,f52,a32,a40,d40,f40,"
        "d50,f50,a62,g20,d50,g50,va62,va40,d40,g44,vf44,d30,g44,a54,"
        "va40,d40,va54,g54,va30,va40,d52,va40,d40,g54,d54,g20,g34,g54,"
        "vg20,vg30,d52,a30,a40,c54,f20,f34,e20,e34,d20,d24,vc20,vc30,vg40,b50,f52,"
        "f54,c20,c30,a50,c50,a64,c54,a40,c40,f44,va50,g54,c30,c44,"
        "c54,c20,c30,va50,d54,e54,f20,f30,a50,f52,b54,c54,d54,e54,f54,g54,"
        "f20,f50,a64,vg54,a40,c40,f40,f50,a62,c32,a40,c40,f40,f50,a60,"
        "c62,va30,f50,va62,va40,d40,f40,va54,a54,f30,va54,c54,va40,"
        "d40,f40,d52,d20,d50,f54,e54,a40,d40,f40,d50,f52,a32,a40,d40,f40,"
        "d50,f50,a62,g20,d50,g50,va62,va40,d40,g44,vf44,d30,g44,a54,"
        "va40,d40,va54,g54,va30,va40,d52,va40,d40,g54,d54,g20,g34,g54,"
        "vg20,vg30,d52,a30,a40,c52,a40,c40,f42,d30,f52,a40,d40,f42,"
        "e30,e54,vg54,b40,d40,e40,b64,e64,vg34,d64,"
        "b40,d40,e40,b64,c64,a40,c40,e40,a61,g30,c40,e40,va52,c32,"
        "f20,f50,a64,vg54,a40,c40,f40,f50,a62,c32,a40,c40,f40,f50,a60,"
        "c62,va30,f50,va62,va40,d40,f40,va54,a54,f30,va54,c54,va40,"
        "d40,f40,d52,d20,d50,f54,e54,a40,d40,f40,d50,f52,a32,a40,d40,f40,"
        "d50,f50,a62,g20,d50,g50,va62,va40,d40,g44,vf44,d30,g44,a54,"
        "va40,d40,va54,g54,va30,va40,d52,va40,d40,g54,d54,g20,g34,g54,"
        "vg20,vg30,d52,a30,a40,c54,f20,f34,e20,e34,d20,d24,vc20,vc30,vg40,b50,f52,"
        "f54,c20,c30,a50,c50,a64,c54,a40,c40,f44,va50,g54,c30,c44,"
        "c54,c20,c30,va50,d54,e54,f20,f30,a50,f51,f10,f20,f50,a60,c61,"        #KONEC TRETJEGA DELA
        "f30,a40,c40,f40,c52,f30,a40,c40,f40,a54,c54,vf30,a40,"
        "c40,vd44,a54,vf30,a40,c40,vd40,c54,a54,g30,c40,e40,g44,c54,g30,"
        "c40,e40,e54,g54,g30,c40,e44,e54,g30,c40,e40,c54,g44,d30,a40,vf40,"
        "a52,d30,a40,vf40,c52,g30,b40,f40,e54,f40,d54,g30,b44,e40,c54,"
        "c30,c41,c20,c30,c50,e50,g50,c61," #ZAČETEK ČETRTEGA DELA
        "f20,d40,f42,f30,a40,vc40,e44,d40,f44,a34,vc40,e44,f30,a40,d40,f42,"
        "")  

platno = pygame.display.set_mode((platno_x,platno_y))
def zaigraj(niz=""):
    global the_entertainer
    hitrost = input("Vnesi hitrost( > 1: hitreje, < 1:počasnjeje): ")
    hitrost = float(hitrost)
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
        if zapisi == "the entertainer":
            niz = the_entertainer
            break
        elif zapisi == "konec":
            break
        elif zapisi[:-1] in slovar_not:
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
                time.sleep(0.7/(hitrost*int(par[2])))
        else:
            if par[-1] == "0":
                #pygame.mixer.Sound.play(slovar_not[par[:3]])
                pygame.mixer.find_channel().play(slovar_not[par[:3]])
            else:
                #pygame.mixer.Sound.play(slovar_not[par[:3]])
                pygame.mixer.find_channel().play(slovar_not[par[:3]])
                time.sleep(0.7/(hitrost*int(par[3])))
        #time.sleep(0.1)


zaigraj()    
