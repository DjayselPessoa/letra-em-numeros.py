def calculo(valorNFinal):
    print("chamada feita!")
    resultado = 0
    indiceStr = 0
    identificador = 0
    strValorNFinal = str(valorNFinal)
    while indiceStr < len(str(valorNFinal)):
        if strValorNFinal[indiceStr] == "1":
            resultado = resultado + 1
        elif strValorNFinal[indiceStr] == "2":
            resultado = resultado + 2
        elif strValorNFinal[indiceStr] == "3":
            resultado = resultado + 3
        elif strValorNFinal[indiceStr] == "4":
            resultado = resultado + 4
        elif strValorNFinal[indiceStr] == "5":
            resultado = resultado + 5
        elif strValorNFinal[indiceStr] == "6":
            resultado = resultado + 6
        elif strValorNFinal[indiceStr] == "7":
            resultado = resultado + 7
        elif strValorNFinal[indiceStr] == "8":
            resultado = resultado + 8
        elif strValorNFinal[indiceStr] == "9":
            resultado = resultado + 9
        elif strValorNFinal[indiceStr] == "0":
            resultado = resultado + 0
        indiceStr += 1
    indice2 = 0
    resultado2 = 0
    if resultado > 22 and resultado < 100:
        identificador = 1
        strResultado = str(resultado)
        while indice2 < len(str(resultado)):
            if strResultado[indice2] == "1":
                resultado2 = resultado2 + 1
            elif strResultado[indice2] == "2":
                resultado2 = resultado2 + 2
            elif strResultado[indice2] == "3":
                resultado2 = resultado2 + 3
            elif strResultado[indice2] == "4":
                resultado2 = resultado2 + 4
            elif strResultado[indice2] == "5":
                resultado2 = resultado2 + 5
            elif strResultado[indice2] == "6":
                resultado2 = resultado2 + 6
            elif strResultado[indice2] == "7":
                resultado2 = resultado2 + 7
            elif strResultado[indice2] == "8":
                resultado2 = resultado2 + 8
            elif strResultado[indice2] == "9":
                resultado2 = resultado2 + 9
            elif strResultado[indice2] == "0":
                resultado2 = resultado2 + 0
            indice2 += 1

    if identificador == 1:
        print("2- O resultado final é: ", resultado2)
        return ""
    else:
        print("1 - O resultado final é: ", resultado)
        return ""
