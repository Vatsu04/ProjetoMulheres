import sys
 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Tela_de_Resumo(QWidget):

    def __init__(self, parent, nome_da_imagem):
        super().__init__()
        self.__nome_da_imagem = nome_da_imagem
        
        self.initUI(parent)
        
    def initUI(self, parent):
        
        mulher = self.__nome_da_imagem[0:-5]
        
        if(mulher == "Irmã Mary Kenneth Keller"):
            mulher = "Mary Keller"
            
        label_nome_da_mulher = QLabel(mulher, self)
        label_nome_da_mulher.move(550, 30)
        label_nome_da_mulher.setFont(QFont("Arial", 30, QFont.Bold))
        label_nome_da_mulher.setAlignment(Qt.AlignCenter)
        label_nome_da_mulher.setStyleSheet("background-color: lightblue; color: purple")

        pixmap = QPixmap(f"./{self.__nome_da_imagem}")
        label_imagem = QLabel(self)
        label_imagem.setPixmap(pixmap)
        label_imagem.move(300, 110)
        label_imagem.setAlignment(Qt.AlignCenter)
        
        button_reiniciar = QPushButton("Reiniciar", self)
        button_reiniciar.setFont(QFont("Calibri", 20, QFont.Bold))
        button_reiniciar.move(1200, 650)
        button_reiniciar.clicked.connect(parent.reiniciar)
        button_reiniciar.setStyleSheet("background-color: lightblue; color: purple")
        
        button_sair = QPushButton("Sair", self)
        button_sair.move(1100, 650)
        button_sair.setFont(QFont("Calibri", 20, QFont.Bold))
        button_sair.clicked.connect(parent.sair)
        button_sair.setStyleSheet("background-color: lightblue; color: purple")
        
        self.showMaximized()
        self.setWindowTitle("Tela de Resumo")
        self.show()

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Tela_de_Resumo()
    sys.exit(app.exec_())
