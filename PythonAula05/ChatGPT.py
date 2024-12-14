import json

# Função para carregar os dados do estoque de um arquivo JSON
def carregar_estoque(arquivo):
    try:
        with open(arquivo, 'r') as f:
            estoque = json.load(f)
    except FileNotFoundError:
        estoque = {}
    return estoque

# Função para salvar os dados do estoque de volta no arquivo JSON
def salvar_estoque(arquivo, estoque):
    with open(arquivo, 'w') as f:
        json.dump(estoque, f, indent=4)

# Função para registrar a venda e atualizar o estoque
def registrar_venda(arquivo, venda):
    estoque = carregar_estoque(arquivo)
    
    for produto, quantidade_vendida in venda.items():
        if produto in estoque:
            if estoque[produto] >= quantidade_vendida:
                estoque[produto] -= quantidade_vendida
            else:
                print(f"Erro: Estoque insuficiente para o produto {produto}. Estoque atual: {estoque[produto]}")
                return
        else:
            print(f"Erro: Produto {produto} não encontrado no estoque.")
            return
    
    salvar_estoque(arquivo, estoque)
    print(f"Venda registrada com sucesso! Estoque atualizado.")

# Função para exibir o estoque atual
def exibir_estoque(arquivo):
    estoque = carregar_estoque(arquivo)
    if estoque:
        print("Estoque atual:")
        for produto, quantidade in estoque.items():
            print(f"{produto}: {quantidade} unidades")
    else:
        print("O estoque está vazio ou não foi inicializado.")

# Exemplo de uso
arquivo_estoque = 'guardar.json'

# Exibindo o estoque atual
exibir_estoque(arquivo_estoque)

# Registrando uma venda
venda = {
    "Produto A": 2,
    "Produto B": 1
}

registrar_venda(arquivo_estoque, venda)

# Exibindo o estoque após a venda
exibir_estoque(arquivo_estoque)
