import random
import os

def clear_screen():
    """
    Clear the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def roll_die(sides: int) -> int:
    """
    Roll a single die with the specified number of sides.

    Args:
        sides (int): Number of sides on the die.

    Returns:
        int: Result of the roll (1 to sides).
    """
    return random.randint(1, sides)

def roll_percentile_dice() -> int:
    """
    Roll two ten-sided dice to get a number from 1 to 100.

    Returns:
        int: Result of the percentile roll.
    """
    tens = roll_die(10) - 1  # 0-9
    ones = roll_die(10) - 1  # 0-9
    result = tens * 10 + ones + 1
    return result

def print_dice_description():
    """
    Print a description of the standard DnD dice set.
    """
    print("Standard Dungeons & Dragons Dice:")
    print("-------------------------------")
    print("d4  - Four-sided die (tetrahedron)")
    print("d6  - Six-sided die (cube)")
    print("d8  - Eight-sided die (octahedron)")
    print("d10 - Ten-sided die (regular)")
    print("d10 - Ten-sided die (percentile, marked in tens: 00, 10, 20...)")
    print("d12 - Twelve-sided die (dodecahedron)")
    print("d20 - Twenty-sided die (icosahedron)")
    print()

def roll_dnd_dice_set():
    """
    Roll the standard set of DnD dice and print the results.
    """
    dice = [
        ('d4', 4),
        ('d6', 6),
        ('d8', 8),
        ('d10 (regular)', 10),
        ('d12', 12),
        ('d20', 20),
    ]

    print("Rolling the 7 standard DnD dice:")
    total = 0

    # Roll all dice except percentile
    for name, sides in dice:
        result = roll_die(sides)
        print(f"{name}: {result}")
        total += result

    # Roll percentile die separately
    percentile_result = roll_percentile_dice()
    print(f"d10 (percentile): {percentile_result}")

    total += percentile_result

    print(f"\nTotal sum (including percentile d10): {total}")

def main():
    clear_screen()
    print_dice_description()

    try:
        rolls = int(input("How many times would you like to roll the dice set? "))
        if rolls < 1:
            print("Please enter a positive number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    for i in range(rolls):
        print(f"\nRoll #{i+1}:")
        roll_dnd_dice_set()

if __name__ == "__main__":
    main()
