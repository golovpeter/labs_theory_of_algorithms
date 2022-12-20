import tkinter
import tkinter as tk

from frames.main_frame import MainFrame


class Application(tk.Tk):  # Основной класс приложения
    WINDOW_WIDTH = 600  # Ширина окна
    WINDOW_HEIGHT = 600  # Высота окна

    def __init__(self):  # Конструктор класса
        tk.Tk.__init__(self)

        self.__init_base_params()  # Инициализируем базовые параметры

        self.main_frame = MainFrame(self)  # Создаём основной фрейм
        self.main_frame.grid(row=0, column=0)

        self.show_frame(MainFrame.__name__)  # Показываем фрейм

    # Метод для инициализации базовых параметров при запуске приложения
    def __init_base_params(self):  # Метод для инициализации базовых параметров
        self.title("Электронная рабочая тетрадь")  # Меняем заголовок окна
        position_right = int(self.winfo_screenwidth() / 2 - self.WINDOW_WIDTH / 2)
        position_down = int(self.winfo_screenheight() / 2 - self.WINDOW_HEIGHT / 2)
        self.geometry("{}x{}".format(self.WINDOW_WIDTH, self.WINDOW_HEIGHT))  # Меняем размер окна
        self.geometry("+{}+{}".format(position_right, position_down))

    # Метод для отображения фрейма
    def show_frame(self, frame_name):  # Метод для показа нужного фрейма
        self.config(menu=self.main_frame.menubar())  # Добавляем на фрейм менюбар

        self.main_frame.render() # Рендерим основной фрейм
        self.main_frame.tkraise()
