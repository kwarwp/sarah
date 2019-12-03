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
BILHETE = "https://i.imgur.com/DANjfy8.png"
STYLE ["width"] = 1320
STYLE ["height"] = "600px"

#INICIO DO JOGO
class gameInicio:
    def __init__(self):
        gameInicio = Cena(CENAINICIO)
        gameInicio.vai()
        self.play = Elemento(PLAY, x=560, y=470,w=180,h=120, cena=gameInicio, vai = self.mostradia)
    
    def mostradia(self,ev=0):
        fake = Cena()
        fake.vai = self.elevador
        dia = Cena(FUNDODIA, direita=fake )
        dia.vai()
        self.bil = Elemento(BILHETE, x=500, y=120,w=400,h=400, cena=dia, vai = self.elevador)
    
    def elevador(self, ev=0):
        todos = Cena(FUNDODIA)
        todos.vai()
        self.predio = Elemento(PREDIO, x=500, y=120,w=400,h=400, cena=todos, vai=self.sobe_desce)
        #predio.vai()
        
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
    
gameInicio()

