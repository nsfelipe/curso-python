# Crie um programa que le 6 valores inteiros
# Mostre na tela os valores lidos na ordem inversa


vetor = []

# lê os valores do vetor
for i in range(6):
    valor = int(input('Digite um valor: '))
    vetor.append(valor)

# Inverte a ordem dos valores do vetor
vetor.reverse()
print(vetor)

