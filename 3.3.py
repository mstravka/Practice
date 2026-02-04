import tkinter as tk

def save_info():
    gender = gender_var.get()
    consent = "Так" if consent_var.get() else "Ні"
    result_label.config(text=f"Ім'я: {name_entry.get()}, Стать: {gender}, Погодився: {consent}")

root = tk.Tk()
root.title("Анкета користувача")

tk.Label(root, text="Ім'я:").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Стать:").grid(row=1, column=0, sticky="w")
gender_var = tk.StringVar(value="Чоловіча")
tk.Radiobutton(root, text="Чоловіча", variable=gender_var, value="Чоловіча").grid(row=1, column=1)
tk.Radiobutton(root, text="Жіноча", variable=gender_var, value="Жіноча").grid(row=1, column=2)

consent_var = tk.BooleanVar()
tk.Checkbutton(root, text="Погоджуюсь із умовами", variable=consent_var).grid(row=2, column=1, columnspan=2)

tk.Button(root, text="Зберегти", command=save_info).grid(row=3, column=1)
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=3)

root.mainloop()
