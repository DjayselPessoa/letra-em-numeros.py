ligado = True
while ligado:
    nome = str(input("INFORME UM NOME VÁLIDO: "))
    nome = nome.lower()
    valor = 0
    i = 0
    active = True
    # ----------------------------------------------------
    # nova forma de iterar no nome e obter os valores!
    # ----------------------------------------------------
    tac = 0
    teste = False
    falso =  False
    lista = [" ", "aâáãjs", "bkt", "cçlu", "dmv", "eénw", "foõôx", "gpy", "hqz", "ir"]
    for x in nome:
        # print("x: " + str(x))
        for y in lista:
            # print("y: " + str(y))
            if x in y:
                valor = valor + tac
                print(f" {x}  -> {tac} : {valor} ")
                teste = True
            elif tac == 9 and teste is False:
                print("Caractere informado não é válido!")
                active = False
                falso = True
                break
            if tac < 9:
                tac = tac + 1
            else:
                continue
        if teste is False and tac == 9 and falso is True:
            print("Reiniciando!")
            break
        elif teste is True and tac == 9 and falso is False:
            teste = False
            tac = 0
            continue
    # ----------------------------------------------------
    # antiga forma de iterar no nome e obter os valores!
    # ----------------------------------------------------
    # while i < len(nome):
    #     if nome[i] in "aáãjs":
    #         valor = valor + 1
    #         print(f" {nome[i]}  -> {1} : {valor} ")
    #     elif nome[i] in "bkt":
    #         valor = valor + 2
    #         print(f" {nome[i]}  -> {2} : {valor} ")
    #     elif nome[i] in "cçlu":
    #         valor = valor + 3
    #         print(f" {nome[i]}  -> {3} : {valor} ")
    #     elif nome[i] in "dmv":
    #         valor = valor + 4
    #         print(f" {nome[i]}  -> {4} : {valor} ")
    #     elif nome[i] in "eénw":
    #         valor = valor + 5
    #         print(f" {nome[i]}  -> {5} : {valor} ")
    #     elif nome[i] in "foõôx":
    #         valor = valor + 6
    #         print(f" {nome[i]}  -> {6} : {valor} ")
    #     elif nome[i] in "gpy":
    #         valor = valor + 7
    #         print(f" {nome[i]}  -> {7} : {valor} ")
    #     elif nome[i] in "hqz":
    #         valor = valor + 8
    #         print(f" {nome[i]}  -> {8} : {valor} ")
    #     elif nome[i] in "ir":
    #         valor = valor + 9
    #         print(f" {nome[i]}  -> {9} : {valor} ")
    #     elif nome[i] in " ":
    #         pass
    #     else:
    #         print("- caractere incompatível detectado!")
    #         active = False
    #         break
    #     i += 1
    cont1 = 0
    cont2 = 0

    while active is True and falso is False:
        # print(f"valor parcial: {valor}")
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
    if active is True and falso is False:
        print("Valor final é: " + str(valor))
        escolha = str(input("Informe \'S\' para sair ou \'C\' para continuar:"))
        if escolha not in "SsCc":
            print("O programa será finalizado!")
            ligado = False
        else:
            if escolha in "Cc":
                continue
            elif escolha in "Ss":
                ligado = False
                print("O programa será finalizado!")
    elif active is True and falso is True:
        escolha = str(input("Informe \'S\' para sair ou \'C\' para continuar:"))
        if escolha not in "SsCc":
            print("O programa será finalizado!")
            ligado = False
        else:
            if escolha in "Cc":
                continue
            elif escolha in "Ss":
                ligado = False
                print("O programa será finalizado!")
