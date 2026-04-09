#Desenvolva um programa que seja capaz de
#coletar uma sequência de 5 números inteiros
#fornecidos pelo usuário. Ao final da leitura
#desses valores, o programa deve calcular o
#somatório total e exibir o resultado na tela.
soma = 0
for i in range(0,5):
    n = int(input("digite um número "))
    soma = soma + n
print(f"O somatório de todos os números é {soma}")