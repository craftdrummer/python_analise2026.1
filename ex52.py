# Desenvolva um código python que leia 3 notas
# e calcule a média. Se a média for maior ou igual a 6
# imprima aprovado, senão imprima recuperação
# Identação
n1 = float(input("Digite a primeira nota => "))
n2 = float(input("Digite a segunda nota => "))
n3 = float(input("Digite a terceira nota=> "))
media = (n1 + n2 + n3) / 3
print(f"media final: {media}")
if media >= 6:
    print("Aprovado")
else:
    print("Recuperção")