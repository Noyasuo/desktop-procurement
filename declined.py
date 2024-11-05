import tkinter as tk

class DeclinedScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="Declined Requests", font=("Arial", 16))
        label.pack(pady=20)
