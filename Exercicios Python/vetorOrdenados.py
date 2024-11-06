vetor = [5, 10 , 15 , 20 , 25]

def inserir_ordenando(vetor, elemento):
    for i in range(len(vetor)):
        if elemento < vetor[i]:
            vetor.insert(i , elemento)
            return
    vetor.append(elemento)


print('Inserir elemento no vetor ordenado...') 
inserir_ordenando(vetor, 12)
inserir_ordenando(vetor, 7)
inserir_ordenando(vetor, 30)
print(f'Vetor após inserções {vetor}\n')

#2 - Consiltando elemntos no vetor ordenado

def consultar(vetor, elemento):
    if elemento in vetor:
        return vetor.index(elemento)
    return -1

print('Consultando elmentos no vetor ordenado...')
elemento_consulta = 15
posicao = consultar(vetor, elemento_consulta)
if posicao != -1:
    print(f'O elemento {elemento_consulta} encontrado na posição {posicao}')
else:
    print(f'O elemento {elemento_consulta} não foi encontrado no vetor')

elemento_consulta = 100
posicao = consultar(vetor, elemento_consulta)
if posicao != -1:
    print(f'O elemento {elemento_consulta} foi encontrado na posição {posicao}')
else:
    print(f'O elememento {elemento_consulta} não foi encontrado no vetor')
print()

#3 - remoção de elemntos no vetor ordenado
def remover(vetor, elememento):
    if elememento in vetor:
        vetor.remove(elememento)
        return True
    return False

print('Removendo elemento do vetor ordenado...')
elemento_remocao = 10 
if remover(vetor, elemento_remocao):
    print(f'O elemento { elemento_remocao} removido. vetor atual: {vetor}')
else:
    print(f'O elemento {elemento_remocao} não foi encontrado no vetor para remoção')

elemento_remocao = 50
if remover(vetor, elemento_remocao):
    print(f'O elemento {elemento_remocao} removido. vetor atual: {vetor}')
else:
    print(f'O elemento {elemento_remocao} não foi encontrado no vetor para remoção')