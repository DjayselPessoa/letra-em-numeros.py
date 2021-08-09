strIterar = str(input("INFORME SEU NOME SEM ACENTO E COM LETRA MINÚSCULA: "))
valor = 0
valorN = 0
indice = 0


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

while indice < len(strIterar):
    
    if strIterar[indice] == "a" or strIterar[indice] == "j" or strIterar[indice] == "s":
        valor = valor + 1
        print (strIterar[indice], valor)
    elif strIterar[indice] == "b" or strIterar[indice] == "k" or strIterar[indice] == "t":
        valor = valor + 2
        print (strIterar[indice], valor)
    elif strIterar[indice] == "c" or strIterar[indice] == "ç" or strIterar[indice] == "l" or strIterar[indice] == "u":
        valor = valor + 3
        print (strIterar[indice], valor)
    elif strIterar[indice] == "d" or strIterar[indice] == "m" or strIterar[indice] == "v":
        valor = valor + 4
        print (strIterar[indice], valor)
    elif strIterar[indice] == "e" or strIterar[indice] == "n" or strIterar[indice] == "w":
        valor = valor + 5
        print (strIterar[indice], valor)
    elif strIterar[indice] == "f" or strIterar[indice] == "o" or strIterar[indice] == "x":
        valor = valor + 6
        print (strIterar[indice], valor)
    elif strIterar[indice] == "g" or strIterar[indice] == "p" or strIterar[indice] == "y":
        valor = valor + 7
        print (strIterar[indice], valor)
    elif strIterar[indice] == "h" or strIterar[indice] == "q" or strIterar[indice] == "z":
        valor = valor + 8
        print (strIterar[indice], valor)
    elif strIterar[indice] == "i" or strIterar[indice] == "r":
        valor = valor + 9
        print (strIterar[indice], valor)
    elif strIterar[indice] == " ":
        valorN = valorN + valor
        print (valorN)
        valor = 0
    
    indice += 1


if indice == len(strIterar) and strIterar[indice - 1] == " ":
    print (valorN);
    print (calculo(valorN));
else:
    valor2 = valorN + valor
    print (valorN + valor)
    print (calculo(valor2))

    

