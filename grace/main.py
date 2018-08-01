# sarah.grace.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE 
from _spy.vitollino.main import INVENTARIO as inv

STYLE['width'] = 700

TARZAN = "https://vignette.wikia.nocookie.net/disney/images/e/e2/Tarzan_Character.png/revision/latest?cb=20180126232838"
ALICE = "https://3.bp.blogspot.com/-o7Y78sYGkjY/V6O1G7WysSI/AAAAAAAAMO8/IG0Q7cJKKcYA70fLNINSaLG02t9fQT52QCLcB/s1600/ALICE%2B%25283%2529.png"
HOMEM_ARANHA = "http://3.bp.blogspot.com/-uv54jlZoqfU/T9eUlpul_CI/AAAAAAAAFos/NCmWuK9X9Nw/s1600/Homem-Aranha-png-Queroimagem.com+%284%29.png"
MESA_DE_CHA = "https://limaoflor.files.wordpress.com/2013/01/festa-alice0002.jpg"
FLORESTA = "https://img.elo7.com.br/product/original/10C700C/painel-floresta-g-frete-gratis-painel-impresso.jpg"
CIDADE = "http://amelhorcoisadaminhavida.com.br/wp-content/uploads/2018/01/Cidade-do-panama.jpg"
CASINHA = "https://media-cdn.tripadvisor.com/media/photo-s/04/61/33/29/casinha-amarela.jpg"

def game():
    mesa_de_cha = Cena(img=MESA_DE_CHA)
    floresta = Cena(img=FLORESTA)
    cidade = Cena(img=CIDADE)
    casinha = Cena(img=CASINHA)
    mesa_de_cha.direita = floresta
    floresta.direita = cidade
    cidade.direita = casinha
    casinha.esquerda = cidade
    cidade.esquerda = floresta
    floresta.esquerda = mesa_de_cha
    
    tarzan = Elemento(img=TARZAN, tit="Tarzan", style=dict(left=100, top=100, width=100, height="200px"))
    tarzan.entra(mesa_de_cha)
    mesa_de_cha.vai()
    
    
game()
