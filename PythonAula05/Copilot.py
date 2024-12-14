import json

# Função para ler o estoque do arquivo JSON
def ler_estoque(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Função para salvar o estoque no arquivo JSON
def salvar_estoque(filename, estoque):
    with open(filename, 'w') as file:
        json.dump(estoque, file, indent=4)

# Função para registrar uma venda
def registrar_venda(estoque, produto, quantidade):
    if produto in estoque['produtos']:
        if estoque['produtos'][produto] >= quantidade:
            estoque['produtos'][produto] -= quantidade
            print(f"Venda registrada: {quantidade} unidades de {produto}.")
        else:
            print(f"Estoque insuficiente para {produto}. Disponível: {estoque['produtos'][produto]}")
    else:
        print(f"Produto {produto} não encontrado no estoque.")

# Exemplo de uso
if __name__ == "__main__":
    filename = 'estoque3.json'
    
    # Ler o estoque inicial
    estoque = ler_estoque(filename)
    
    # Registrar uma venda
    produto_vendido = "ProdutoA"
    quantidade_vendida = 10
    registrar_venda(estoque, produto_vendido, quantidade_vendida)
    
    # Salvar o estoque atualizado
    salvar_estoque(filename, estoque)
