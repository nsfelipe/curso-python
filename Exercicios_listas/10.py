# Escreva um programa que leia a nota de 15 alunos e armazene num vetor
# Calcule e imprima a média geral

vetor = []
contador = 0

# lê os valores do vetor
for i in range(15):
    contador = contador + 1
    valor = int(input(f'Digite a nota do aluno {contador}: '))
    vetor.append(valor)

# Calcula a média
media = sum(vetor) / len(vetor)
print(f'A média geral das notas é: {media}')

