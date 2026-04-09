#Desenvolva um código python que leia um valor
#e mostre a tabuada deste valor
v = int(input("digite um valor => "))
for i in range(0,11):
    x = i*v
    print(f"{v} X {i} = {x}")