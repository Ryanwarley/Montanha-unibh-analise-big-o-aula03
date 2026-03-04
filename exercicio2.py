def somar_lista(lista):
    total = 0
    for elemento in lista:
        total += elemento
    return total

# Teste
numeros = [1, 2, 3, 4, 5]
resultado = somar_lista(numeros)

print("Soma:", resultado)