from folder1.funcaoExt1 import calculo
iT = str(input("INFORME SEU NOME: "))
iT = iT.lower()
valor = 0
valorN = 0
i = 0


while i < len(iT):
    try:
        if iT[i] == "a" or iT[i] == "ã" or iT[i] == "j" or iT[i] == "s":
            valor = valor + 1
            print(iT[i], valor)
        elif iT[i] == "b" or iT[i] == "k" or iT[i] == "t":
            valor = valor + 2
            print(iT[i], valor)
        elif iT[i] == "c" or iT[i] == "ç" or iT[i] == "l" or iT[i] == "u":
            valor = valor + 3
            print(iT[i], valor)
        elif iT[i] == "d" or iT[i] == "m" or iT[i] == "v":
            valor = valor + 4
            print(iT[i], valor)
        elif iT[i] == "e" or iT[i] == "é" or iT[i] == "n" or iT[i] == "w":
            valor = valor + 5
            print(iT[i], valor)
        elif iT[i] == "f" or iT[i] == "o" or iT[i] == "õ" or iT[i] == "ô" or iT[i] == "x":
            valor = valor + 6
            print(iT[i], valor)
        elif iT[i] == "g" or iT[i] == "p" or iT[i] == "y":
            valor = valor + 7
            print(iT[i], valor)
        elif iT[i] == "h" or iT[i] == "q" or iT[i] == "z":
            valor = valor + 8
            print(iT[i], valor)
        elif iT[i] == "i" or iT[i] == "r":
            valor = valor + 9
            print(iT[i], valor)
        elif iT[i] == " ":
            valorN = valorN + valor
            print(valorN)
            valor = 0
        else:
            raise ValueError(" - caractere especial detectado!")
        i += 1
    except ValueError as e:
        print("Inválido!", e)
        break

if i == len(iT) and iT[i - 1] == " ":
    print(valorN)
    print(calculo(valorN))
else:
    valor2 = valorN + valor
    print(valorN + valor)
    print(calculo(valor2))
