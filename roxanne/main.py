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
PANTANO = "https://cdn.xl.thumbs.canstockphoto.com.br/p%C3%A2ntano-ilustra%C3%A7%C3%A3o_csp15440725.jpg"

def game():
    cha = Cena(img=CHA)
    pantano = Cena(img=PANTANO)
    castelo = Cena(img=CASTELO)
    floresta = Cena(img=FLORESTA)
    cha.direita = pantano
    pantano.direita= castelo
    castelo.direita = floresta
    floresta.esquerda = castelo
    castelo.esquerda = pantano
    pantano.esquerda = cha
    
    alice = Elemento(img=ALICE, tit="ALICE", style=dict(left=500, top=360, width=100, height="200px"))
    alice.entra(cha)
    
    falaalice = Texto(cha, "Vou reunir meus amigos no final de semana")
    alice.vai = falaalice.vai
    
    
    cha.vai()
    
    
game()