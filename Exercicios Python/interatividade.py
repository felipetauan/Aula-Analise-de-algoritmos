def busca_pares(arr, target):
    pares = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:  # Se a soma for igual ao alvo
                pares.append((arr[i], arr[j]))  # Adiciona o par à lista de resultados
    return pares

# Exemplo de uso:
numeros = [3, 6, 9, 10, 14]
target = 16
pares = busca_pares(numeros, target)
print(f'Pares que somam {target}: {pares}')