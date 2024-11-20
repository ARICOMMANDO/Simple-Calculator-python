import tkinter as tk

class DarkThemeCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Dark Theme Calculator")
        self.geometry("300x400")
        self.configure(bg="black")

        self.display = tk.Entry(self, font=("Arial", 24), bg="black", fg="green", bd=10, relief=tk.FLAT, justify="right")
        self.display.insert(0, "0")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        self.current_operator = ""
        self.first_operand = None
        self.is_new_input = True

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", "=", "+"
        ]

        for i, button_text in enumerate(buttons):
            row, col = divmod(i, 4)
            button = tk.Button(
                self,
                text=button_text,
                font=("Arial", 18),
                bg="black",
                fg="white",
                relief=tk.FLAT,
                command=lambda b=button_text: self.on_button_click(b)
            )
            button.grid(row=row + 1, column=col, sticky="nsew", padx=5, pady=5)

        for i in range(5):  # Make all rows and columns equally expandable
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

    def on_button_click(self, button_text):
        if button_text.isdigit():
            if self.is_new_input:
                self.display.delete(0, tk.END)
                self.is_new_input = False
            self.display.insert(tk.END, button_text)
        elif button_text in "/*-+":
            self.first_operand = float(self.display.get())
            self.current_operator = button_text
            self.is_new_input = True
        elif button_text == "=":
            if self.current_operator and self.first_operand is not None:
                second_operand = float(self.display.get())
                result = self.calculate(self.first_operand, second_operand, self.current_operator)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
                self.first_operand = None
                self.current_operator = ""
            self.is_new_input = True
        elif button_text == "C":
            self.display.delete(0, tk.END)
            self.display.insert(0, "0")
            self.first_operand = None
            self.current_operator = ""
            self.is_new_input = True

    @staticmethod
    def calculate(operand1, operand2, operator):
        try:
            return {
                "+": operand1 + operand2,
                "-": operand1 - operand2,
                "*": operand1 * operand2,
                "/": operand1 / operand2 if operand2 != 0 else "Error"
            }.get(operator, operand2)
        except Exception:
            return "Error"


if __name__ == "__main__":
    app = DarkThemeCalculator()
    app.mainloop()
