# Faça um programa que leia um vetor de 8 posições
# Em seguida leia tambem dois valores: X e Y quaisquer correspondentes a duas posições no vetor
# Escrever a soma dos valores X e Y

vetor = []

# Lê os 8 valores
for i in range(8):
    valor = int(input('Digite um número: '))
    vetor.append(valor)

# lê o valor de X e Y 
x = int(input('Digite o valor de X: '))
y = int(input('Digite o valor de Y: '))
x = x - 1
y = y - 1

# Soma do valor de Y e Y
soma = vetor[x] + vetor[y]
print(vetor)
print(soma)


