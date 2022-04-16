# Escreva um programa que leia 10 numeros inteiros e armazene em um vetor
# imprima o vetor
# Imprima o maior elemento e a sua posição

vetor = []

# lê os valores do vetor
for i in range(10):
    valor = int(input('Digite um valor: '))
    vetor.append(valor)

print(vetor)

# Define o maior valor
maior = max(vetor)

# Busca no vetor o indice do maior valor 
for i, elemento in enumerate(vetor):
    if elemento == maior:
        position = i

print(f'O maior valor é: {maior}, sua posição é: {position}.')



