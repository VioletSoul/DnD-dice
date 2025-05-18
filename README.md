# Dungeons & Dragons Dice Roller

A simple Python script that simulates rolling the standard set of Dungeons & Dragons dice.  
It supports rolling the classic seven dice (d4, d6, d8, d10, percentile d10, d12, d20) and outputs individual results along with the total sum.

---

## Features

- Clear terminal output with screen clearing before each run.
- Descriptive display of the standard DnD dice set.
- Accurate percentile dice roll (combining two d10 dice to generate a number from 1 to 100).
- Interactive input: choose how many times to roll the full dice set.
- Clear, readable output of each roll and total sums.

---

## Dice Included

| Die          | Description                              |
|--------------|----------------------------------------|
| d4           | Four-sided die (tetrahedron)           |
| d6           | Six-sided die (cube)                    |
| d8           | Eight-sided die (octahedron)           |
| d10          | Ten-sided die (regular)                 |
| d10 (percentile) | Ten-sided die (marked in tens: 00, 10, 20...) |
| d12          | Twelve-sided die (dodecahedron)         |
| d20          | Twenty-sided die (icosahedron)          |

---

## How to Use

1. Clone or download this repository.
2. Run the script with Python 3:

python dice_roller.py


3. When prompted, enter how many times you want to roll the full dice set.
4. View the results printed in the terminal.

---

## Example Output

Standard Dungeons & Dragons Dice:
d4  - Four-sided die (tetrahedron) d6  - Six-sided die (cube) d8  - Eight-sided die (octahedron) d10 - Ten-sided die (regular) d10 - Ten-sided die (percentile, marked in tens: 00, 10, 20…) d12 - Twelve-sided die (dodecahedron) d20 - Twenty-sided die (icosahedron)
How many times would you like to roll the dice set? 2
Roll #1: d4: 3 d6: 5 d8: 2 d10 (regular): 7 d12: 11 d20: 14 d10 (percentile): 63
Total sum (including percentile d10): 105
Roll #2: d4: 1 d6: 6 d8: 8 d10 (regular): 3 d12: 9 d20: 20 d10 (percentile): 27
Total sum (including percentile d10): 74


---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributions

Feel free to fork the repository and submit pull requests.  
Suggestions and issues are welcome!

---

## Contact

For questions or feedback, please open an issue or contact me directly.

---

Enjoy your rolls and may the dice be ever in your favor!
