import random  # Built-in random number generator

# Highest number a Dice can roll
MAX_DICE_VALUE = 6


def roll_dice_pair():
    # Roll Dice 01
    dice1: int = random.randint(1, MAX_DICE_VALUE)
    # Roll Dice 02
    dice2: int = random.randint(1, MAX_DICE_VALUE)
    # Calculate the total of two dices
    total: int = dice1 + dice2
    # Print total
    print(f"Total of two Dices: {total}")


def print_dice():
    # Assign a fixed value to dice1
    dice1: int = 10
    print(f"dice1 in \"print_dice()\" starts as: {dice1}")
    # Calling Roll Dice Pair Function
    roll_dice_pair()
    roll_dice_pair()
    roll_dice_pair()
    print(f"dice1 in \"print_dice()\" ends as: {dice1}")


# No need to edit beyond this point
if __name__ == '__main__':
    print_dice()
