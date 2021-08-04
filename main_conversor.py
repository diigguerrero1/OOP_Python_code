

import random
from Class_menu import Menu
from User_Conversor import User
from Request_for_Use import Request_For_Use
from money_select import Money_Select
from Conversion import Conversion

def menu_1():
    Menu._id = random.randint(1, 1000)
    Menu.mensaje = """
     ¿Qué moneda posee?

     1 - Pesos colombianos
     2 - Pesos argentinos
     3 - Pesos mexicanos
     4 - Dolares
     5 - Euros
     6 - Libras esterlinas

     elige una opción: """
    Menu.valor_entrada = int(input(Menu.mensaje))

def menu_2():
    Menu._id = random.randint(1, 1000)
    Menu.mensaje = """
     ¿A qué moneda desea convertir su dinero?

     1 - Pesos colombianos
     2 - Pesos argentinos
     3 - Pesos mexicanos
     4 - Dolares
     5 - Euros
     6 - Libras esterlinas

     elige una opción: """
    Menu.valor_entrada = input(Menu.mensaje)


def run():
    User.name = (input(f'Bienvenido al conversor de Monedas, para empezar, danos tu nombre: '))
    User.id = random.randint(1, 1000)
    Money_Select.id = random.randint(1, 1000)
    print(f'Hola {User.name}')
    menu_1()
    menu_2()


if __name__ == '__main__':
    run()
