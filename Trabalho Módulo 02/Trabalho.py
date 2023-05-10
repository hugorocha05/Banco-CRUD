import os
os.system('cls')

def pedir_dados():
    nome = input("\nDigite o nome da pessoa relacionada a essa transação: ").title().strip()
    data = input("Digite a data em que a transação ocorreu (no formato dd/mm/aaaa): ").strip()
    categoria = input("Digite a categoria dessa transação: ").title().strip()
    valor = float(input("Digite o valor da transação: R$ "))
    print()

    return nome, data, categoria, valor

def guardar_dados(nome, data, categoria, valor):
    with open('Trabalho Módulo 02\Dados.csv', 'a') as a:  # f = open('Dados.csv', 'a')
        a.write(f"{nome}, {data}, {categoria}, {valor}\n")

def extrato(agrupado=False):
    print(f"\n{'=' * 20} Extrato {'=' * 20}")
    soma_total = 0

    with open('Trabalho Módulo 02\Dados.csv', 'r') as r:
        dados = r.readlines()

    lista = []
    for i in range(len(dados)):
        dados[i] = dados[i].strip()
        lista.append(dados[i].split(', '))

    if agrupado == False:
        for i in range(len(lista)):
            soma_total += float(lista[i][3])
            print(f"{i+1})\nNome: {lista[i][0]}\nData: {lista[i][1]}\nCategoria: {lista[i][2]}\nValor: R$ {float(lista[i][3]) :.2f}\n")
    
    elif agrupado == True:
        dic = {}
        for i in range(len(lista)):  # lista[i][2] == categoria da transação
            dic[lista[i][2]] = [lista[i]]  # lista[i] é uma transação completa
            for j in range(len(lista)):
                if i != j and lista[i][2] == lista[j][2]:
                    dic[lista[i][2]].append(lista[j])
        
        for chave, valor in dic.items():
            soma_categoria = 0
            print(f"\n*{chave}*\n")
            for i in range(len(valor)):
                soma_total += float(valor[i][3])
                soma_categoria += float(valor[i][3])
                print(f"Nome: {valor[i][0]}\nData: {valor[i][1]}\nCategoria: {valor[i][2]}\nValor: R$ {float(valor[i][3]) :.2f}\n")
                
            print(f"Extrato da categoria {chave}: R$ {soma_categoria :.2f}")
            print(f"{'-' * 47}")

    print(f"\nExtrato total das transações: R$ {soma_total :.2f}\n")
    print(f"{'=' * 47}")

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
        break



    elif opcao == 2:
        while True:
            tipo_extrato = int(input("""\n[1] Mostrar extrato em ordem de adição das transações
[2] Mostrar extrato agrupado por categoria
Que tipo de extrato você quer?: """))
            
            if tipo_extrato == 1:
                extrato()
                break
            elif tipo_extrato == 2:
                extrato(agrupado=True)
                break
            else:
                print("Escolha inválida, por favor tente novamente.\n")
        break



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