from pergunta import *

class Leia_Perguntas:

    def __init__(self):
        self.__lista_de_perguntas = []

        arquivo = open("perguntas.txt", "r")
        lista_de_perguntas = arquivo.readlines()
        arquivo.close()
        
        for indice in range(0, len(lista_de_perguntas), 15):
            nome_da_pergunta = lista_de_perguntas[indice][0:-1]
            
            lista_de_alternativas = []
            lista_de_mulheres = []
            
            contador = indice + 1
            for num in range(0, 4):
                
                alternativa = lista_de_perguntas[contador + num][0:-1]
                
                mulher_1 = lista_de_perguntas[contador + num + 1][0:-1]
                mulher_2 = lista_de_perguntas[contador + num + 2][0:-1]
                
                lista_de_alternativas.append(alternativa)
                lista_de_mulheres.append(mulher_1)
                lista_de_mulheres.append(mulher_2)
                
                contador += 2
            
            resposta = lista_de_perguntas[indice + 13][0:-1]
            
            pergunta = Pergunta(nome_da_pergunta, lista_de_alternativas, resposta, lista_de_mulheres)
            self.__lista_de_perguntas.append(pergunta)
        
    #Método que mostra a lista de perguntas ao usuário
    def get_lista_de_perguntas(self):
        return self.__lista_de_perguntas
