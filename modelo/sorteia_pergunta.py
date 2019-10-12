from leia_perguntas import *
from random import choice

class sorteia_pergunta:

    def __init__(self):
        self.__lista_de_perguntas = Leia_Perguntas().get_lista_de_perguntas()
        self.__perguntas_sorteadas = set()

    def get_pergunta_sorteada(self):
        pergunta_sorteada = choice(self.__lista_de_perguntas)

        while(pergunta_sorteada in self.__perguntas_sorteadas):
            pergunta_sorteada = choice(self.__lista_de_perguntas)

        self.__perguntas_sorteadas.add(pergunta_sorteada)
        return pergunta_sorteada
