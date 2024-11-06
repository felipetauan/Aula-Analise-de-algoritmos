#funcao       decionario
def busca_prof(grafo, vertice, visitado):   
    visitado.add(vertice) #adicionado vertices a lista 
    
    #imprimir vertice raiz ou principal 
    print(vertice)
    for i in grafo.get(vertice, []): #Percorar o grafo pegue(get) o item e adicone na lista/fila
        if i not in visitado: #Se o vertice visinho não tiver sido visitado
            busca_prof(grafo, i, visitado)#agora visitar o visinho 

grafo = {
    'A': ['B' , 'C'] , 
    'B': ['A' , 'C' , 'E'], 
    'C': ['A' , 'B' , 'D' ,'E' ],
    'D': ['B' , 'C'],
    'E': ['A' , 'C']
}
visitado = set()
busca_prof(grafo, 'A', visitado)