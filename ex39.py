#Desenvolva um código python em que
#o usuário digite um nº e irá mostrar
#a tabuada deste nº usando while
n = int(input("Digite o número para ver a tabuada: "))
c = 0
while c <= 10:
    r = n * c
    print(f"{n} x {c} = {r}")
    c += 1 #Esta linha é fundamental para evitar um loop infinito. Ela aumenta o valor do contador em 1 a cada volta, permitindo que a condição contador <= 10 eventualmente se torne falsa, encerrando o programa.