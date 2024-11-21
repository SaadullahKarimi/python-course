
import tkinter as tk
from tkinter import messagebox

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Yasin Calculator")
        self.geometry("400x600")
        self.configure(bg="#d9f9d9")
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        
        title_label = tk.Label(
            self, text="Yasin Calculator", font=("Arial", 24, "bold"),
            bg="#27ae60", fg="white", pady=10
        )
        title_label.grid(row=0, column=0, columnspan=4, sticky="nsew")


        self.entry = tk.Entry(
            self, font=("Arial", 24), borderwidth=5, relief="ridge",
            justify="right", bg="#ecf9ec"
        )
        self.entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # تعریف دکمه‌ها
        buttons = [
            '7', '8', '9', '÷',
            '4', '5', '6', '×',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]


        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.grid_columnconfigure(j, weight=1)

        # ساخت دکمه‌ها
        row = 2
        col = 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(
                self, text=button, font=("Arial", 20), bg="#2ecc71", fg="white",
                activebackground="#27ae60", activeforeground="white",
                relief="raised", borderwidth=3, command=action
            ).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, char):
        if char == 'C':
            self.entry.delete(0, tk.END)
        elif char == '=':
            try:
                expression = self.entry.get()
                expression = expression.replace('÷', '/').replace('×', '*')
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except Exception:
                messagebox.showerror("خطا", "عبارت وارد شده نامعتبر است.")
        else:
            self.entry.insert(tk.END, char)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()

