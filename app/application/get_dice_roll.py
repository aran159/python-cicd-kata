import random


def get_dice_roll() -> int:
    return random.randint(1, 6) + 1 # noqa: S311
