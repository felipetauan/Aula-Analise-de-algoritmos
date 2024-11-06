from collections import deque # o deque é um modulo do collection, para implemenrtar/ chamer uma fila

def busca_largura (grafo, inicio):
    #queue é FILA para busca
    queue = deque([inicio])
    
    #criar um conjunto de vertices
    visitados = set()
    
    #niveis é um dicionario que deve mapear cada vertice
    #o none coresponde ao primeiro vertice, ou seja,
    # ele não tem pai entao vai criar nó raiz para o caminho de cada vertices
    niveis = {inicio: None}
    while queue:
        vertice = queue.popleft()
        if vertice not in  visitados:
            visitados.add(vertice)
            for visinho in grafo.get(vertice, []):
                if visinho not in visitados:
                    queue.append(visinho)
                    if visinho not in visitados:
                        niveis[visinho] = vertice
    return visitados, niveis
grafo = {
    1:[2, 3, 4],
    2:[5, 6],
    3:[],
    4:[7, 8],
    5:[9, 10],
    6:[],
    7:[11, 12],
    8:[],
    9:[],
    10:[],
    11:[],
    12:[]
}
visitados , niveis = busca_largura(grafo, 1)
print("Vertices visitados:" , visitados)
print("Caminhos" , niveis)