import os
import random
from Class_menu import Menu
from User_Conversor import User

from Conversor import conversor
from dicts_info_monedas import dictionary_Moneys

def menu_3():
    Menu._id = random.randint(1, 1000)
    Menu.mensaje = """
     ¿A qué moneda deseas convertir tu dinero?

     1 - Pesos colombianos
     2 - Pesos argentinos
     3 - Pesos mexicanos
     4 - Dolares
     5 - Euros
     6 - Libras esterlinas

     elige una opción: """
    Menu.valor_entrada = int(input(Menu.mensaje))


def menu_2(valor_entrada):
    Menu.id = random.randint(1,1000)
    print('')
    Menu.mensaje = (f'¿Qué cantidad de {(dictionary_Moneys[valor_entrada])[0]} tienes?: ')
    Menu.valor_entrada = int(input(Menu.mensaje))

def menu_1():
    Menu._id = random.randint(1, 1000)
    Menu.mensaje = """
     ¿Qué moneda tienes?

     1 - Pesos colombianos
     2 - Pesos argentinos
     3 - Pesos mexicanos
     4 - Dolares
     5 - Euros
     6 - Libras esterlinas

     elige una opción: """
    Menu.valor_entrada = int(input(Menu.mensaje))

def run():
    User.name = (input(f'Bienvenido al conversor de Monedas, para empezar, danos tu nombre: '))
    User.id = random.randint(1, 1000)
    print(f'Hola {User.name}, ¡es un gusto poder ayudarte!')

    menu_1()
    conversor.id = random.randint(1, 1000)
    conversor.money_A = Menu.valor_entrada

    menu_2(Menu.valor_entrada)
    conversor.amount_coin = Menu.valor_entrada

    menu_3()
    conversor.money_B = Menu.valor_entrada
    conversor(conversor.id, conversor.money_A, conversor.money_B, conversor.amount_coin)

if __name__ == '__main__':
    os.system('cls')
    run()
