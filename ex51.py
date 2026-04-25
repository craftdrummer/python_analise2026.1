# Desenvolva um código que o usuário digite o peso e a altura e calcule o imc
# Pesquise a fórmula do imc e no final mostre o imc
peso = float(input("Digite o seu peso => "))
altura = float(input("Digite a sua altura => "))
imc = peso / (altura ** 2)  # ou imc = p / (a*a)
print(f"Seu imc é {imc}")