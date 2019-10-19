import sys
 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Tela_de_Resumo(QWidget):

    def __init__(self, objeto_resumo):
        super().__init__()
        self.__obj_resumo = objeto_resumo
        
        self.initUI()
        
    def initUI(self):
        
        label_nome_da_mulher = QLabel(self.__obj_resumo.get_nome())
        label_nome_da_mulher.setFont(QFont("Calibri", 30))
        label_nome_da_mulher.setAlignment(Qt.AlignCenter)

        pixmap = QPixmap(f"./{self.__obj_resumo.get_nome_da_imagem()}")
        
        label_foto = QLabel()
        label_foto.setPixmap(pixmap)
        label_foto.setAlignment(Qt.AlignCenter)

        label_resumo = QLabel(self.__obj_resumo.get_resumo())
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

    def __init__(self, parent, objeto_resumo):
        super().__init__()
        self.__obj_resumo = objeto_resumo
        
        self.initUI(parent)

    def initUI(self, parent):

        tela_resumo = Tela_de_Resumo(self.__obj_resumo)

        barra_de_rolagem = QScrollArea(self)
        barra_de_rolagem.setWidget(tela_resumo)
        
        button_reiniciar = QPushButton("Reiniciar")
        button_sair = QPushButton("Sair")

        button_reiniciar.setFont(QFont("Calibri", 20))
        button_sair.setFont(QFont("Calibri", 20))

        button_reiniciar.clicked.connect(parent.reiniciar)
        button_sair.clicked.connect(parent.sair)
        
        hbox_buttons = QHBoxLayout()
        hbox_buttons.addStretch(1)
        hbox_buttons.addWidget(button_sair)
        hbox_buttons.addWidget(button_reiniciar)
        
        vbox = QVBoxLayout()
        vbox.addWidget(barra_de_rolagem)
        vbox.addLayout(hbox_buttons)

        self.setLayout(vbox)
        self.show()
       
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Roda_Resumo()
    sys.exit(app.exec_())
