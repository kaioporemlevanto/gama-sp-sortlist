def ordenar_por_frequencia(palavras, caracter):
    
    def contar_caracter(palavra):
        return palavra.lower().count(caracter.lower())
    
    palavras_ordenadas = sorted(palavras, key=contar_caracter, reverse=True)
    
    return palavras_ordenadas

palavras = input("Digite as palavras separadas por vírgula: ").split(',')
caracter = input("Digite o caractere: ")

palavras = [palavra.strip() for palavra in palavras]

resultado = ordenar_por_frequencia(palavras, caracter)
print(resultado)
