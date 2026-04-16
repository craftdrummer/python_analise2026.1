# 1. Definimos a função que sabe somar
def somar(a, b):
    resultado = a + b
    return resultado
def subt(x, y):
    resulyado = x - y
    return x
#sem o return o resultado não vem
# 2. Criamos as variáveis com os valores
numero1 = 10
numero2 = 5
# 3. Chamamos a função e guardamos o que ela calculou
total = somar(numero1, numero2)
menos = subt(numero1, numero2)
# 4. Mostramos o resultado na tela
print("A soma é:", total)
print("A subtração é:", menos)
menos2 = subt(numero2, numero1)
print("A subtração é:", menos2)