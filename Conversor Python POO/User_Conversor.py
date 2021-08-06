class User:
    id = int
    name = str

    def __init__(self, id, name):
        self._id = id
        self.name = name