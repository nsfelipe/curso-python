# Leia um vetor de 10 numeros.
# Leia um número x.
# Conte os multiplos de um numero inteiro x e mostre-os na tela


vetor = []

# Lê os valores do vetor
for i in range(10):
    valor = int(input('Digite um valor: '))
    vetor.append(valor)

x = int(input('Digite o valor de X:'))

multiplos = []


for i in vetor:
    # Verifica se o número no vetor é multiplo de 'x'
    if i % x == 0:
        # Se sim insere ele num vetor de multiplos
        multiplos.append(i)

print(f'A quantidade de números divisíveis por {x} é: {len(multiplos)}')
print(f'Os números são: {multiplos}')

