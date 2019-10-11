class Pergunta:

    def __init__(self, nome_da_imagem, lista_de_alternativas, lista_de_mulheres, resposta):
        self.__nome_da_imagem = nome_da_imagem
	self.__lista_de_alternativas = lista_de_alternativas
	self.__lista_de_mulheres = lista_de_mulheres
        self.__resposta = resposta

    def get_nome_da_imagem(self):
        return self.__nome_da_imagem

    def get_lista_de_alternativas(self):
        return self.__lista_de_alternativas

    def get_lista_mulheres(self):
        return self.__lista_de_mulheres

    def getResposta(self):
        return self.__resposta
