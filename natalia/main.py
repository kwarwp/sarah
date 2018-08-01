# sarah.natalia.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from _spy.vitollino.main import INVENTARIO as inv

STYLE['width'] = 700

TARZAN = "https://vignette.wikia.nocookie.net/vsbattles/images/6/68/Tarzan.png/revision/latest/scale-to-width-down/399?cb=20170117061234"
CASA = "http://pngimg.com/uploads/house/house_PNG50.png"
HOMEMARANHA = "http://i.imgur.com/DuuGIgb.png"
CASTELO = "https://gallery.yopriceville.com/var/resizes/Free-Clipart-Pictures/Castles-PNG/Pink_Castle_PNG_Clipart_Image.png?m=1507172106"
CINDERELA = "https://2.bp.blogspot.com/--O7PEMf5dgI/V1WAINEMFgI/AAAAAAAAGQg/MLO8j1u-iJEhPyuXEEVZ8hksqAfPTAYNQCLcB/s1600/cinderella-transp.png"
PANTANO = "https://vignette.wikia.nocookie.net/starwars/images/f/f0/InYouMustGo-TCGCS.png/revision/latest?cb=20141218063223"

def game():
    tarzan = Cena(img=TARZAN)
    tarzan_casa = Elemento(img=TARZAN,style=dict(top=220, left=420, width="120px", height="120px"))
    casa = Cena(img=CASA)
    homemaranha = Cena(img=HOMEMARANHA)
    homemaranha_castelo = Elemento(img=HOMEMARANHA,style=dict(top=192, left=315, width="90px", height="90px"))
    castelo = Cena(img=CASTELO)
    cinderela = Cena(img=CINDERELA)
    pantano = Cena(img=PANTANO)
    
    tarzan.direita = casa
    tarzan_casa.entra(casa)
    casa.direita = homemaranha
    homemaranha.direita = castelo
    
    castelo.direita = cinderela
    cinderela.direita = castelo
    castelo.direita = cinderela
    cinderela.direita = pantano
    pantano.direita = tarzan
    
    fala_aranha = Texto(castelo, "Cadê o Venom???")
    homemaranha_castelo.vai = fala_aranha.vai
    homemaranha_castelo.entra(castelo)
    
    castelo.vai()
    
game()