import tkinter as tk
from tkinter import filedialog

def open_file():
    path = filedialog.askopenfilename()
    if path:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        text.delete("1.0", tk.END)
        text.insert(tk.END, content)

def save_file():
    path = filedialog.asksaveasfilename(defaultextension=".txt")
    if path:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text.get("1.0", tk.END))

window = tk.Tk()
window.title("Файлова система")
window.geometry("400x300")

text = tk.Text(window)
text.pack(expand=True, fill=tk.BOTH)

btn_open = tk.Button(window, text="Відкрити файл", command=open_file)
btn_open.pack(side=tk.LEFT, padx=10, pady=5)

btn_save = tk.Button(window, text="Зберегти файл", command=save_file)
btn_save.pack(side=tk.RIGHT, padx=10, pady=5)

window.mainloop()
