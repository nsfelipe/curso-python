"""
Funções com parâmetro(de entrada):
- Funções que recebem dados para serem processados dentro da mesma;
- Geralmente em um programa temos: entrada -> processamento -> saída

Se pensarmos em uma função sabemos que temos as seguintes variações de funções:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;

# Refatorando uma função: Calcular o quadrado de um número

def quadrado(numero): # Parametro é obrigatório caso a função precise de um valor de entrada;
    # return numero * numero
    return numero ** 2

print(quadrado(9))

# Refatorando a função: Cantar parabens:

def cantar_parabens(aniversariante):
    print('Parabens pra voce')
    print('Nessa data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o {aniversariante}!!!')

cantar_parabens('Felipe Nunes')

# Funções podemm ter 'n' parametros de entrada. Ou seja, podemos receber como entrada em uma função quantos paramentos forem necessarios, separados por virgula

# Exemplos:

def soma(a, b): # Soma o valor a + b
    return a + b

def multiplica(num1, num2): # Multiplica num1 + num2
    return num1 * num2

def outra(num1, b, msg):
    return(num1 + b) * msg

print(soma(5, 6))
print(multiplica(5, 3))
print(outra(5, 4, 'Felipe'))

#OBS: Se informar um numero errado de parametro ou argumentos, teremos TypeError

# Nomeando parâmetros:

def nome_completo(nome, sobrenome): # Utilizar sempre um nome entendível por outra pessoa no nome do parâmetro
    return f'Seu nome completo é: {nome} {sobrenome}'

print(nome_completo('Felipe', 'Nunes')) # Argumentos

# Diferencça entre parâmetros e Argumentos:

# Parametros: São variáveis declaradas na definição de uma função;
# Argumentos: São dados passados durante a execução de uma função;

# A ordem dos parametros importa e impacta na execução da função

nome = 'Felipe'
sobrenome = 'Santos'

print(nome_completo(sobrenome, nome)) # Será impresso invertido pois a ordem dos parâmetros está incorreta

# Argumentos nomeados (Keyword Arguments)

# Caso utilizemos nomes dos parametros nos argumentos para informá-los, podemos utilizar qualquer ordem.

print(nome_completo(nome='Felipe', sobrenome='Nunes'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Silvestre', nome='Tábata')) # Posso inverter pois estou usando argumentos nomeados

"""

# Erro comum na utilizaçã do return

def soma_impares(numeros): # Calcula a soma dos numeros impares de um vetor
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total # Se o return fica no bloco do if o for não vai ser percorrido corretamente

lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

