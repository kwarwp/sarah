# sarah.roxanne.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from _spy.vitollino.main import INVENTARIO as inv

STYLE['width']=700

BARBIE = "http://4.bp.blogspot.com/-XNMtYvCUcRc/UdNuuEBNjaI/AAAAAAAA5O8/GgshXcDS_vQ/s480/barbie1-758236+(1).png"
TARZAN = "http://imagens.us/gifs/tarzan/Tarzan%20(22).png"
HOMEM_ARANHA = "http://3.bp.blogspot.com/-uv54jlZoqfU/T9eUlpul_CI/AAAAAAAAFos/NCmWuK9X9Nw/s1600/Homem-Aranha-png-Queroimagem.com+%284%29.png"
ALICE = "https://3.bp.blogspot.com/-o7Y78sYGkjY/V6O1G7WysSI/AAAAAAAAMO8/IG0Q7cJKKcYA70fLNINSaLG02t9fQT52QCLcB/s1600/ALICE%2B%25283%2529.png"
FLORESTA = "https://img.elo7.com.br/product/zoom/12F2BAA/painel-de-festa-floresta-3-painel-em-tecido.jpg"
CASTELO = "http://www.imagenspng.com.br/wp-content/uploads/2015/04/branca-de-neve-cute-castelo-03.png"
CHA = "https://img.elo7.com.br/product/zoom/1825D14/painel-para-festa-paisagem-festa-jardim-encantado-luxo.jpg"
CHADOIS = "https://img.elo7.com.br/product/zoom/1825D14/painel-para-festa-paisagem-festa-jardim-encantado-luxo.jpg"
PANTANO = "https://cdn.xl.thumbs.canstockphoto.com.br/p%C3%A2ntano-ilustra%C3%A7%C3%A3o_csp15440725.jpg"

def game():
    cha = Cena(img=CHA)
    chadois = Cena(img=CHADOIS)
    pantano = Cena(img=PANTANO)
    castelo = Cena(img=CASTELO)
    floresta = Cena(img=FLORESTA)
    cha.direita = chadois
    chadois.direita = pantano
    pantano.direita= castelo
    castelo.direita = floresta
    floresta.esquerda = castelo
    castelo.esquerda = pantano
    pantano.esquerda = chadois
    chadois.esquerda = cha
    
    alice = Elemento(img=ALICE, tit="ALICE", style=dict(left=500, top=360, width=150, height="200px"))
    alice.entra(cha)
    
    falaalice = Texto(cha, "Vou reunir meus amigos no final de semana")
    alice.vai = falaalice.vai
    
    
    homem_aranha = Elemento(img=HOMEM_ARANHA, tit="Homem Aranha", style=dict(left=400, top=300, width=200, height="200px"))
    homem_aranha.entra(chadois)
    
    falahomem_aranha = Texto(chadois, "Oba, fui convidado diz o homem aranha")
    homem_aranha.vai = falahomem_aranha.vai
    
    
    barbie = Elemento(img=BARBIE, tit="Barbie", style=dict(left=400, top=300, width=300, height="300px"))
    barbie.entra(pantano)
    
    falabarbie = Texto(pantano, "Enquanto isso Barbie se perdeu no Pantano")
    barbie.vai = falabarbie.vai
    
    alice = Elemento(img=ALICE, tit="ALICE", style=dict(left=500, top=400, width=250, height="300px"))
    alice.entra(castelo)
    
    falaalice = Texto(castelo, "Alice saiu do Castelo pois estava preocupada com a demora de Barbie")
    alice.vai = falaalice.vai
    
    tarzan = Elemento(img=TARZAN, tit="Tarzan", style=dict(left=500, top=50, width=250, height="300px"))
    tarzan.entra(floresta)
    
    falatarzan = Texto(floresta, "Tarzan em seu caminho pela floresta ajudou as meninas e caminharam para o chá")
    tarzan.vai = falatarzan.vai
    
    cha.vai()
    
    
game()