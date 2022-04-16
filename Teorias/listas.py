"""
Listas: funcionam como vetores/matrizes(arrays) em outras linguagens, com a diferença de ser DINAMICOS e de podermos colocar QUALQUER tipo de dado.

- Dinâmico: Não possui tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos a ela;
- Qualquer tipo de dado: As listas não possuem tipo de dado fixo;

As listas em python são representadas por colchetes []

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['a', 'z', 'c', ' ', 'y']

lista3 = []

lista4 = list(range(0, 100))

lista5 = list('Felipe Nunes Santos')

lista6 = [1, 2.34, True, 'Felipe', 'xD', [1, 2, 3], 123135341241]

cores = ['verde', 'amarelo', 'azul', 'branco']

#  Podemos checar se determinado valor esta contido na lista
num = int(input('Digite um número para pesquisar: '))

if num in lista4:
    print(f'Número {num} encontrado!')
else:
    print(f'Número {num} não encontrado! :(')

#  Ordenar uma lista

lista1.sort()
print(lista1)

# Contar um numero de ocorrencias de um valor em uma lista

print(lista1.count(1))
print(lista2.count('a'))

# Adicionar elementos em listas

# Para adicionar elementos ou valor em listar utilizamos a função append
# Com o append só conseguimos adicionar um elemento por vez 

print(lista1)
lista1.append(2)
print(lista1)

# Adicionar valores dentro de uma lista ja existente

lista1.extend([1, 3, 5, 99, 50, 11, 56, 41])


# Podemos inserir um novo elemento na lista informando a posição do índice
# insert(posição, valor)
lista1.insert(2, 69)

# Juntar duas listas
lista1 = lista1 + lista2
lista1.extend(lista5)

# Remover elementos pelo numero do indice
lista5.pop(2)

# Converter uma string em uma lista
curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)
# Por padrão o split separa os elementos da lista pelo espaço entre elas

# Exemplo 2
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split()
print(curso)

# Convertendo uma lista em uma string
lista6 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista6)

# Abaixo juntamos cada elemento da string formando uma string unica, uma frase, pode ser feito com vários simbolos
curso = ' '.join(lista6)
print(curso)

# Iterando sobre listas
# Exemplo 1 utilizando for

soma = 0

for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 utilizando while

carrinho = []
produto = ''

while produto != 'sair':
    print('Adicione um produto na lista ou digite "sair" para sair: ')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(f'Adicionados ao carrinho: {produto}')

# Utilizando variaveis em listas

numeros = [1, 2, 3, 4, 5]

# é igual a:
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
numeros = [num1, num2, num3, num4, num5]

# Fazemos acesso aos elementos de forma indexada

cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[1]) # verde
print(cores[3]) # branco

# Para entender melhor o indice negativo, pense na lista como um circulo onde o final de um elemento esta igado ao inicio da lista
print(cores[-1]) # exibe o ultimo item da lista = branco

# Imprimir itens de uma lista com for

for cor in cores:
    print(cor)

# Imprimir itens de uma lista com while

i = 0
while i < len(cores):
    print(cores[i])
    i = i + 1

# Gerar indice de uma lista com for

cores = ['verde', 'amarelo', 'azul', 'branco']
for i, cor in enumerate(cores):
    print(i, cor)

# Encontrar um indice de elementos na lista

numeros = list(range(1, 1000))
print(numeros.index(99))

# Caso o elemento não exista na lista será apresentado ValueError
# Caso o numero esteja duplicado ele retorna o indice do primeiro elemento encontrado

# Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar

print(numeros.index(3, 1)) # Busca a partir do indice 1
print(numeros.index(5, 2)) # Busca a partir do indice 2
# Caso o elemento não exista na lista será apresentado ValueError

# Podemos buscar dentro de um range inicio/fim
print(numeros.index(8, 6, 10)) # Buscar o indice do valor 8, entre os indices 6 e 10

# trabalhando com slice de lista com parametro 'inicio'

# lista[inicio:fim:passo]
# range(inicio, fim, passo)

numeros = [1, 2, 3, 4, 5]
print(numeros[0:4]) # Itera sobre a lista do indice 0 ao 4 de 2 em 2 numeros

# Trabalhando com slice de lista com parametro 'fim'
print(numeros[:2]) # Começa em 0, pega até o indice 2 - 1
print(numeros[1:3]) # Começa em 1, vai te o indice 3 - 1

# Trabalhando com slice de lista com parametro 'passo'
print(numeros[::2]) # Itera sobre a lista do indice de 2 em 2 numeros

# Invertendo valores

nomes = ['Felipe', 'Nunes']

nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

# Invertendo com função reverse
nomes.reverse()
print(nomes)

nomeCompleto = ' '.join(nomes)
print(nomeCompleto)

# Soma*, Valor maximo*, Valor minimo*, tamanho
# * se os valores forem todos inteiros ou reais



print(sum(lista)) # Soma
print(max(lista)) # Maximo
print(min(lista)) # Minimo
print(len(lista)) # Tamanho da lista


# Transformar uma lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)

tupla = tuple(lista)
print(tupla)

# Desempacotamento de listas

lista = [1, 2, 3]
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)

# Para desempacotar deve-se sempre ter o numero de variaveis para o numero de elementos da lista

# Copiando uma lista para outra: (Shallow Copy e Deep Copy)

# Forma 1 - Deep Copy
lista = [1, 2, 3]
print(lista)

# Ao utilizarmos a lista.copy() copiamos os dados da lista para uma nova lista, mas elas ficaram totalmente independentes
nova = lista.copy()
print(nova)

nova.append(4)
print(nova)

# Forma 2 - Shallow Copy

lista = [1, 2, 3]
print(lista)

nova = lista
print(nova)

nova.append(4)
print(lista)
print(nova)

# Veja que utilizamos a copia via atribuição e copiamos os dados da lista para a nova lista mas após realizar a modificaçao
# em uma das listas ela refletiu em ambas as listas


"""

numero = 3.1622776601683795
print(round(numero, 2))

