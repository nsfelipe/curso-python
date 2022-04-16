# leia um vetor de 10 posições
# #contar e escrever quantos valores pares ele possui

vetor = []

for i in range(10):
    valor = int(input('Digite um valor: '))
    vetor.append(valor)

pares = 0 
for i in vetor:
    if i % 2 == 0:
        pares = pares + 1
        print(f'Valor par: {i}')

print(f'O vetor possui {pares} valores pares')
