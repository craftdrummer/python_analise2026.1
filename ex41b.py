#Desenvolva um código python usando while
#que digite um nome e imprima, e só pare
#o programa ao digitar "sair"
#!= -> diferente
#break
nome = ""
while nome != "sair":
    nome = input("digite um nome => ")
    print(f"Olá {nome}")