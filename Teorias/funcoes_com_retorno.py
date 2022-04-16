"""
Funções com retorno

numeros = [1, 2, 3]

ret = numeros.pop()

print(f'Retorno de pop: {ret} ')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr} ')

# Exemplo de função

def quadrado_de_7():
    print(7 * 7) # não retorna nada pois não foi passado o retorno

# Em Python quando uma função não retorna nenhum valor, o retorno é none

# Funções Python que retornam valores, devem retornar estes valores com a palavra reservada return

def quadrado_de_7():
    return 7 * 7

ret = quadrado_de_7()

print(f'Retorno: {ret} ') 

# Não precisamos necessáriamente criar uma variável para recebere o retorno de uma função. Podemos passar a execução da função para outras funções.

print(f'Retorno: {quadrado_de_7()}')

# Refatorando a primeira função diz_oi()

def diz_oi():
    return 'Oii!'

# Adicionando uma variavel e utilizando-a junto com a função:
alguem = 'Pedro'
print(diz_oi() + alguem)

# OBS: Sobre a palavra return

# 1 - Ela finaliza a função, ou seja, ela sai da execução da função;
# 2 - Podemos ter, em uma função, diferentes returns;
# 3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo multiplos valores;

# Exemplo 2:

def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

# Exemplo 3:

def outra_funcao():
    return [2, 3, 4, 5]


#num1, num2, num3, num4 = outra_funcao()
#print(num1, num2, num3, num4)

print(outra_funcao())

# Uma função para jogar a moeda: Cara ou coroa

from random import random

def joga_moeda():
    #Gera um numero pseudo-randominco entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())

"""
# Erros comuns na utilização do retorno, que na verdade não é erro mas sim uma condificação desnecessária.

def impar():
    numero = 5
    if numero % 2 != 0:
        return True
    return False # não é necessário o else pois o ultimo return é a ultima possibilidade da lógica

