def mostrar_animais(animais):
    if not animais:
        print("Nenhum animal na lista.")
    else:
        print("\nLista de Animais:")
        for i, animal in enumerate(animais, 1):
            print(f"{i}. {animal['nome']} - {animal['descricao']}")

# Função para adicionar um novo animal
def adicionar_animal(animais):
    nome = input("\nDigite o nome do animal: ")
    descricao = input("Digite a descrição do animal: ")
    animal = {"nome": nome, "descricao": descricao}
    animais.append(animal)
    print(f"Animal '{nome}' adicionado com sucesso!")

# Função para editar um animal existente
def editar_animal(animais):
    mostrar_animais(animais)
    try:
        indice = int(input("\nDigite o número do animal que deseja editar: ")) - 1
        if 0 <= indice < len(animais):
            nome_atual = animais[indice]["nome"]
            descricao_atual = animais[indice]["descricao"]
            print(f"Nome atual: {nome_atual}")
            print(f"Descrição atual: {descricao_atual}")
            
            nome = input("Novo nome (deixe em branco para manter o atual): ")
            descricao = input("Nova descrição (deixe em branco para manter a atual): ")

            if nome:
                animais[indice]["nome"] = nome
            if descricao:
                animais[indice]["descricao"] = descricao

            print(f"Animal '{nome_atual}' editado com sucesso!")
        else:
            print("Animal não encontrado.")
    except ValueError:
        print("Entrada inválida. Tente novamente.")

# Função para excluir um animal da lista
def excluir_animal(animais):
    mostrar_animais(animais)
    try:
        indice = int(input("\nDigite o número do animal que deseja excluir: ")) - 1
        if 0 <= indice < len(animais):
            nome = animais[indice]["nome"]
            animais.pop(indice)
            print(f"Animal '{nome}' excluído com sucesso!")
        else:
            print("Animal não encontrado.")
    except ValueError:
        print("Entrada inválida. Tente novamente.")

# Função para exibir o menu e processar as opções
def menu():
    animais = []  # Lista de animais (armazenamento temporário)
    
    while True:
        print("\nMenu de Opções:")
        print("1. Mostrar lista de animais")
        print("2. Adicionar um novo animal")
        print("3. Editar um animal existente")
        print("4. Excluir um animal")
        print("5. Sair")
        
        opcao = input("Escolha uma opção (1-5): ")
        
        if opcao == "1":
            mostrar_animais(animais)
        elif opcao == "2":
            adicionar_animal(animais)
        elif opcao == "3":
            editar_animal(animais)
        elif opcao == "4":
            excluir_animal(animais)
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Inicia o programa
if __name__ == "__main__":
    menu()
