#Desenvolva um código python que leia
#3 valores. Ao final mostre 
#qual é o maior entre os 3
i=0
maior=0
while i < 3:
    v = int(input("digite um valor => "))
    if v > maior:
        maior = v
    i=i+1
print(f"{maior}")