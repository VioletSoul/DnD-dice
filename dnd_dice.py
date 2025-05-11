import random
import os

def clear_screen():
    """
    Clear the terminal screen.

    Uses 'cls' command on Windows and 'clear' on Unix-like systems (Linux/macOS).
    This helps to start with a clean slate each time the script runs.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def roll_die(sides: int) -> int:
    """
    Simulate rolling a single die with the specified number of sides.

    Args:
        sides (int): Number of sides on the die.

    Returns:
        int: Random integer between 1 and 'sides', inclusive.
    """
    return random.randint(1, sides)

def print_dice_description():
    """
    Print a clear and informative description of the standard DnD dice.

    This helps users understand the dice involved before seeing the roll results.
    """
    print("Standard Dungeons & Dragons Dice:")
    print("-------------------------------")
    print("d4  - Four-sided die (tetrahedron)")
    print("d6  - Six-sided die (cube)")
    print("d8  - Eight-sided die (octahedron)")
    print("d10 - Ten-sided die (pentagonal trapezohedron)")
    print("d12 - Twelve-sided die (dodecahedron) - normal")
    print("d12 - Twelve-sided die (dodecahedron) - percentile (used for percentages)")
    print("d20 - Twenty-sided die (icosahedron)")
    print()  # Blank line for spacing

def roll_dnd_dice_set():
    """
    Roll all seven standard DnD dice once and display individual results and total sum.

    The dice rolled are:
    - d4, d6, d8, d10, d12 (normal), d12 (percentile), d20

    Note: The percentile d12 is simplified here as a d12 for demonstration.
    """
    # Define the dice as tuples of (name, number_of_sides)
    dice = [
        ('d4', 4),
        ('d6', 6),
        ('d8', 8),
        ('d10', 10),
        ('d12 (normal)', 12),
        ('d12 (percentile)', 12),  # Typically a d10 marked in tens, simplified here
        ('d20', 20),
    ]

    print("Rolling the 7 standard DnD dice:")
    total = 0  # Initialize total sum of all dice rolls

    # Iterate through each die, roll it, print result, and add to total
    for name, sides in dice:
        result = roll_die(sides)
        print(f"{name}: {result}")
        total += result

    # After all rolls, print the total sum
    print(f"\nTotal sum: {total}")

if __name__ == "__main__":
    # Clear the screen before starting output for a clean display
    clear_screen()

    # Print descriptive info about the dice being rolled
    print_dice_description()

    # Perform the dice rolls and display results
    roll_dnd_dice_set()
