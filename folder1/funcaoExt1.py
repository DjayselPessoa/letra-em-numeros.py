def calculo(valorNFinal):
    print("chamada feita!")
    resultado = 0
    indiceStr = 0
    # identificador = 0
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
        
    print("O resultado final é: ", resultado)
    return ""
