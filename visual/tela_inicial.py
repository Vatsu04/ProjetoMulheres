import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Tela_inicial(QWidget):
    
    def __init__(self, parent):
        super().__init__()
        
        self.initUI(parent)
        
    def initUI(self, parent):

        texto_inicial_label = QLabel("Seja bem vindo(a) ao Quiz das\n mulheres na Tecnologia\n", self)
        texto_inicial_label.move(260, 200)
        texto_inicial_label.setAlignment(Qt.AlignCenter)
        texto_inicial_label.setFont(QFont("Calibri", 40))
        
        button_iniciar = QPushButton("Iniciar", self)
        button_iniciar.resize(300, 70)
        button_iniciar.move(530, 400)
        button_iniciar.setFont(QFont("Calibri", 20))
        button_iniciar.clicked.connect(parent.iniciar)
        
        self.show()
    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Tela_inicial(self)
    sys.exit(app.exec_())
