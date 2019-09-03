import sys
 
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QHBoxLayout, QVBoxLayout,
                             QPushButton, QLineEdit, QGridLayout)
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Exemplo(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
    
        label = QLabel(""" PERGUNTA 01 Meu Nome eh ... """, self)
        label.move(500,100)
         
        a = QPushButton(" a) ")
        op1 = QLabel(""" OPCAO A """, self)
        op1.move(560,200) # LARGURA # ALTURA 
        
        b = QPushButton(" b) ")
        op2 = QLabel(""" OPCAO B """, self)
        op2.move(560,225)
        
        c = QPushButton(" c) ")
        op3 = QLabel(""" OPCAO C """, self)
        op3.move(560,250)

        d = QPushButton(" d) ")
        op4 = QLabel(""" OPCAO D """, self)
        op4.move(560,275)


        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(a)
        hbox.addWidget(b)
        hbox.addWidget(c)
        hbox.addWidget(d)
         
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.setWindowTitle(" Projeto Mulheres!!! ")
        self.showMaximized()
        self.show()
 
if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Exemplo()
    sys.exit(app.exec_())
