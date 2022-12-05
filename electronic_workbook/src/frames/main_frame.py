import tkinter as tk


class MainFrame(tk.Frame):

    def __init__(self, root, controller):
        tk.Frame.__init__(self, root)

        self.start_button = tk.Button(self, text="Начать", width=20, height=3)
        self.start_button.pack(pady=200)

    def render(self):
        self.pack()
