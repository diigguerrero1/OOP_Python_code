class Money:
    id = int
    name = str
    valor_respecto_a = dict

    def __init__(self, id, name, valor_respecto_a):
        self.id = id
        self.name = name
        self.valor_respecto_a = valor_respecto_a

