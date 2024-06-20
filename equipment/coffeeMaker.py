class CoffeeMaker:
    def __init__(self, amount):
        self._amount = amount

    def get_amount(self):
        return self._amount

    def set_amount(self, coffee):
        self._amount = coffee

    def has_coffee(self, has_amount):
        if has_amount <= self._amount:
            return True
        elif self._amount == 0 or has_amount > self._amount:
            return False

    def give_coffee(self, give_amount):
        print('We are giving you your dear coffee.')
        print(f'{give_amount} added.')
        updating = self._amount - give_amount
        self.set_amount(updating)
        print(f'Coffee status: {self.get_amount()}')
