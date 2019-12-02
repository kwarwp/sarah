# sarah.roxanne.main.py
#Autor: Isabel Hortencia Garnica
from _spy.vitollino.main import Cena, Elemento, INVENTARIO, STYLE
from texto.main import Texto

#STYLE.update(width=1300, height=500)
CENAINICIO = "https://i.imgur.com/3qdowNm.jpg"
PREDIO= "https://i.imgur.com/vL9kR9Y.png"
CESTA = "https://i.imgur.com/qtw6IoO.png"
DOG = "https://i.imgur.com/ZQ9SSMz.png"
MENINOHAPPY = "https://i.imgur.com/LsinOyd.png"
MENINOSAD = "https://i.imgur.com/x3JZ93M.png"
IRMAHAPPY = "https://i.imgur.com/XZJuxnZ.png"
IRMASAD = "https://i.imgur.com/Iv9gWTD.png"
PLAY = "https://i.imgur.com/Jcnz4vj.png"
SAIR = "https://i.imgur.com/PISMKLy.png"
FUNDODIA = "https://i.imgur.com/ArB36nt.png"
FUNDONOITE = "https://i.imgur.com/2Vff3L0.png"
FOGOLARGO = "https://i.imgur.com/S1AyGFi.png"
FOGOESTREITO = "https://i.imgur.com/N93X5s1.png"
ROLDADA = "https://i.imgur.com/FvD7tcb.png"
CONFETES = "https://i.imgur.com/SIV1CTm.png"
CORDA="https://i.imgur.com/cUf3qAv.png"
STYLE ["width"] = 1250
STYLE ["height"] = "600px"

#INICIO DO JOGO
class gameInicio:
    def __init__(self):
        gameInicio = Cena(CENAINICIO)
        gameInicio.vai()
        self.play = Elemento(PLAY, x=500, y=450,w=120,h=180, cena=gameInicio)
        play.vai()
"""

class Elevador:
    def __init__(self):
        dia = Cena(FUNDODIA)
        dia.vai()
        self.predio = Elemento(PREDIO, x=300, y=100,w=180,h=180, cena=dia, vai=self.sobe_desce))
        predio.vai()
        # Musica("https://raw.githubusercontent.com/kwarwp/anita/master/bensound-creativeminds.mp3")
        self._sobe_desce = self._desce
        self._entra_sai = self._entra
        self._doggie_sobe_desce = lambda *_:None
        self._doggie_desce = lambda *_:None
        self._doggie_sobe = lambda *_:None
        self.na_cesta = "nada"
        self.cesta = Elemento(CESTA, x=300, y=100,w=180,h=180, cena=predio, vai=self.sobe_desce)
        self.doggie = Elemento(Doggie, x=350, y=80, cena=predio, vai=self.entra_sai)
        INVENTARIO.score(casa="elevador", carta=self.na_cesta, move="desce", ponto=0, valor=0, _level=0)
        a = Texto(predio, "oi", foi=lambda op="YY": Texto(predio, f"escolheu {op}").vai(), A="ee", B="uu")
        a.vai()
        #b = 
        
    def sobe_desce(self, *_):
        self.cesta.y = 400
        self._sobe_desce()
        
    def _desce(self, *_):
        self._sobe_desce = self._sobe
        self._doggie_desce()
        self.cesta.elt.style.top = 400
        INVENTARIO.score(casa="elevador", carta=self.na_cesta, move="desce", ponto=0, valor=0, _level=1)
        
    def _sobe(self, *_):
        self._sobe_desce = self._desce
        self._doggie_sobe()
        self.cesta.elt.style.top = 100
        INVENTARIO.score(casa="elevador", carta=self.na_cesta, move="sobe", ponto=0, valor=0, _level=1)
        
    def entra_sai(self, *_):
        self._entra_sai()
        
    def _move_doggie(self, tanto):
        self.doggie.elt.style.top = tanto
        
    def _entra(self, *_):
        self._entra_sai= self._sai
        self._doggie_sobe = lambda:self._move_doggie(100)
        self._doggie_desce = lambda:self._move_doggie(400)
        self.na_cesta="doggie"
        self.doggie.elt.style.left = 300
        INVENTARIO.score(casa="doggie", carta=self.na_cesta, move="entra", ponto=0, valor=0, _level=1)
        
    def _sai(self, *_):
        self._entra_sai= self._entra
        self._doggie_sobe = lambda:None
        self._doggie_desce = lambda:None
        self.na_cesta="nada"
        self.doggie.elt.style.left = 350
        INVENTARIO.score(casa="doggie", carta=self.na_cesta, move="sai", ponto=0, valor=0, _level=1)
        
Elevador()

"""
gameInicio()
"""
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

"""