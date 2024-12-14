import json
import os

# Função para carregar o estoque do arquivo JSON
def carregar_estoque(arquivo):
    if not os.path.exists(arquivo):
        return {}
    with open(arquivo, 'r') as f:
        return json.load(f)

# Função para salvar o estoque no arquivo JSON
def salvar_estoque(estoque, arquivo):
    with open(arquivo, 'w') as f:
        json.dump(estoque, f, indent=4)

# Função para registrar uma venda
def registrar_venda(estoque, venda):
    produto = venda['produto']
    quantidade_vendida = venda['quantidade']

    if produto in estoque:
        if estoque[produto] >= quantidade_vendida:
            estoque[produto] -= quantidade_vendida
            print(f"Venda registrada: {quantidade_vendida} unidades de '{produto}' vendidas.")
        else:
            print(f"Estoque insuficiente para '{produto}'. Disponível: {estoque[produto]}, Tentativa de venda: {quantidade_vendida}.")
    else:
        print(f"Produto '{produto}' não encontrado no estoque.")

# Função principal
def main():
    arquivo_estoque = 'estoque.json'
    estoque = carregar_estoque(arquivo_estoque)

    while True:
        print("\nControle de Estoque")
        print("1. Registrar venda")
        print("2. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            produto = input("Nome do produto: ")
            quantidade = int(input("Quantidade vendida: "))
            venda = {'produto': produto, 'quantidade': quantidade}
            registrar_venda(estoque, venda)
            salvar_estoque(estoque, arquivo_estoque)
        elif opcao == '2':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()