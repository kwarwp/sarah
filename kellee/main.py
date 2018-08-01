# sarah.kellee.main.py

'''Yoda estava na cidade;
Depois foi encontrar a Alice para tomarem um cha;
Ao fim, voltou pra casa para assisitir Tarzan;
'''
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from _spy.vitollino.main import INVENTARIO as inv 

STYLE['with'] = 1000 

YODA = "https://3.bp.blogspot.com/-mnbOb6pCOVk/V0nMMYhny-I/AAAAAAAAhJE/RyTXasp8OykQIbNMJhA4R9lVlcjiuHliACLcB/s1600/star-wars-yoda-sixth-scale-hot-toys-silo-902738.png"
TARZAN = "https://vignette.wikia.nocookie.net/vsbattles/images/6/68/Tarzan.png"
ALICE = "https://2.bp.blogspot.com/-gbvgbBcZsIg/V2YHCoD6yMI/AAAAAAAAGOk/RevcsxQgQ7YhqyL5j8gDx-zrRq8MriNzACLcB/s320/1b.png"
CHA = "http://weshareideas.com.br/blog/wp-content/uploads/2016/08/cha-da-alice-1.jpg"
CASA = "https://images.homify.com/c_fill,f_auto,q_auto:eco,w_440/v1439854761/p/photo/image/538636/faz.m.alegre_ft.Marcelo_Marona_5562.jpg"
CIDADE = "https://i2.wp.com/cbncuritiba.com/wp-content/uploads/2017/05/por-do-sol-na-cidade-com-arranha-ceus_1127-192.jpg"

def game():
    cidade = Cena(img=CIDADE)
    cha = Cena(img=CHA)
    casa = Cena(img=CASA)
    cidade.direita = cha
    cha.direita = casa
    casa.direita = cidade


    yoda = Elemento(img=YODA, tit="Yoda", Stile=dict(left=250, top=250, width=50, heigth="100px"))
    yoda.entra(cidade)
    cidade.vai()


    
game()