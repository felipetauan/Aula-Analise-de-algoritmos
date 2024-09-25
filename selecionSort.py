def selection_sort(lista):
    for i in range(len(lista)):
        # Encontra o menor elemento na parte não ordenanda
        menor_indice = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[menor_indice]:
                menor_indice = j
        #Troca o menor elemento encontrado com o primeiro elemento não
        lista[i], lista[menor_indice] = lista[menor_indice], lista[i]
    return lista

# Exemplo de uso 
numeros = [64, 34, 25, 12, 22, 11, 90]
numeros_ordenados = selection_sort(numeros)
print(f'Lista ordenada:{numeros_ordenados}')