# Desenvolva um código python que entre com a idade e o gênero (m ou f).
# Se a idade for maior e/ou igaul  18 e o gênero for m imprima 
# Apto ao alistamento militar. Senão imprima não apto ao alistamento militar
idade = int(input("Digite a sua idade => "))
genero = input("Digite o gênero (m para masculino / f para feminino) => ")
if idade >= 18 and genero == 'm':
    print("Apto ao alistamento militar.")
else:
    print("Não apto ao alistamento militar.")