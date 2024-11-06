def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j +1]:
                #troca de elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


o = 0
tamanho = int(input('Tamanho lista:'))
x = tamanho
numero = []

while x < 1:    
    listasuario = int(input('Digite um numero por vez para organizar:'))
    numero.append(listasuario)
    if x :
        break

numeros_ordenados = bubble_sort(numero)
print(f'Lista ordenada:{numeros_ordenados}')