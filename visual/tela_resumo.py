import sys
 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

'''
kj = 0 # Katherine Johnson
mz = 0 # Mayana Zats
al = 0 # Ada Lovelace
sg = 0 # Sonia Guimarães
'''

class Tela_de_Resumo(QWidget):

    def __init__(self, mulher, imagem, resumo):
        super().__init__()
        #self.__resumo = objeto_resumo
        self.__mulher = mulher
        self.__imagem = imagem
        self.__resumo = resumo
        
        self.initUI()
        
    def initUI(self):
        
        label_nome_da_mulher = QLabel(self.__mulher)
        label_nome_da_mulher.setFont(QFont("Calibri", 30))

        label_foto = QLabel()
        pixmap = QPixmap(f"./{self.__imagem}")
        label_foto.setPixmap(pixmap)

        label_resumo = QLabel(self.__resumo)
        label_resumo.setFont(QFont("Calibri", 20))
        
        hbox_resumo = QHBoxLayout()
        hbox_resumo.setAlignment(Qt.AlignCenter)
        hbox_resumo.addWidget(label_resumo)

        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignCenter)
        vbox.addWidget(label_nome_da_mulher)
        vbox.addWidget(label_foto)
        vbox.addLayout(hbox_resumo)

        self.setLayout(vbox)
        self.show()

class Roda_Resumo(QWidget):

    def __init__(self, parent, mulher, imagem, resumo):
        super().__init__()
        #self.__obj_resumo = objeto_resumo
        self.__mulher = mulher
        self.__imagem = imagem
        self.__resumo = resumo
        
        self.initUI(parent)

    def initUI(self, parent):

        tela_resumo = Tela_de_Resumo(self.__mulher, self.__imagem, self.__resumo)

        barra_de_rolagem = QScrollArea(self)
        barra_de_rolagem.setWidget(tela_resumo)
        
        button_reiniciar = QPushButton("Reiniciar")
        button_sair = QPushButton("Sair")
        
        button_sair.clicked.connect(parent.sair)
        
        hbox_buttons = QHBoxLayout()
        hbox_buttons.addStretch(1)
        hbox_buttons.addWidget(button_sair)
        hbox_buttons.addWidget(button_reiniciar)
        
        vbox = QVBoxLayout()
        vbox.addWidget(barra_de_rolagem)
        vbox.addLayout(hbox_buttons)

        self.setLayout(vbox)
        
        self.showMaximized()
        self.show()
       
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Roda_Resumo()
    sys.exit(app.exec_())
