from equipment.coffeeMaker import CoffeeMaker
from equipment.sugarBowl import Sugar
from equipment.cup import Cup


class SmallCup(Cup):
    pass


class MediumCup(Cup):
    pass


class LargeCup(Cup):
    pass


class CoffeeMachine:
    def __init__(self, small_cup_amount, medium_cup_amount, large_cup_amount, coffee_amount, sugar_amount,
                 small_cup_content, medium_cup_content, large_cup_content):
        self._small_cup = SmallCup(small_cup_amount, small_cup_content)
        self._medium_cup = MediumCup(medium_cup_amount, medium_cup_content)
        self._large_cup = LargeCup(large_cup_amount, large_cup_content)
        self._coffee_maker = CoffeeMaker(coffee_amount)
        self._sugar = Sugar(sugar_amount)

    def get_type_cup(self, cup_type):
        if cup_type.lower() == 'small':
            return self._small_cup
        elif cup_type.lower() == 'medium':
            return self._medium_cup
        elif cup_type.lower() == 'large':
            return self._large_cup
        else:
            print(f'No available.')

    def get_coffee(self, cup_type, cup_amount, sugar_amount, coffee_amount):
        if not self.get_type_cup(cup_type).has_cups(cup_amount):
            print('Sorry, we have no enough cups for you.')
            return None
        elif not self._coffee_maker.has_coffee(coffee_amount):
            print('We are sorry, we do not have this amount of coffee available.')
            return None
        elif not self._sugar.has_sugar(sugar_amount):
            print('We are sorry, we do not have this amount of sugar available.')
            return None
        else:
            print(f'You want a {cup_type} cup!')
            self.get_type_cup(cup_type).give_cups(cup_amount)
            self._coffee_maker.give_coffee(coffee_amount)
            self._sugar.give_sugar(sugar_amount)