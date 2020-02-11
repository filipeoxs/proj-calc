import math

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
    resto = n1 % n2
    print(div)
    print(resto)

def potencia(n1,n2):
    pot:int = n1 ** n2
    print(pot)

def raiz():
    num_1 = input('Insira um numero:')
    n1 = float(num_1)
    rai:float = math.sqrt(n1)
    print(rai)

msg()
