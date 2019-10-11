from LeiaPerguntas import *
from random import choice

class SorteiaPergunta:

    def __init__(self):
        self.__lista_de_perguntas = LeiaPerguntas().getPerguntas()
        self.__perguntas_sorteadas = set()

    def getPerguntaSorteada(self):
        pSorteada = choice(self.__lista_de_perguntas)

        while pSorteada in self.__perguntas_sorteadas:
            pSorteada = choice(self.__lista_de_perguntas)

        self.__perguntas_sorteadas.add(pSorteada)
        return pSorteada
