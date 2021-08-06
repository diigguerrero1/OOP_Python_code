
from moneda import Money
from dicts_info_monedas import dict_Cop
from dicts_info_monedas import dict_arg
from dicts_info_monedas import dict_mx
from dicts_info_monedas import dict_dol
from dicts_info_monedas import dict_eur
from dicts_info_monedas import dict_lib

class peso_COP(Money):
    
    def __init__(self, id, name, valor_respecto_a):
        super().__init__(id, name, valor_respecto_a)
        peso_COP.id = 1010
        peso_COP.name = dict_Cop
        peso_COP.valor_respecto_a = dict_Cop

class peso_MX(Money):
    
    def __init__(self, id, name, valor_respecto_a):
        super().__init__(id, name, valor_respecto_a)
        peso_MX.id = 1020
        peso_MX.name = 'Peso Mexicano'
        peso_MX.valor_respecto_a = dict_mx

class peso_Arg(Money):
    
    def __init__(self, id, name, valor_respecto_a):
        super().__init__(id, name, valor_respecto_a)
        peso_Arg.id = 1030
        peso_Arg.name = 'Peso Argentino'
        peso_Arg.valor_respecto_a = dict_arg

class euro(Money):
    
    def __init__(self, id, name, valor_respecto_a):
        super().__init__(id, name, valor_respecto_a)
        euro.id = 2020
        euro.name = 'Euro'
        euro.valor_respecto_a = dict_eur

class dollar(Money):
    
    def __init__(self, id, name, valor_respecto_a):
        super().__init__(id, name, valor_respecto_a)
        dollar.id = 2010
        dollar.name = 'Dollar Americano'
        dollar.valor_respecto_a = dict_dol

class libra(Money):
    
    def __init__(self, id, name, valor_respecto_a):
        super().__init__(id, name, valor_respecto_a)
        libra.id = 2030
        libra.name = dict_lib
        libra.valor_respecto_a = dict_lib
