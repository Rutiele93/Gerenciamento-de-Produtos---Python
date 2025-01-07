import json

# Função para carregar os produtos


def carregar_produtos():
    try:
        with open("inventory.json", "r") as file:
            # Tenta ler e carregar o arquivo JSON
            data = file.read().strip()
            if not data:  # Se o arquivo estiver vazio
                return []
            try:
                return json.loads(data)
            except json.JSONDecodeError:
                print("Erro ao ler o arquivo JSON. O conteúdo pode estar corrompido.")
                return []  # Retorna lista vazia caso haja erro na leitura
    except FileNotFoundError:
        return []  # Caso o arquivo não exista


# Função para salvar os produtos
def salvar_produtos(produtos):
    with open("inventory.json", "w") as file:
        json.dump(produtos, file, indent=4)


# Adicionar Produto
def adicionar_produto():
    produtos = carregar_produtos()
    nome = input("Nome do Produto: ")
    categoria = input("Categoria: ")
    quantidade = int(input("Quantidade em Estoque: "))
    preco = float(input("Preço: "))

    # Gerar ID único
    produto_id = len(produtos) + 1
    novo_produto = {
        "id": produto_id,
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade,
        "preco": preco
    }

    produtos.append(novo_produto)
    salvar_produtos(produtos)
    print(f"Produto {nome} adicionado com sucesso.")


# Listar Produtos
def listar_produtos():
    produtos = carregar_produtos()
    print("ID | Nome | Categoria | Quantidade | Preço")
    for produto in produtos:
        print(f"{produto['id']} | {produto['nome']} | {produto['categoria']} | {
              produto['quantidade']} | {produto['preco']}")


# Atualizar Produto
def atualizar_produto():
    produtos = carregar_produtos()
    produto_id = int(input("Digite o ID do produto a ser atualizado: "))
    for produto in produtos:
        if produto["id"] == produto_id:
            print("Produto encontrado. O que deseja atualizar?")
            print("1. Nome")
            print("2. Categoria")
            print("3. Quantidade")
            print("4. Preço")
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                produto["nome"] = input("Novo Nome: ")
            elif opcao == 2:
                produto["categoria"] = input("Nova Categoria: ")
            elif opcao == 3:
                produto["quantidade"] = int(input("Nova Quantidade: "))
            elif opcao == 4:
                produto["preco"] = float(input("Novo Preço: "))

            salvar_produtos(produtos)
            print("Produto atualizado com sucesso.")
            return

    print("Produto não encontrado.")


# Excluir Produto
def excluir_produto():
    produtos = carregar_produtos()
    produto_id = int(input("Digite o ID do produto a ser excluído: "))
    for produto in produtos:
        if produto["id"] == produto_id:
            confirmacao = input(f"Tem certeza que deseja excluir {
                                produto['nome']}? (s/n): ")
            if confirmacao.lower() == "s":
                produtos.remove(produto)
                salvar_produtos(produtos)
                print("Produto excluído com sucesso.")
            return

    print("Produto não encontrado.")


# Buscar Produto
def buscar_produto():
    produtos = carregar_produtos()
    busca = input("Digite o ID ou parte do nome do produto: ")

    for produto in produtos:
        if str(produto["id"]) == busca or busca.lower() in produto["nome"].lower():
            print(f"ID: {produto['id']}, Nome: {produto['nome']}, Categoria: {
                  produto['categoria']}, Quantidade: {produto['quantidade']}, Preço: {produto['preco']}")
            return

    print("Produto não encontrado.")

# Menu de opções


def menu():
    while True:
        print("\nAgilStore - Gerenciamento de Produtos")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Excluir Produto")
        print("5. Buscar Produto")
        print("6. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            adicionar_produto()
        elif opcao == 2:
            listar_produtos()
        elif opcao == 3:
            atualizar_produto()
        elif opcao == 4:
            excluir_produto()
        elif opcao == 5:
            buscar_produto()
        elif opcao == 6:
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
