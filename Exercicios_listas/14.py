# Faça um programa que leia um vetor de 10 posições
# Verifique se existem valores duplicados/iguais
# Exiba os valores duplicados/iguais na tela # Criar um vetor pra armazenar o valor duplicado


vetor = []

# lê os valores do vetor
for i in range(10):
    valor = float(input('Digite um valor: '))
    vetor.append(valor)

repetidos = []

# Verifica se o numero se repete 
for i in vetor:
    if vetor.count(i) > 1:
        # Adiciona o numero repetido no vetor de repetidos
        repetidos.append(i)
        print(f'O valor {i} se repete.')

print(repetidos)

