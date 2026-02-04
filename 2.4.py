import tkinter as tk

def calculate_square():
    num = int(entry.get())
    result = num ** 2
    label_result.config(text=f"Квадрат числа: {result}")

window = tk.Tk()
window.title("Обчислення квадрата")
window.geometry("300x150")

entry = tk.Entry(window)
entry.pack(pady=10)

button = tk.Button(window, text="Обчислити", command=calculate_square)
button.pack(pady=5)

label_result = tk.Label(window, text="")
label_result.pack(pady=10)

window.mainloop()
