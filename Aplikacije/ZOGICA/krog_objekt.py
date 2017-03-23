

class krog():
    def __init__(self,poz,r,v=(0,0),g=10,t=0,a=(0,0),ro=1,pritisnjen = False,prijem = (0,0),igraj = False):
        self.pozicija = poz
        self.radij = r
        self.hitrost = v
        self.pospesek = a
        self.proznost = ro
        self.pritisnjen = pritisnjen
        self.gravitacija = g
        self.igraj = igraj

    def colision(self,other):
        """Preveri ali se dva kroga dotikata."""
        if (self.pozicija[0]-other.pozicija[0])**2 + (self.pozicija[1]-other.pozicija[1])**2 <= (self.radij + other.radij)**2:
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
        
    def pospesi(self):
        """Krog se pada sam, brez nase pomoci."""
        upor = .999
        v1 = self.hitrost[0]*upor + (self.pospesek[0])
        v2 = self.hitrost[1] + (self.gravitacija-self.pospesek[1])
        self.hitrost = (v1,v2)
        
    def na_tleh(self,tla):
        """Preverimo ali se krog dotika tal."""
        if self.pozicija[1] + self.radij >= tla:
            return True
        return False

    def zaleti_v_rob(self,velikost_platna):
        if self.pozicija[0]-self.radij <0:
            self.pozicija = (self.radij,self.pozicija[1])
            self.hitrost = (-self.hitrost[0]*self.proznost,self.hitrost[1])
            self.igraj = True
        elif self.pozicija[0] + self.radij > velikost_platna[0]:
            self.pozicija = (velikost_platna[0] - self.radij,self.pozicija[1])
            self.hitrost = (-self.hitrost[0]*self.proznost,self.hitrost[1])
            self.igraj = True
        if self.pozicija[1]-self.radij < 0:
            self.pozicija = (self.pozicija[0], self.radij)
            self.hitrost = (self.hitrost[0],-self.hitrost[1]*self.proznost)
            self.igraj = True
        

    

    

    
