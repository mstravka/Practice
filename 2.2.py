import tkinter as tk

def show_message():
    print("Кнопку натиснуто!")

window = tk.Tk()
window.title("Demo кнопки")

button = tk.Button(window, text="Натисни мене", command=show_message)
button.pack(pady=20)

window.mainloop()
