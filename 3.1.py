import tkinter as tk

def close_window():
    root.destroy()

root = tk.Tk()
root.title("Перша програма")
root.geometry("1024x768")

label = tk.Label(root, text="Hello, world!", font=("Arial", 24))
label.pack(pady=50)

button = tk.Button(root, text="Закрити", command=close_window)
button.pack(pady=20)

root.mainloop()
