import os
os.system('cls')

while True:  # Pergunta qual serviço ousuário deseja realisar e ramifica o código para a situação adequada
    opcao = int(input("""[1] Adicionar transação
[2] Ver transações passadas
[3] Atualizar transações passadas
[4] Deletar transações passadas
Que tipo de serviço você deseja realizar?: """))
    
    if opcao == 1:  # Sistema de adição 
        while True:
            tipo_transacao = int(input("""[1] Entrada de Dinheiro
        [2] Saída de Dinheiro
        Que tipo de transação você deseja adicionar?: """))

            if tipo_transacao == 1:
                # Pedir nome, data, categoria e valor (considerando o mesmo como positivo)
                # Guaradar informações em banco de dados (arquivo .csv)
                break
            elif tipo_transacao == 2:
                # Pedir nome, data, categoria e valor (considerando o mesmo como negativo)
                # Guaradar informações em banco de dados (arquivo .csv)
                break
            else:
                print("Escolha inválida, por favor tente novamente.\n")

    elif opcao == 2:
        # Criar sistema de leitura de transações passadas
        # Criar um extrato com as dispesas agrupadas por categoria
        break

    elif opcao == 3:
        # Criar sistema de atualização de transações passadas
        break

    elif opcao == 4:
        # Criar sistema de deleção de transações passadas
        break

    else:
        print("Escolha inválida, por favor tente novamente.\n")