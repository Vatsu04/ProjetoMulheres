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
        pixmap = QPixmap("MarieCurie.jpg")
        foto.setPixmap(pixmap)

        self.label_pergunta = QLabel("""
                                              MARIE CURIE
                                              
                Uma mulher corajosa e determinada de uma época onde
                apenas os homens iam a universidade. Descobriu um elemento
                quimico e iniciou uma verdadeira revolução no meio cientifico.
                Icniciou os estudos em “radioatividade”.

                Marie Curie e seu marido Pierre descobriram dois elementos
                quimicos,o polónio e o radio. Marie falece devido a lucemia
                causada pela longa exposição aos elementos radioativos.
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
