function skrijkviz(){
    var div = document.getElementById('vidnostKviza');
    if (div.style.display !== 'none') {
        div.style.display = 'none';
    }
    else {
        div.style.display = 'block';
    }
}

function initialise(i) {
	document.getElementById("vprasanje").innerHTML = vprasanja[i];
	document.getElementById("odg1").innerHTML = odgovor1[i];
	document.getElementById("odg2").innerHTML = odgovor2[i];
	document.getElementById("odg3").innerHTML = odgovor3[i];
	document.getElementById("odg4").innerHTML = odgovor4[i];
}

function konec() {
	smoKonec=true;
	var pravilnih=0;
	for	(i= 0; i < vprasanja.length; i++) {
		if (pravilni[i]==mojOdg[i]){
			pravilnih +=1; 
		}
	} 
	document.getElementById("trenutni").innerHTML = "Stevilo pravilnih odgovorov:"+pravilnih;
}

function potrdi(){
	if (mojOdg[stevec] <0) {
		mojOdg[stevec]=kliknil;
	}
	if (mojOdg[stevec] >= 0) {
		obarvajMe()
	}
	

}

function obarvajMe(){
	if (mojOdg[stevec] >= 0) {
		var nasOdg="odg";
		nasOdg += (mojOdg[stevec]+1);
		document.getElementById(nasOdg).className += " narobe";
		document.getElementById("odg1").setAttribute('opisnapake', obrazlozitev1[stevec]);
		document.getElementById("odg2").setAttribute('opisnapake', obrazlozitev2[stevec]);
		document.getElementById("odg3").setAttribute('opisnapake', obrazlozitev3[stevec]);
		document.getElementById("odg4").setAttribute('opisnapake', obrazlozitev4[stevec]);
	}
	var pravOdg="odg";
	pravOdg += (pravilni[stevec]+1);
	document.getElementById(pravOdg).className = "list-group-item";
	document.getElementById(pravOdg).className += " prav";

}



function naslednjeVprasanje() {
	document.getElementById("odg1").className = "list-group-item";
	document.getElementById("odg2").className = "list-group-item";
	document.getElementById("odg3").className = "list-group-item";
	document.getElementById("odg4").className = "list-group-item";
	document.getElementById("odg1").removeAttribute('opisnapake');
	document.getElementById("odg2").removeAttribute('opisnapake');
	document.getElementById("odg3").removeAttribute('opisnapake');
	document.getElementById("odg4").removeAttribute('opisnapake');
	if (mojOdg[stevec] >=0){
		obiskane[stevec]=true;	
	}
	kliknil = -1; //neodgovorjeno vprasanje oznacimo z -1


	if (stevec < vprasanja.length-2) {
		napr = napr+korak;
		document.getElementById("napredek").style.width= napr +'%';
		stevec +=1;
		initialise(stevec);
	}
	else if (stevec == vprasanja.length-2){
		napr=100;
		document.getElementById("napredek").style.width= napr + '%';
		stevec = vprasanja.length-1;
		document.getElementById("gumbKonec").innerHTML = "Pokaži rezultate!";
		initialise(stevec)
	}	
	else{
		konec()
	}
	if (mojOdg[stevec] >= 0) {
	obarvajMe()
	}		
}
 
function prejsnjeVprasanje() {
	document.getElementById("gumbKonec").innerHTML = "Naslednje vprašanje";
	document.getElementById("odg1").removeAttribute('opisnapake');
	document.getElementById("odg2").removeAttribute('opisnapake');
	document.getElementById("odg3").removeAttribute('opisnapake');
	document.getElementById("odg4").removeAttribute('opisnapake');
	document.getElementById("odg1").className = "list-group-item";
	document.getElementById("odg2").className = "list-group-item";
	document.getElementById("odg3").className = "list-group-item";
	document.getElementById("odg4").className = "list-group-item";
	
	//if (stevec > 0) {
	//	napr = napr-korak;
	//	document.getElementById("napredek").style.width= napr +'%';
	//}
	if (stevec > 0) {
		napr = napr-korak;
		document.getElementById("napredek").style.width= napr +'%';
		stevec -= 1;
    		initialise(stevec);
	}
	if (mojOdg[stevec] >= 0) {
		obarvajMe()
	}	

}

function klik0(){
	kliknil=0;	
}

function klik1(){
	kliknil=1;	
}

function klik2(){
	kliknil=2;	
}

function klik3(){
	kliknil=3;	
}



var smoKonec = false;
var obiskane=[false,false,false,false,false,false,false,false,false];
var korak = 100/9;
var napr=korak;
var kliknil=-1;
var stevec=0;
var mojOdg=[-1,-1,-1,-1,-1,-1,-1,-1,-1];

