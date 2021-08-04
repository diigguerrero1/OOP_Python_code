from Monedas import peso_COP
from Monedas import peso_Arg
from Monedas import peso_MX
from Monedas import euro
from Monedas import dollar
from Monedas import libra

import random
from User_Conversor import User
from Request_for_Use import Request_For_Use
from money_select import Money_Select
from Conversion import Conversion

def run():
    User.name = (f'Bienvenido al conversor de Monedas, para empezar, danos tu nombre: ')
    User.id = random.randint(1, 1000)
    Money_Select.id = random.randint(1, 1000)
    print(f'Hola {User.name}, ¿qué moneda tienes para hacer tu conversión?')
    menu_1 = """
     1 - Pesos colombianos
     2 - Pesos argentinos
     3 - Pesos mexicanos
     4 - Dolares
     5 - Euros
     6 - Libras esterlinas

     elige una opción: """

    moneda_A = int(input(menu_1))

    menu_2 = """
     ¿A qué moneda deseas hacer la conversión?

     1 - Pesos colombianos
     2 - Pesos argentinos
     3 - Pesos mexicanos
     4 - Dolares
     5 - Euros
     6 - Libras esterlinas

     elige una opción: """

    moneda_B = int(input(menu_2))

    if menu_1 == 1 and menu_2 == 2


if __name__ == '__main__':
    run()
