#Desenvolva um código python que leia 5 idades
#Diga se cada um é maior de idade, menor de idade ou idoso
for i in range(5):
    idade = int(input("digite a idade => "))
    if idade < 18:
        print("menor de idade")
    elif idade >= 18 and idade < 65:
        print("maior de idade")
    else:
        print("idoso")