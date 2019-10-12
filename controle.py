import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from visual.tela_resumo import *
from modelo.leia_resumos import *

class Controle(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        
        lista_de_resumos = Leia_Resumos().get_lista_de_resumos()
        
        mulher = lista_de_resumos[0].get_nome()
        imagem = lista_de_resumos[0].get_nome_da_imagem()
        resumo = lista_de_resumos[0].get_resumo()
        
        print (imagem)
        tela_de_resumo = Roda_Resumo(self, mulher, imagem, resumo)
        
        vbox = QVBoxLayout()
        vbox.addWidget(tela_de_resumo)
        
        self.setLayout(vbox)
        self.showMaximized()
        self.show()
        
    def sair(self):
        sys.exit(app.exec_())
    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Controle()
    sys.exit(app.exec_())
