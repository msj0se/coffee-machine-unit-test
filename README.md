# Coffee Machine Program

This program simulates the functionality of a coffee machine. It includes classes and methods to manage cups, coffee, and sugar.

## Classes and Methods

### SmallCup Class

#### `has_cups(amount: int) -> bool`
- Checks if there are enough small cups available.
- Returns `True` if there are enough cups, otherwise `False`.

#### `give_cups(amount: int)`
- Subtracts the given amount of cups from the available small cups.
- No return value.

#### `get_amount() -> int`
- Returns the current number of small cups available.

### CoffeeMaker Class

#### `has_coffee(amount: int) -> bool`
- Checks if there is enough coffee available.
- Returns `True` if there is enough coffee, otherwise `False`.

#### `give_coffee(amount: int)`
- Subtracts the given amount of coffee from the available coffee.
- No return value.

#### `get_amount() -> int`
- Returns the current amount of coffee available.

### Sugar Class

#### `has_sugar(amount: int) -> bool`
- Checks if there is enough sugar available.
- Returns `True` if there is enough sugar, otherwise `False`.

#### `give_sugar(amount: int)`
- Subtracts the given amount of sugar from the available sugar.
- No return value.

#### `get_amount() -> int`
- Returns the current amount of sugar available.

### CoffeeMachine Class

#### `__init__(small_cup_amount, medium_cup_amount, large_cup_amount, coffee_amount, sugar_amount, small_cup_content, medium_cup_content, large_cup_content)`
- Initializes a coffee machine with given amounts of cups (small, medium, large), coffee, sugar, and their respective contents.

#### `get_type_cup(cup_type: str) -> SmallCup or MediumCup or LargeCup or None`
- Returns the type of cup specified ('small', 'medium', 'large').

#### `get_coffee(coffee_amount, cup_amount, cup_type, sugar_amount) -> str or None`
- Checks if there are enough cups, coffee, and sugar.
- If everything is available, prepares the coffee.
- Returns "Congratulations." if successful, otherwise returns a message indicating why it failed.

## Testing

The program includes tests for various functionalities:
- Checking cup availability (`test_true_if_theres_cups`, `test_false_if_theres_not_cups`).
- Checking coffee availability (`test_true_if_theres_coffee`, `test_false_if_theres_not_coffee`).
- Checking sugar availability (`test_true_if_theres_sugar`, `test_false_if_theres_not_sugar`).
- Subtraction of cups (`test_subtract_cups`), coffee (`test_subtract_coffee`), and sugar (`test_subtract_sugar`).
- Returning specific types of cups (`test_return_small_cup`, `test_return_medium_cup`, `test_return_large_cup`).
- Handling cases where there are no cups, coffee, or sugar (`test_return_no_cups`, `test_return_no_coffee`, `test_return_no_sugar`).
- Subtraction of coffee, cups, and sugar after preparing coffee (`test_should_subtract_coffee`, `test_should_subtract_cup`, `test_should_subtract_sugar`).
- Checking successful coffee preparation (`test_return_congratulations`).

Each test checks the expected behavior of different components of the coffee machine.

## Installation

### Step 1: Clone the repository

Clone the repository from GitHub:

```bash
git clone <repository_url>
cd <repository_directory>
```

### Step 1: Install dependencies

Install pytest:

```bash
pip install pytest
```
