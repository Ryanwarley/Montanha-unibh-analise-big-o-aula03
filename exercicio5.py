def imprimir_pares_e_soma(lista):

    # Bloco 1
    for i in range(len(lista)):
        print(lista[i])

    # Bloco 2
    for i in range(len(lista)):
        for j in range(len(lista)):
            print(lista[i], lista[j])

# Teste
lista = [1, 2, 3]
imprimir_pares_e_soma(lista)