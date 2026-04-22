#Desenvolva um código python que imprima
#na tela os números de 15 a 30 e diga
#cada um deles se é par ou impar
for i in range(15,31):
    print({i})
    r=i % 2
    if r % 2 == 0:
        input(f"{i} é par")
    else:
        input(f"{i} é impar")