valor = float(input("Digite um valor "))
if valor < 100:
    p = valor * 0.05
    d = valor - p
elif valor < 400:
    p = valor * 0.15
    d = valor - p
else:
    p = valor *0.2
    d = valor - p
print(f"o valor de {valor} com desconto de {p} ficará em {d}")