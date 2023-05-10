import os
os.system('cls')

def pedir_dados():
    nome = input("\nDigite o nome da pessoa relacionada a essa transação: ")
    data = input("Digite a data em que a transação ocorreu (no formato dd/mm/aaaa): ")
    categoria = input("Digite a categoria dessa transação: ")
    valor = float(input("Digite o valor da transação: R$ "))
    print()

    return nome, data, categoria, valor

def guardar_dados(nome, data, categoria, valor):
    with open('Dados.csv', 'a') as a:  # f = open('Dados.csv', 'a')
        a.write(f"{nome}, {data}, {categoria}, {valor}\n")

def extrato(agrupado=False):
    print(f"\n{'-' * 20} Extrato {'-' * 20}")

    with open('Dados.csv', 'r') as r:
        dados = r.readlines()

    lista = []
    for i in range(len(dados)):
        dados[i] = dados[i].strip()
        lista.append(dados[i].split(', '))

    if agrupado == False:
        for i in range(len(lista)):
            print(f"{i+1})\nNome: {lista[i][0]}\nData: {lista[i][1]}\nCategoria: {lista[i][2]}\nValor: R$ {float(lista[i][3]) :.2f}\n")
    
    elif agrupado == True:
        # Fazer um sistema de extrato agrupado por categoria
        pass

while True:  # Pergunta qual serviço ousuário deseja realisar e ramifica o código para a situação adequada
    opcao = int(input("""[1] Adicionar transação
[2] Ver transações passadas
[3] Atualizar transações passadas
[4] Deletar transações passadas
[5] Sair do programa
Que tipo de serviço você deseja realizar?: """))
    
    if opcao == 1:  # Sistema de adição de transações
        while True:
            tipo_transacao = int(input("""\n[1] Entrada de Dinheiro
[2] Saída de Dinheiro
Que tipo de transação você deseja adicionar?: """))

            if tipo_transacao == 1:  # Entrada de dinheiro
                nome, data, categoria, valor  = pedir_dados()
                guardar_dados(nome, data, categoria, valor)
                break

            elif tipo_transacao == 2:  # Saída de dinheiro
                nome, data, categoria, valor  = pedir_dados()
                valor = -valor
                guardar_dados(nome, data, categoria, valor)
                break
            else:
                print("Escolha inválida, por favor tente novamente.\n")

    elif opcao == 2:
        while True:
            tipo_extrato = print("""[1] Mostrar extrato em ordem de adição das transações
[2] Mostrar extrato agrupado por categoria""")
            
            if tipo_extrato == 1:
                extrato()
            elif tipo_extrato == 2:
                extrato(agrupado=True)
            else:
                print("Escolha inválida, por favor tente novamente.\n")

    elif opcao == 3:
        # Criar sistema de atualização de transações passadas
        pass

    elif opcao == 4:
        # Criar sistema de deleção de transações passadas
        pass
    
    elif opcao == 5:
        break
    else:
        print("Escolha inválida, por favor tente novamente.\n")