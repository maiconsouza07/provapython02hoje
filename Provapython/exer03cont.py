# Analise o código abaixo:

def processar_dados():
    produtos = [
        ("Arroz", 5.50, 10),
        ("Feijão", 7.25, 8),
        ("Macarrão", 3.20, 15),
    ]

    total_estoque = sum(produto[2] for produto in produtos)
    precos_acima_da_media = [produto[0] for produto in produtos
    if produtos[1]> (sum(produto[1] for produto in produtos) / len(peodutos)) ]

    return total_estoque, precos_acima_da_media
    estoque_toal, produtos_mais_caros = processar dados ()

    print("Estoque total:", estoque_total)
    print("Produtos com preço acima da média:", produtos_mais_caros)

    # qual sera a saida?
    # >>> "Estoque toal:"
    # >>> "Produtos(s) com preço acima da media:"