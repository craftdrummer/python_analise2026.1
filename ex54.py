# Desenvolva um código python que leia o salário de um funcionário
# Se o salário for maior que 5000 calcule o irrf que será 7,5% sobre o salário
# Se for menor que 5000 não paga imposto
# Se for maior que 8000 o imposto ser´de 27%
# Ao final mostre: o salário, o valor do imposto pago e salário final
sal=float(input("Digite o salário do funcionário => "))
if sal <= 5000:
    imposto = 0
elif sal <= 8000:
    imposto = sal * 0.075
else:
    imposto = sal * 0.27
salfinal = sal - imposto
print(f"salário {sal}, imposto - {imposto}, Salário Bruto {salfinal} ")