"""
Definindo funções:
- São pequenas partes de código que realizam tarefas específicas;
- Elas podem ou não receber entrada de dados e retornar uma saída de dados;
- Muito úteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela, é bom fazer uma verificação para que a função seja simplificada.

# Exemplo de utilização de funções:

cores = ['verde', 'amarelo', 'azul', 'braco']

# Utilizando funcão integrada (Built-in) do Python
print(cores)

# Adicionando mais uma cor na lista cores:
cores.append('roxo')

# Como definir funções

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

nome_da_funcao = Sempre com letras minusculas e se for nome compostos, separado por underline (snake_case);
parametros_de_entrada = Opicionais, onde tendo mais de um, cada um separado por virgula, podendo ser opicionais ou não;
bloco_da_funcao =  Também chamado de corpo da função ou implementação

OBS: Veja que para definir uma função, utilizamos a paravra reservada 'def' informando ao Python que estamos definindo uma função.
Também abrimos o bloco de código com o ja conhecido dois pontos: que é utilizado em Python para definir os blocos.

"""
# Definindo a primeira função:

def diz_oi():
    print('Oii!')

# Veja que, dentro das nossas funções podemos utilizar outras funções;
# Veja que nossa função só executa 1 tarefa, ou seja, a unica coisa q ela faz é dizer oi;
# Veja que essa função não recebe nenhum parametro de entrada;
# Veja que essa função não retorna nada.

# Utilizando funções: Chamada de execução
diz_oi() # Sempre com os parenteses logo após o nome da função

def cantar_parabens():
    print('Parabens pra voce')
    print('Nessa data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida!!!')

cantar_parabens() # Executa a função acima 

# Executando funções dentro do for

for i in range(5):
    diz_oi()

# Podemo inclusive cria variaveis do tipo de uma função e executar essa função atravez da variável

canta = cantar_parabens

canta()



