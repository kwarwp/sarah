# sarah.courtney.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from _spy.vitollino.main import INVENTARIO as inv

STYLE['width'] = 700

YODA = "https://upload.wikimedia.org/wikipedia/pt/6/6f/Yoda_Attack_of_the_Clones.png"
CASA_FLORESTA = "https://png.pngtree.com/element_origin_min_pic/16/07/17/17578b4cfbd4e93.jpg"
CINDERELA = "https://png.pngtree.com/element_pic/00/16/09/0957d1be2423435.jpg" 
CHA_DE_DESANIVERSARIO = "http://images1.fanpop.com/images/photos/1700000/Alice-in-Wonderland-1951-alice-in-wonderland-1758796-500-372.jpg"
HOMEM_ARANHA = "https://cdn1.mundodastribos.com/wp-admin/uploads/2011/07/homemaranha11.jpg"
CASTELO = "https://i0.wp.com/melprandatoemorlando.com.br/wp-content/uploads/2015/04/IMG_0311-copy.jpg"

def game():
    casa_floresta = Cena(img=CASA_FLORESTA)
    cha_de_desaniversario = Cena(img=CHA_DE_DESANIVERSARIO)
    castelo = Cena(img=CASTELO)
    casa_floresta.direita = cha_de_desaniversario
    cha_de_desaniversario.direita = castelo
    castelo.esquerda = cha_de_desaniversario
    cha_de_desaniversario.esquerda = casa_floresta
    
    yoda = Elemento(img=YODA, tit="Yoda", style=dict(left=300, top=100, width=50, height="200px"))
    yoda.entra(casa_floresta)
    
    casa_floresta.vai()


game()
