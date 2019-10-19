#from resumo import *

class Leia_Resumos:
    
    def __init__(self):
        self.__resumos = []
        
        arquivo = open("resumos.txt", "r")
        resumos = arquivo.readlines()
        arquivo.close()
        
        nome_da_imagem = resumos[0][0:-1]
        nome_da_mulher = resumos[1][0:-1]
        resumo = ""
        
        for num in range(0, len(resumos)):
            
            if("jpg" in resumos[num]):
                nome_da_imagem = resumos[num][0:-1] 
                nome_da_mulher = resumos[num + 1][0:-1]
            elif(resumos[num] == "\n"):
                resumo_obj = Resumo(nome_da_mulher, nome_da_imagem, resumo[len(nome_da_mulher) + 1:-1])
                self.__resumos.append(resumo_obj)
                resumo = ""
                continue
            else:
                resumo += resumos[num]
        
    def get_lista_de_resumos(self):
        return self.__resumos


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
