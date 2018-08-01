# sarah.sara.main.py
"""A cinderela saiu para tomar um chá. Barbie iria encontrar com a Cinderela mas ainda estava em seu castelo.
como estava muito tarde o homem aranha deu uma carona para as duas. todos tomaram um susto ao encontrar o yoda na floresta."""
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from _spy.vitollino.main import INVENTARIO as inv

STYLE['width'] = 700
CINDERELA = "http://imagensemoldes.com.br/wp-content/uploads/2018/04/Imagem-de-Personagens-Cinderela-29-PNG-300x283.png"
BARBIE = "http://pngimg.com/uploads/barbie/barbie_PNG42.png"
HOMEM = "http://3.bp.blogspot.com/-uv54jlZoqfU/T9eUlpul_CI/AAAAAAAAFos/NCmWuK9X9Nw/s1600/Homem-Aranha-png-Queroimagem.com+%284%29.png"
YODA = "http://pngimg.com/uploads/starwars/starwars_PNG40.png"
CHA = "http://iphotochannel.com.br/wp-content/uploads/2016/07/iphoto-como-fazer-um-cenario-barato-pra-fotografia-2.jpg"
LUAR = "https://st3.depositphotos.com/2739581/16638/v/600/depositphotos_166383456-stock-video-scary-autumn-forest-at-moonlight.jpg"
CASTELO = "https://vignette.wikia.nocookie.net/reinodesolaria/images/1/15/Castelo_real_branco.jpg/revision/latest?cb=20120906132605&path-prefix=pt-br"

def game():
    cha = Cena(img = CHA)
    castelo = Cena(img = CASTELO)
    luar = Cena(img = LUAR)
    cha.direita = castelo
    castelo.direita = luar
    luar.esquerda = cha
    cha.vai()

game()




    
