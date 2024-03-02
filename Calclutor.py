import tkinter as tk
import math

class Ratul(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Advanced Calculator")
        self.geometry("400x500")
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry widget to display the result
        entry = tk.Entry(self, textvariable=self.result_var, font=('Helvetica', 20), justify='right')
        entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('sqrt', 5, 0), ('x^2', 5, 1), ('1/x', 5, 2), ('C', 5, 3),
            ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('pi', 6, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self, text=text, font=('Helvetica', 14), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky='nsew')

        # Configure row and column weights so that they expand proportionally
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

    def on_button_click(self, value):
        current_value = self.result_var.get()

        if value == 'C':
            self.result_var.set('')
        elif value == '=':
            try:
                result = eval(current_value)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set('Error')
        elif value == 'sqrt':
            try:
                result = math.sqrt(eval(current_value))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set('Error')
        elif value == 'x^2':
            try:
                result = eval(current_value) ** 2
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set('Error')
        elif value == '1/x':
            try:
                result = 1 / eval(current_value)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set('Error')
        elif value == 'pi':
            self.result_var.set(current_value + str(math.pi))
        elif value in ('sin', 'cos', 'tan'):
            try:
                radians_value = math.radians(eval(current_value))
                if value == 'sin':
                    result = math.sin(radians_value)
                elif value == 'cos':
                    result = math.cos(radians_value)
                elif value == 'tan':
                    result = math.tan(radians_value)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set('Error')
        else:
            self.result_var.set(current_value + str(value))

if __name__ == "__main__":
    calculator = Ratul()
    calculator.mainloop()
