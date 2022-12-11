import tkinter
import tkinter as tk

from frames.main_frame import MainFrame


class Application(tk.Tk):
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 600

    def __init__(self):
        tk.Tk.__init__(self)

        self.__init_base_params()

        self.config()

        self.frames = {}

        self.main_frame = MainFrame(self)
        self.main_frame.grid(row=0, column=0)

        self.show_frame(MainFrame.__name__)

    # Метод для инициализации базовых параметров при запуске приложения
    def __init_base_params(self):
        self.title("Электронная рабочая тетрадь")
        position_right = int(self.winfo_screenwidth() / 2 - self.WINDOW_WIDTH / 2)
        position_down = int(self.winfo_screenheight() / 2 - self.WINDOW_HEIGHT / 2)
        self.geometry("{}x{}".format(self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.geometry("+{}+{}".format(position_right, position_down))

    # Метод для отображения фрейма
    def show_frame(self, frame_name):
        self.config(menu=self.main_frame.menubar())

        self.main_frame.render()
        self.main_frame.tkraise()
