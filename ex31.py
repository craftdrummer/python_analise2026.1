#Desenvolva um código python que leia
#10 médias de um aluno, e ao momento que está lendo
#mostre se o aluno está aprovado se for maior que 5
#ou em recuperação se for menor ou igual a 5 está em recuperação
for i in range(0,10):
    m = float(input("digite a média => "))
    if m > 5:
        print("aluno aprovado")
    else:
        print("aluno em recuperação")