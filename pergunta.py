class Pergunta:

    def __init__(self, nome_da_pergunta, lista_de_alternativas, lista_de_mulheres):
        self.__nome_da_pergunta = nome_da_pergunta
        self.__lista_de_alternativas = lista_de_alternativas
        self.__lista_de_mulheres = lista_de_mulheres

    def get_nome_da_pergunta(self):
        return self.__nome_da_pergunta

    def get_lista_de_alternativas(self):
        return self.__lista_de_alternativas

    def get_lista_de_mulheres(self):
        return self.__lista_de_mulheres
