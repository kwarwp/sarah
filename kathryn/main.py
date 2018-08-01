# sarah.kathryn.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from _spy.vitollino.main import INVENTARIO as inv

STYLE['width'] = 700

BARBIE = "http://pngimg.com/uploads/barbie/barbie_PNG34.png"
HOMEM_ARANHA = "https://2.bp.blogspot.com/-Sx288TzGsV0/V5E7WpC1S2I/AAAAAAAALNE/46iReRzHSMslkQKxOgLr6jb5Pl4LTXEnwCLcB/s1600/B78144.jpg"
ALICE = "https://3.bp.blogspot.com/-o7Y78sYGkjY/V6O1G7WysSI/AAAAAAAAMO8/IG0Q7cJKKcYA70fLNINSaLG02t9fQT52QCLcB/s1600/ALICE%2B%25283%2529.png"
FLORESTA = "https://vignette.wikia.nocookie.net/producaocultural/images/9/96/Floresta_Sombria.png/revision/latest?cb=20110605015107&path-prefix=pt-br"
CASTELO = "https://img.elo7.com.br/product/zoom/14C140D/painel-banner-paisagem-castelo-3-00x2-00-paisagem-castelo.jpg"
CIDADE = "https://png.pngtree.com/element_origin_min_pic/16/12/28/72a8682347bade87f11b895fb8a2b2d6.jpg" 

def game():
    castelo = Cena(img=CASTELO)
    floresta = Cena(img=FLORESTA)
    cidade = Cena(img=CIDADE)
    castelo.direita = floresta
    floresta.direita = cidade
    cidade.esquerda = floresta
    floresta.esquerda = castelo
    
    barbie = Elemento(img=BARBIE, 
    tit="Barbie", style=dict(left=300, 
    top=100, width=50, height="200px"))
    barbie.entra(castelo)
    
    castelo.vai()
    
    
game()
    