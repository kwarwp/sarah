# sarah.natalia.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from _spy.vitollino.main import INVENTARIO as inv

STYLE['width'] = 700

TARZAN = "https://vignette.wikia.nocookie.net/vsbattles/images/6/68/Tarzan.png/revision/latest/scale-to-width-down/399?cb=20170117061234"
CASA = "http://pngimg.com/uploads/house/house_PNG50.png"
HOMEMARANHA = "https://www.desicomments.com/wp-content/uploads/2017/02/Spiderman-Nice-Pic-600x432.png"
CASTELO = "https://gallery.yopriceville.com/var/resizes/Free-Clipart-Pictures/Castles-PNG/Pink_Castle_PNG_Clipart_Image.png?m=1507172106"
CINDERELA = "https://2.bp.blogspot.com/--O7PEMf5dgI/V1WAINEMFgI/AAAAAAAAGQg/MLO8j1u-iJEhPyuXEEVZ8hksqAfPTAYNQCLcB/s1600/cinderella-transp.png"
PANTANO = "https://vignette.wikia.nocookie.net/starwars/images/f/f0/InYouMustGo-TCGCS.png/revision/latest?cb=20141218063223"

def game():
    tarzan = Cena(img=TARZAN)
    tarzan_casa = Elemento(img=TARZAN,style=dict(top=220, left=400, width=100, height="100px"))
    casa = Cena(img=CASA)
    homemaranha = Cena(img=HOMEMARANHA)
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
    
    casa.vai()
    
game()