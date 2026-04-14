#Usando while desenvolva um código python
#que some os números de 1 a 100
s = 0
c = 1
while c <= 100:
    s += c #Adiciona o valor atual de 'numero' à 'soma'
    c += 1 #Incrementa o contador para não criar um loop infinito
print(f"A soma dos números de 1 a 100 é: {s}")