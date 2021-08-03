from money_select import Money_Select
from User_Conversor import User

class Request_For_Use(Money_Select):
    id = str
    id_user = User.id

    def __init__(self, id, id_user, id_moneda_A, id_moneda_B):
        super().__init__(id_moneda_A, id_moneda_B)
        self._id = id
        self.id_user = id_user





