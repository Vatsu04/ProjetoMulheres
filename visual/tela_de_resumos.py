import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Tela_de_resumos(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):

        foto = QLabel(self)
        pixmap = QPixmap("Ada.jpg")
        foto.setPixmap(pixmap)
        
        titulo = QFont("Calibri", 20)

        self.label_resumo = QLabel("""
                                              ADA LOVELACE

        Mulher otimista, a condessa de lovelace também chamada de Ada lovelace.
        Foi uma Matemática e escritora inglesa.
        Hoje é reconhecida principalmente por ter escrito o primeiro algoritmo
        para ser processado por uma máquina, a máquina analética de Charles Bobbage.
        Durante o período em que esteve envolvida com o projeto de Bobbage,
        ela desenvolveu os algoritmos que permitiram á máquina computar os
        valores de Funções Matemáticas, além de publicar uma coleção de notas
        sobre a máquina analética, por esse trabalho é a primeira programadora
        de toda a história. Recebeu op título de condessa em 1838 após seu marido,
        William Lord King ser nomeado Conde de Lovelace.
                                     """)
        self.label_resumo.setFont(titulo)

        hbox_Label = QHBoxLayout()
        hbox_Label.setAlignment(Qt.AlignCenter)
        hbox_Label.addWidget(self.label_resumo)

        vbox = QVBoxLayout()
        vbox.addWidget(foto)
        vbox.addLayout(hbox_Label)

        self.setLayout(vbox)
        self.show()

class visualiza_resumo(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        resumo = Tela_de_resumos()

        barra_de_rolagem = QScrollArea(self)
        barra_de_rolagem.setWidget(resumo)

        vbox = QVBoxLayout()
        vbox.addWidget(barra_de_rolagem)

        self.setLayout(vbox)
        self.showMaximized()
        self.show()
    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = visualiza_resumo()
    #ex = Tela_de_resumos()
    sys.exit(app.exec_())
