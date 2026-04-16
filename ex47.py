# Crie uma função que receba o lado de um quadrado
# e retorne o valor de sua área (A = lado^2)
# l = v ** 2 => fórmula para calcular o lado
def lado(x):
    l = x ** 2
    return l
v = int(input("Digite um valor => "))
y = lado(v)
print(f"A área do quadrado com um lado de tamanho {v} é {y}")