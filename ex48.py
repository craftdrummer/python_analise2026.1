# Crie uma função que recebe dois números e 
# retorne o maior deles.
def comparar_numeros(a, b):
    r = a > b
    return r
v1 = int(input("Digite o primeiro número: "))
v2 = int(input("Digite o segundo número: "))
r = comparar_numeros(v1, v2)
print(f"O primeiro número é maior que o segundo? {r}")