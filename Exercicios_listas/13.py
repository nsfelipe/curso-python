# Ler 5 valores
# Mostrar a posição do maior e do menor valor

vetor = []

# lê os valores do vetor
for i in range(5):
    valor = int(input('Digite um valor: '))
    vetor.append(valor)

maior = max(vetor)
menor = min(vetor)

for i, elemento in enumerate(vetor):
    if elemento == maior:
        indiceMaior = i

    if elemento == menor:
        indiceMenor = i

print(f'O valor maximo: {maior}, esta no posição: {indiceMaior}')
        
print(f'O valor menor: {menor}, esta na posição: {indiceMenor}') 


