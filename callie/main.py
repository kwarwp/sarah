# sarah.callie.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from _spy.vitollino.main import INVENTARIO as inv

STYLE['width'] = 700

BARBIE = "http://4.bp.blogspot.com/-x3s2-mSb_pg/UcsTQuFUwuI/AAAAAAAANVs/5NQp3g72WQE/s1600/9.jpg"
CINDERELA = "https://1.bp.blogspot.com/-V2tLZSbQiXk/WD8fBBsCwDI/AAAAAAAACAo/ik35d327hAAa6YfTwuN-tD2RozNXOgzpwCLcB/s1600/23.png"
HOMEM ARANHA = "https://2.bp.blogspot.com/-Sx288TzGsV0/V5E7WpC1S2I/AAAAAAAALNE/46iReRzHSMslkQKxOgLr6jb5Pl4LTXEnwCLcB/s1600/B78144.jpg"
MESTRE YODA = "https://1.bp.blogspot.com/-R9novqwzprA/V1LnhAeWayI/AAAAAAAAEuQ/6jOkfjgu6KsauBmAMBGBuWZmRHpkoa8QACLcB/s1600/Yodar.png"
TARZAN = "https://vignette.wikia.nocookie.net/vsdebating/images/6/68/Tarzan.png/revision/latest?cb=20170707201517"
FLORESTA = "https://img.elo7.com.br/product/zoom/1360B4C/painel-floresta-g-frete-gratis-lona-festa-infantil.jpg"
CASTELO = "https://vignette.wikia.nocookie.net/ouat/images/a/af/Castelo.png/revision/latest?cb=20121027032937&path-prefix=pt-br"
CIDADE = "https://img.elo7.com.br/product/zoom/1ABC2E1/painel-adesivo-decorativo-cidade-painel-decorativo-de-parede.jpg"
PANTANO = "https://www.meusonhar.com.br/wp-content/uploads/2016/12/sonhar-com-pantano-e1483464058111.jpg"

def game():
    floresta = Cena(img=FLORESTA)
    floresta2 = Cena(img=FLORESTA)
    castelo = Cena(img=CASTELO)
    floresta3 = Cena(img=FLORESTA)
    cidade = Cena(img=CIDADE)
    pantano = Cena(img=PANTANO)
    