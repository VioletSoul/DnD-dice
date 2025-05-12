import random
import os

def clear_screen():
    """
    Clear the terminal screen.

    This function clears the terminal screen, using 'cls' on Windows
    and 'clear' on Unix-like systems (Linux/macOS). It ensures a clean
    output each time the script runs.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def roll_die(sides: int) -> int:
    """
    Simulate rolling a single die with the specified number of sides.

    Args:
        sides (int): The number of sides on the die.

    Returns:
        int: A random integer between 1 and 'sides' (inclusive).
    """
    return random.randint(1, sides)

def print_dice_description():
    """
    Print a clear description of the standard Dungeons & Dragons dice set.

    This provides users with information about the dice being used in the script,
    including the common names and number of sides for each die.
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
    print()  # Add a blank line for better readability

def roll_dnd_dice_set():
    """
    Roll all seven standard DnD dice once and display individual results and the total sum.

    The standard dice set includes:
    - d4, d6, d8, two d10 (one for percentile), d12, d20

    The percentile d10 is used in conjunction with the regular d10 to generate
    a number between 1 and 100.
    """
    # Correct dice set: d4, d6, d8, two d10, d12, d20
    dice = [
        ('d4', 4),
        ('d6', 6),
        ('d8', 8),
        ('d10 (regular)', 10),
        ('d10 (percentile)', 10),  # Percentile die (tens values)
        ('d12', 12),
        ('d20', 20),
    ]

    print("Rolling the 7 standard DnD dice:")
    total = 0  # Initialize the total sum

    # Iterate through each die, roll it, print the result, and add to the total
    for name, sides in dice:
        result = roll_die(sides)
        print(f"{name}: {result}")
        total += result

    # Print the total sum of all dice rolls
    print(f"\nTotal sum: {total}")

if __name__ == "__main__":
    # Clear the screen for a clean display
    clear_screen()

    # Print descriptive information about the dice
    print_dice_description()

    # Perform the dice rolls and display the results
    roll_dnd_dice_set()
