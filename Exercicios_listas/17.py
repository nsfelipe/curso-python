# Leia um vetor de 10 posições
# Atribua o valor 0 caso o numero seja negativo

vetor = []

for i in range(10):
    valor = int(input('Digite um número: '))
    if valor < 0:
        valor = 0
    vetor.append(valor)

print(vetor)

