import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Tela_de_perguntas(QWidget):
    
    def __init__(self, parent, alternativa, nome_da_imagem, resposta):
        super().__init__()

        #Definindo plano de fundo das perguntas
        parent.plano_de_fundo("background.jpeg")

        self.__nome_da_imagem = imagem
        self.__nome_da_alternativa = alternativa
        self.resposta = resposta
        
        self.initUI(parent)
        
    def initUI(self, parent):

        #Criando label com texto
        label_pergunta = QLabel(" Pergunta " + str(self.__numero) , self)       
        label_pergunta.move(540, 50)

        
        # CRIAR AS IMAGENS DAS PERGUNTAS
        pixmap = QPixmap(self.__nome_da_imagem)
        label_imagem = QLabel(self)
        label_imagem.setPixmap(pixmap)
        label_imagem.move(270, 130)

        #Criando Buttons das alternativas
        buttonA = QPushButton("A", self)
        buttonB = QPushButton("B", self)
        buttonC = QPushButton("C", self)
        buttonD = QPushButton("D", self)



        #Conectando buttons a função da classe pai
        buttonA.clicked.connect(parent.verifica_resposta)
        buttonB.clicked.connect(parent.verifica_resposta)
        buttonC.clicked.connect(parent.verifica_resposta)
        buttonD.clicked.connect(parent.verifica_resposta)


        
        self.show()
    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Tela_de_perguntas()
    sys.exit(app.exec_())
