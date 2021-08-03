from money_select import Money_Select
from moneda import Money

def peso_COP():
    peso_COP = Money()
    peso_COP.id = 1010
    peso_COP.name = 'Peso Colombiano'
    peso_COP.valor_respecto_a = {}

def peso_Mex():
    peso_MX = Money()
    peso_MX.id = 1020
    peso_MX.name = 'Peso Mexicano'
    peso_MX.valor_respecto_a = {}

def peso_Arg():
    peso_Arg = Money()
    peso_Arg.id = 1030
    peso_Arg.name = 'Peso Argentino'
    peso_Arg.valor_respecto_a = {}

def euro():
    Euro = Money()
    Euro.id = 2020
    Euro.name = 'Euro'
    Euro.valor_respecto_a = {}

def dollar():
    Dollar = Money()
    Dollar.id = 2010
    Dollar.name = 'Dollar Americano'
    Dollar.valor_respecto_a = {}

def libra():
    Libra = Money()
    Libra.id = 2030
    Libra.name = 'Libra Esterlina'
    Libra.valor_respecto_a = {}