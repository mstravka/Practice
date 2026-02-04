import tkinter as tk

def greet():
    message_label.config(text="Вітаю, користувач!")

def clear():
    message_label.config(text="")

root = tk.Tk()
root.title("Кнопки")
root.geometry("300x200")

message_label = tk.Label(root, text="", font=("Arial", 14))
message_label.pack(pady=10)

tk.Button(root, text="Привітати", command=greet).pack(pady=5)
tk.Button(root, text="Очистити", command=clear).pack(pady=5)
tk.Button(root, text="Вийти", command=root.destroy).pack(pady=5)

root.mainloop()
