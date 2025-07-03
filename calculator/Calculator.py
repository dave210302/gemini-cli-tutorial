import tkinter as tk
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("계산기")

        self.expression = ""
        self.current_value = tk.StringVar()
        self.current_value.set("0")
        self.memory = 0

        # Display
        self.display = tk.Entry(master, textvariable=self.current_value, font=('Arial', 24), bd=10, insertwidth=4, width=14, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, pady=5)

        # Memory Buttons
        memo_buttons = ['MC', 'MR', 'M+', 'M-', 'MS']
        col_val = 0
        for button in memo_buttons:
            self.create_button(button, 1, col_val, pady=5)
            col_val += 1

        # Buttons
        buttons = [
            '%', 'CE', 'C', '⌫',
            '¹/x', 'x²', '²√x', '÷',
            '7', '8', '9', '×',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '±', '0', '.', '='
        ]

        row_val = 2
        col_val = 0
        for button in buttons:
            self.create_button(button, row_val, col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def create_button(self, text, row, col, pady=20):
        # Special styling for some buttons
        if text in "0123456789.":
            bg_color = '#FFFFFF'
            fg_color = '#000000'
        elif text in "+-×÷=":
            bg_color = '#E0E0E0'
            fg_color = '#000000'
        else:
            bg_color = '#F0F0F0'
            fg_color = '#000000'
        
        if text == '=':
            bg_color = '#ADD8E6'


        btn = tk.Button(self.master, text=text, padx=20, pady=pady, font=('Arial', 14), command=lambda: self.on_button_click(text), bg=bg_color, fg=fg_color)
        btn.grid(row=row, column=col, sticky="nsew")


    def on_button_click(self, caption):
        if caption.isdigit():
            if self.current_value.get() == "0":
                self.current_value.set(caption)
            else:
                self.current_value.set(self.current_value.get() + caption)
        elif caption == '.':
            if '.' not in self.current_value.get():
                self.current_value.set(self.current_value.get() + '.')
        elif caption == 'C':
            self.expression = ""
            self.current_value.set("0")
        elif caption == 'CE':
            self.current_value.set("0")
        elif caption == '⌫':
            self.current_value.set(self.current_value.get()[:-1] or "0")
        elif caption == '±':
            if self.current_value.get() != "0":
                if self.current_value.get().startswith('-'):
                    self.current_value.set(self.current_value.get()[1:])
                else:
                    self.current_value.set('-' + self.current_value.get())
        elif caption in '+-×÷':
            self.expression = self.current_value.get() + caption
            self.current_value.set("0")
        elif caption == '=':
            try:
                # Replace display operators with python operators
                self.expression = self.expression.replace('×', '*').replace('÷', '/')
                result = str(eval(self.expression + self.current_value.get()))
                self.current_value.set(result)
                self.expression = ""
            except:
                self.current_value.set("Error")
                self.expression = ""
        elif caption == 'x²':
            try:
                result = str(eval(self.current_value.get()) ** 2)
                self.current_value.set(result)
            except:
                self.current_value.set("Error")
        elif caption == '²√x':
            try:
                result = str(math.sqrt(eval(self.current_value.get())))
                self.current_value.set(result)
            except:
                self.current_value.set("Error")
        elif caption == '¹/x':
            try:
                result = str(1 / eval(self.current_value.get()))
                self.current_value.set(result)
            except:
                self.current_value.set("Error")
        elif caption == '%':
            # In windows calculator, percent is handled differently depending on context
            # For simplicity here, we'll just calculate the percentage of the number
            try:
                result = str(eval(self.current_value.get()) / 100)
                self.current_value.set(result)
            except:
                self.current_value.set("Error")
        elif caption == 'MC':
            self.memory = 0
        elif caption == 'MR':
            self.current_value.set(str(self.memory))
        elif caption == 'M+':
            self.memory += eval(self.current_value.get())
        elif caption == 'M-':
            self.memory -= eval(self.current_value.get())
        elif caption == 'MS':
            self.memory = eval(self.current_value.get())


if __name__ == '__main__':
    root = tk.Tk()
    for i in range(7):
        root.grid_rowconfigure(i, weight=1)
    for i in range(4):
        root.grid_columnconfigure(i, weight=1)
    my_gui = Calculator(root)
    root.mainloop()