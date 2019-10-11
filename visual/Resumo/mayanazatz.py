import sys
 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import random

'''
kj = 0 # Katherine Johnson
mz = 0 # Mayana Zats
al = 0 # Ada Lovelace
sg = 0 # Sonia Guimarães
'''

class Primeira_Pergunta(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        titulo = QFont("Calibri", 20)

        foto = QLabel(self)
        pixmap = QPixmap("MayanaZatz.jpg")
        foto.setPixmap(pixmap)

        self.label_pergunta = QLabel("""
                                              MAYANA ZATZ
                                              
                Curiosa e movida pela paixão, Mayana Zatz dedica seus dias
                á pesquisa científica ,tentando descobrir os segredos para
                a longetividade e para qualidade devida. Conciliando a ciência
                com a ética,acredita que este ramo promoverá a maior revolução
                do século 21.
                                     """)

        self.label_pergunta.setFont(titulo)
        
        hbox_Label = QHBoxLayout()
        hbox_Label.setAlignment(Qt.AlignCenter)
        hbox_Label.addWidget(self.label_pergunta)

        vbox = QVBoxLayout()
        vbox.addWidget(foto)
        vbox.addLayout(hbox_Label)

        self.setLayout(vbox)
        self.show()

class Roda_Resumo(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        tela_resumo = Primeira_Pergunta()

        barra_de_rolagem = QScrollArea(self)
        barra_de_rolagem.setWidget(tela_resumo)

        vbox = QVBoxLayout()
        vbox.addWidget(barra_de_rolagem)

        self.setLayout(vbox)
        
        self.showMaximized()
        self.show()
       
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Roda_Resumo()
    #ex.show()
    sys.exit(app.exec_())
