rango = range(105)
numeros = [i for i in rango]


while len(numeros) > 0:
    num = int(input('Numero: '))
    try:
        numeros.pop(numeros.index(num))
    except ValueError as error:
        print(error)
    finally:
        print(numeros)
