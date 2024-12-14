import json
import os

ARQUIVO_ESTOQUE = "estoque.json"

def carregar_estoque():
    if os.path.exists(ARQUIVO_ESTOQUE):
        with open(ARQUIVO_ESTOQUE, 'r') as arquivo:
            return json.load(arquivo)
    else:
        return {}

def salvar_estoque(estoque):
    with open(ARQUIVO_ESTOQUE, 'w') as arquivo:
        json.dump(estoque, arquivo, indent=4)

def atualizar_estoque(estoque, venda):
    produto = venda['produto']
    quantidade = venda['quantidade']
    
    if produto not in estoque:
        print(f"Erro: O produto '{produto}' não existe no estoque.")
        return False
    
    if estoque[produto] < quantidade:
        print(f"Erro: Estoque insuficiente. Há apenas {estoque[produto]} unidades de '{produto}' disponíveis.")
        return False
    
    estoque[produto] -= quantidade
    print(f"Venda registrada: {quantidade} unidades de '{produto}'")
    return True

def exibir_estoque(estoque):
    print("\nEstoque atual:")
    for produto, quantidade in estoque.items():
        print(f"{produto}: {quantidade} unidades")

def main():
    estoque = carregar_estoque()
    
    while True:
        exibir_estoque(estoque)
        
        acao = input("\nDigite 'v' para registrar uma venda, 'a' para adicionar um produto ou 'q' para sair: ").lower()
        
        if acao == 'q':
            break
        elif acao == 'v':
            produto = input("Digite o nome do produto vendido: ")
            try:
                quantidade = int(input("Digite a quantidade vendida: "))
                if quantidade <= 0:
                    raise ValueError
            except ValueError:
                print("Erro: Por favor, digite um número inteiro positivo para a quantidade.")
                continue
            
            venda = {'produto': produto, 'quantidade': quantidade}
            if atualizar_estoque(estoque, venda):
                salvar_estoque(estoque)
        elif acao == 'a':
            produto = input("Digite o nome do novo produto: ")
            try:
                quantidade = int(input("Digite a quantidade inicial: "))
                if quantidade < 0:
                    raise ValueError
            except ValueError:
                print("Erro: Por favor, digite um número inteiro não negativo para a quantidade.")
                continue
            
            estoque[produto] = quantidade
            salvar_estoque(estoque)
            print(f"Produto '{produto}' adicionado ao estoque com {quantidade} unidades.")
        else:
            print("Opção inválida. Por favor, tente novamente.")
    
    print("Programa encerrado. Obrigado por usar o controle de estoque!")

if __name__ == "__main__":
    main()