import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Tela_de_Perguntas(QWidget):
    
    def __init__(self, parent, pergunta, lista_de_alternativas):
        super().__init__()

        self.__pergunta = pergunta
        self.__lista_de_alternativas = lista_de_alternativas
        self.__labeis_alt = []
        self.__buttons_alt = []
        self.__lista_de_letras = ["A", "B", "C", "D"]
        
        self.initUI(parent)
        
    def initUI(self, parent):

        #Criando label com texto
        label_pergunta = QLabel(self.__pergunta, self)
        label_pergunta.setAlignment(Qt.AlignCenter)
        label_pergunta.setStyleSheet("background-color: beige; color: darkgreen")
        label_pergunta.setFont(QFont("Calibri", 25, QFont.Bold))
        label_pergunta.move(300, 200)

        cont = 260
        for i in range(len(self.__lista_de_letras)):

            #Criando botões para letras das alternativas
            button_alt = QPushButton(self.__lista_de_letras[i], self)
            button_alt.setFont(QFont("Calibri", 25, QFont.Bold))
            button_alt.clicked.connect(parent.verifica_resposta)
            button_alt.resize(150, 50)
            button_alt.move(300, cont)
            
            #Criando label com alternativa
            label_alt = QLabel(self.__lista_de_alternativas[i], self)
            label_alt.setAlignment(Qt.AlignCenter)
            label_alt.setFont(QFont("Calibri", 25, QFont.Bold))
            label_alt.setStyleSheet("background-color: beige; color: darkgreen")
            label_alt.move(470, cont + 5)
            
            self.__labeis_alt.append(label_alt)
            self.__buttons_alt.append(button_alt)

            cont += 60
            
        self.showMaximized()
        self.show()
    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Tela_de_Perguntas()
    sys.exit(app.exec_())
