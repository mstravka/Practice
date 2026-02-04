import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    global current_file
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filename:
        with open(filename, "r", encoding="utf-8") as f:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, f.read())
        current_file = filename

def save_file():
    global current_file
    if current_file:
        with open(current_file, "w", encoding="utf-8") as f:
            f.write(text_area.get(1.0, tk.END))
    else:
        filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text files", "*.txt")])
        if filename:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(text_area.get(1.0, tk.END))
            current_file = filename

def exit_notepad():
    if messagebox.askyesno("Вийти", "Зберегти зміни перед виходом?"):
        save_file()
    root.destroy()

current_file = None
root = tk.Tk()
root.title("Блокнот")
root.geometry("600x400")

text_area = tk.Text(root)
text_area.pack(expand=True, fill="both")

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Відкрити", command=open_file)
file_menu.add_command(label="Зберегти", command=save_file)
file_menu.add_command(label="Вийти", command=exit_notepad)

root.mainloop()
