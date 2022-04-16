# Leia um conjunto de números reais, armazenando-os em vetor
# Calcular o quadrado dos elementos desse vetor
# Armazenar o resultado em outro vetor
# Os conjuntos tem 10 elementos cada, imprimir todos os conjuntos

conjunto = []

# Recebe os valores e adiciona na lista
for i in range(0, 10):
    valor = int(input('Digite um número inteiro: '))
    conjunto.append(valor)

# Calcula a raiz dos elementos da lista e adiciona em uma nova lista
resultadoQuadrado = []
for i in conjunto:
    quadrado = i ** 0.5
    resultadoQuadrado.append(round(quadrado, 2))

print(conjunto)
print(resultadoQuadrado)
    
