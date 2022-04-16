# Leia 6 valores inteiros pares
# Mostre os valores na ordem inversa


# Outra forma de resolver esse código seria verificar primeiro se o número é impar com um if e caso fosse entrar no while
# caso não fosse impar iria entrar no if fazendo append do valor no vetor
vetor = []

# lê os valores do vetor
for i in range(6):
    valor = int(input('Digite um valor par: '))
    par = False

    # Verifica se o elemento é par
    if valor % 2 == 0:
        par = True
        print('Número valido!')
    
    # Retorna caso elemento seja ímpar
    while par != True:
        print('Numero inválido. O valor informado é ímpar!')
        valor = int(input('Digite um valor par: '))
        
        # Confirma que o valor informado é par
        if valor % 2 == 0:
            par = True
            print('Número valido!')
    
    vetor.append(valor)

vetor.reverse()
print(vetor)




