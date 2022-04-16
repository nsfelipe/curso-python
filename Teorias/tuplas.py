"""
Tuplas (tuple) - São bastante parecidas com listas mas existem basicamente duas diferenças:

1 - As tuplas são representadas por parenteses: 

tupla = (1, 2, 3, 4, 5, 6)

2 - As tuplas sao imutaveis: Isso significa que ao se criar uma tupla ela não muda. Toda operação em uma tupla gera uma nova tupla.

# CUIDADO 1: As tuplas são representadas por parenteses (), mas veja:
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# CUIDADO 2: Tuplas com 1 elemento:
tupla3 = (4) # Isso não é considerado uma tupla pois tem apenas um elemento
print(tupla3)
print(type(tupla3))

tupla4 = (4, ) # Isso é uma tupla pois ela é considerada quando possui um parenteses, mesmo tendo apenas um elemento 
print(tupla4)
print(type(tupla4))

# CONCLUSÃO: Podemos concluir que tuplas é definida pela virgula e não pelo uso do parenteses.

(4) > não é tupla
(4, ) > é tupla
4, > é tupla

# Podemos gerar uma tupla dinamicamente com o range(inicio, fim, passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla

tupla = ('Felipe Nunes', 'Aprendendo a programar em Python')

aluno, curso = tupla

print(aluno)
print(curso)

# OBS: Gera erro (ValueError) se colocarmos um numero diferente de elementos para desempacotar.

# Métodos para adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutaveis.
# Soma*, Valor Máximo*, Valor Mínimo* e Tamanho

# * Se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

print(tupla1 + tupla2) # Tuplas são imutaveis, portanto elas não serão alteradas com esse método.

# Verificar se um determinado elemento se encontra na tupla:

tupla = (1, 2, 3)

print(3 in tupla) # Retorna true caso verdadeiro ou false caso seja falso

# Iterando sobre uma tupla

tupla = (1, 2, 3, 4, 5, 6)

# imprime o valor de cada elemento em uma linha
for n in tupla:
    print(n)

# Imprime a posição na tupla e o valor da posição:
for i, valor in enumerate(tupla):
    print(i, valor)

# Iterando com while

meses =  ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1

# Contando elementos dentro de uma tupla:

tupla = ('a', 'b', 'c', 'a')

print(tupla.count('a')) # Retorna 2 pois a letra 'a' repete duas vezes

# Converter uma string para uma tupla:

aluno = tuple('Felipe Nunes Santos') 

print(aluno)
print(aluno.count('e')) # Retorna 3 pois a letra 'e' aparece 3 vezes na tupla

"""
# Dicas na utilização de tuplas: Devemos utilizar as tuplas SEMPRE que não precisar modificar os dados contidos em uma coleção.

# Exemplo 1:

meses =  ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

print(meses)

# O acesso de elementos de uma tupla é semelhante ao de uma lista
print(meses[3])

# Verificando em qual indice o elemento esta na tupla:

print(meses.index('Maio')) # OBS: Gera erro (ValueError) se colocarmos um valor diferente de elementos da tupla


