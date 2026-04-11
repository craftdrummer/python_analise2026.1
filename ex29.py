#Desenvolva um código python que o usuário digite
#5 valores, e após o digitar informe
#Se o valor é par ou impar
for i in range(0,5):
    x=int(input("digite um valor => "))
    r = x % 2
    if r % 2 == 0:
        input(f"o valor {x} é par")
    else:
        input(f"o valor {x} é impar")
