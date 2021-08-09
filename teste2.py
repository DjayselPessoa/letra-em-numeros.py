from folder1.funcaoExt1 import calculo
strIterar = str(input("INFORME SEU NOME SEM ACENTO E COM LETRA MINÚSCULA: "))
valor = 0
valorN = 0
indice = 0


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

    

