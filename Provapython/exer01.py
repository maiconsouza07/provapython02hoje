# Palíndromo é uma palavra, frase ou número que permanece igual quando lida de trás para diante. Por extensão, palíndromo
 #é qualquel série de elementos com simetria lineal, ou seja, que apresenta a mesma sequencia de unidades nos dois sentidos.
 #Exemplo: OVO é um polídromo

 #Pode se escrever um código em python que:
 #Receba um input de entrada no usuário;
 #Cria um método para verificar se a entrada de informação é um políndromo;
 #Fazer todas as verificações/validações necessária.

def eh_palindromo(s):
    # Remove espaços e converte para minúsculas
    s = s.replace(" ", "").lower()
    # Compara a string com sua reversa
    return s == s[::-1]

def main():
    entrada = input("Digite uma palavra ou frase: ")
    
    if not entrada:  # Verifica se a entrada não está vazia
        print("Entrada inválida. Por favor, digite algo.")
        return
    
    if eh_palindromo(entrada):
        print(f'"{entrada}" é um palíndromo!')
    else:
        print(f'"{entrada}" não é um palíndromo.')

# Executa a função principal
if __name__ == "__main__":
    main()
