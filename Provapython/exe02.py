# Voce tem uma lista de tuplas, onde cada tupla representa uma cidade como o nome da cidade e uma lista de temperaturas 
# registradas ao longo de uma semana (7 temperaturas). Escreva uma função que calcule a temperatura média para 
# cada cidade e retorne uma lista de tuplas com o nome da cidade e a temperatura média.

def calcular_temperatura_media(cidades):
    medias = []
    
    for cidade, temperaturas in cidades:
        temperatura_media = sum(temperaturas) / len(temperaturas)
        medias.append((cidade, temperatura_media))
    
    return medias

# Exemplo de uso
cidades = [
    ("São Paulo", [25, 26, 27, 24, 28, 29, 30]),
    ("Rio de Janeiro", [30, 31, 32, 29, 28, 27, 30]),
    ("Belo Horizonte", [22, 23, 24, 25, 26, 27, 28]),
]

resultado = calcular_temperatura_media(cidades)
print(resultado)

