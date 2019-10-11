from Pergunta import *

class LeiaPerguntas:

    def __init__(self):
        self.__perguntas = []

        #Variaveis temporarias
        arquivo = open("perguntas.txt", "r")
        lista_de_perguntas = arquivo.readlines()
        arquivo.close()

        #Lendo e organizando perguntas da lista_de_perguntas
        for i in range(0, len(lista_de_perguntas), 2):
            nome_da_imagem = lista_de_perguntas[i][0:-1]
            resposta = lista_de_perguntas[i + 1][0:-1]

            #armazenando dados coletados em self.__perguntas
            self.__perguntas.append(Pergunta(nome_da_imagem, resposta))

    #Função que mostra a lista de perguntas ao usuário
    def getPerguntas(self):
        return self.__perguntas
            
        
