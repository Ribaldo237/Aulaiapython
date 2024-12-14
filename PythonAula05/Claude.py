import json
import os
from datetime import datetime

class InventoryManager:
    def __init__(self, inventory_file='inventory.json', sales_file='sales.json'):
        """
        Inicializa o gerenciador de estoque
        
        :param inventory_file: Caminho para o arquivo de inventário
        :param sales_file: Caminho para o arquivo de vendas
        """
        self.inventory_file = inventory_file
        self.sales_file = sales_file
        
        # Cria os arquivos se não existirem
        self.create_files_if_not_exist()
    
    def create_files_if_not_exist(self):
        """
        Cria arquivos de inventário e vendas se não existirem
        """
        # Arquivo de inventário
        if not os.path.exists(self.inventory_file):
            with open(self.inventory_file, 'w') as f:
                json.dump([], f)
        
        # Arquivo de vendas
        if not os.path.exists(self.sales_file):
            with open(self.sales_file, 'w') as f:
                json.dump([], f)
    
    def load_inventory(self):
        """
        Carrega o inventário do arquivo JSON
        
        :return: Lista de produtos no inventário
        """
        with open(self.inventory_file, 'r') as f:
            return json.load(f)
    
    def save_inventory(self, inventory):
        """
        Salva o inventário no arquivo JSON
        
        :param inventory: Lista de produtos atualizada
        """
        with open(self.inventory_file, 'w') as f:
            json.dump(inventory, f, indent=4)
    
    def add_product(self, name, quantity, price):
        """
        Adiciona um novo produto ao inventário
        
        :param name: Nome do produto
        :param quantity: Quantidade do produto
        :param price: Preço do produto
        """
        inventory = self.load_inventory()
        
        # Verifica se o produto já existe
        for product in inventory:
            if product['name'].lower() == name.lower():
                print(f"Produto {name} já existe no inventário.")
                return
        
        # Adiciona novo produto
        new_product = {
            'id': len(inventory) + 1,
            'name': name,
            'quantity': quantity,
            'price': price
        }
        inventory.append(new_product)
        self.save_inventory(inventory)
        print(f"Produto {name} adicionado com sucesso!")
    
    def update_inventory(self, sales_data):
        """
        Atualiza o estoque com base em dados de venda
        
        :param sales_data: Dicionário com detalhes da venda
        """
        inventory = self.load_inventory()
        sales_log = []
        
        # Carrega registros de vendas anteriores
        try:
            with open(self.sales_file, 'r') as f:
                sales_log = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            sales_log = []
        
        # Atualiza o estoque com base na venda
        for item in sales_data['items']:
            for product in inventory:
                if product['name'].lower() == item['name'].lower():
                    # Reduz a quantidade no estoque
                    if product['quantity'] >= item['quantity']:
                        product['quantity'] -= item['quantity']
                    else:
                        print(f"Erro: Estoque insuficiente para {item['name']}")
                        return False
        
        # Salva o inventário atualizado
        self.save_inventory(inventory)
        
        # Registra a venda
        sale_record = {
            'id': len(sales_log) + 1,
            'date': datetime.now().isoformat(),
            'total_value': sales_data['total_value'],
            'items': sales_data['items']
        }
        sales_log.append(sale_record)
        
        # Salva o registro de vendas
        with open(self.sales_file, 'w') as f:
            json.dump(sales_log, f, indent=4)
        
        print("Estoque atualizado com sucesso!")
        return True
    
    def view_inventory(self):
        """
        Exibe o inventário atual
        """
        inventory = self.load_inventory()
        print("\n--- INVENTÁRIO ATUAL ---")
        for product in inventory:
            print(f"ID: {product['id']} | Nome: {product['name']} | Quantidade: {product['quantity']} | Preço: R$ {product['price']:.2f}")
    
    def view_sales_history(self):
        """
        Exibe o histórico de vendas
        """
        try:
            with open(self.sales_file, 'r') as f:
                sales_log = json.load(f)
            
            print("\n--- HISTÓRICO DE VENDAS ---")
            for sale in sales_log:
                print(f"\nVenda ID: {sale['id']}")
                print(f"Data: {sale['date']}")
                print(f"Valor Total: R$ {sale['total_value']:.2f}")
                print("Itens:")
                for item in sale['items']:
                    print(f"  - {item['name']} | Quantidade: {item['quantity']} | Preço Unitário: R$ {item['price']:.2f}")
        except (FileNotFoundError, json.JSONDecodeError):
            print("Nenhum registro de venda encontrado.")

def main():
    # Exemplo de uso
    manager = InventoryManager()
    
    # Adiciona alguns produtos iniciais
    manager.add_product("Camisa", 50, 79.99)
    manager.add_product("Calça", 30, 129.99)
    manager.add_product("Tênis", 20, 249.99)
    
    # Visualiza o inventário inicial
    manager.view_inventory()
    
    # Exemplo de venda
    venda = {
        'total_value': 359.98,
        'items': [
            {'name': 'Camisa', 'quantity': 2, 'price': 79.99},
            {'name': 'Calça', 'quantity': 1, 'price': 129.99}
        ]
    }
    
    # Atualiza o estoque
    manager.update_inventory(venda)
    
    # Visualiza o inventário após a venda
    manager.view_inventory()
    
    # Visualiza o histórico de vendas
    manager.view_sales_history()

if __name__ == "__main__":
    main()