import json

def carregar_estoque(arquivo):
    """Carrega as informações do estoque a partir de um arquivo JSON."""
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Arquivo de estoque não encontrado. Criando um novo...")
        return {}

def salvar_estoque(arquivo, estoque):
    """Salva as informações do estoque em um arquivo JSON."""
    with open(arquivo, 'w') as f:
        json.dump(estoque, f, indent=4)

def realizar_venda(estoque, venda):
    """Realiza uma venda e atualiza o estoque."""
    produto = venda['produto']
    quantidade = venda['quantidade']

    if produto in estoque:
        if estoque[produto] >= quantidade:
            estoque[produto] -= quantidade
            print(f"Venda realizada com sucesso! Restante em estoque: {estoque[produto]}")
        else:
            print(f"Estoque insuficiente para o produto {produto}.")
    else:
        print(f"Produto {produto} não encontrado no estoque.")

if __name__ == "__main__":
    arquivo_estoque = 'estoque2.json'  # Alterado para estoque2
    estoque = carregar_estoque(arquivo_estoque)

    while True:
        print("\nOpções:")
        print("1. Realizar venda")
        print("2. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            produto = input("Nome do produto: ")
            quantidade = int(input("Quantidade vendida: "))
            venda = {'produto': produto, 'quantidade': quantidade}
            realizar_venda(estoque, venda)
            salvar_estoque(arquivo_estoque, estoque)
        elif opcao == '2':
            break
        else:
            print("Opção inválida.")