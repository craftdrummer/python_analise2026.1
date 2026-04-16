# Desenvolva um código python que envie um valor
# para uma função que verifique se o número
# é ímpar ou par
def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return (f"O número {numero} é par")
    else:
        return (f"O número {numero} é impar")
try:
    valor = int(input("Digite um número inteiro: "))
    resultado = verificar_par_ou_impar(valor)
    print(resultado)
except ValueError:
    print("Erro: Por favor, digite apenas números inteiros")