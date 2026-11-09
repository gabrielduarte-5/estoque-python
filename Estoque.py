print("     SISTEMA DE CONTROLE DE ESTOQUE")


produto = input("Digite o nome do produto: ")
estoque = int(input("Digite a quantidade inicial: "))
estoque_minimo = int(input("Digite o estoque mínimo: "))

if estoque < 0:
    estoque = 0

if estoque_minimo < 0:
    estoque_minimo = 0

while True:
    print("\n========== MENU ==========")
    print("1 - Consultar estoque")
    print("2 - Adicionar produtos")
    print("3 - Retirar produtos")
    print("4 - Verificar estoque mínimo")
    print("5 - Alterar nome do produto")
    print("6 - Sair")
    print("==========================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n--- CONSULTA DE ESTOQUE ---")
        print("Produto:", produto)
        print("Quantidade disponível:", estoque)

    elif opcao == "2":
        print("\n--- ENTRADA DE PRODUTOS ---")

        quantidade = int(input("Quantidade para adicionar: "))

        if quantidade > 0:
            estoque = estoque + quantidade

            print("Entrada registrada com sucesso!")
            print("Estoque atualizado:", estoque)
        else:
            print("Erro: informe uma quantidade positiva!")

    elif opcao == "3":
        print("\n--- SAÍDA DE PRODUTOS ---")

        quantidade = int(input("Quantidade para retirar: "))

        if quantidade <= 0:
            print("Erro: quantidade inválida!")

        elif quantidade > estoque:
            print("Erro: estoque insuficiente!")
            print("Quantidade disponível:", estoque)

        else:
            estoque = estoque - quantidade

            print("Saída registrada com sucesso!")
            print("Estoque restante:", estoque)

            if estoque <= estoque_minimo:
                print("ATENÇÃO: estoque baixo!")

    elif opcao == "4":
        print("\n--- VERIFICAÇÃO DE ESTOQUE ---")

        print("Produto:", produto)
        print("Estoque atual:", estoque)
        print("Estoque mínimo:", estoque_minimo)

        if estoque == 0:
            print("STATUS: PRODUTO ESGOTADO!")

        elif estoque <= estoque_minimo:
            print("STATUS: ESTOQUE BAIXO!")

        else:
            print("STATUS: ESTOQUE NORMAL!")

    elif opcao == "5":
        print("\n--- ALTERAR PRODUTO ---")

        novo_produto = input("Digite o novo nome: ")

        if novo_produto != "":
            produto = novo_produto
            print("Nome atualizado com sucesso!")
        else:
            print("Erro: nome inválido!")

    elif opcao == "6":
        print("\nSistema encerrado!")
        print("Obrigado por utilizar o sistema.")
        break

    else:
        print("\nOpção inválida! Tente novamente.")
