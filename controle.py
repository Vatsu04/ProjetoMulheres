import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from visual.tela_de_resumo import *
from visual.tela_inicial import *
from visual.tela_de_perguntas import *
from visual.tela_final import *

from sorteia_pergunta import *
from leia_resumos import *

class Controle(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):

        self.valores_iniciais()
        
        self.tela_inicial = Tela_inicial(self)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.tela_inicial)
        
        self.setLayout(vbox)
        self.showMaximized()
        self.setWindowTitle("Jogo das Mulheres")
        self.show()
        
    def sair(self):
        sys.exit(app.exec_())

    def iniciar(self):
        self.tela_inicial.setParent(None)
        self.layout().removeWidget(self.tela_inicial)

        self.proxima_pergunta()

    def proxima_pergunta(self):

        if(self.cont > 0):
            self.tela_de_pergunta.setParent(None)
            self.layout().removeWidget(self.tela_de_pergunta)

        
        if(self.cont == 4):
            return self.fim_de_jogo()
        
        self.pergunta_sorteada = self.sorteia_pergunta.get_pergunta_sorteada()
        
        self.tela_de_pergunta = Tela_de_Perguntas(self, self.pergunta_sorteada.get_nome_da_pergunta(),
                                                  self.pergunta_sorteada.get_lista_de_alternativas(),
                                                  self.pergunta_sorteada.get_resposta())

        self.layout().addWidget(self.tela_de_pergunta)
        
    def verifica_resposta(self):
        self.cont += 1

        if(self.tela_de_pergunta.resposta == self.sender().text()):
            for nome_da_mulher in self.pergunta_sorteada.get_lista_de_mulheres():
                if(nome_da_mulher in list(self.acertos.keys())):
                    self.acertos[nome_da_mulher] += 1

        self.proxima_pergunta()
                
    def fim_de_jogo(self):
        self.tela_final = Tela_Final(self, self.mulher_vencedora())
        self.layout().addWidget(self.tela_final)
        
    def ver_resumo(self):

        self.tela_final.setParent(None)
        self.layout().removeWidget(self.tela_final)

        obj_res = ""
        for i in range(len(self.lista_de_resumos)):
            if(self.lista_de_resumos[i].get_nome() == self.mulher_vencedora()):
                obj_res = self.lista_de_resumos[i]
                break

        print ('Ver resumo')
        
        self.tela_resumo = Roda_Resumo(self, obj_res)
        self.layout().addWidget(self.tela_resumo)
    
    def valores_iniciais(self):
        self.sorteia_pergunta = Sorteia_Pergunta()
        self.cont = 0

        self.acertos = {"Ada Lovelace": 0,
                        "Bertha Lutz": 0,
                        "Irmã Mary Kenneth Keller": 0,
                        "Jacqueline lyra": 0,
                        "Marie Curie": 0,
                        "Sônia Guimarães": 0,
                        "Mayana Zatz": 0,
                        "Katherine Johnson": 0}

        self.lista_de_resumos = Leia_Resumos().get_lista_de_resumos()
        
    def mulher_vencedora(self):
        maior_numero = max(list(self.acertos.values()))
        for mulher in self.acertos:
            if(maior_numero == self.acertos[mulher]):
                return mulher
            
    def reiniciar(self):
        self.valores_iniciais()

        self.tela_resumo.setParent(None)
        self.layout().removeWidget(self.tela_resumo)

        self.tela_inicial = Tela_inicial(self)
        self.layout().addWidget(self.tela_inicial)
    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Controle()
    sys.exit(app.exec_())
