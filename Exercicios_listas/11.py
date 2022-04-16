# Escreva um programa que preencha um vetor com 10 numeros reais
# Calcule e mostre a quantidade de numeros negativos
# Calcule a soma dos numeros positivos

vetor = []

negativos = 0
somaPositivos = 0

# lê os valores do vetor
for i in range(10):
    valor = float(input('Digite um valor: '))
    vetor.append(valor)
    
    #Verifica se é positivo ou negativo
    if valor < 0:
        negativos = negativos + 1
    else:
        somaPositivos = somaPositivos + valor


print(f'Quantidade de números negativos: {negativos}')
print(f'Soma dos números positivos: {somaPositivos}')

