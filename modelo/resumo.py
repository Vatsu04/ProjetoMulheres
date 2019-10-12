class Resumo:
    
    def __init__(self, nome, nome_da_imagem, resumo):
        self.__nome = nome
        self.__nome_da_imagem = nome_da_imagem
        self.__resumo = resumo
        
    def get_nome(self):
        return self.__nome
    
    def get_nome_da_imagem(self):
        return self.__nome_da_imagem
    
    def get_resumo(self):
        return self.__resumo
