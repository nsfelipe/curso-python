# leia um vetor com 10 posições
# Imprima o maior elemento do vetor
# Imprima o menor elemento do vetor

vetor = []

for i in range(10):
    valor = int(input('Digite um valor: '))
    vetor.append(valor)

valorMax = max(vetor)
valorMin = min(vetor)

print(f'Maior valor: {valorMax} \nMenor valor: {valorMin}')
