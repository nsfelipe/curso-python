# Leia um vetor de 5 numeros reais
# Leia um codigo inteiro onde:
# 0 encerra o programa; 1 mostra o vetor na ordem direta; 2 Mostra o vetor na ordem inversa
# Caso seja diferente dos numeros acima encerre o programa

vetor = []

for i in range(5):
    valor = float(input('Digite um número: '))
    vetor.append(valor)

vetor.sort()
print(vetor)
print('Digite 1 para exibir o vetor na ordem direta. \nDigite 2 para exibir o vetor na ordem inversa. \nDigite 0 para sair')
option = int(input('Digite uma opção:'))

if option == 0:
    print('Fechado o programa!')
    quit()

if option == 1:
    print(f'O vetor na ordem direta: {vetor}')

if option == 2:
    print(f'O vetor na ordem inversa: {vetor.reverse()}')

if option != 0 or option != 1 or option != 2:
    print('O valor informado é inválido, reinicie o programa!')
    quit()
