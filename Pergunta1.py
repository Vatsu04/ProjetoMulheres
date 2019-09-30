import sys
 
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QHBoxLayout, QVBoxLayout,
                             QPushButton, QLineEdit, QGridLayout)
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Pergunta2 import Segunda_Pergunta

import random
'''
kj = 0 # Katherine Johnson
mz = 0 # Mayana Zats
al = 0 # Ada Lovelace
sg = 0 # Sonia Guimarães
'''

class Primeira(QWidget):

    def __init__(self, parent):
        
        super().__init__(parent)
        #QWidget.__init__(self, parent)
        self.initUI(parent)
        
    def initUI(self, parent):
        
        #Adiciona o Tamanho da Fonte
        fonte = QFont("Calibri", 20)
        
        self.label_pergunta = QLabel("""1. Em qual área você mais se identifica?
                                     """)
        #label_pergunta.setAlignment(Qt.AlignCenter)
        
        self.label_altA = QLabel("Matemática")
        self.label_altB = QLabel("Biologia")
        self.label_altC = QLabel("Português")
        self.label_altD = QLabel("Física")

        self.label_pergunta.setFont(fonte)
        self.label_altA.setFont(fonte)
        self.label_altB.setFont(fonte)
        self.label_altC.setFont(fonte)
        self.label_altD.setFont(fonte)
        
        buttonA = QPushButton("A")
        buttonB = QPushButton("B")
        buttonC = QPushButton("C")
        buttonD = QPushButton("D")

        buttonA.clicked.connect(parent.Segunda_Pergunta)
        buttonB.clicked.connect(self.button_B)
        buttonC.clicked.connect(self.button_C)
        buttonD.clicked.connect(self.button_D)

        # Adiciona o label_pergunta
        hbox_label = QHBoxLayout()
        hbox_label.addWidget(self.label_pergunta)
        
        #ButtonA e altA
        hbox_altA = QHBoxLayout()
        hbox_altA.addWidget(buttonA)
        hbox_altA.addWidget(self.label_altA)
                
        #ButtonB e altB
        hbox_altB = QHBoxLayout()
        hbox_altB.addWidget(buttonB)
        hbox_altB.addWidget(self.label_altB)

        #ButtonC e altC
        hbox_altC = QHBoxLayout()
        hbox_altC.addWidget(buttonC)
        hbox_altC.addWidget(self.label_altC)

        #ButtonD e altD
        hbox_altD = QHBoxLayout()
        hbox_altD.addWidget(buttonD)
        hbox_altD.addWidget(self.label_altD)

        '''
        vbox_Label = QVBoxLayout()
        vbox_Label.setAlignment(Qt.AlignCenter)
        vbox_Label.addLayout(hbox_label)
        '''
                
        vbox_button_e_alt = QVBoxLayout()
        vbox_button_e_alt.setAlignment(Qt.AlignCenter)
        vbox_button_e_alt.addLayout(hbox_label)
        vbox_button_e_alt.addLayout(hbox_altA)
        vbox_button_e_alt.addLayout(hbox_altB)
        vbox_button_e_alt.addLayout(hbox_altC)
        vbox_button_e_alt.addLayout(hbox_altD)
        
        #add hboxB
        #...

        self.setLayout(vbox_button_e_alt)
       # self.showMaximized()
        self.show()

        
    def button_A(self):
       ''' kj = 0 # Katherine Johnson
        kj = kj + 1 # Contador para Katherine Johnson
        print("Botão A")
        print("{}".format(kj))
       '''
#       parent.Segunda_Pergunta()
       
    def button_B(self):
        mz = 0 # Mayana Zats
        mz = mz + 1 # Contador para Mayana Zats
        print ("Botão B")
        print("{}".format(mz))
        
    def button_C(self):
        al = 0 # Ada Lovelace
        al = al + 1 # Contador para Ada Lovelace
        print ("Botão C")
        print("{}".format(al))
        
    def button_D(self):
        sg = 0 # Sonia Guimarães
        sg = sg + 1 # Contador para Sonia Guimarães
        print ("Botão D")
        print("{}".format(sg))
        
    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    #ex = Primeira()
    #ex.show()
    sys.exit(app.exec_())
