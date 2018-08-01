# sarah.stacy.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from _spy.vitollino.main import INVENTARIO as inv

STYLE['width'] = 700

YODA = "http://3.bp.blogspot.com/-bJt5MBHwLAY/UxorHfGu7yI/AAAAAAAAJoQ/ISkePDNKDdc/s1600/Yoda+Do+or+do+not.png"
HOMEM ARANHA = "https://opcaonews.com.br/wp-content/uploads/2017/07/homem-aranha.png"
CINDERELA = "https://vignette.wikia.nocookie.net/disneyprincess/images/f/fd/Cinderellabarefoot.png/revision/latest?cb=20180601173051"
BARBIE = "http://3.bp.blogspot.com/_XVXE0u_nSqY/S-r2RF-K84I/AAAAAAAAApY/m-cVhub0zm4/s1600/Untitled+2.png"
TARZAN = "https://vignette.wikia.nocookie.net/projectcrusade/images/f/fd/Tarzan-clip-art-july03.gif/revision/latest?cb=20160903224123"
FLORESTA = "https://vignette.wikia.nocookie.net/kingdomhearts/images/a/ac/Wonderland-_Tea_Party_Garden_%28Art%29_KH.png/revision/latest?cb=20131218033510"
SHOPPING = "https://us.123rf.com/450wm/artisticco/artisticco1404/artisticco140400047/27698737-a-vector-illustration-of-scene-inside-shopping-mall.jpg?ver=6"
CASA = "https://odoruinu.files.wordpress.com/2014/07/1327.png"
PANTANO = "https://vignette.wikia.nocookie.net/grandchase/images/e/e1/Sky0.png/revision/latest?cb=20120108122805&path-prefix=pt-br"

def jogo():
    floresta =  Cena(img=FLORESTA)
    casa = Cena(img=CASA)
    floresta2 =  Cena(img=FLORESTA)
    floresta3 =  Cena(img=FLORESTA)
    pantano =  Cena(img=PANTANO)
    shopping =  Cena(img=SHOPPING)
    floresta.direita = casa
    casa.direita = floresta2
    floresta2.direita = floresta3
    floresta3.direita = pantano
    pantano.direita = shopping
    shopping
    
    
   
   
    
    