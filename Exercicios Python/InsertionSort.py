def insertion_sort(lista):
    #Começa da segunnda posição pq a primeia posição é considerada como parte de lista ordenada
    for i in range(1, len(lista)):
        chave = lista[i] # Elemento a ser inserido na parte ordenda
        j = i - 1

        # Move os elementos da parte ordenada que são maiores que a chave para uma posição à frente 
        while j >= 0 and  lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1

        #Insere a chave na posição correta
        lista[j + 1 ] = chave

        # Exibe a lista após cada inserção
        print(f'Lista aops inserir o elemento na posição{i}: {lista}')

    return lista

#exemplo de uso
numeros =  [64, 34, 25, 12, 22, 11, 90]
numeros_ordenados = insertion_sort(numeros)
print(f'Lista ordenada: {numeros_ordenados}')