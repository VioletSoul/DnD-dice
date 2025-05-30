import random
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import tkinter.font as tkFont

class DiceRollerApp:
    RESULTS_COLOR_HEX = "#4e6e4a"  # цвет результатов в HEX

    def __init__(self, root):
        self.root = root
        self.root.title("D&D Dice Master 9000")
        self.root.geometry("500x655")
        self.root.resizable(False, True)  # Запретить изменение ширины, разрешить высоту

        self.info_font = tkFont.Font(family='Arial', size=16)
        self.result_font = tkFont.Font(family='Courier New', size=14)
        self.result_bold_font = tkFont.Font(family='Courier New', size=14, weight="bold")

        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.info_frame = ttk.LabelFrame(self.root, text="О кубиках D&D")
        self.info_text = scrolledtext.ScrolledText(
            self.info_frame,
            wrap=tk.WORD,
            height=10,
            font=self.info_font
        )
        self.info_text.insert(tk.END, self.get_dice_description())
        self.info_text.tag_add("colored", "1.0", "end")
        self.info_text.tag_configure("colored", foreground="#276877")
        self.info_text.configure(state='disabled')

        self.control_frame = ttk.Frame(self.root)
        self.rolls_label = ttk.Label(self.control_frame, text="Количество бросков:", font=self.info_font)
        self.rolls_entry = ttk.Entry(self.control_frame, width=5, font=self.info_font)
        self.rolls_entry.insert(0, "2")
        self.roll_button = ttk.Button(
            self.control_frame,
            text="Бросить кубики!",
            command=self.execute_rolls
        )

        self.result_frame = ttk.LabelFrame(self.root, text="Результаты бросков")
        self.result_text = scrolledtext.ScrolledText(
            self.result_frame,
            wrap=tk.WORD,
            height=15,
            font=self.result_font
        )
        # Цвет результатов берём из переменной
        self.result_text.tag_configure("result_color", foreground=self.RESULTS_COLOR_HEX)
        # Итоговая строка
        self.result_text.tag_configure("total_light_green_bold", foreground="#7baf73", font=self.result_bold_font)
        self.result_text.configure(state='disabled')

    def setup_layout(self):
        self.info_frame.pack(pady=0, padx=0, fill=tk.X)
        self.info_text.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

        self.control_frame.pack(pady=10)
        self.rolls_label.grid(row=0, column=0, padx=5)
        self.rolls_entry.grid(row=0, column=1, padx=5)
        self.roll_button.grid(row=0, column=2, padx=10)

        self.result_frame.pack(pady=0, padx=0, fill=tk.BOTH, expand=True)
        self.result_text.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

    def get_dice_description(self):
        return (
            "Standard Dungeons & Dragons Dice:\n"
            "-------------------------------\n"
            "d4  - Four-sided die (tetrahedron)\n"
            "d6  - Six-sided die (cube)\n"
            "d8  - Eight-sided die (octahedron)\n"
            "d10 - Ten-sided die (regular)\n"
            "d10 - Ten-sided die (percentile, marked in tens: 00, 10, 20...)\n"
            "d12 - Twelve-sided die (dodecahedron)\n"
            "d20 - Twenty-sided die (icosahedron)\n"
        )

    def roll_die(self, sides: int) -> int:
        return random.randint(1, sides)

    def roll_percentile_dice(self) -> int:
        tens = self.roll_die(10) - 1
        ones = self.roll_die(10) - 1
        return tens * 10 + ones + 1

    def roll_dnd_dice_set(self) -> dict:
        dice = [
            ('d4', 4),
            ('d6', 6),
            ('d8', 8),
            ('d10 (regular)', 10),
            ('d12', 12),
            ('d20', 20),
        ]

        results = {}
        total = 0

        for name, sides in dice:
            result = self.roll_die(sides)
            results[name] = result
            total += result

        percentile_result = self.roll_percentile_dice()
        results['d10 (percentile)'] = percentile_result
        total += percentile_result

        results['Total (including percentile)'] = total
        return results

    def execute_rolls(self):
        try:
            rolls = int(self.rolls_entry.get())
            if rolls < 1:
                raise ValueError
        except ValueError:
            messagebox.showerror("Ошибка", "Введите положительное число!")
            return

        self.result_text.configure(state='normal')
        self.result_text.delete(1.0, tk.END)

        for i in range(rolls):
            results = self.roll_dnd_dice_set()
            self.result_text.insert(tk.END, f"Бросок #{i+1}:\n{'-'*30}\n", "result_color")
            for name, value in results.items():
                if name == 'Total (including percentile)':
                    self.result_text.insert(tk.END, f"{name}: {value}\n", "total_light_green_bold")
                else:
                    self.result_text.insert(tk.END, f"{name}: {value}\n", "result_color")
            self.result_text.insert(tk.END, "\n")

        self.result_text.configure(state='disabled')


def main():
    root = tk.Tk()
    app = DiceRollerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
