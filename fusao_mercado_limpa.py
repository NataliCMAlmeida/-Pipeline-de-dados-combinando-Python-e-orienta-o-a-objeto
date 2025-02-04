#Importação de bibliotecas
from processamento_dados import Dados

##Declaração de caminhos
path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

#Extract

dados_empresaA = Dados.leitura_dados(path_json, 'json');
#print(dados_empresaA) #<processamento_dados.Dados object at 0x7fa5f6d0ffd0> -> numero do registro da memória
print(dados_empresaA.nome_colunas)
print(dados_empresaA.qtd_linhas)
#print(dados_empresaA.__path) #atribulto privado

dados_empresaB = Dados.leitura_dados(path_csv, 'csv');
print(dados_empresaB.nome_colunas)
print(dados_empresaB.qtd_linhas)

#Dados.__leitura_csv(path_csv, 'csv')


#Transform
key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)
print(dados_empresaB.nome_colunas)

dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print (dados_fusao)
print(dados_fusao.nome_colunas)
print(dados_fusao.qtd_linhas)

#Load
path_dados_combinados = 'data_processed/dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)
print(path_dados_combinados)