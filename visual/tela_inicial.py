import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Tela_inicial(QWidget):
    
    def __init__(self, parent):
        super().__init__()
        
        self.initUI(parent)
        
    def initUI(self, parent):

        texto_inicial_label = QLabel("Seja bem vindo(a) ao Quiz das\nMulheres na Ciência e Tecnologia\n", self)
        texto_inicial_label.move(210, 250)
        texto_inicial_label.setAlignment(Qt.AlignCenter)
        texto_inicial_label.setFont(QFont("Heltica", 40, QFont.Bold))
        texto_inicial_label.setStyleSheet("background-color: beige; color: purple")
        
        button_iniciar = QPushButton("Iniciar", self)
        button_iniciar.resize(300, 70)
        button_iniciar.move(500, 390)
        button_iniciar.setFont(QFont("Calibri", 20, QFont.Bold))
        button_iniciar.clicked.connect(parent.iniciar)
        button_iniciar.setStyleSheet("background-color: lightblue; color: purple")
        
        self.show()
    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Tela_inicial(self)
    sys.exit(app.exec_())
