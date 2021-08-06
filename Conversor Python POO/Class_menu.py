class Menu:
    id = int
    mensaje = str
    valor_entrada = input

    def __init__(self, id, mensaje, valor_entrada):
        self._id = id
        self.mensaje = mensaje
        self.valor_entrada = valor_entrada