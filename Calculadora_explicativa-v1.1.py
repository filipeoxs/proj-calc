import math


# print('') mostra ao usuario uma mensagem, pode conter variaveis ou somente texto

# para coletar dados do usuario se usa a função input(''), que enviara um texto e 
# o que o usuario digitar sera gravado, por isso é associado a uma variaval : n1 = input('')
# para definir o tipo de valor que a variavel recebera, basta usa tipo(input(''))
# exemplo: str(input('')) para string, int(input('')) para numeros inteiros e float(input('')) para numeros com virgula

# o \n durante uma exibição de mensagem serve para quebrar linhas, ou voce pode usar (''' texto ''') assim as quebras de linha são
# consideradas normalmente




#print('''

'''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                  Digital
  ___     ___    __         ___
 |         |   |  ___ |  |   |       |         |
 |    __|   | |     ||  |   |       |    __|
 |   |         | |___||  |   |       |   |
 |   |__    |   __  |  |   |       |   |___
 |         |   |  |   | |  |   |___  |         |
 |___|   |_|   ||  |___| |___|

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='''

#''')

'''while True:
    n1 = float(input('Digite um numero: ')) # Requisita ao usuario o primeiro valor
    n2 = float(input('Digite outro numero: ')) # Requisita ao usuario o segundo valor
    home = ' '
    home = int(input('Escolha uma operação \n [+]1 \n [-]2 \n [*]3\n')) # Requisita que o usuario escolha a operação
    # Começo dos calculos

    if home == 1:
        s = n1+n2
        print('A soma dos numeros {} e {} é igual a {}'.format(n1, n2, s)) #Exibe os dois valores digitados pelo usuario e o resultado da soma entre eles

    elif home == 2:
        sb = n1-n2
        print('A subtração dos numeros {} e {} é igual a {}'.format(n1, n2, sb)) #Exibe os dois valores digitados pelo usuario e o resultado da subtração entre eles

    elif home == 3:
        mult = n1*n2
        print('A multiplicação dos numeros {} e {} é igual a {}'.format(n1, n2, mult,)) #Exibe os dois valores digitados pelo usuario e o resultado da multiplicação entre eles
    elif home > 3:
        print('opção invalida. Digite uma das opções acima.')
    # Fim dos calculos
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer digitar uma nova operação: [S/N}')).upper().strip()[0]
    if resposta == 'N':
        break'''


'''GP2'''



def msg():
    print('''
     = -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -=
    Digital
    ___
    ___
    __
    ___
    | | | ___ | | | | |
    | __ | | | | | | | | __ |
    | | | | ___ | | | | | |
    | | __ | __ | | | | | ___
    | | | | | | | | ___ | |
    | ___ | | _ | | | | ___ | | ___ |

    = -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= -= 
    ''')

    home = int(input('Escolha uma operação \n[+]1\n[-]2\n[*]3\n[/]4\n[n]5\n[√]6\n[%]7')) # Requisita que o usuario escolha a operação
    try:
        num_1 = input('Insira um numero:')
        n1 = float(num_1)
        num_2 = input('Insira outro numero:')
        n2 = float(num_2)
        if home == 1:
            soma(n1,n2)
        elif home == 2:
            subtrair(n1,n2)
        elif home == 3:
            multiplicar(n1,n2)
        elif home == 4:
            dividir(n1,n2)
        elif home == 5:
            potencia(n1,n2)
        elif home == 6:
            raiz()
        else:
            print('Escolha uma das opções acima!')


    except Exception as e:
        print(f"Error! digite somente numeros.\nError {e}")



def soma(n1,n2):
    somar:int = n1+n2
    print(somar)

def subtrair(n1,n2):
    sub:int = n1-n2
    print(sub)

def multiplicar(n1,n2):
    mult:int = n1 * n2
    print(mult)

def dividir(n1,n2):
    div:int = n1 / n2
    print(div)

def potencia(n1,n2):
    pot:int = n1 ** n2
    print(pot)

def raiz():
    num_1 = input('Insira um numero:')
    n1 = float(num_1)
    rai:float = math.sqrt(n1)
    print(rai)

msg()