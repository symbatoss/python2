class BankAccount:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def set_balance(self, balance):
        if balance in range(0, 100000):
            return self._balance
        else:
            print(f'Баланс: Error')

    def get_balance(self):
        return self._balance

    def set_name(self):
        return self._name

    def get_name(self):
        return self._name

    def show(self):
        print(f'Название карты: {self._name} \nБаланс: {self._balance}')


myacc = BankAccount('Card', 56888)
myacc.show()
myacc.set_balance(-575)