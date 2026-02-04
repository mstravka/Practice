import tkinter as tk
from tkinter import messagebox

def calculate(op):
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        if op == '+':
            res = a + b
        elif op == '-':
            res = a - b
        elif op == '*':
            res = a * b
        elif op == '/':
            res = a / b
        result_label.config(text=f"Результат: {res}")
    except ValueError:
        messagebox.showerror("Помилка", "Введіть числа")
    except ZeroDivisionError:
        messagebox.showerror("Помилка", "Ділення на нуль!")

root = tk.Tk()
root.title("Калькулятор")

entry1 = tk.Entry(root)
entry1.pack()
entry2 = tk.Entry(root)
entry2.pack()

for op in ['+', '-', '*', '/']:
    tk.Button(root, text=op, command=lambda o=op: calculate(o)).pack(side="left", padx=5)

result_label = tk.Label(root, text="Результат:")
result_label.pack()

root.mainloop()
