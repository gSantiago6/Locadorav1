filmes = []
while True:
    print("\n 1. Listar Filmes.\n 2. Adicionar Filme.\n 3. Remover um Filme.\n 4. Quantidade de Filmes.\n 5. Sair.")
    opcao = int(input("\nDigite a sua opção: "))

    if opcao == 1:
        if len(filmes) > 0:
            print("Lista de filmes:")
            for item in filmes:
                print("-",item)
        else:
            print("Não há filmes a serem exibidos.")

    elif opcao == 2:
        novoFilme = input("Digite o nome do filme: ")
        filmes.append(novoFilme)
        print("Filme adicionado com sucesso!")

    elif opcao == 3:
        filmeRemove = input("Qual filme você deseja remover?")
        filmes.remove(filmeRemove)
        print("Filme removido com sucesso!")

    elif opcao == 4:
        quantidadeFilme = len(filmes)
        print("Atualmente temos",quantidadeFilme,"Filmes")

    elif opcao == 5:
        break

    else:
        print("Opção inválida")
print("Inté")


