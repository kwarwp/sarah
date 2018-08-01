# sarah.parisa.main.py

'''Mestre Yoda marcou um cha com alice, quando chegou, ela nao estava la e ele achou estranho
mas resolveu nao disperdicar toda aquela comida. Depois de beber o priemiro gole do cha, mestre Yoda
adormeceu e acordou em um pantano. Assim que acordou ouviu um grito: "Tarzan, nao surfe nesse lago de fogo!", 
ele reconheceu a voz: era alice Mestre Yoda tentou encontralos, mas se viu envolto num emaranhado de teias e 
no final do caminho viu um importante aliado nesta busca, seu amigo de sempre, homem aranha.
'''


from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from _spy.vitollino.main import INVENTARIO as inv
STYLE['width'] = 700

HOMEM_ARANHA = "http://3.bp.blogspot.com/-uv54jlZoqfU/T9eUlpul_CI/AAAAAAAAFos/NCmWuK9X9Nw/s1600/Homem-Aranha-png-Queroimagem.com+%284%29.png"
PANTANO = "http://4.bp.blogspot.com/-hE1u7v-c2v0/Vjq_YbcIwfI/AAAAAAAAACk/gPbNpntWPl4/s1600/P%25C3%25A2ntano%2BManchac%2B1.jpg"
TARZAN_FOGO = "https://i.imgur.com/wB93zqI.jpg"
ALICE = "http1.bp.blogspot.com-sJykitngfbQVk9VANJv_4IAAAAAAAALaQUi9Mw02CRSUs1600ALICE_TEKA%2B24.png"
YODA = "http://pngimg.com/uploads/starwars/starwars_PNG62.png"
FOGO = "http://2.bp.blogspot.com/-HOxFQa9iGv8/T6s9kuBLAAI/AAAAAAAAGiw/sjK-EuhC5gE/s1600/fire.png"
CHA = "https://i.imgur.com/TXBPGM9.jpg"
YODA_ACORDA = "https://i.imgur.com/iG00lnv.png"
TARZAN = "http://vsbattles.wikia.com/wiki/File:Tarzan.png"
def game():
    cha = Cena(img=CHA)
    yoda_acorda = Cena(img=YODA_ACORDA)
    pantano = Cena(img=PANTANO)
    tarzan_fogo = Cena(img=TARZAN_FOGO)
    cha.direita = yoda_acorda
    yoda_acorda.direita = tarzan_fogo
    tarzan_fogo.esquerda = yoda_acorda
    yoda_acorda.esquerda = cha
    
    falayoda = Texto(cha, "Onde está Alice?")
    yoda.vai = falayoda.vai
    cha.vai()
game()    
    
