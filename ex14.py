n1 = int(input("informe o ano em que a pessoa nasceu "))
n2 = int(input("informe o ano atual "))
i = n2 - n1
if i >= 18:
    print(f"{i} a pessoa é maior de idade")
else:
    print("a pessoa não é maior de idade")