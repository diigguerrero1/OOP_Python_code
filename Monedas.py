from moneda import Money

class peso_COP(Money):
    
    def __init__(self, id, name, valor_respecto_a):
        super().__init__(id, name, valor_respecto_a)
        peso_COP.id = 1010
        peso_COP.name = 'Peso Colombiano'
        peso_COP.valor_respecto_a = {}

class peso_MX(Money):
    
    def __init__(self, id, name, valor_respecto_a):
        super().__init__(id, name, valor_respecto_a)
        peso_MX.id = 1020
        peso_MX.name = 'Peso Mexicano'
        peso_MX.valor_respecto_a = {}

class peso_Arg(Money):
    
    def __init__(self, id, name, valor_respecto_a):
        super().__init__(id, name, valor_respecto_a)
        peso_Arg.id = 1030
        peso_Arg.name = 'Peso Argentino'
        peso_Arg.valor_respecto_a = {}

class euro(Money):
    
    def __init__(self, id, name, valor_respecto_a):
        super().__init__(id, name, valor_respecto_a)
        euro.id = 2020
        euro.name = 'Euro'
        euro.valor_respecto_a = {}

class dollar(Money):
    
    def __init__(self, id, name, valor_respecto_a):
        super().__init__(id, name, valor_respecto_a)
        dollar.id = 2010
        dollar.name = 'Dollar Americano'
        dollar.valor_respecto_a = {}

class libra(Money):
    
    def __init__(self, id, name, valor_respecto_a):
        super().__init__(id, name, valor_respecto_a)
        libra.id = 2030
        libra.name = 'Libra Esterlina'
        libra.valor_respecto_a = {}