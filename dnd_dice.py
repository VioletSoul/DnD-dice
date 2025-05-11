import random

def roll_die(sides: int) -> int:
    """Roll a single die with the given number of sides."""
    return random.randint(1, sides)

def roll_dnd_dice_set():
    # Define the 7 standard DnD dice:
    # d4, d6, d8, d10, d12 (normal), d12 (percentile), d20
    dice = [
        ('d4', 4),
        ('d6', 6),
        ('d8', 8),
        ('d10', 10),
        ('d12 (normal)', 12),
        ('d12 (percentile)', 12),  # usually a d10 for percentile, simplified here as d12
        ('d20', 20),
    ]

    print("Rolling the 7 standard DnD dice:")
    total = 0
    for name, sides in dice:
        result = roll_die(sides)
        print(f"{name}: {result}")
        total += result

    print(f"Total sum: {total}")

if __name__ == "__main__":
    roll_dnd_dice_set()
