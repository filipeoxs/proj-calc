from math import pow, sqrt, factorial, sin, cos, tan, radians
from time import sleep


def msg():
    while True:
        inicio()
        try:
            home = int(input('Escolha uma operação \n[+]1\n[-]2\n[*]3\n[/]4\n[n]5\n[√]6\n[%]7\n[n!]8\n[sen]9\n[cos]10\n[tan]11\n  => '))  # Requisita que o usuario escolha a operação
            if home == 1:
                soma()
            elif home == 2:
                subtrair()
            elif home == 3:
                multiplicar()
            elif home == 4:
                dividir()
            elif home == 5:
                potencia()
            elif home == 6:
                raiz()
            elif home == 7:
                porcentagem()
            elif home == 8:
                fatorial()
            elif home == 9:
                seno()
            elif home == 10:
                coseno()
            elif home == 11:
                tangente()
            else:
                print('Opcão inválida!')
                sleep(2)
                print('_'*20, '\n'*20)
        except ValueError:
            print(f'Isto não é um numero. Digite somente valor numérico.')
        except ZeroDivisionError:
            print(f'O denominador nã pode ser zero.')
        except Exception as e:
            print(f'Aconteceu algum erro inesperado.\nErro {e}')
            sleep(3)
        while True:
            finalizar = str(input('Finalizar programa? [S/N] ')).upper().strip()[0]
            if finalizar in 'S':
                print('finalizando...')
                sleep(1)
                exit()
            elif finalizar == 'N':
                msg()
            else:
                print('\n'*20)
                print('Digite S para sair ou N para continuar')



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
    somar = n1 + n2
    print('_'*20)
    print(f'Resultado: {somar}')
    print('_'*20)


def subtrair():
    n1 = float(input('Insira um numero: '))
    n2 = float(input('Insira outro numero: '))
    sub = n1 - n2
    print('_' * 20)
    print(f'Resultado: {sub}')
    print('_' * 20)


def multiplicar():
    n1 = float(input('Insira um numero: '))
    n2 = float(input('Insira outro numero: '))
    mult = n1 * n2
    print('_' * 20)
    print(f'Resultado: {mult}')
    print('_' * 20)


def dividir():
    n1 = float(input('Insira um numero: '))
    n2 = float(input('Insira outro numero: '))
    div = n1 / n2
    print('_' * 20)
    print(f'Resultado: {div:.2f}')
    print('_' * 20)


def potencia():
    n1 = float(input('Insira um numero: '))
    n2 = float(input('Insira o expoente: '))
    pot = pow(n1, n2)
    print('_' * 20)
    print(f'Resultado: {pot}')
    print('_' * 20)


def raiz():
    n1 = float(input('Insira um numero: '))
    rai: float = sqrt(n1)
    print('_' * 20)
    print(f'Resultado: {rai:.2f}')
    print('_' * 20)


def porcentagem():
    n1 = float(input('Insira um numero: '))
    n2 = float(input('Insira a porcentagem: '))
    porc = (n2 * n1) / 100
    print(f'Resultado: {porc:.2f}')

def fatorial():
    n1 = int(input('Insira um numero inteiro: '))
    fat = factorial(n1)
    print(f'Resultado: {fat:.2f}')

def seno():
    n1 = int(input('Insira um angulo: '))
    angulo = radians(n1)
    s = sin(angulo)
    print(f'Resultado: {s:.2f}')

def coseno():
    n1 = int(input('Insira um angulo: '))
    angulo = radians(n1)
    s = cos(angulo)
    print(f'Resultado: {s:.2f}')

def tangente():
    n1 = int(input('Insira um angulo: '))
    angulo = radians(n1)
    s = tan(angulo)
    print(f'Resultado: {s:.2f}')


msg()
