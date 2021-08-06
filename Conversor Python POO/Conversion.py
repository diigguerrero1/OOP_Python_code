from money_select import Money_Select

class Conversion(Money_Select):
    id = int
    id_money_select_A = int
    id_money_select_B = int

    def __init__(self, id_money_A, id_money_B, id, id_money_select):
        super().__init__(id_money_A, id_money_B)
        self._id = id
        self.id_money_select = id_money_select


    
