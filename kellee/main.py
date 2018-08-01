# sarah.kellee.main.py

'''Yoda estava na cidade, Depois foi encontrar a Alice para tomarem um cha, Ao fim, voltou pra casa para assistir Tarzan.'''

from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from _spy.vitollino.main import INVENTARIO as inv

STYLE['width'] = 700

YODA = "https://2.bp.blogspot.com/-V8V5RPZUD1M/V1LnlY7xeOI/AAAAAAAAEu4/lKAEq2C0z5Y1NUmrGvSdspKHiz6RiM9gACLcB/s640/Yodauur.png"
ALICE = "https://3.bp.blogspot.com/-o7Y78sYGkjY/V6O1G7WysSI/AAAAAAAAMO8/IG0Q7cJKKcYA70fLNINSaLG02t9fQT52QCLcB/s1600/ALICE%2B%25283%2529.png"
TARZAN = "https://vignette.wikia.nocookie.net/disney-infinity/images/e/e0/Young_Tarzan.png"
CIDADE = "https://s2.glbimg.com/1Wh9VrSZokI1CoRhHpdgeTapEnI=/e.glbimg.com/og/ed/f/original/2018/02/22/cidade.jpg"
CHA = "https://conteudo.imguol.com.br/c/noticias/b4/2017/09/29/cha-com-alice-minipanquecas-americanas-1506696952132_1920x1080.jpg"
CASA = "https://www.plantapronta.com.br/projetos/140/01.jpg"

def game():
    cidade = Cena(img=CIDADE)
    cha = Cena(img=CHA)
    casa = Cena(img=CASA)
    cidade.direita = cha
    cha.direita = casa
    casa.esquerda = cha
    cha.esquerda = cidade
    
    yoda = Elemento(img=YODA, tit="Yoda", style=dict(left=50, top=50, width=200, height="200px"))
    yoda.entra(cidade)
        
    falayoda = Texto(cidade, "Mim, programa fazer, padawan! (Sotaque do Yoda)")
    yoda.vai = falayoda.vai
    
    alice = Elemento(img=ALICE, tit="Alice", style=dict(left=250, top=100, width=200, height="200px"))
    alice.entra(cha)
    yodasegundo = yoda
    yodasegundo.entra(cha)
    falaalice = Texto(cha, "Cadê seu sabre de luz, yoda?")
    alice.vai = falaalice.vai
    falayodasegundo = Texto(cha, "Yoda sabre de luz no tempo perder!")
    yoda.vai = falayodasegundo.vai

    yodaterceiro = yoda
    yodaterceiro.entra(casa)
    tarzan = Elemento(img=TARZAN, tit="Tarzan", style=dict(left=400, top=50, width=200, height="200px"))
    tarzan.entra(casa)
    
    falatarzan = Texto(casa, "Hoje vou ver a Jane na Tela quente!")
    tarzan.vai = falatarzan.vai
    falayodaterceiro = Texto(casa, "Mim filme, hoje verei :)")
    yoda.vai=falayodaterceiro.vai
    cidade.vai()
    
    
game()