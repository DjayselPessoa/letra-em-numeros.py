nome = str(input("INFORME SEU NOME: "))
nome = nome.lower()
valor = 0
i = 0

while i < len(nome):
    try:
        if nome[i] in "aáãjs":
            valor = valor + 1
            print(f" {nome[i]}  -> {1} : {valor} ")
        elif nome[i] in "bkt":
            valor = valor + 2
            print(f" {nome[i]}  -> {2} : {valor} ")
        elif nome[i] in "cçlu":
            valor = valor + 3
            print(f" {nome[i]}  -> {3} : {valor} ")
        elif nome[i] in "dmv":
            valor = valor + 4
            print(f" {nome[i]}  -> {4} : {valor} ")
        elif nome[i] in "eénw":
            valor = valor + 5
            print(f" {nome[i]}  -> {5} : {valor} ")
        elif nome[i] in "foõôx":
            valor = valor + 6
            print(f" {nome[i]}  -> {6} : {valor} ")
        elif nome[i] in "gpy":
            valor = valor + 7
            print(f" {nome[i]}  -> {7} : {valor} ")
        elif nome[i] in "hqz":
            valor = valor + 8
            print(f" {nome[i]}  -> {8} : {valor} ")
        elif nome[i] in "ir":
            valor = valor + 9
            print(f" {nome[i]}  -> {9} : {valor} ")
        elif nome[i] in " ":
            pass
        else:
            raise ValueError(" - caractere especial detectado!")
        i += 1
    except ValueError as e:
        print("Inválido!", e)
        break
cont1 = 0
cont2 = 0
print(f"valor parcial: {valor}")
active = True
while active:
    print("partes em unidade: ")
    for i in str(valor):
        # print(f"valor: {len(str(valor))}")
        cont1 = cont1 + int(i)
        print(f"{cont2 + 1}º valor : {str(i)}")
        cont2 = cont2 + 1
    valor = int(cont1)
    cont1 = 0
    cont2 = 0
    if len(str(valor)) >= 2:
        print("valor atual: " + str(valor))
        continue
    elif len(str(valor)) == 1:
        break
print("Valor final é: " + str(valor))
