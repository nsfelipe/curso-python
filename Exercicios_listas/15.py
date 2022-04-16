# Leia um vetor com 20 numeros inteiros
# Escreva os elementos eliminando os numeros repetidos

vetor = []

for i in range(20):
    valor = int(input('Digite um numero inteiro: '))
    vetor.append(valor)

repetidos = []
vetor.sort()
print(vetor)

for i in vetor:
    # Verifica se o numero aparece mais de uma vez
    if vetor.count(i) > 1:
        repetidos.append(i)
        print(f'Removendo o elemento {i} por estar repetido!')
        # Remove o elemento duplicado conforme validação acima
        vetor.pop(i)

print(vetor)
print(repetidos)