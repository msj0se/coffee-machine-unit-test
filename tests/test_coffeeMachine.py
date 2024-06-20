from coffeeMachine import SmallCup, CoffeeMachine
from equipment.coffeeMaker import CoffeeMaker
from equipment.sugarBowl import Sugar


def test_true_if_theres_cups():
    small_cup = SmallCup(2, 10)
    assert small_cup.has_cups(1) == True;


def test_false_if_theres_not_cups():
    small_cup = SmallCup(1, 10)
    assert small_cup.has_cups(2) == False;


def test_subtract_cups():
    small_cup = SmallCup(5, 10)
    small_cup.give_cups(1)
    assert small_cup.get_amount() == 4


def test_true_if_theres_coffee():
    coffee_maker = CoffeeMaker(10)
    assert coffee_maker.has_coffee(5) == True


def test_false_if_theres_not_coffee():
    coffee_maker = CoffeeMaker(10)
    assert coffee_maker.has_coffee(11) == False


def test_subtract_coffee():
    coffe_maker = CoffeeMaker(10)
    coffe_maker.give_coffee(7)
    assert coffe_maker.get_amount() == 3


def test_true_if_theres_sugar():
    sugar = Sugar(10)
    assert sugar.has_sugar(5) == True
    assert sugar.has_sugar(10) == True


def test_false_if_theres_not_sugar():
    sugar = Sugar(10)
    assert sugar.has_sugar(15) == False


def test_subtract_sugar():
    sugar = Sugar(10)
    sugar.give_sugar(5)
    assert sugar.get_amount() == 5
    sugar.give_sugar(2)
    assert sugar.get_amount() == 3


def test_return_small_cup():
    coffee_machine = CoffeeMachine(small_cup_amount=5,
                                   medium_cup_amount=5,
                                   large_cup_amount=5,
                                   coffee_amount=50,
                                   sugar_amount=20,
                                   small_cup_content=10,
                                   medium_cup_content=20,
                                   large_cup_content=30)

    small_cup = coffee_machine.get_type_cup('small')
    assert small_cup == coffee_machine._small_cup


def test_return_medium_cup():
    coffee_machine = CoffeeMachine(small_cup_amount=5,
                                   medium_cup_amount=5,
                                   large_cup_amount=5,
                                   coffee_amount=50,
                                   sugar_amount=20,
                                   small_cup_content=10,
                                   medium_cup_content=20,
                                   large_cup_content=30)

    medium_cup = coffee_machine.get_type_cup('medium')
    assert medium_cup == coffee_machine._medium_cup


def test_return_large_cup():
    coffee_machine = CoffeeMachine(small_cup_amount=5,
                                   medium_cup_amount=5,
                                   large_cup_amount=5,
                                   coffee_amount=50,
                                   sugar_amount=20,
                                   small_cup_content=10,
                                   medium_cup_content=20,
                                   large_cup_content=30)

    large_cup = coffee_machine.get_type_cup('large')
    assert large_cup == coffee_machine._large_cup


def test_return_no_cups():
    coffee_machine = CoffeeMachine(small_cup_amount=5,
                                   medium_cup_amount=5,
                                   large_cup_amount=5,
                                   coffee_amount=50,
                                   sugar_amount=20,
                                   small_cup_content=10,
                                   medium_cup_content=20,
                                   large_cup_content=30)

    assert coffee_machine.get_coffee(cup_type='small', cup_amount=10,
                                     coffee_amount=2, sugar_amount=4) is None, 'There are no cups.'


def test_return_no_coffee():
    coffee_machine = CoffeeMachine(small_cup_amount=5,
                                   medium_cup_amount=5,
                                   large_cup_amount=5,
                                   coffee_amount=50,
                                   sugar_amount=20,
                                   small_cup_content=10,
                                   medium_cup_content=20,
                                   large_cup_content=30)

    assert coffee_machine.get_coffee(coffee_amount=100, cup_amount=2,
                                     cup_type='small', sugar_amount=4) is None, "Not enough coffee."


def test_return_no_sugar():
    coffee_machine = CoffeeMachine(small_cup_amount=5,
                                   medium_cup_amount=5,
                                   large_cup_amount=5,
                                   coffee_amount=50,
                                   sugar_amount=20,
                                   small_cup_content=10,
                                   medium_cup_content=20,
                                   large_cup_content=30)

    assert coffee_machine.get_coffee(coffee_amount=10, cup_amount=2,
                                     cup_type='small', sugar_amount=30) is None, "Not enough sugar."


def test_should_subtract_coffee():
    coffee_machine = CoffeeMachine(small_cup_amount=5,
                                   medium_cup_amount=5,
                                   large_cup_amount=5,
                                   coffee_amount=50,
                                   sugar_amount=20,
                                   small_cup_content=10,
                                   medium_cup_content=20,
                                   large_cup_content=30)

    coffee_machine.get_coffee(coffee_amount=10, cup_amount=2, cup_type='small', sugar_amount=5)
    coffee_amount = coffee_machine._coffee_maker.get_amount()
    assert coffee_amount == 40


def test_should_subtract_cup():
    coffee_machine = CoffeeMachine(small_cup_amount=5,
                                   medium_cup_amount=5,
                                   large_cup_amount=5,
                                   coffee_amount=50,
                                   sugar_amount=20,
                                   small_cup_content=10,
                                   medium_cup_content=20,
                                   large_cup_content=30)

    coffee_machine.get_coffee(coffee_amount=10, cup_amount=1, cup_type='small', sugar_amount=5)
    cup_amount = coffee_machine.get_type_cup(cup_type='small').get_amount()
    assert cup_amount == 4


def test_should_subtract_sugar():
    coffee_machine = CoffeeMachine(small_cup_amount=5,
                                   medium_cup_amount=5,
                                   large_cup_amount=5,
                                   coffee_amount=50,
                                   sugar_amount=20,
                                   small_cup_content=10,
                                   medium_cup_content=20,
                                   large_cup_content=30)

    coffee_machine.get_coffee(coffee_amount=10, cup_amount=1, cup_type='small', sugar_amount=3)
    sugar_amount = coffee_machine._sugar.get_amount()
    assert sugar_amount == 17


def test_return_congratulations():
    coffee_machine = CoffeeMachine(small_cup_amount=5,
                                   medium_cup_amount=5,
                                   large_cup_amount=5,
                                   coffee_amount=50,
                                   sugar_amount=20,
                                   small_cup_content=10,
                                   medium_cup_content=20,
                                   large_cup_content=30)

    result = coffee_machine.get_coffee(coffee_amount=10, cup_amount=1, cup_type='small', sugar_amount=3)
    assert 'Congratulations.', result
