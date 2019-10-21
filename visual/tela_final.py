import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Tela_Final(QWidget):

    def __init__(self, parent, nome_da_mulher):
        super().__init__()
        self.__nome_da_mulher = nome_da_mulher

        self.initUI(parent)

    def initUI(self, parent):

        texto = QLabel(f"Parabéns! Você se parece com\n{self.__nome_da_mulher}")
        texto.setAlignment(Qt.AlignCenter)
        texto.setFont(QFont("Calibri", 40, QFont.Bold))
        texto.setStyleSheet("background-color: lightblue; color: purple")
        
        hbox_texto = QHBoxLayout()
        hbox_texto.setAlignment(Qt.AlignCenter)
        hbox_texto.addWidget(texto)

        button_ver_resumo = QPushButton("Ver Resumo")
        button_ver_resumo.clicked.connect(parent.ver_resumo)
        button_ver_resumo.setFont(QFont("Calibri", 20, QFont.Bold))
        button_ver_resumo.setStyleSheet("background-color: lightblue; color: purple")

        hbox_button = QHBoxLayout()
        hbox_button.addStretch(1)
        hbox_button.addWidget(button_ver_resumo)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox_texto)
        vbox.addLayout(hbox_button)

        self.setLayout(vbox)
        self.show()
        
if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Controle()
    sys.exit(app.exec_())
