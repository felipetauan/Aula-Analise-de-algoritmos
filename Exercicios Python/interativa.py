import time
def soma_acumulada(arr):
    result =[]
    total = 0
    
    for num in arr:
        total += num 
        result.append(total)
    return result

numeros = [3, 6, 9, 10, 14, 100, 23444, 235455, 9000, 124324, 1]
start_time = time.time()
soma_numeros = soma_acumulada(numeros)
end_time = time.time()

print(f'Tempo gasto:{end_time}, e esse foi o resultado da acumulação {soma_numeros}')