var vprasanja=["1. Kateri ukaz je nujno potreben, da poženemo funkcije iz modula Pygame?",
"2. Kako deluje koordinatni sistem v Pygame? ",
"3. Katera od spodnjih trditev predstavlja zeleno barvo v Pygame?",
"4. Kateri izraz nam definira platno velikosti 800x600?",
"5. Kako naložimo sliko Slika.png?",
"6. Kateri ukaz nam shrani sliko zarotirano za 90 stopinj v desno?",
"7. Z ukazom platno.blit(slika,[x,y]) narišemo sliko na platno na mesto (x,y). Kateri del slike predstavlja seznam koordinat[x,y]?",
"8. Kaj nam ukaz pygame.event.get() vrne? ",
"9. Z ukazom pygame.update() ... "];

var odgovor1=["pygame.init()",
"x koordinata narašča desno, y koordinata narašča navzgor",
"\"green\"",
"platno = pygame.display.set_mode((x=800,y=600))",
"slika = pygame.image('Slika.png')",
"novaSlika = pygame.rotate(slika,90)",
"točko na sredini slike",
"seznam dogodkov po vrsti",
"narišemo zadnjo sliko, ki smo jo shranili"];

var odgovor2=[
"pygame.start()", 
"x koordinata narašča levo, y koordinata narašča navzgor",
"(0,255,0)",
"platno = pygame.display((800,600))",
"slika = pygame.image.load('Slika.png')",
"novaSlika = pygame.rotate(slika,270)",
"točko v levem spodnjem vogalu",
"par(x,y), ki predstavlja koordinati miške",
"posodobimo prikaz na platnu"];

var odgovor3=["pygame.load()",
"x koordinata narašča desno, y koordinata narašča navzdol", 
"(\"0\",\"255\",\"0\")",
"platno = pygame.display((0,0),(800,600))",
"slika = pygame.image.blit('Slika.png')",
"novaSlika = pygame.transform.rotate(slika,270)",
"točko v levem zgornjem vogalu",
"vrne zadnji dogodek, ki se je zgodil",
"skočimo iz zanke"];

var odgovor4=["pygame.quit()",
"x koordinata narašča levo, y koordinata narašča navzdol",
"(255,0,0)",
"platno = pygame.display.set_mode((800,600))",
"slika = 'Slika.png' ",
"novaSlika = pygame.transform.rotate(slika,90)",
"v seznamu bi morale biti 4 koordinate od leve zgornje in desne spodnje točke",
"nič, saj je ukaz napačno zapisan",
"ne naredimo nič, saj je ukaz napačno zapisan"];

var obrazlozitev1=["pygame.init() požene funkcije v knjižnici pygame",
"Izhodišče je v zgornjem levem kotu",
"Barva v pygame je zapisana v obliki trojice",
"x in y v parametru sta odveč",
"Manjka transform nad pygame",
"Metoda rotate nad pygame ne obstaja",
"V pygame koordinate pravokotnih objektov vedno predstavljajo zgornji levi kot",
"TAKO JE",
"Ne obstaja ukaz za izris zadnje shranjene slike"];

var obrazlozitev2=["Ne obstaja ukaz pygame.start()",
"Izhodišče je v zgornjem levem kotu",
"TAKO JE",
"Potrebna je metoda set_mode nad pygame.display",
"TAKO JE",
"Manjka metoda transform nad pygame",
"V pygame koordinate pravokotnih objektov vedno predstavljajo zgornji levi kot",
"Koordinate miške dobimo z ukazom pygame.mouse.get_pos()",
"Da posodobimo prikaz na platnu manjka metoda, pravilno je pygame.display.update()"];

var obrazlozitev3=["Ukaz pygame.load() ne obstaja",
"TAKO JE",
"V naboru trojice so cela števila, ne nizi",
"Potrebna je metoda set_mode nad pygame.display in potrebujemo samo en par(velikost_X,velikost_Y)",
"S tem ukazom slike ne shranimo slike, ampak jo narišemo",
"TAKO JE",
"TAKO JE",
"Da dobimo zadnji dogodek, se moramo sprehoditi po seznamu, ki nam jih pygame.event.get() vrne",
"Za skok iz zanke uporabimo break"];

var obrazlozitev4=["pygame.quit zaključi funkcije v knjižnici pygame",
"Izhodišče je v zgornjem levem kotu",
"Nabor (255,0,0) predstavlja rdečo barvo, saj trojica predstavlja zapis v RGB",
"TAKO JE",
"S tem ukazom bi pod slika shranili le niz",
"Rotacije delujejo v nasprotni smeri urinega kazalca, torej bi sliko rotirali v levo",
"V seznamu podamo samo 1 točko (x,y), in ta predstavlja levi zgornji kot slike",
"Ukaz je pravilno zapisan",
"TAKO JE, manjka metoda nad pygame in sicer pygame.display.update(), tedaj bi posodobili prikaz na platnu"];

var pravilni=[0,2,1,3,1,2,2,0,3];




