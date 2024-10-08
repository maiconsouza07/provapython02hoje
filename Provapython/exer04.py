# Voce é responsavel por desenvolver um sistema simples de gerenciamento de produtos para uma loja
# em python. Cada produto é representado por uma tupla que contem as seguintes informações:

# Nome do produto(string)
# Código do produto(inteiro)
#Preço(float)
#Estoque diponível(inteiro)

# pede-se: 

# A) Crie uma função chamada criar_produto que recebe quatro parametros: nome, codigo, preço
# e estoque, e retorne uma tupla representando um produto. Atupla deve estar no formato:
# (nome codigo, preço, estoque)

# B) Em seguida, crie uma função chamada atualizar_estoque que receba duas tuplas: a tupla do produto e a quantidade
# a ser adicionada (um inteiro). Esta função deve retornar uma nova tupla com estoque atualizado

# C) Crie uma função chamada listar_produtos que receba uma lista de tuplas(produtos) e imprime as informações 
# de cada produto

# D) Por fim escreva um código que demonstre a utilização das funções acima. Voce deve cria pelo menos tres produtos utilizando a função criar_produto
# Atualizar o estoque de um dos produtos utilizando a função atualiza_estoque. Listar todos os produtos utilizando a função listar_prdutos



# A) Função para criar um produto
def criar_produto(nome, codigo, preco, estoque):
    return (nome, codigo, preco, estoque)

# B) Função para atualizar o estoque
def atualizar_estoque(produto, quantidade):
    nome, codigo, preco, estoque = produto
    estoque_atualizado = estoque + quantidade
    return (nome, codigo, preco, estoque_atualizado)

# C) Função para listar produtos
def listar_produtos(produtos):
    for produto in produtos:
        nome, codigo, preco, estoque = produto
        print(f"Nome: {nome}, Código: {codigo}, Preço: R${preco:.2f}, Estoque: {estoque}")

# D) Demonstração da utilização das funções
if __name__ == "__main__":
    # Criando produtos
    produto1 = criar_produto("Produto A", 101, 29.90, 50)
    produto2 = criar_produto("Produto B", 102, 49.90, 30)
    produto3 = criar_produto("Produto C", 103, 19.90, 20)

    # Listando produtos antes da atualização
    print("Produtos antes da atualização:")
    listar_produtos([produto1, produto2, produto3])

    # Atualizando o estoque do Produto A
    produto1 = atualizar_estoque(produto1, 10)

    # Listando produtos após a atualização
    print("\nProdutos após a atualização:")
    listar_produtos([produto1, produto2, produto3])
