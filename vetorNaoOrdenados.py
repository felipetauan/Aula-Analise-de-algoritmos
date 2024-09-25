#Vetor vazio
vetor = [ ]

#1 - Inserção de elementos no vetor
print('inserindo elementosno vetor')

#Incerindo valores do 25 ate 5
vetor.append(25)
vetor.append(10)
vetor.append(30)
vetor.append(15)
vetor.append(5)
print(f'Vetor após inserção: { vetor}\n')

#2 - Consiulta de elementos no vetor
print('consultando elementos no vetor..')

elemento_consulta = 30

if elemento_consulta in vetor:
    print(f'O elemento {elemento_consulta} foi encontrado na posição {vetor.index(elemento_consulta)}')#.index vai buscar o valor no vetor e falar sua posição
else:
    print(f'Elemento {elemento_consulta} não foi encontrado no vetor')

#Alterado o valoer para teste
elemento_consulta = 100

if elemento_consulta in vetor:
    print(f'O elemento {elemento_consulta} foi encontrado na posição {vetor.index(elemento_consulta)}')
else:
    print(f'elemento {elemento_consulta} não foi enconttrado no vetor')
print()

#3 - Remoção de elemento no vetor 
print('Removendo elemento do vetor...')
elemento_remocao = 10

if elemento_remocao in vetor:
    vetor.remove(elemento_remocao)
    print(f'O elemento {elemento_remocao} foi removido. Vetor atual{vetor}')
else:
    print(f'O elemento {elemento_remocao} não foi encontrado para remoção')

#Alterando valor para teste
elemento_remocao = 50
if elemento_remocao in vetor:
    vetor.remove(elemento_remocao)
    print(f'O elemento {elemento_remocao} foi removido. vetor atual {vetor}')

else:
    print(f'O elemento {elemento_remocao} não foi encontrado para remoção')