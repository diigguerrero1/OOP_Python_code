from dicts_info_monedas import dictionary_Moneys

class conversor:

    def __init__(self, id, money_A, money_B, amount_coin):
        self._id = id
        self.money_A = money_A
        self.money_B = money_B
        self.amount_coin = amount_coin
        
        x = (dictionary_Moneys[money_A])[money_B]

        resultado = conversor.amount_coin * x
        resultado = round(resultado, 3)
        print(f'Tienes ${resultado} {(dictionary_Moneys[money_B])[0]}')
        
    

    
