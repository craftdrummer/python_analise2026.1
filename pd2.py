import pandas as pd

dados = {
    'cargos': ["assistente", "analista", "gerente", "diretor"],
    'salarios': [1000, 2000, 3000, 4000]
}
dados_bi = pd.DataFrame(dados)
#exportando para o csv
print(dados_bi)
dados_bi.to_csv('meus_dados.csv', index=False, sep=';', enco"ding='utf-8')

print("Arquivo exportado com sucesso!")
#imprime tudo
#print(dados_bi)
#imprime a quantidade especificada dentro dos parenteses internos
#print(dados_bi.head(2))
#imprime os ultimos da lista com um número dentro dos parenteses internos definindo
#print(dados_bi.tail(3))
#print imprime o nº de linhas e colunas
#print(dados_bi.shape)
#exibe trechos específicos, no caso da linha 1 a 3
#print(dados_bi[1:3])