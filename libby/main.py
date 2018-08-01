# sarah.libby.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from _spy.vitollino.main import INVENTARIO as inv

STYLE ['width'] = 700
CINDERELA = "https://imagensemoldes.com.br/wp-content/uploads/2018/04/Imagem-de-Personagens-Cinderela-3-PNG-211x300.png"
PANTANO = "https://get.pxhere.com/photo/tree-nature-forest-swamp-wilderness-branch-plant-sunlight-leaf-wildlife-stream-jungle-autumn-vegetation-rainforest-deciduous-wetland-woodland-habitat-tilos-ecosystem-palma-biome-old-growth-forest-natural-environment-geographical-feature-atmospheric-phenomenon-woody-plant-temperate-broadleaf-and-mixed-forest-temperate-coniferous-forest-1190614.jpg"
BARBIE = "http://1.bp.blogspot.com/-LJWdHVZII9U/UdNuaOHnodI/AAAAAAAA5Mo/N0Pv10SU_Dk/s1599/1zbrssk.png"
CASTELO = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Pa%C3%A7os_do_Concelho_de_Viana_do_Castelo.jpg/800px-Pa%C3%A7os_do_Concelho_de_Viana_do_Castelo.jpg"
ALICE = "https://3.bp.blogspot.com/-o7Y78sYGkjY/V6O1G7WysSI/AAAAAAAAMO8/IG0Q7cJKKcYA70fLNINSaLG02t9fQT52QCLcB/s400/ALICE%2B%25283%2529.png"
FLORESTA = "https://www.viajali.com.br/wp-content/uploads/2017/06/florestas-mais-incriveis-do-mundo-4.jpg"

def games():
    pantano = Cena(img=PANTANO)
    floresta = Cena(img=FLORESTA)
    castelo = Cena(img=CASTELO)
    pantano.direita = floresta
    floresta.direita = castelo
    castelo.esquerda = pantano
    
    cinderela = Elemento(img=CINDERELA, tit="cinderela",style=dict(left=300,
    top=200, width=50, height="200px"))
    cinderela.entra(pantano)
    
    falacinderela = Texto(pantano, "Me tira daqui! Socorro! Estou perdida!")
    cinderela.vai = falacinderela.vai
    
    barbie = Elemento(img=BARBIE, tit="barbie",style=dict(left=300,
    top=200, width=50, height="200px"))
    barbie.entra(floresta)
    
    falabarbie = Texto(floresta, "Me tira daqui! Socorro! Estou perdida!")
    cinderela.vai = falacinderela.vai
    
    pantano.vai()
    

games()
    