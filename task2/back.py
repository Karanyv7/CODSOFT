import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("320x400")
        self.root.resizable(False, False)

        self.expression = ""

        # Entry display
        self.entry = tk.Entry(root, font=("Arial", 24), bd=10, relief=tk.RIDGE, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, sticky="nsew")
        self.entry.focus_set()  # Auto focus

        # Button definitions
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
            ("=", 5, 0, 4)
        ]

        for (text, row, col, colspan) in [(*b, 1) if len(b) == 3 else b for b in buttons]:
            btn = tk.Button(root, text=text, font=("Arial", 18), bd=5, relief=tk.RAISED,
                            command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", ipadx=5, ipady=15)

        for i in range(6):
            root.rowconfigure(i, weight=1)
        for i in range(4):
            root.columnconfigure(i, weight=1)

        # Keyboard bindings
        root.bind("<Key>", self.on_key_press)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "=":
            self.calculate()
        else:
            self.expression += str(char)
        self.update_display()

    def on_key_press(self, event):
        key = event.keysym
        if key in '0123456789':
            self.expression += key
        elif key in ('plus', 'KP_Add'):
            self.expression += '+'
        elif key in ('minus', 'KP_Subtract'):
            self.expression += '-'
        elif key in ('asterisk', 'KP_Multiply'):
            self.expression += '*'
        elif key in ('slash', 'KP_Divide'):
            self.expression += '/'
        elif key == 'period' or event.char == '.':
            self.expression += '.'
        elif key == 'Return':
            self.calculate()
        elif key == 'BackSpace':
            self.expression = self.expression[:-1]
        elif key in ('Escape', 'c', 'C'):
            self.expression = ""
        else:
            return  # Ignore unknown keys
        self.update_display()

    def calculate(self):
        try:
            self.expression = str(eval(self.expression))
        except:
            self.expression = "Error"

    def update_display(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
