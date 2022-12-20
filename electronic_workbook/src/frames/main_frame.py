import tkinter as tk

from tkinter.messagebox import showinfo
from tkinter import filedialog as fd
from model.question import Question
from textwrap import wrap


class MainFrame(tk.Frame):  # Класс основного фрейма программы

    def __init__(self, root):  # Конструктор класса
        tk.Frame.__init__(self, root)  # Инициализируем конструктор класса tk.Frame

        # Атрибуты класса

        self.file_path = ""  # Путь к файлу с данными

        self.b1 = tk.Button(text="Готово", width=10, height=2,
                            command=self.__check_results)  # Кнопка для завершения теста

        self.top_menu = tk.Menu(self)  # Создания верхнего меню
        self.file_menu = tk.Menu(self.top_menu, tearoff=0)  # Создание подменю для пункта меню "Файл"

        self.questions = []  # Список для вопросов из файла
        self.radio_button_answers = []  # Список ответов на вопросы

    def menubar(self):  # Метод для генерации меню
        self.top_menu.add_cascade(label="Файл", menu=self.file_menu)
        self.file_menu.add_command(label="Открыть файл", command=self.__open_file_dialog)

        self.top_menu.add_command(label="Выход", command=exit)
        return self.top_menu

    def __show_questions(self):  # Метод для отрисовки вопросов
        row = 0

        for i in range(len(self.questions)):
            text_var = tk.StringVar()  # Создаём объект класса StringVar для записи в него вопроса
            text_var.set(self.questions[i].question)  # Записываем вопрос

            textEntry = tk.Label(textvariable=text_var, font='Arial 13', justify="center", state="disabled",
                                 disabledforeground="black", background="white")  # Создаём вопрос ыв

            textEntry.pack(pady=10)  # Отображаем вопрос

            rad_val = tk.StringVar()  # Создаём еще один объект StringVar для записи в него ответ на вопрос
            for j in range(len(self.questions[i].answers_array)):  # Цикл для отображения вопросов

                answer = self.questions[i].answers_array[j]  # Берем ответ из массива вопросов

                if answer[0] == "_":  #
                    answer = answer[1:]

                tk.Radiobutton(text=answer, variable=rad_val, value=answer).pack(pady=5)  # Отоброжаем вопрос
                row += 3

            self.radio_button_answers.append(rad_val)  # Добавляем ответ на вопрос в список ответов на вопросы

        self.b1.pack()  # Отображаем кнопку для окончания теста

    def __open_file_dialog(self):  # Метод для открытия диалога для работы с файлом
        self.file_path = fd.askopenfilename(
            title="Open a file",
            initialdir="./../..")

        self.__open_db()  # После выбора файла вызываем метод для открытия файла

    def __open_db(self):  # Метод для открытия файла
        if self.file_path == () or self.file_path == '':
            return

        my_file = open(self.file_path, 'r').read().splitlines()

        for line in my_file:
            splt = line.split(";")
            answers_array = splt[2:len(splt)]

            for i in range(len(answers_array)):  # Цикл для добавления пробелов в ответы для корректного отображения
                if len(answers_array[i]) > 40:
                    answers_array[i] = '\n'.join(wrap(answers_array[i], 40))

            correct_answer = ""

            for el in answers_array:
                if el[0] == "_":
                    correct_answer = el[1:]
                    break

            question = Question(  # Записываем полученные данные в объект класса Question
                splt[0],
                splt[1],
                answers_array,
                correct_answer
            )

            self.questions.append(question)  # Добавляем вопрос в список со всеми вопросами

        self.__show_questions()  # Вызываем метод для показа вопросов

    def __check_results(self):  # Метод для проверки правильности ответов
        right_questions = 0  # Счётчик правильных ответов

        for i in range(len(self.questions)):  # Сравниваем ответы пользователя с правильными ответами
            if self.radio_button_answers[i].get() == self.questions[i].correct_answers:
                right_questions += 1

            self.radio_button_answers[i].set('')  # Ставим все кнопки в первоначальное положение

        showinfo("Тест пройден!",  # Вывод результата
                 f"Количество правильных ответов: {right_questions}\n"
                 f"Процент правильных ответов: {round(right_questions / len(self.questions) * 100)}%")

    def render(self):  # Метод для рендера фрейма
        self.pack()
