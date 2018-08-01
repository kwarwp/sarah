# sarah.natalia.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from _spy.vitollino.main import INVENTARIO as inv

STYLE['width'] = 700

TARZAN = "https://vignette.wikia.nocookie.net/vsbattles/images/6/68/Tarzan.png/revision/latest/scale-to-width-down/399?cb=20170117061234"
CASA = "http://pngimg.com/uploads/house/house_PNG50.png"
CASA_2 = "http://pngimg.com/uploads/house/house_PNG50.png"
HOMEMARANHA = "http://i.imgur.com/DuuGIgb.png"
HOMEMARANHA_SUSTO = "https://vignette.wikia.nocookie.net/spiderman/images/9/93/Spidey_4.png/revision/latest?cb=20140816174042"
CASTELO = "https://gallery.yopriceville.com/var/resizes/Free-Clipart-Pictures/Castles-PNG/Pink_Castle_PNG_Clipart_Image.png?m=1507172106"
CASTELO_INTERIOR = "http://www.willpearson.co.uk/wp-content/images/studio-blog/windsor_castle_001.jpg"
CINDERELA = "https://2.bp.blogspot.com/--O7PEMf5dgI/V1WAINEMFgI/AAAAAAAAGQg/MLO8j1u-iJEhPyuXEEVZ8hksqAfPTAYNQCLcB/s1600/cinderella-transp.png"
CINDERELA_SUSTO = "https://www.disneyclips.com/imagesnewb3/images/clipcindyshoe.gif"
CINDERELA_ENCONTRO = "https://www.disneyclips.com/imagesnewb3/images/cinderella_stairs2.gif"
PANTANO = "https://vignette.wikia.nocookie.net/starwars/images/f/f0/InYouMustGo-TCGCS.png/revision/latest?cb=20141218063223"

def game():
    tarzan = Cena(img=TARZAN)
    tarzan_casa = Elemento(img=TARZAN,style=dict(top=220, left=420, width="120px", height="120px"))
    casa = Cena(img=CASA)
    homemaranha = Cena(img=HOMEMARANHA)
    homemaranha_castelo = Elemento(img=HOMEMARANHA,style=dict(top=192, left=315, width="90px", height="90px"))
    homemaranha_susto_castelo = Elemento(img=HOMEMARANHA_SUSTO,style=dict(top=145, left=400, width="211px", height="180px"))
    castelo = Cena(img=CASTELO)
    castelo_interior = Cena(img=CASTELO_INTERIOR)
    cinderela = Cena(img=CINDERELA)
    cinderela_susto_castelo = Elemento(img=CINDERELA_SUSTO,style=dict(top=100, left=150, width="153px", height="275px"))
    cinderela_correndo = Elemento(img=CINDERELA,style=dict(top=160, left=180, width="386px", height="424px"))
    cinderela_encontro = Elemento(img=CINDERELA_ENCONTRO,style=dict(top=320, left=320, width="100px", height="123px"))
    pantano = Cena(img=PANTANO)
    casa_2 = Cena(img=CASA_2)
    
    #tarzan.direita = casa
    tarzan_casa.entra(casa)
    #casa.direita = homemaranha
    casa.direita = castelo
    homemaranha.direita = castelo
    homemaranha_castelo.entra(castelo)
    #castelo.direita = cinderela
    castelo.direita = castelo_interior
    #cinderela.direita = castelo_interior
    homemaranha_susto_castelo.entra(castelo_interior)
    cinderela_susto_castelo.entra(castelo_interior)
    castelo_interior.direita = pantano
    cinderela_correndo.entra(pantano)
    #castelo_interior.direita = cinderela
    #cinderela.direita = pantano
    pantano.direita = casa_2
    cinderela_encontro.entra(casa_2)
    
    
    fala_tarzan = Texto(casa, "Algo estranho na selva... Preciso investigar!!!")
    tarzan_casa.vai = fala_tarzan.vai
    
    susto_cinderela = Texto(castelo_interior, "Ai, meu Deus!!! Quem é você???")
    cinderela_susto_castelo.vai = susto_cinderela.vai
    
    fuga_cinderela = Texto(pantano, "Preciso me esconder... Já sei! Na casa do pântano!!!")
    cinderela_correndo.vai = fuga_cinderela.vai
    
    fala_aranha = Texto(castelo, "Cadê o Venom???")
    homemaranha_castelo.vai = fala_aranha.vai
    
    casa.vai()
    
game()