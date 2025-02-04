#Paradigma de Orientação a Objetos
# self -> representação do objeto

import json
import csv

#classe criada pelo método construtor
class Dados:

    def __init__(self, dados):
        # self.__path = path
        # self.__tipo_dados = tipo_dados
        self.dados = dados #registro da leitura
        self.nome_colunas = self.__get_columns()
        self.qtd_linhas =  self.__size_data ()

    #Função de leitura para .json
    def __leitura_json(path): 
        dados_json = []
        with open(path, 'r') as file:
            dados_json = json.load(file)   
        return dados_json

    #Função de leitura para .csv
    def __leitura_csv(path): 
        dados_csv = []
        with open(path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter = ',')
            for row in spamreader:
                dados_csv.append(row)  
        return dados_csv

    @classmethod
    #Função de leitura que identifica o formato entre as duas opções
    def leitura_dados(cls, path, tipo_dados):
        dados = []

        if tipo_dados == 'csv':
            dados = cls.__leitura_csv(path) #método de leitura
        
        elif tipo_dados == 'json':
            dados = cls.__leitura_json(path) #método de leitura
       
        return cls(dados)
    
    #Função para acessar colunas
    def __get_columns(self):
        return list(self.dados[-1].keys())

    #Função para renomear colunas
    def rename_columns(self, key_mapping):
        new_dados = []

        for old_dict in self.dados:
                dict_temp = {}
                for old_key, value in old_dict.items():
                        dict_temp[key_mapping[old_key]] = value
                new_dados.append(dict_temp)

        self.dados = new_dados
        self.nome_colunas = self.__get_columns() 


    #Função de tamanho
    def __size_data(self):
        return len(self.dados)

    #Função de união (Método estático)
    def join(dadosA, dadosB):
           combined_list = []
           combined_list.extend(dadosA.dados)
           combined_list.extend(dadosB.dados)
           
           return Dados(combined_list)
    
    #Função tabular
    def __transformando_dados_tabela(self):
        
        dados_combinados_tabela = [self.nome_colunas]

        for row in self.dados:
            linha = []
            for colunas in self.nome_colunas:
                linha.append(row.get(colunas, 'Indisponível'))
            dados_combinados_tabela.append(linha)

        return dados_combinados_tabela

    #Função de salvamento (não usa return, pois não modifica nenhum dado)
    def salvando_dados(self, path):

        dados_combinados_tabela = self.__transformando_dados_tabela() #formato sem atualizar a classe

        with open(path, 'w') as file:
            write = csv.writer(file)
            write.writerows(dados_combinados_tabela)
