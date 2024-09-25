pessoas = []
p = 'sim'
while p:
    nome = input("Digite o nome da pessoa: ")
    if nome.lower() == 'sair':
        break

    altura = float(input(f"Digite a altura de {nome} (em metros): "))
    peso = float(input(f"Digite o peso de {nome} (em kg): "))

    # Calculando o IMC de forma direta
    imc = peso / (altura ** 2)

    # Adicionando os dados à lista
    pessoas.append([nome, altura, peso, imc])

# Exibindo os resultados
if len(pessoas) > 0:
    maior_imc = pessoas[0][3]
    menor_imc = pessoas[0][3]
    nome_maior_imc = pessoas[0][0]
    nome_menor_imc = pessoas[0][0]

    # Percorrendo a lista para encontrar o maior e menor IMC
    for pessoa in pessoas:
        if pessoa[3] > maior_imc:
            maior_imc = pessoa[3]
            nome_maior_imc = pessoa[0]
        if pessoa[3] < menor_imc:
            menor_imc = pessoa[3]
            nome_menor_imc = pessoa[0]

    print(f"\nTotal de pessoas cadastradas: {len(pessoas)}")
    print(f"Maior IMC: {maior_imc:.2f}, Nome: {nome_maior_imc}")
    print(f"Menor IMC: {menor_imc:.2f}, Nome: {nome_menor_imc}")
else:
    print("Nenhuma pessoa foi cadastrada.")
pessoas = []
p = 'sim'
while True:
    nome = input("Digite o nome da pessoa (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break

    altura = float(input(f"Digite a altura de {nome} (em metros): "))
    peso = float(input(f"Digite o peso de {nome} (em kg): "))

    # Calculando o IMC de forma direta
    imc = peso / (altura ** 2)

    # Adicionando os dados à lista
    pessoas.append([nome, altura, peso, imc])

# Exibindo os resultados
if len(pessoas) > 0:
    maior_imc = pessoas[0][3]
    menor_imc = pessoas[0][3]
    nome_maior_imc = pessoas[0][0]
    nome_menor_imc = pessoas[0][0]

    # Percorrendo a lista para encontrar o maior e menor IMC
    for pessoa in pessoas:
        if pessoa[3] > maior_imc:
            maior_imc = pessoa[3]
            nome_maior_imc = pessoa[0]
        if pessoa[3] < menor_imc:
            menor_imc = pessoa[3]
            nome_menor_imc = pessoa[0]

    print(f"\nTotal de pessoas cadastradas: {len(pessoas)}")
    print(f"Maior IMC: {maior_imc:.2f}, Nome: {nome_maior_imc}")
    print(f"Menor IMC: {menor_imc:.2f}, Nome: {nome_menor_imc}")
else:
    print("Nenhuma pessoa foi cadastrada.")
