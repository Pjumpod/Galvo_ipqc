from tkinter import simpledialog
import tkinter as tk

class MyDialog(simpledialog.Dialog):

    def __init__(self, parent, title, message, size):
        self.result = None
        self.e1 = None
        self.message = message
        self.size = size
        super().__init__(parent, title)

    def body(self, master):
        self.geometry(self.size)
        self._label = tk.Label(master, text=self.message, width=25, font=("Arial", 25))
        self._label.pack(pady=10)
        self.e1 = tk.Entry(master, width=25, font=("Arial", 25))
        self.e1.pack(pady=20)
        # self.e1.grid(row=0, column=1)
        return self.e1 # initial focus


    def apply(self):
        first = self.e1.get()
        self.result = first