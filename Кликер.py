import tkinter as tk
from tkinter import ttk, messagebox
import time

class ClickerApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Clicker App')
        self.master.geometry('400x300')

        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 12), padding=5)
        self.style.configure('TLabel', font=('Arial', 14))
        self.style.theme_use('clam')

        self.click_count = 0
        self.time_left = tk.StringVar()

        self.label_countdown = ttk.Label(self.master, textvariable=self.time_left, font=('Arial', 30))
        self.label_countdown.pack(pady=10)

        self.entry_time = ttk.Entry(self.master, font=('Arial', 12))
        self.entry_time.pack(pady=10, ipadx=10)

        self.button_start = ttk.Button(self.master, text="Старт", command=self.start_clicker)
        self.button_start.pack(pady=10)

        self.button_click = ttk.Button(self.master, text="Клик", command=self.click, state=tk.DISABLED)
        self.button_click.pack(pady=10)

        self.button_finish = ttk.Button(self.master, text="Завершить", command=self.finish, state=tk.DISABLED)
        self.button_finish.pack(pady=10)

        self.label_clicks = ttk.Label(self.master, text="Количество кликов: 0", font=('Arial', 16))
        self.label_clicks.pack(pady=10)

        self.theme_selector = ttk.Combobox(self.master, values=["Светлая", "Темная"], state="readonly")
        self.theme_selector.bind("<<ComboboxSelected>>", self.change_theme)
        self.theme_selector.current(0)
        self.theme_selector.pack(pady=10)

        self.change_theme(None)

    def start_clicker(self):
        self.time_left.set(self.entry_time.get())
        self.button_start.config(state=tk.DISABLED)
        self.button_click.config(state=tk.NORMAL)
        self.button_finish.config(state=tk.NORMAL)
        for t in range(int(self.entry_time.get()), -1, -1):
            self.time_left.set(t)
            self.master.update()
            time.sleep(1)
        self.button_start.config(state=tk.NORMAL)
        self.button_click.config(state=tk.DISABLED)
        self.button_finish.config(state=tk.DISABLED)
        self.label_clicks.config(text=f"Количество кликов: {self.click_count}")
        messagebox.showinfo("Время вышло!", f"Время вышло! Количество кликов: {self.click_count}")

    def click(self):
        self.click_count += 1
        self.label_clicks.config(text=f"Количество кликов: {self.click_count}")

    def finish(self):
        self.time_left.set("")
        self.entry_time.delete(0, tk.END)
        self.click_count = 0
        self.label_clicks.config(text="Количество кликов: 0")

    def change_theme(self, event):
        chosen_theme = self.theme_selector.get()
        if chosen_theme == "Темная":
            self.master.config(bg="#2B2B2B")
            self.style.theme_use('clam')
            self.style.map("TButton",
                foreground=[('active', 'white'), ('!disabled', 'white')],
                background=[('active', '#666666'), ('!disabled', '#4D4D4D')]
            )
            self.style.configure('TLabel', foreground='white')
            self.style.configure('TEntry', fieldbackground='#737373', foreground='white')
            self.time_left.set("Время")
            self.label_clicks.config(foreground="white")
        else:
            self.master.config(bg="white")
            self.style.theme_use('clam')
            self.style.map("TButton",
                foreground=[('active', 'black'), ('!disabled', 'black')],
                background=[('active', '#E6E6E6'), ('!disabled', '#D9D9D9')]
            )
            self.style.configure('TLabel', foreground='black')
            self.style.configure('TEntry', fieldbackground='white', foreground='black')
            self.time_left.set("Time")
            self.label_clicks.config(foreground="black")

root = tk.Tk()
app = ClickerApp(root)
root.mainloop()
