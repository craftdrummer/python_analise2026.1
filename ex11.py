n1 = float(input("Digite a nota 1 ")) #string - dados em forma de texto
n2 = float(input("Digite a nota 2 "))
n3 = float(input("Digite a nota 3 "))
m = (n1 + n2 + n3) / 3
print(f"Sua média é => {m}")
if m >= 6:
    print("Aprovado")
else:
    print("Recuperação")