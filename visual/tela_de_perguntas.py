import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Tela_de_Perguntas(QWidget):
    
    def __init__(self, parent, pergunta, lista_de_alternativas, resposta):
        super().__init__()

        self.__pergunta = pergunta
        self.lista_de_alternativas = lista_de_alternativas
        self.resposta = resposta

        self.initUI(parent)
        
    def initUI(self, parent):

        #Criando label com texto
        label_pergunta = QLabel("Pergunta: {}".format(self.__pergunta))
        label_pergunta.setAlignment(Qt.AlignCenter)

        #Criando label para todas as alternativas
        label_altA = QLabel(self.lista_de_alternativas[0])
        label_altB = QLabel(self.lista_de_alternativas[1])
        label_altC = QLabel(self.lista_de_alternativas[2])
        label_altD = QLabel(self.lista_de_alternativas[3])

        #Criando Buttons das alternativas
        buttonA = QPushButton("A")
        buttonB = QPushButton("B")
        buttonC = QPushButton("C")
        buttonD = QPushButton("D")

        #mudando tamanho da fonte
        label_pergunta.setFont(QFont("Calibri", 25))
        label_altA.setFont(QFont("Calibri", 25))
        label_altB.setFont(QFont("Calibri", 25))
        label_altC.setFont(QFont("Calibri", 25))
        label_altD.setFont(QFont("Calibri", 25))
        buttonA.setFont(QFont("Calibri", 25))
        buttonB.setFont(QFont("Calibri", 25))
        buttonC.setFont(QFont("Calibri", 25))
        buttonD.setFont(QFont("Calibri", 25))
        
        #Conectando buttons a função da classe pai
        buttonA.clicked.connect(parent.verifica_resposta)
        buttonB.clicked.connect(parent.verifica_resposta)
        buttonC.clicked.connect(parent.verifica_resposta)
        buttonD.clicked.connect(parent.verifica_resposta)

        hbox_altA = QHBoxLayout()
        hbox_altA.addWidget(buttonA)
        hbox_altA.addWidget(label_altA)
        
        hbox_altB = QHBoxLayout()
        hbox_altB.addWidget(buttonB)
        hbox_altB.addWidget(label_altB)
        
        hbox_altC = QHBoxLayout()
        hbox_altC.addWidget(buttonC)
        hbox_altC.addWidget(label_altC)
        
        hbox_altD = QHBoxLayout()
        hbox_altD.addWidget(buttonD)
        hbox_altD.addWidget(label_altD)
        
        vbox_tudo = QVBoxLayout()
        vbox_tudo.addWidget(label_pergunta)
        vbox_tudo.setAlignment(Qt.AlignCenter)
        vbox_tudo.addLayout(hbox_altA)
        vbox_tudo.addLayout(hbox_altB)
        vbox_tudo.addLayout(hbox_altC)
        vbox_tudo.addLayout(hbox_altD)

        self.setLayout(vbox_tudo)
        self.show()
    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Tela_de_perguntas()
    sys.exit(app.exec_())
