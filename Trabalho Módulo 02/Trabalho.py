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

def extrato(agrupar=None):
    print(f"\n{'=' * 20} Extrato {'=' * 20}\n")
    soma_total = 0

    with open('Trabalho Módulo 02\Dados.csv', 'r') as r:
        dados = r.readlines()

    matriz = []
    for i in range(len(dados)):
        dados[i] = dados[i].strip()
        matriz.append(dados[i].split(', '))
        
    dic = {}

    if agrupar == None:
        for i in range(len(matriz)):
            soma_total += float(matriz[i][3])
            print(f"{i+1})\nNome: {matriz[i][0]}\nData: {matriz[i][1]}\nCategoria: {matriz[i][2]}\nValor: R$ {float(matriz[i][3]) :,.2f}\n")
        print()


    elif agrupar == "nome":
        for i in range(len(matriz)):  # matriz[i][0] == nome relacionado à da transação
            dic[matriz[i][0]] = [matriz[i]]  # matriz[i] é uma transação completa
            for j in range(len(matriz)):
                if i != j and matriz[i][0] == matriz[j][0]:
                    dic[matriz[i][0]].append(matriz[j])

    elif agrupar == "data":
        for i in range(len(matriz)):  # matriz[i][1] == data da transação
            dic[matriz[i][1]] = [matriz[i]]  # matriz[i] é uma transação completa
            for j in range(len(matriz)):
                if i != j and matriz[i][1] == matriz[j][1]:
                    dic[matriz[i][1]].append(matriz[j])

    elif agrupar == "categoria":
        for i in range(len(matriz)):  # matriz[i][2] == categoria da transação
            dic[matriz[i][2]] = [matriz[i]]  # matriz[i] é uma transação completa
            for j in range(len(matriz)):
                if i != j and matriz[i][2] == matriz[j][2]:
                    dic[matriz[i][2]].append(matriz[j])
        
    for chave, valor in dic.items():
        soma_categoria = 0
        print(f"*{chave}*\n")
        for i in range(len(valor)):
            soma_total += float(valor[i][3])
            soma_categoria += float(valor[i][3])
            print(f"Nome: {valor[i][0]}\nData: {valor[i][1]}\nCategoria: {valor[i][2]}\nValor: R$ {float(valor[i][3]) :,.2f}\n")
                
        print(f"Extrato {agrupar} '{chave}': R$ {soma_categoria :,.2f}\n")
        print(f"{'-' * 47}\n")

    print(f"Extrato total das transações: R$ {soma_total :,.2f}\n")
    print(f"{'=' * 47}\n")

    return matriz

def apagar_tudo():
    with open('Trabalho Módulo 02\Dados.csv', 'w') as w:  # f = open('Dados.csv', 'a')
        w.write("")

while True:  # Pergunta qual serviço o usuário deseja realisar e ramifica o código para a situação adequada
    opcao = input("""[1] Adicionar transação
[2] Ver transações passadas
[3] Atualizar transações passadas
[4] Deletar transações passadas
[5] Sair do programa
Que tipo de serviço você deseja realizar?: """)
    


    if opcao == '1':  # Sistema de adição de transações
        while True:
            tipo_transacao = input("""\n[1] Entrada de Dinheiro
[2] Saída de Dinheiro
Que tipo de transação você deseja adicionar?: """)

            if tipo_transacao == '1':  # Entrada de dinheiro
                nome, data, categoria, valor  = pedir_dados()
                guardar_dados(nome, data, categoria, valor)
                print("Transação adicionada com sucesso\n")
                break

            elif tipo_transacao == '2':  # Saída de dinheiro
                nome, data, categoria, valor  = pedir_dados()
                valor = -valor
                guardar_dados(nome, data, categoria, valor)
                print("Transação adicionada com sucesso\n")
                break
            else:
                print("Escolha inválida, por favor tente novamente.\n")


    elif opcao == '2':
        while True:
            tipo_extrato = input("""\n[1] Mostrar extrato em ordem de adição das transações
[2] Mostrar extrato agrupado por nome
[3] Mostrar extrato agrupado por data
[4] Mostrar extrato agrupado por categoria
Que tipo de extrato você quer?: """)
            
            if tipo_extrato == '1':
                extrato()
                break
            elif tipo_extrato == '2':
                extrato(agrupar='nome')
                break
            elif tipo_extrato == '3':
                extrato(agrupar='data')
                break
            elif tipo_extrato == '4':
                extrato(agrupar='categoria')
                break
            else:
                print("Escolha inválida, por favor tente novamente.\n")


    elif opcao == '3':
        matriz = extrato()

        opcoes = []
        for i in range(len(matriz)):
            opcoes.append(str(i + 1))


        while True:
            escolha = input("""Digite o número da transação que você deseja atualizar: """)

            if escolha not in opcoes:
                print("Escolha inválida, por favor tente novamente.\n")
            else:
                apagar_tudo()
                
                index = int(escolha) - 1

                matriz[index][0], matriz[index][1], matriz[index][2], matriz[index][3] = pedir_dados()

                for transacao in matriz:
                    guardar_dados(transacao[0], transacao[1], transacao[2], transacao[3])

                print("Transação atualizada com sucesso!\n")

                break


    elif opcao == '4':
        matriz = extrato()

        opcoes = []
        for i in range(len(matriz)):
            opcoes.append(str(i + 1))


        while True:
            escolha = input("""Digite o número da transação que você deseja deletar: """)

            if escolha not in opcoes:
                print("Escolha inválida, por favor tente novamente.\n")
            else:
                apagar_tudo()

                matriz.pop(int(escolha) - 1)

                for transacao in matriz:
                    guardar_dados(transacao[0], transacao[1], transacao[2], transacao[3])

                print("Transação deletada com sucesso!\n")

                break


    elif opcao == '5':
        print()
        break


    else:
        print("Escolha inválida, por favor tente novamente.\n")