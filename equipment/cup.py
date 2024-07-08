class Cup:
    def __init__(self, amount, content):
        self._amount = amount
        self._content = content

    def set_amount(self, cup):
        self._amount = cup

    def get_amount(self):
        return self._amount

    def set_content(self, cup_content):
        self._content = cup_content

    def get_content(self):
        return self._content

    def has_cups(self, has_amount):
        if has_amount <= self._amount:
            return string
        elif self._amount == 0 or has_amount > self._amount:
            return False

    def give_cups(self, give_amount):
        print(f'Yup! Here you go, take your {give_amount} cups.')
        updating = self._amount - give_amount
        self.set_amount(updating)
        print(f'Cup status: {self.get_amount()}')
