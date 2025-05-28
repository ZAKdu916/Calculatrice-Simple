import tkinter as tk

class SimpleCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculatrice Simple")
        self.geometry("300x400")
        self.configure(bg="white")

        self.expression = ""

        self.display = tk.Entry(self, font=("Arial", 20), borderwidth=2, relief="groove", justify="right")
        self.display.pack(fill="both", ipadx=8, ipady=20, padx=10, pady=10)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
        ]

        for row in buttons:
            frame = tk.Frame(self)
            frame.pack(expand=True, fill="both")
            for btn in row:
                b = tk.Button(frame, text=btn, font=("Arial", 18), command=lambda val=btn: self.on_click(val))
                b.pack(side="left", expand=True, fill="both", padx=2, pady=2)

        clear_btn = tk.Button(self, text="C", font=("Arial", 18), bg="red", fg="white", command=self.clear)
        clear_btn.pack(fill="both", padx=10, pady=5)

    def on_click(self, char):
        if char == '=':
            try:
                result = str(eval(self.expression))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
                self.expression = result
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Erreur")
                self.expression = ""
        else:
            self.expression += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)

if __name__ == "__main__":
    app = SimpleCalculator()
    app.mainloop()
