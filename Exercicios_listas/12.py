# Ler 5 valores
# Mostrar todos os valores lidos
# Mostrar o maior valor, menor e a média dos valores

vetor = []

# lê os valores do vetor
for i in range(5):
    valor = float(input('Digite um valor: '))
    vetor.append(valor)

# Apresenta os valores do vetor
for valor in vetor:
    print(valor)

# Apresenta o maior e o menor
print(f'Valor maximo: {max(vetor)}')
print(f'Valor minimo: {min(vetor)}')