v1 = int(input("Digite o valor 1 ")) #tem que ser com int ou float
v2 = int(input("Digite o valor 2 "))
v3 = int(input("Digite o valor 3 "))
if v1 > v2 and v1 > v3:
    print(f"{v1} é maior que {v2} e {v3}") #(f"{v}) sempre
elif v2 > v1 and v2 > v3:
    print(f"{v2} é maior que {v1} e {v3}")
else:
    print(f"{v3} é maior que {v2} e {v1}")