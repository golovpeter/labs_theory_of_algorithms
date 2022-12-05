import tkinter as tk

from frames.main_frame import MainFrame


class Application(tk.Tk):
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 520

    def __init__(self):
        tk.Tk.__init__(self)

        self.__init_base_params()

        container = tk.Frame(self)
        container.pack()

        self.frames = {}
        for F in (MainFrame,):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0)

        self.show_frame(MainFrame.__name__)

    def __init_base_params(self):
        self.title("Электронная рабочая тетрадь")
        position_right = int(self.winfo_screenwidth() / 2 - self.WINDOW_WIDTH / 2)
        position_down = int(self.winfo_screenheight() / 2 - self.WINDOW_HEIGHT / 2)
        self.geometry("{}x{}".format(self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.geometry("+{}+{}".format(position_right, position_down))
        self.resizable(False, False)

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.render()
        frame.tkraise()

    def __open_db(self):
        pass
