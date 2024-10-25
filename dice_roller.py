


    #### write  your code here - make sure to return the result of your roll ###
    #### your function, called roll_die, should meet these requirements.  
    #### Include this documentation inside of your function!
"""Rolls a die with the specified number of sides and returns the result.

    Args:
        sides (int): The number of sides on the die (must be at least 4).

    Returns:
        int: The result of the roll.
    """


import random

def roll_die(sides):
    if sides < 4:
        raise ValueError("Die must have at least 4 sides.")
    return random.randint(1, sides)

def test_dice_roller():
    for _ in range(100):
        roll = roll_die(6)
        assert 1 <= roll <= 6, f"Roll {roll} is out of range for a 6-sided die"

    for _ in range(100):
        roll = roll_die(10)
        assert 1 <= roll <= 10, f"Roll {roll} is out of range for a 10 sided die"

    print("All tests passed.")

if __name__ == "__main__":
    test_dice_roller()

## You should be able to run this program directly to use this unit test before moving on to the dice_stats.py
def test_dice_roller():
    """Runs unit tests for the dice_roller function."""

    results = [roll_die(6) for _ in range(100)]
    assert all(1 <= result <= 6 for result in results), "D6 roll results invalid"

    results = [roll_die(10) for _ in range(100)]
    assert all(1 <= result <= 10 for result in results), "D10 roll results invalid"

    print("Dice roller tests passed successfully!")

if __name__ == "__main__":
    test_dice_roller()  # Run the unit tests when executed directly

