from math import pow, sqrt
from time import sleep


def msg():
    while True:
        inicio()
        try:
            home = int(input('Escolha uma operação \n[+]1\n[-]2\n[*]3\n[/]4\n[n]5\n[√]6\n  => '))  # Requisita que o usuario escolha a operação
            if home == 1:
                soma()
            elif home == 2:
                subtrair()
                break
            elif home == 3:
                multiplicar()
                break
            elif home == 4:
                dividir()
                break
            elif home == 5:
                potencia()
                break
            elif home == 6:
                raiz()
                break
            else:
                print('Opcão inválida!')
                sleep(2)
                print('_'*20, '\n'*20)
        except Exception as e:
            print(f"Error! digite somente numeros.\nErro: {e}")
            sleep(3)
        while True:
            finalizar = str(input('Finaliar programa? [S/N] ')).upper().strip()[0]
            if finalizar in 'S':
                print('finalizando...')
                sleep(1)
                exit()
            elif finalizar == 'N':
                msg()
            else:
                print('\n'*20)
                print('Digite S para sair ou N paracontinuar')



def inicio():
    print('''
         =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                      D i g i t a l
            _____       _       __       _____
           |     |    /   \    |  |     |     | 
           |   __|   /  _  \   |  |     |   __| 
           |  |     /  /_\  \  |  |     |  |    
           |  |__  |    _    | |  |___  |  |__      
           |     | |   / \   | |      | |     | 
           |_____| |__|   | _| |______| |_____|   
        =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        ''')


def soma():
    n1 = float(input('Insira um numero: '))
    n2 = float(input('Insira outro numero: '))
    somar: int = n1 + n2
    print('_'*20)
    print(f'Resultado: {somar}')
    print('_'*20)


def subtrair():
    n1 = float(input('Insira um numero: '))
    n2 = float(input('Insira outro numero: '))
    sub: int = n1 - n2
    print('_' * 20)
    print(f'Resultado: {sub}')
    print('_' * 20)


def multiplicar():
    n1 = float(input('Insira um numero: '))
    n2 = float(input('Insira outro numero: '))
    mult: int = n1 * n2
    print('_' * 20)
    print(f'Resultado: {mult}')
    print('_' * 20)


def dividir():
    n1 = float(input('Insira um numero: '))
    n2 = float(input('Insira outro numero: '))
    div: int = n1 / n2
    print('_' * 20)
    print(f'Resultado: {div:.2f}')
    print('_' * 20)


def potencia():
    n1 = float(input('Insira um numero: '))
    n2 = float(input('Insira o expoente: '))
    pot: int = pow(n1, n2)
    print('_' * 20)
    print(f'Resultado: {pot}')
    print('_' * 20)


def raiz():
    n1 = float(input('Insira um numero: '))
    rai: float = sqrt(n1)
    print('_' * 20)
    print(f'Resultado: {rai:.2f}')
    print('_' * 20)


msg()