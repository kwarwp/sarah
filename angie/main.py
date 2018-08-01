# sarah.angie.main.py

# Yoda está no pantano meditando quando teve uma visão onde,
# Homem-aranha está no rolé na cidade e recebeu um convite.
# Passou na casa da Barbie e, juntos
# Foram ao baile funk no Castelo das Pedras.


from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from _spy.vitollino.main import INVENTARIO  as  inv


STYLE['width'] = 700

YODA = "https://vignette.wikia.nocookie.net/disney/images/9/95/Master_Yoda.png/revision/latest/scale-to-width-down/258?cb=20161024220430&path-prefix=pt-br";
HOMEMARANHA = "https://static.wixstatic.com/media/dd9c2d_63f04202d4a4430cb4d4c479ed917932~mv2.png/v1/fill/w_269,h_224,al_c,usm_0.66_1.00_0.01/dd9c2d_63f04202d4a4430cb4d4c479ed917932~mv2.png"
BARBIE = "http://1.bp.blogspot.com/-grB1NKIXwqw/UzRDyJiVLeI/AAAAAAAAdSE/v6FWRgv-2Hc/s1600/Baibie-em-png-queroimagem-cei%C3%A7a-crispim+(2).png"
GALERA = "http://3.bp.blogspot.com/_OEGFJSPEAj4/TSN_q4EI28I/AAAAAAAAM4k/_4kfgcqOYrA/s1600/tripledance_5XXXXXXX.gif"
PANTANO = "http://1.bp.blogspot.com/-pl302GLRMJA/VjycgVhnfOI/AAAAAAAAJow/ELVAKG5UFU8/s1600/Dagobah-680x306.jpg"
CIDADE = "http://www.quintaldomaracana.com.br/wp-content/uploads/2016/05/hostel-rio-de-janeiro-tijuca-maracana-foto-mauriciotravels.jpg"
CASTELO = "https://speaknowblog.files.wordpress.com/2011/10/cimg22931.jpg"
CASA = "https://vignette.wikia.nocookie.net/lifeinthedreamhouse/images/3/31/Location-barbie-dreamhouse-foyer.png/revision/latest?cb=20130701144936"


def game():
    pantano = Cena(img=PANTANO)
    cidade =  Cena(img=CIDADE)
    casa = Cena(img=CASA)
    castelo = Cena(img=CASTELO)
    
      
    pantano.direita = cidade
    cidade.direita = casa
    casa.direita = castelo
    
    #volta ao inicio
    castelo.direita = pantano
    
    castelo.esquerda = casa
    casa.esquerda = cidade
    cidade.esquerda = pantano
    
    yoda = Elemento(img=YODA, tit = "DJ Yoda", style=dict(left=300, top=100, width=150, height="100px"))
    yoda.entra(pantano)
    NOME = input("Qual é o seu nome?")
    
    falayoda = Texto(pantano, "Olá,  " + NOME + " quer ir ao baile?" ) #"Sexta-feira... Vou chamar o Homem Aranha pra dar um rolé!")
    yoda.vai =falayoda.vai
    
    homemaranha = Elemento(img=HOMEMARANHA, tit = "Homem Aranha Boyzão", style=dict(left=200, top=100, width=150, height="100px"))
    homemaranha.entra(cidade)
    falaaranha = Texto(cidade, "Ih, caraca, " + NOME +"! É nóis! Vou levar a Barbie também!")
    homemaranha.vai = falaaranha.vai
    
    barbie = Elemento(img=BARBIE, tit = "Barbie Boladona", style=dict(left=400, bottom=100, width=100, height="100px"))
    barbie.entra(casa)
    falabarbie = Texto(casa, "Mozão me ligou, aonde será que ele vai me levar?")
    barbie.vai = falabarbie.vai    
    
    
    galera = Elemento(img=GALERA, tit= "Galera do baile",style=dict(left=250, top=50, width=300, height="100px"))
    galera.entra(castelo)
    falagalera = Texto(castelo, "Esse é o baile da Gaiola")
    galera.vai = falagalera.vai
    


    pantano.vai()

game()