import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Tela_inicial(QWidget):
    
    def __init__(self, parent):
        super().__init__()
        
        #Definindo plano de fundo das perguntas
        parent.plano_de_fundo("imagem_perguntas.jpeg")
        
        self.initUI()
        
    def initUI(self):
        
        self.show()
    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Tela_inicial()
    sys.exit(app.exec_())
