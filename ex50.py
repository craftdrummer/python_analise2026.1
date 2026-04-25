# Desenvolva um código em python que armazene o ano atual
# E a idade de um indivíduo.
# Calcule e ache o ano de nascimento.
# Mostre o ano de nascimento.
aa = 2026
idade = int(input("Digite a sua idade => "))
an = aa - idade
print(f"Se você já fez aniversário em {aa}, seu ano de nascimento é {an}.")
print(f"Caso ainda não tenha feito, você nasceu em {an - 1}.")